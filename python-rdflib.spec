
%include /usr/lib/rpm/macros.python

%define	module	rdflib

Summary:	Python library for working with RDF
Summary(pl):	Biblioteka Pythona do pracy z RDF
Name:		python-%{module}
Version:	1.2.4
Release:	1
License:	UNKNOWN
Vendor:		Robin Dunn <robin@alldunn.com>
Group:		Development/Languages/Python
Source0:	http://rdflib.net/2003/03/05/%{module}-%{version}.tgz
# Source0-md5:	32b361bc4b4ad01c773f7e83fb5a52a6
URL:		http://rdflib.net/
BuildRequires:	python-devel >= 2.3
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RDFLib is a Python library for working with RDF, a simple yet powerful
language for representing information. The library contains an RDF/XML
parser/serializer, a TripleStore, an InformationStore and various
store backends. It is being developed by Daniel Krech along with the
help of a number of contributors.


%prep
%setup -q -n %{module}-%{version}

%build
env CFLAGS="%{rpmcflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python -- setup.py install --root=$RPM_BUILD_ROOT --optimize=2
find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE doc example.py index.html
%{py_sitescriptdir}/%{module}
