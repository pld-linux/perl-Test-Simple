#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Simple
Summary:	Test::Simple - basic utilities for writing tests
Summary(pl.UTF-8):	Test::Simple - podstawowe narzędzia do pisania testów
Name:		perl-Test-Simple
Version:	1.001_006
%define	fver	%(echo %{version} | tr -d _)
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{fver}.tar.gz
# Source0-md5:	581ac4d2d7ace1f56409bc112e8ad02c
URL:		http://search.cpan.org/dist/Test-Simple/
%{?with_tests:BuildRequires:	perl-Test-Harness >= 2.03}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Provides:	perl-Test-Builder-Tester = 1.24
Obsoletes:	perl-Test-Builder-Tester = 0:1.01
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(threads)' 'perl(threads::shared)'

%description
AHHHHHHH!!!! NOT TESTING! Anything but testing! Beat me, whip me, send
me to Detroit, but don't make me write tests!
   -- perldoc Test::Tutorial

Test::Simple is an extremely simple, extremely basic module for
writing tests suitable for CPAN modules and other pursuits. If you
wish to do more complicated testing, use the Test::More module (a
drop-in replacement for this one).

The purpose of Test::More is to provide a wide range of testing
utilities. Various ways to say "ok" with better diagnostics,
facilities to skip tests, test future features and compare complicated
data structures. While you can do almost anything with a simple "ok()"
function, it doesn't provide good diagnostic output.

%description -l pl.UTF-8
AAAAAAAA!!! NIE TESTOWANIE! Wszystko tylko nie testowanie! Bijcie
mnie, biczujcie mnie, wyślijcie do Detroit, ale nie każcie pisać
testów!
   -- perldoc Test::Tutorial

Test::Simple jest bardzo prostym, bardzo podstawowym modułem do
pisania testów pasujących do modułów CPAN i innych. Do bardziej
skomplikowanych testów lepiej używać modułu Test::More (zastępującego
ten).

Celem Test::More jest dostarczenie szerokiego zakresu narzędzi do
testowania. Różne sposoby powiedzenia "ok" z lepszą diagnostyką,
ułatwienia przy pomijaniu testów, testowaniu przyszłych możliwości i
porównywaniu skomplikowanych struktur danych. O ile można zrobić
prawie wszystko prostą funkcją "ok()", nie daje ona dobrego wyjścia
diagnostycznego.

%prep
%setup -q -n %{pdir}-%{pnam}-%{fver}
%{__perl} -nli -e 'print unless /^\s+sleep\s+\d+;\s*/' Makefile.PL

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Test/Tutorial.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Test/Builder
%{perl_vendorlib}/Test/Builder.pm
%{perl_vendorlib}/Test/More.pm
%{perl_vendorlib}/Test/Simple.pm
%{_mandir}/man3/Test::Builder*.3pm*
%{_mandir}/man3/Test::More.3pm*
%{_mandir}/man3/Test::Simple.3pm*
%{_mandir}/man3/Test::Tutorial.3pm*
