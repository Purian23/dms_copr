Name:           dms-git
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        DankMaterialShell - Material 3 inspired shell for Wayland compositors (niri, Hyprland git-version).

License:        GPL-3.0-only
URL:            https://github.com/AvengeMedia/DankMaterialShell
VCS:            {{{ git_dir_vcs }}}

# Main DMS shell repository
Source0:        {{{ git_dir_pack }}}

# dms CLI tool repository
Source1:        https://github.com/AvengeMedia/danklinux/archive/refs/heads/master.tar.gz#/danklinux-master.tar.gz

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

# Recommended system packages
Recommends:     material-symbols-fonts
Recommends:     NetworkManager
Recommends:     gammastep
Recommends:     qt6ct

# Auto-require the dms-cli-git sub-package
Requires:       dms-cli-git = %{version}-%{release}

Provides:       dms = %{version}-%{release}
Provides:       dms-git = %{version}-%{release}
Conflicts:      dms

%description
DankMaterialShell (DMS) is a modern Wayland desktop shell built with Quickshell
and optimized for the niri and Hyprland compositors. Features notifications,
app launcher, wallpaper customization, and fully customizable with plugins.

This is the development version built from the latest git commit.

%package -n dms-cli-git
Summary:        Dank Linux installer CLI (git version)
License:        GPL-3.0-only
URL:            https://github.com/AvengeMedia/danklinux
Provides:       dms-cli = %{version}-%{release}
Conflicts:      dms-cli

%description -n dms-cli-git
Command-line interface for Dank Linux system installation and configuration.
This is the development version built from the latest git commit.

%prep
{{{ git_dir_setup_macro }}}

# Extract danklinux for building dms CLI
tar -xzf %{SOURCE1} -C %{_builddir}

%build
# Build the dms CLI binary from danklinux
pushd %{_builddir}/danklinux-master
export CGO_CPPFLAGS="${CPPFLAGS}"
export CGO_CFLAGS="${CFLAGS}"
export CGO_CXXFLAGS="${CXXFLAGS}"
export CGO_LDFLAGS="${LDFLAGS}"
export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"

go build -o dms ./cmd/dms
popd

%install
# Install dms-cli binary
install -Dm755 %{_builddir}/danklinux-master/dms %{buildroot}%{_bindir}/dms-cli

# Install shell files to XDG config location
install -dm755 %{buildroot}%{_sysconfdir}/xdg/quickshell/dms
cp -r ./* %{buildroot}%{_sysconfdir}/xdg/quickshell/dms/

# Install documentation
install -Dm644 README.md %{buildroot}%{_docdir}/%{name}/README.md
install -Dm644 LICENSE %{buildroot}%{_docdir}/%{name}/LICENSE
install -Dm644 CONTRIBUTING.md %{buildroot}%{_docdir}/%{name}/CONTRIBUTING.md

# Install docs directory if present
if [ -d docs ]; then
    cp -r docs/* %{buildroot}%{_docdir}/%{name}/
fi

# Remove git-related files
rm -rf %{buildroot}%{_sysconfdir}/xdg/quickshell/dms/.git*
rm -f %{buildroot}%{_sysconfdir}/xdg/quickshell/dms/.gitignore
rm -rf %{buildroot}%{_sysconfdir}/xdg/quickshell/dms/.github

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_sysconfdir}/xdg/quickshell/dms/
%{_docdir}/%{name}/

%files -n dms-cli-git
%{_bindir}/dms-cli

%changelog
{{{ git_dir_changelog }}}
