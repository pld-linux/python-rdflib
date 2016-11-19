
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define	module	rdflib

Summary:	Python library for working with RDF
Summary(pl.UTF-8):	Biblioteka Pythona do pracy z RDF
Name:		python-%{module}
Version:	4.2.1
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	https://github.com/RDFLib/rdflib/archive/%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	ce76cb39a5737aeb99f557cff3826a5f
URL:		https://github.com/RDFLib/rdflib
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RDFLib is a Python library for working with RDF, a simple yet powerful
language for representing information. The library contains an RDF/XML
parser/serializer, a TripleStore, an InformationStore and various
store backends. It is being developed by Daniel Krech along with the
help of a number of contributors.

%description -l pl.UTF-8
RDFLib to biblioteka Pythona do pracy z RDF - prostym, ale potężnym
językiem do reprezentowania informacji. Biblioteka zawiera
parser/serializer RDF/XML, TripleStore, InformationStore oraz różne
backendy do przechowywania informacji. Jest rozwijana przez Daniela
Krecha z pomocą wielu współpracowników.

%package -n python3-%{module}
Summary:	Python library for working with RDF
Summary(pl.UTF-8):	Biblioteka Pythona do pracy z RDF
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
RDFLib is a Python library for working with RDF, a simple yet powerful
language for representing information. The library contains an RDF/XML
parser/serializer, a TripleStore, an InformationStore and various
store backends. It is being developed by Daniel Krech along with the
help of a number of contributors.

%description -n python3-%{module} -l pl.UTF-8
RDFLib to biblioteka Pythona do pracy z RDF - prostym, ale potężnym
językiem do reprezentowania informacji. Biblioteka zawiera
parser/serializer RDF/XML, TripleStore, InformationStore oraz różne
backendy do przechowywania informacji. Jest rozwijana przez Daniela
Krecha z pomocą wielu współpracowników.

%package -n rdflib-tools
Summary:	Utilities from python-rdflib
Group:		Applications
%if %{with python3}
Requires:	python3-%{module}
%else
Requires:	%{name}
%endif

%description -n rdflib-tools
Utilities from python-rdflib.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md CONTRIBUTORS examples/*.py
%{py_sitescriptdir}/rdflib
%{py_sitescriptdir}/rdflib-*.egg-info

%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md CONTRIBUTORS examples/*.py
%{py3_sitescriptdir}/rdflib
%{py3_sitescriptdir}/rdflib-*.egg-info

%files -n rdflib-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
