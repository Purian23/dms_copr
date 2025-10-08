Name:           cliphist
Version:        0.6.1
Release:        1%{?dist}
Summary:        Wayland clipboard history manager

License:        GPL-3.0-or-later
URL:            https://github.com/sentriz/cliphist
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  golang >= 1.21
BuildRequires:  git-core
Requires:       wl-clipboard

%description
Wayland clipboard manager with support for text and images.

%prep
%autosetup -n cliphist-%{version}

%build
go build -o cliphist

%install
install -Dm755 cliphist %{buildroot}%{_bindir}/cliphist

%files
%{_bindir}/cliphist
%license LICENSE
%doc README.md

%changelog
* Mon Oct 07 2024 Purian23 <purian23@users.noreply.github.com> - 0.6.1-1
- Initial Copr package release
- Version 0.6.1
