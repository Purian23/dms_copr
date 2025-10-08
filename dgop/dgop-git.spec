Name:           dgop-git
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        System monitoring CLI and REST API (git version)

License:        MIT
URL:            https://github.com/AvengeMedia/dgop
VCS:            {{{ git_dir_vcs }}}

Source0:        {{{ git_dir_pack }}}

BuildRequires:  git-core
BuildRequires:  golang >= 1.21

Requires:       glibc

Provides:       dgop = %{version}-%{release}
Conflicts:      dgop

%description
dgop is a Go-based system monitoring tool that provides both a CLI interface
and REST API for retrieving system metrics including CPU, memory, disk, network,
processes, and GPU information.

This is the development version built from the latest git commit.

Features:
- Interactive TUI with real-time system monitoring
- REST API server with OpenAPI specification
- JSON output for all metrics
- GPU temperature monitoring (NVIDIA)
- Lightweight single-binary deployment

%prep
{{{ git_dir_setup_macro }}}

%build
# Build dgop from source
export CGO_CPPFLAGS="${CPPFLAGS}"
export CGO_CFLAGS="${CFLAGS}"
export CGO_CXXFLAGS="${CXXFLAGS}"
export CGO_LDFLAGS="${LDFLAGS}"
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"

# Build the binary
go build -v -o dgop ./cmd/cli

%install
# Install dgop binary
install -Dm755 dgop %{buildroot}%{_bindir}/dgop

%files
%license LICENSE
%doc README.md
%{_bindir}/dgop

%changelog
{{{ git_dir_changelog }}}
