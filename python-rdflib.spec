

%include /usr/lib/rpm/macros.python
%define	pname	rdflib

%define py_ver         2.3
%define py_prefix      %{_prefix}
%define py_scriptdir   %{py_prefix}/share/python%{py_ver}
%define py_sitescriptdir %{py_scriptdir}/site-packages

Summary:	Python library for working with RDF
Summary(pl):	Biblioteka Pythona do pracy z RDF
Name:		python-%{pname}
Version:	2.0.0
Release:	1
License:	UNKNOWN
Vendor:		Robin Dunn <robin@alldunn.com>
Group:		Development/Languages/Python
Source0:	 http://rdflib.net/2004/03/10/%{pname}-%{version}.tgz
# Source0-md5:	0118a5b5b56bc3662ae96240440aba83
URL:		http://rdflib.net/
BuildRequires:	python-devel >= 2.3
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RDFLib is a Python library for working with RDF, a simple yet powerful
language for representing information. The library contains an RDF/XML
parser/serializer, a TripleStore, an InformationStore and various store
backends. It is being developed by Daniel Krech along with the help of
a number of contributors.


%prep
%setup -q -n %{pname}-%{version}

%build
env CFLAGS="%{rpmcflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python -- setup.py install --root=$RPM_BUILD_ROOT --optimize=2


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO LICENSE doc example.py index.html
%{py_sitescriptdir}/%{pname}
