#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Clone
Summary:	Clone - perl module for recursively copying Perl datatypes
Summary(pl):	Clone - modu� perla obs�uguj�cy rekursywne kopiowanie zmiennych w Perl'u
Name:		perl-Clone
Version:	0.15
Release:	1
# as perl itself
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	5cac94da96835758462133f3afd8fe22
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a clone() method which makes recursive copies
of nested hash, array, scalar and reference types, including tied
variables and objects.

%description -l pl
Ten modu� dostarcza clone(), metod� s�u��c� do rekusywnego kopiowania
zagnie�d�onych tablic asocjacyjnych, referencji, zwi�zanych zmiennych
i obiekt�w.

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
