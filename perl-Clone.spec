#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Clone
Summary:	Clone - Perl module for recursively copying Perl datatypes
Summary(pl.UTF-8):	Clone - moduł Perla obsługujący rekursywne kopiowanie zmiennych w Perlu
Name:		perl-Clone
Version:	0.31
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Clone/%{pdir}-%{version}.tar.gz
# Source0-md5:	65f34e7280d7b7dfb72ab6224e5767f5
URL:		http://search.cpan.org/dist/Clone/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a clone() method which makes recursive copies
of nested hash, array, scalar and reference types, including tied
variables and objects.

%description -l pl.UTF-8
Ten moduł dostarcza clone(), metodę służącą do rekurencyjnego
kopiowania zagnieżdżonych tablic asocjacyjnych, tablic, skalarów i
referencji, włącznie ze związanymi zmiennymi i obiektami.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
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
%{perl_vendorarch}/auto/Clone/autosplit.ix
%{_mandir}/man3/*
