#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (few failures as of 5.0.0)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module
%bcond_without	tools	# package tools

%define	module	rdflib

Summary:	Python 2 library for working with RDF
Summary(pl.UTF-8):	Biblioteka Pythona 2 do pracy z RDF
Name:		python-%{module}
# keep 5.x here for python2 support
Version:	5.0.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://github.com/RDFLib/rdflib/releases
Source0:	https://github.com/RDFLib/rdflib/archive/%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	aaca854daef803da19010181eb99e3e1
URL:		https://rdflib.dev/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-doctest-ignore-unicode
BuildRequires:	python-html5lib
BuildRequires:	python-isodate
BuildRequires:	python-networkx
BuildRequires:	python-nose
BuildRequires:	python-pyparsing
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-doctest-ignore-unicode
BuildRequires:	python3-html5lib
BuildRequires:	python3-isodate
BuildRequires:	python3-networkx
BuildRequires:	python3-nose
BuildRequires:	python3-pyparsing
BuildRequires:	python3-six
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-sphinxcontrib-apidoc
BuildRequires:	sphinx-pdg >= 2.4
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

%package apidocs
Summary:	API documentation for Python rdflib module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona rdflib
Group:		Documentation

%description apidocs
API documentation for Python rdflib module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona rdflib.

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

%if %{with doc}
%{__make} -C docs html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%if %{with python3} || %{without tools}
%{__rm} $RPM_BUILD_ROOT%{_bindir}/*
%endif

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p examples/*.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%endif

%if %{with python3}
%py3_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
cp -p examples/*.py $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}

%if %{without tools}
%{__rm} $RPM_BUILD_ROOT%{_bindir}/*
%endif
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG.md CONTRIBUTORS LICENSE README.md
%{py_sitescriptdir}/rdflib
%{py_sitescriptdir}/rdflib-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGELOG.md CONTRIBUTORS LICENSE README.md
%{py3_sitescriptdir}/rdflib
%{py3_sitescriptdir}/rdflib-%{version}-py*.egg-info
%{_examplesdir}/python3-%{module}-%{version}
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_images,_modules,_static,apidocs,*.html,*.js}
%endif

%if %{with tools}
%files -n rdflib-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/csv2rdf
%attr(755,root,root) %{_bindir}/rdf2dot
%attr(755,root,root) %{_bindir}/rdfgraphisomorphism
%attr(755,root,root) %{_bindir}/rdfpipe
%attr(755,root,root) %{_bindir}/rdfs2dot
%endif
