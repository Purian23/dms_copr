# Modular DMS spec file - supports both stable and git builds
# Build stable: rpmbuild -bs dms.spec
# Build git:    rpmbuild -bs dms.spec --define '_git_build 1'

# Disable debug package - QML files and pre-built binaries don't need debug symbols
%global debug_package %{nil}

%if 0%{?_git_build:1}
# ====== GIT BUILD ======
Name:           dms-git
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        DankMaterialShell - Material 3 inspired shell for Wayland compositors (git development version)

VCS:            {{{ git_dir_vcs }}}

# Main DMS shell repository from git
Source0:        {{{ git_dir_pack }}}

# dms CLI tool - built from danklinux master
Source1:        https://github.com/AvengeMedia/danklinux/archive/refs/heads/master.tar.gz#/danklinux-master.tar.gz
# Vendored Go dependencies for danklinux (Copr has no network access)
Source2:        danklinux-vendor.tar.gz

BuildRequires:  git-core
BuildRequires:  golang >= 1.21

Provides:       dms = %{version}-%{release}
Provides:       dms-git = %{version}-%{release}
Conflicts:      dms

# Auto-require the git CLI sub-package
Requires:       dms-cli-git = %{version}-%{release}

%else
# ====== STABLE BUILD ======
Name:           dms
Version:        0.1.4
Release:        1%{?dist}
Summary:        DankMaterialShell - Material 3 inspired shell for Wayland compositors (stable release)

# DMS configuration from tagged release
Source0:        https://github.com/AvengeMedia/DankMaterialShell/archive/refs/tags/v%{version}.tar.gz#/DankMaterialShell-%{version}.tar.gz

# dms CLI binary from DankMaterialShell releases (pre-built)
Source1:        https://github.com/AvengeMedia/DankMaterialShell/releases/download/v%{version}/dms-amd64.gz
Source2:        https://github.com/AvengeMedia/DankMaterialShell/releases/download/v%{version}/dms-amd64.gz.sha256
Source3:        https://github.com/AvengeMedia/DankMaterialShell/releases/download/v%{version}/dms-arm64.gz
Source4:        https://github.com/AvengeMedia/DankMaterialShell/releases/download/v%{version}/dms-arm64.gz.sha256

# Note: NOT noarch because we install architecture-specific binaries
BuildRequires:  gzip

Provides:       dms = %{version}-%{release}

# Auto-require the stable CLI sub-package
Requires:       dms-cli = %{version}-%{release}

%endif

# ====== COMMON METADATA ======
License:        GPL-3.0-only
URL:            https://github.com/AvengeMedia/DankMaterialShell

# Core requirements - Shell and fonts
Requires:       quickshell
Requires:       fira-code-fonts
Requires:       rsms-inter-fonts

# Core utilities (REQUIRED for DMS functionality)
Requires:       dgop
Requires:       cava
Requires:       wl-clipboard
Requires:       brightnessctl
Requires:       matugen
Requires:       cliphist
Requires:       material-symbols-fonts

# Recommended system packages
Recommends:     NetworkManager
Recommends:     gammastep
Recommends:     qt6ct

%description
DankMaterialShell (DMS) is a modern Wayland desktop shell built with Quickshell
and optimized for the niri and Hyprland compositors. Features notifications,
app launcher, wallpaper customization, and fully customizable with plugins.

Includes auto-theming for GTK/Qt apps with matugen, 20+ customizable widgets,
process monitoring, notification center, clipboard history, dock, control center,
lock screen, and comprehensive plugin system.

%if 0%{?_git_build:1}
This is the development version built from the latest git commit.
%else
This is the stable release version.
%endif

# ====== CLI SUB-PACKAGE ======
%if 0%{?_git_build:1}
%package -n dms-cli-git
Summary:        DankMaterialShell CLI tool (git development version)
License:        GPL-3.0-only
URL:            https://github.com/AvengeMedia/danklinux
Provides:       dms-cli = %{version}-%{release}
Conflicts:      dms-cli

%description -n dms-cli-git
Command-line interface for DankMaterialShell configuration and management.
Provides native DBus bindings, NetworkManager integration, and system utilities.
Built from danklinux repository master branch. This is the development version.

%else
%package -n dms-cli
Summary:        DankMaterialShell CLI tool (stable release)
License:        GPL-3.0-only
URL:            https://github.com/AvengeMedia/DankMaterialShell

%description -n dms-cli
Command-line interface for DankMaterialShell configuration and management.
Provides native DBus bindings, NetworkManager integration, and system utilities.
%endif

# ====== PREP ======
%prep
%if 0%{?_git_build:1}
# Git build: Use rpkg macros
{{{ git_dir_setup_macro }}}

# Extract danklinux for building dms CLI
tar -xzf %{SOURCE1} -C %{_builddir}

# Extract vendored Go dependencies
tar -xzf %{SOURCE2} -C %{_builddir}/danklinux-master/

%else
# Stable build: Standard autosetup
%setup -q -n DankMaterialShell-%{version}

# Extract and verify the appropriate dms binary based on architecture
%ifarch x86_64
# Verify checksum of compressed file
echo "$(cat %{SOURCE2} | cut -d' ' -f1)  %{SOURCE1}" | sha256sum -c - || { echo "Checksum mismatch!"; exit 1; }
gunzip -c %{SOURCE1} > dms
%endif
%ifarch aarch64
# Verify checksum of compressed file
echo "$(cat %{SOURCE4} | cut -d' ' -f1)  %{SOURCE3}" | sha256sum -c - || { echo "Checksum mismatch!"; exit 1; }
gunzip -c %{SOURCE3} > dms
%endif
chmod +x dms
%endif

# ====== BUILD ======
%build
%if 0%{?_git_build:1}
# Git build: Compile dms CLI from source
pushd %{_builddir}/danklinux-master
export CGO_CPPFLAGS="${CPPFLAGS}"
export CGO_CFLAGS="${CFLAGS}"
export CGO_CXXFLAGS="${CXXFLAGS}"
export CGO_LDFLAGS="${LDFLAGS}"
export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=vendor -modcacherw"

go build -mod=vendor -o dms ./cmd/dms
popd
%else
# Stable build: Use pre-built binary (nothing to build)
%endif

# ====== INSTALL ======
%install
# Install dms-cli binary
%if 0%{?_git_build:1}
# Git: Install built binary
install -Dm755 %{_builddir}/danklinux-master/dms %{buildroot}%{_bindir}/dms-cli
%else
# Stable: Install pre-built binary
install -Dm755 dms %{buildroot}%{_bindir}/dms-cli
%endif

# Install shell files to XDG config location
install -dm755 %{buildroot}%{_sysconfdir}/xdg/quickshell/dms
cp -r ./* %{buildroot}%{_sysconfdir}/xdg/quickshell/dms/

# Remove git-related files
rm -rf %{buildroot}%{_sysconfdir}/xdg/quickshell/dms/.git*
rm -f %{buildroot}%{_sysconfdir}/xdg/quickshell/dms/.gitignore
rm -rf %{buildroot}%{_sysconfdir}/xdg/quickshell/dms/.github

%if ! 0%{?_git_build:1}
# Stable: Remove the dms binary from the config directory
rm -f %{buildroot}%{_sysconfdir}/xdg/quickshell/dms/dms
%endif

# ====== FILES ======
%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_sysconfdir}/xdg/quickshell/dms/

%if 0%{?_git_build:1}
%files -n dms-cli-git
%else
%files -n dms-cli
%endif
%{_bindir}/dms-cli

# ====== CHANGELOG ======
%changelog
* Tue Oct 08 2024 Purian23 <purian23@users.noreply.github.com> - 0.1.4-1
- Create unified spec file supporting both stable and git builds
- Stable: Uses pre-built dms-cli binary from DankMaterialShell releases
- Git: Builds dms-cli from danklinux master with vendored Go dependencies
- Use --define '_git_build 1' to build git version
