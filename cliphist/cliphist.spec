Name:           cliphist
Version:        0.6.1
Release:        1%{?dist}
Summary:        Wayland clipboard history manager

License:        GPL-3.0-or-later
URL:            https://github.com/sentriz/cliphist
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/cliphist-%{version}.tar.gz
# Vendor tarball created with: go mod vendor && tar czf cliphist-0.6.1-vendor.tar.gz vendor/
Source1:        cliphist-%{version}-vendor.tar.gz

BuildRequires:  golang
Requires:       wl-clipboard

%description
Wayland clipboard manager with support for text and images.

%prep
%autosetup -n cliphist-%{version}
# Extract vendored dependencies
tar xzf %{SOURCE1}

%build
# Build using vendored dependencies
go build -mod=vendor -o cliphist

%install
install -Dm755 cliphist %{buildroot}%{_bindir}/cliphist

%files
%{_bindir}/cliphist

%changelog
* Mon Oct 07 2024 Purian23 <purian23@users.noreply.github.com> - 0.6.1-1
- Initial Copr package release
- Version 0.6.1
