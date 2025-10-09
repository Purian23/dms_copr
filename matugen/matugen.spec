Name:           matugen
Version:        2.4.1
Release:        1%{?dist}
Summary:        Material You color generation tool

License:        GPL-2.0-or-later
URL:            https://github.com/InioX/matugen
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/matugen-%{version}.tar.gz
# Vendor tarball created with: cargo vendor && tar czf matugen-2.4.1-vendor.tar.gz vendor/
Source1:        matugen-%{version}-vendor.tar.gz

BuildRequires:  rust
BuildRequires:  cargo

%description
Material You color generation tool for theming.

%prep
%autosetup -n matugen-%{version}
# Extract vendored dependencies
tar xzf %{SOURCE1}
# Configure cargo to use vendored dependencies
mkdir -p .cargo
cat >.cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
cargo build --release --offline

%install
install -Dm755 target/release/matugen %{buildroot}%{_bindir}/matugen

%files
%{_bindir}/matugen
%license LICENSE
%doc README.md

%changelog
* Mon Oct 07 2024 Purian23 <purian23@users.noreply.github.com> - 2.4.1-1
- Initial Copr package release
- Version 2.4.1
