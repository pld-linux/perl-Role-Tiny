#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Role
%define		pnam	Tiny
%include	/usr/lib/rpm/macros.perl
Summary:	Role::Tiny - Roles. Like a nouvelle cuisine portion size slice of Moose.
#Summary(pl.UTF-8):	
Name:		perl-Role-Tiny
Version:	1.003002
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/H/HA/HAARG/Role-Tiny-1.003002.tar.gz
# Source0-md5:	2d9b46cdc8dbb59056710e2c8e35e25f
URL:		http://search.cpan.org/dist/Role-Tiny/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Fatal >= 0.003
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Role::Tiny is a minimalist role composition tool.

# %description -l pl.UTF-8
# TODO

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
%{perl_vendorlib}/Role/*.pm
%{perl_vendorlib}/Role/Tiny
%{_mandir}/man3/*
