Name:           matugen
Version:        2.4.1
Release:        1%{?dist}
Summary:        Material You color generation tool

License:        GPL-2.0-or-later
URL:            https://github.com/InioX/matugen
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  rust
BuildRequires:  cargo

%description
Material You color generation tool for theming.

%prep
%autosetup -n matugen-%{version}

%build
cargo install --path . --root %{_builddir}/matugen-install

%install
install -Dm755 %{_builddir}/matugen-install/bin/matugen %{buildroot}%{_bindir}/matugen

%files
%{_bindir}/matugen
%license LICENSE
%doc README.md

%changelog
* Tue Oct 07 2025 Copr Packaging <copr@localhost> - 3.8.0-1
- Initial Copr package
