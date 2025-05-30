%define		module	sphinx_theme_builder
Summary:	A tool for authoring Sphinx themes with a simple (opinionated) workflow
Summary(pl.UTF-8):	Narzędzie do tworzenia motywów Sphinksa z prostym przebiegiem pracy
Name:		python3-%{module}
Version:	0.2.0b2
Release:	3
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.debian.net/sphinx_theme_builder/sphinx-theme-builder-%{version}.tar.gz
# Source0-md5:	e72c219c88f6f6afdba5ff96e9a7c7f1
URL:		https://pypi.org/project/sphinx-theme-builder/
BuildRequires:	python3-build
BuildRequires:	python3-flit_core >= 3.2
BuildRequires:	python3-flit_core < 4
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Streamline the Sphinx theme development workflow, by building upon
existing standardised tools.
- simplified packaging experience
- simplified JavaScript tooling setup
- development server, with rebuild-on-save and automagical browser
  reloading
- consistent repository structure across themes

%description -l pl.UTF-8
Usprawniony przebieg tworzenia motywów Sphinksa poprzez budowanie w
oparciu o ustandaryzowane narzędzia.
- uproszczone pakietowanie
- uproszczona konfiguracja narzędzi do JavaScriptu
- serwer rozwojowy z przebudowywaniem w trakcie zapisu i automagicznym
  przeładowywaniem przeglądarki
- spójna struktura repozytorium między motywami

%prep
%setup -q -n sphinx-theme-builder-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/stb
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}.dist-info
