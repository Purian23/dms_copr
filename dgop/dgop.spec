# Modular dgop spec file - supports both stable and git builds
# Build stable: rpmbuild -bs dgop.spec
# Build git:    rpmbuild -bs dgop.spec --define '_git_build 1'

%if 0%{?_git_build:1}
# ====== GIT BUILD ======
Name:           dgop-git
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        System monitoring CLI and REST API (git development version)

# Disable debug package - Go binaries are already stripped
%global debug_package %{nil}

VCS:            {{{ git_dir_vcs }}}

# Source from git
Source0:        {{{ git_dir_pack }}}

BuildRequires:  git-core
BuildRequires:  golang >= 1.21

Provides:       dgop = %{version}-%{release}
Conflicts:      dgop

%else
# ====== STABLE BUILD ======
Name:           dgop
Version:        0.1.4
Release:        1%{?dist}
Summary:        System monitoring CLI and REST API (stable release)

# Pre-built binaries from GitHub releases
Source0:        https://github.com/AvengeMedia/dgop/releases/download/v%{version}/dgop-linux-amd64.gz
Source1:        https://github.com/AvengeMedia/dgop/releases/download/v%{version}/dgop-linux-amd64.gz.sha256
Source2:        https://github.com/AvengeMedia/dgop/releases/download/v%{version}/dgop-linux-arm64.gz
Source3:        https://github.com/AvengeMedia/dgop/releases/download/v%{version}/dgop-linux-arm64.gz.sha256

BuildRequires:  gzip
BuildRequires:  coreutils

%endif

# ====== COMMON METADATA ======
License:        MIT
URL:            https://github.com/AvengeMedia/dgop

Requires:       glibc

%description
dgop is a Go-based system monitoring tool that provides both a CLI interface
and REST API for retrieving system metrics including CPU, memory, disk, network,
processes, and GPU information.

%if 0%{?_git_build:1}
This is the development version built from the latest git commit.
%else
This is the stable release version.
%endif

Features:
- Interactive TUI with real-time system monitoring
- REST API server with OpenAPI specification
- JSON output for all metrics
- GPU temperature monitoring (NVIDIA)
- Lightweight single-binary deployment

# ====== PREP ======
%prep
%if 0%{?_git_build:1}
# Git build: Use rpkg macros
{{{ git_dir_setup_macro }}}

%else
# Stable build: Extract pre-built binary
%ifarch x86_64
# Verify checksum of compressed file
echo "$(cat %{SOURCE1} | cut -d' ' -f1)  %{SOURCE0}" | sha256sum -c - || { echo "Checksum mismatch!"; exit 1; }
gunzip -c %{SOURCE0} > dgop
%endif

%ifarch aarch64
# Verify checksum of compressed file
echo "$(cat %{SOURCE3} | cut -d' ' -f1)  %{SOURCE2}" | sha256sum -c - || { echo "Checksum mismatch!"; exit 1; }
gunzip -c %{SOURCE2} > dgop
%endif

chmod +x dgop
%endif

# ====== BUILD ======
%build
%if 0%{?_git_build:1}
# Git build: Compile from source
export CGO_CPPFLAGS="${CPPFLAGS}"
export CGO_CFLAGS="${CFLAGS}"
export CGO_CXXFLAGS="${CXXFLAGS}"
export CGO_LDFLAGS="${LDFLAGS}"
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"

# Build the binary
go build -v -o dgop ./cmd/cli
%else
# Stable build: Use pre-built binary (nothing to build)
%endif

# ====== INSTALL ======
%install
# Install dgop binary
%if 0%{?_git_build:1}
# Git: Install built binary
install -Dm755 dgop %{buildroot}%{_bindir}/dgop
%else
# Stable: Install pre-built binary
install -Dm755 dgop %{buildroot}%{_bindir}/dgop
%endif

# ====== FILES ======
%files
%if 0%{?_git_build:1}
%license LICENSE
%doc README.md
%endif
%{_bindir}/dgop

# ====== CHANGELOG ======
%changelog
* Tue Oct 08 2024 Purian23 <purian23@users.noreply.github.com> - 0.1.4-1
- Create unified spec file supporting both stable and git builds
- Stable: Uses pre-built binaries from GitHub releases with SHA256 verification
- Git: Builds from latest master commit
- Use --define '_git_build 1' to build git version
