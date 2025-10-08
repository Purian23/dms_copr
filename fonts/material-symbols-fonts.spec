Name:           material-symbols-fonts
Version:        1.0
Release:        1%{?dist}
Summary:        Material Symbols variable font by Google

License:        Apache-2.0
URL:            https://github.com/google/material-design-icons
Source0:        https://github.com/google/material-design-icons/raw/master/variablefont/MaterialSymbolsRounded%%5BFILL%%2CGRAD%%2Copsz%%2Cwght%%5D.ttf

BuildArch:      noarch
BuildRequires:  fontpackages-devel

Requires:       fontpackages-filesystem

%description
Material Symbols are the latest icons from Google, an evolution of Material Icons.
This package contains the Material Symbols Rounded variable font, which includes
all icons with adjustable fill, weight, grade, and optical size.

%prep
# No prep needed - direct font file download

%build
# No build needed - pre-built font file

%install
install -d %{buildroot}%{_fontdir}
install -m 0644 %{SOURCE0} %{buildroot}%{_fontdir}/MaterialSymbolsRounded.ttf

%files
%{_fontdir}/MaterialSymbolsRounded.ttf

%changelog
* Tue Oct 07 2025 DMS Packager <your-email@example.com> - 1.0-1
- Initial package for Material Symbols Rounded variable font
- Required for DankMaterialShell UI icons
