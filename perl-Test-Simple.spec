#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Simple
Summary:	Test::Simple - basic utilities for writing tests
Summary(pl):	Test::Simple - podstawowe narzêdzia do pisania testów
Name:		perl-Test-Simple
Version:	0.50
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	df12f1f522307850577992d2da5ba04f
# Source0-size:	51334
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# false requires found by rpm 4.0.2
%if "%(perl -MConfig -e 'print $Config{useithreads};')" != "define"
%define		_noautoreq	'perl(threads)' 'perl(threads::shared)'
%else
Requires:	perl(threads) perl(threads::shared)
%endif

%description
AHHHHHHH!!!!  NOT TESTING!  Anything but testing!  Beat me, whip me,
send me to Detroit, but don't make me write tests!
	-- perldoc Test::Tutorial

Test::Simple is an extremely simple, extremely basic module for writing
tests suitable for CPAN modules and other pursuits. If you wish to do
more complicated testing, use the Test::More module (a drop-in replacement
for this one).

The purpose of Test::More is to provide a wide range of testing utilities.
Various ways to say "ok" with better diagnostics, facilities to skip
tests, test future features and compare complicated data structures.
While you can do almost anything with a simple "ok()" function, it
doesn't provide good diagnostic output.

#%description -l pl
#Test::Simple jest bardzo prostym, bardzo podstawowym modu³em do pisania
#testów pasuj±cych do modu³ów CPAN i innych. Do bardziej skomplikowanych
#testów lepiej u¿ywaæ modu³u Test::More (zastêpuj±cego ten).
# to be updated

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
rm -f t/00signature.t

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Test/*.pm
%{_mandir}/man3/*
