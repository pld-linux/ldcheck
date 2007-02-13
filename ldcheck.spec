Summary:	Broken library dependecies checker
Summary(pl.UTF-8):	Znajdowanie błędnych zależności od bibliotek
Name:		ldcheck
Version:	0.95
Release:	0.1
License:	GPL
Group:		Applications/Console
Source0:	http://dl.sourceforge.net/ldcheck/%{name}_%{version}.tar.gz
# Source0-md5:	9a0f0ba1dfddfa2375771c6ea17267fd
URL:		http://ldcheck.sourceforge.net/
Requires:	bash
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool to check for broken library dependancies in Linux and recommend
which distribution package to re-compile or re-install to resolve the
problem.

%description -l pl.UTF-8
Narzędzie to wyszukuje wyszukuje błędne zależności od bibliotek i
sugeruje które pakiety należy przebudować bądź przekompilować w celu
rozwiązania tego problemu.

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
