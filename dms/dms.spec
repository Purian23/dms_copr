Name:           dms
Version:        0.1.4
Release:        1%{?dist}
Summary:        DankMaterialShell - Material 3 inspired shell for Wayland compositors (niri, Hyprland).

# Disable debug package since we use pre-built binaries
%global debug_package %{nil}

License:        GPL-3.0-only
URL:            https://github.com/AvengeMedia/DankMaterialShell
Source0:        https://github.com/AvengeMedia/DankMaterialShell/archive/refs/tags/v%{version}.tar.gz#/DankMaterialShell-%{version}.tar.gz
# dms CLI binary from DankMaterialShell releases
Source1:        https://github.com/AvengeMedia/DankMaterialShell/releases/download/v%{version}/dms-amd64.gz
Source2:        https://github.com/AvengeMedia/DankMaterialShell/releases/download/v%{version}/dms-amd64.gz.sha256
Source3:        https://github.com/AvengeMedia/DankMaterialShell/releases/download/v%{version}/dms-arm64.gz
Source4:        https://github.com/AvengeMedia/DankMaterialShell/releases/download/v%{version}/dms-arm64.gz.sha256

# Note: NOT noarch because we install architecture-specific binaries
BuildRequires:  gzip

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

# Auto-require the dms-cli sub-package
Requires:       dms-cli = %{version}-%{release}

Provides:       dms = %{version}-%{release}

%description
DankMaterialShell (DMS) is a modern Wayland desktop shell built with Quickshell
and optimized for the niri and Hyprland compositors. Features notifications,
app launcher, wallpaper customization, and fully customizable with plugins.

Includes auto-theming for GTK/Qt apps with matugen, 20+ customizable widgets,
process monitoring, notification center, clipboard history, dock, control center,
lock screen, and comprehensive plugin system.

%package -n dms-cli
Summary:        DankMaterialShell CLI tool
License:        GPL-3.0-only
URL:            https://github.com/AvengeMedia/DankMaterialShell

%description -n dms-cli
Command-line interface for DankMaterialShell configuration and management.
Provides native DBus bindings, NetworkManager integration, and system utilities.

%prep
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

%build
# Nothing to build - QML shell files and pre-built binary

%install
# Install DMS configuration files
mkdir -p %{buildroot}%{_sysconfdir}/xdg/quickshell/dms
cp -r * %{buildroot}%{_sysconfdir}/xdg/quickshell/dms/

# Install dms-cli binary
install -Dm755 dms %{buildroot}%{_bindir}/dms-cli

# Remove git-related files
rm -rf %{buildroot}%{_sysconfdir}/xdg/quickshell/dms/.git*
rm -f %{buildroot}%{_sysconfdir}/xdg/quickshell/dms/.gitignore
rm -f %{buildroot}%{_sysconfdir}/xdg/quickshell/dms/.github

# Remove the dms binary from the config directory
rm -f %{buildroot}%{_sysconfdir}/xdg/quickshell/dms/dms

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_sysconfdir}/xdg/quickshell/dms/

%files -n dms-cli
%{_bindir}/dms-cli

%changelog
* Tue Oct 08 2024 Purian23 <purian23@users.noreply.github.com> - 0.1.4-1
- Update to v0.1.4 release
- Changed dms-cli source from danklinux to DankMaterialShell releases
- dms-cli is now the DankMaterialShell CLI tool (not danklinux installer)