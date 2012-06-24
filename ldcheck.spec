Summary:	Broken library dependecies checker
Summary(pl):	Znajdowanie b��dnych zale�no�ci od bibliotek
Name:		ldcheck
Version:	0.9
Release:	0.1
License:	GPL
Group:		Applications/Console
Source0:	http://dl.sourceforge.net/ldcheck/%{name}_%{version}.tar.gz
# Source0-md5:	a71402adf9957bef9cbfc411e0899828
URL:		http://ldcheck.sourceforge.net/
Requires:	bash
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool to check for broken library dependancies in Linux and recommend
which distribution package to re-compile or re-install to resolve the
problem.

%description -l pl
Narz�dzie to wyszukuje wyszukuje b��dne zale�no�ci od bibliotek i
sugeruje kt�re pakiety nale�y przebudowa� b�d� przekompilowa� w celu
rozwi�zania tego problemu.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

install local/bin/ldcheck 	$RPM_BUILD_ROOT%{_bindir}
install share/man/man8/* 	$RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc share/doc/%{name}-%{version}/README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/%{name}.*
