# Git-only spec for DMS - for Copr SCM builds with webhooks
# Copr will use rpkg to process git macros automatically

%global debug_package %{nil}
%global version {{{ git_dir_version }}}

Name:           dms-git
Version:        %{version}
Release:        1%{?dist}
Summary:        DankMaterialShell - Material 3 inspired shell for Wayland compositors (git development version)

License:        GPL-3.0-only
URL:            https://github.com/AvengeMedia/DankMaterialShell
VCS:            {{{ git_dir_vcs }}}
Source0:        {{{ git_dir_pack }}}

# dms CLI tool - built from danklinux master
Source1:        https://github.com/AvengeMedia/danklinux/archive/refs/heads/master.tar.gz#/danklinux-master.tar.gz
# Vendored Go dependencies for danklinux (Copr has no network access)
Source2:        danklinux-vendor.tar.gz

BuildRequires:  git-core
BuildRequires:  golang >= 1.21

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

# Auto-require the git CLI sub-package
Requires:       dms-cli-git = %{version}-%{release}

Provides:       dms = %{version}-%{release}
Provides:       dms-git = %{version}-%{release}
Conflicts:      dms

%description
DankMaterialShell (DMS) is a modern Wayland desktop shell built with Quickshell
and optimized for the niri and Hyprland compositors. Features notifications,
app launcher, wallpaper customization, and fully customizable with plugins.

Includes auto-theming for GTK/Qt apps with matugen, 20+ customizable widgets,
process monitoring, notification center, clipboard history, dock, control center,
lock screen, and comprehensive plugin system.

This is the development version built from the latest git commit.

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

%prep
{{{ git_dir_setup_macro }}}

# Extract danklinux for building dms CLI
tar -xzf %{SOURCE1} -C %{_builddir}

# Extract vendored Go dependencies
tar -xzf %{SOURCE2} -C %{_builddir}/danklinux-master/

%build
# Build dms CLI from source
pushd %{_builddir}/danklinux-master
export CGO_CPPFLAGS="${CPPFLAGS}"
export CGO_CFLAGS="${CFLAGS}"
export CGO_CXXFLAGS="${CXXFLAGS}"
export CGO_LDFLAGS="${LDFLAGS}"
export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=vendor -modcacherw"

go build -mod=vendor -o dms ./cmd/dms
popd

%install
# Install dms-cli binary
install -Dm755 %{_builddir}/danklinux-master/dms %{buildroot}%{_bindir}/dms-cli

# Install shell files to XDG config location
install -dm755 %{buildroot}%{_sysconfdir}/xdg/quickshell/dms
cp -r ./* %{buildroot}%{_sysconfdir}/xdg/quickshell/dms/

# Remove git-related files
rm -rf %{buildroot}%{_sysconfdir}/xdg/quickshell/dms/.git*
rm -f %{buildroot}%{_sysconfdir}/xdg/quickshell/dms/.gitignore
rm -rf %{buildroot}%{_sysconfdir}/xdg/quickshell/dms/.github

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_sysconfdir}/xdg/quickshell/dms/

%files -n dms-cli-git
%{_bindir}/dms-cli

%changelog
{{{ git_dir_changelog }}}
