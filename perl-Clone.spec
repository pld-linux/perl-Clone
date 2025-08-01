#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Clone
Summary:	Clone - Perl module for recursively copying Perl datatypes
Summary(pl.UTF-8):	Clone - moduł Perla obsługujący rekursywne kopiowanie zmiennych w Perlu
Name:		perl-Clone
Version:	0.46
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Clone/%{pdir}-%{version}.tar.gz
# Source0-md5:	cafa8984a2c2e005e54b27dd1e3f0afe
URL:		https://metacpan.org/dist/Clone
%if %{with tests}
BuildRequires:	perl-B-COW >= 0.004
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
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
%attr(755,root,root) %{perl_vendorarch}/auto/Clone/Clone.so
%{perl_vendorarch}/auto/Clone/autosplit.ix
%{_mandir}/man3/Clone.3pm*
