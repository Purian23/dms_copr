Name:           dgop
Version:        0.1.4
Release:        1%{?dist}
Summary:        System monitoring CLI and REST API

License:        MIT
URL:            https://github.com/AvengeMedia/dgop
Source0:        https://github.com/AvengeMedia/dgop/releases/download/v%{version}/dgop-linux-amd64.gz
Source1:        https://github.com/AvengeMedia/dgop/releases/download/v%{version}/dgop-linux-amd64.gz.sha256
Source2:        https://github.com/AvengeMedia/dgop/releases/download/v%{version}/dgop-linux-arm64.gz
Source3:        https://github.com/AvengeMedia/dgop/releases/download/v%{version}/dgop-linux-arm64.gz.sha256

BuildRequires:  gzip
BuildRequires:  coreutils

Requires:       glibc

%description
dgop is a Go-based system monitoring tool that provides both a CLI interface
and REST API for retrieving system metrics including CPU, memory, disk, network,
processes, and GPU information.

Features:
- Interactive TUI with real-time system monitoring
- REST API server with OpenAPI specification
- JSON output for all metrics
- GPU temperature monitoring (NVIDIA)
- Lightweight single-binary deployment

%prep
# Extract the appropriate binary based on architecture
%ifarch x86_64
gunzip -c %{SOURCE0} > dgop
# Verify checksum
sha256sum dgop > dgop.sha256
grep "$(cat %{SOURCE1} | cut -d' ' -f1)" dgop.sha256 || { echo "Checksum mismatch!"; exit 1; }
%endif

%ifarch aarch64
gunzip -c %{SOURCE2} > dgop
# Verify checksum
sha256sum dgop > dgop.sha256
grep "$(cat %{SOURCE3} | cut -d' ' -f1)" dgop.sha256 || { echo "Checksum mismatch!"; exit 1; }
%endif

chmod +x dgop

%build
# Nothing to build - using pre-compiled binary

%install
# Install dgop binary
install -Dm755 dgop %{buildroot}%{_bindir}/dgop

%files
%{_bindir}/dgop

%changelog
# * Tue Oct 07 2025 DankMaterialShell Team <maintainer@example.com> - 0.1.4-1
- Initial Copr package release
- Version 0.1.4 with pre-built binaries from GitHub releases
