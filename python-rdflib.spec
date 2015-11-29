
%define	module	rdflib

Summary:	Python library for working with RDF
Summary(pl.UTF-8):	Biblioteka Pythona do pracy z RDF
Name:		python-%{module}
Version:	3.2.0
Release:	3
License:	BSD
Group:		Development/Languages/Python
Source0:	http://www.rdflib.net/%{module}-%{version}.tar.gz
# Source0-md5:	ab3d3a5f71ebb6fe4fd33539f5d5768e
URL:		http://www.rdflib.net/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
Requires:	python-isodate
%pyrequires_eq	python-modules
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

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README examples/*.py
%{py_sitescriptdir}/rdflib
%{py_sitescriptdir}/rdflib-*.egg-info
