#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Clone
Summary:	Clone - Perl module for recursively copying Perl datatypes
Summary(pl):	Clone - modu³ Perla obs³uguj±cy rekursywne kopiowanie zmiennych w Perlu
Name:		perl-Clone
Version:	0.20
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	f369cb742a92733688a9a7b8514a2538
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a clone() method which makes recursive copies
of nested hash, array, scalar and reference types, including tied
variables and objects.

%description -l pl
Ten modu³ dostarcza clone(), metodê s³u¿±c± do rekurencyjnego
kopiowania zagnie¿d¿onych tablic asocjacyjnych, tablic, skalarów i
referencji, w³±cznie ze zwi±zanymi zmiennymi i obiektami.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/Clone.pm
%{perl_vendorarch}/auto/Clone/Clone.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Clone/Clone.so
%{_mandir}/man3/*
