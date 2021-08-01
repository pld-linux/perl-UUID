#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	UUID
Summary:	UUID - DCE compatible Universally Unique Identifier library for Perl
Name:		perl-UUID
Version:	0.28
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/UUID/%{pdir}-%{version}.tar.gz
# Source0-md5:	15c17e1044f7ff686dafa27ff381b007
URL:		https://metacpan.org/release/UUID
%if %{with tests}
BuildRequires:	perl(Test::More)
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The UUID library is used to generate unique identifiers for objects
that may be accessible beyond the local system. For instance, they
could be used to generate unique HTTP cookies across multiple web
servers without communication between the servers, and without fear
of a name clash.

The generated UUIDs can be reasonably expected to be unique within a
system, and unique across all systems, and are compatible with those
created by the Open Software Foundation (OSF) Distributed Computing
Environment (DCE) utility uuidgen.

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
%{perl_vendorarch}/UUID.pm
%dir %{perl_vendorarch}/auto/UUID
%attr(755,root,root) %{perl_vendorarch}/auto/UUID/UUID.so
%{_mandir}/man3/UUID.3pm*
