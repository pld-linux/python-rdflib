#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define	module	rdflib

Summary:	Python 2 library for working with RDF
Summary(pl.UTF-8):	Biblioteka Pythona 2 do pracy z RDF
Name:		python-%{module}
Version:	4.2.2
Release:	2
License:	BSD
Group:		Development/Languages/Python
Source0:	https://github.com/RDFLib/rdflib/archive/%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	1dd95c6443302d6a44a908e4af8fdc5d
URL:		https://github.com/RDFLib/rdflib
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.6
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
Summary:	Python 3 library for working with RDF
Summary(pl.UTF-8):	Biblioteka Pythona 3 do pracy z RDF
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

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
Summary(pl.UTF-8):	Narzędzia z pakietu python-rdflib
Group:		Applications/File
%if %{with python3}
Requires:	python3-%{module} = %{version}-%{release}
%else
Requires:	%{name} = %{version}-%{release}
%endif

%description -n rdflib-tools
Utilities from python-rdflib.

%description -n rdflib-tools -l pl.UTF-8
Narzędzia z pakietu python-rdflib.

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

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p examples/*.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%endif

%if %{with python3}
%py3_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
cp -p examples/*.py $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md CONTRIBUTORS LICENSE README.md
%{py_sitescriptdir}/rdflib
%{py_sitescriptdir}/rdflib-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}

%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGELOG.md CONTRIBUTORS LICENSE README.md
%{py3_sitescriptdir}/rdflib
%{py3_sitescriptdir}/rdflib-%{version}-py*.egg-info
%{_examplesdir}/python3-%{module}-%{version}

%files -n rdflib-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/csv2rdf
%attr(755,root,root) %{_bindir}/rdf2dot
%attr(755,root,root) %{_bindir}/rdfgraphisomorphism
%attr(755,root,root) %{_bindir}/rdfpipe
%attr(755,root,root) %{_bindir}/rdfs2dot
