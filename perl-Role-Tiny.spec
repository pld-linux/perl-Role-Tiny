#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Role
%define		pnam	Tiny
%include	/usr/lib/rpm/macros.perl
Summary:	Role::Tiny - Roles; like a nouvelle cuisine portion size slice of Moose
Summary(pl.UTF-8):	Role::Tiny - role; podobnie jak nowy kuzyn o ułamku rozmiaru Moose
Name:		perl-Role-Tiny
Version:	2.000001
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/H/HA/HAARG/Role-Tiny-%{version}.tar.gz
# Source0-md5:	f350f1f8c13652bf85da172380b39ec8
URL:		http://search.cpan.org/dist/Role-Tiny/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Fatal >= 0.003
BuildRequires:	perl-Test-Simple >= 0.96
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Role::Tiny is a minimalist role composition tool.

%description -l pl.UTF-8
Role::Tiny to minimalistyczne narzędzie do kompozycji ról.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Role/Tiny.pm
%{perl_vendorlib}/Role/Tiny
%{_mandir}/man3/Role::Tiny.3pm*
%{_mandir}/man3/Role::Tiny::With.3pm*
