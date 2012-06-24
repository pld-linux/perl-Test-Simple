#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Simple
Summary:	Test::Simple Perl module
Summary(cs):	Modul Test::Simple pro Perl
Summary(da):	Perlmodul Test::Simple
Summary(de):	Test::Simple Perl Modul
Summary(es):	M�dulo de Perl Test::Simple
Summary(fr):	Module Perl Test::Simple
Summary(it):	Modulo di Perl Test::Simple
Summary(ja):	Test::Simple Perl �⥸�塼��
Summary(ko):	Test::Simple �� ����
Summary(nb):	Perlmodul Test::Simple
Summary(pl):	Modu� Perla Test::Simple
Summary(pt):	M�dulo de Perl Test::Simple
Summary(pt_BR):	M�dulo Perl Test::Simple
Summary(ru):	������ ��� Perl Test::Simple
Summary(sv):	Test::Simple Perlmodul
Summary(uk):	������ ��� Perl Test::Simple
Summary(zh_CN):	Test::Simple Perl ģ��
Name:		perl-Test-Simple
Version:	0.49
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e22ed16f8451c64277c7ef4fbd55251a
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
This is an extremely simple, extremely basic module for writing tests
suitable for CPAN modules and other pursuits. If you wish to do more
complicated testing, use the Test::More module (a drop-in replacement
for this one).

%description -l pl
To jest bardzo prosty, bardzo podstawowy modu� do pisania test�w
pasuj�cych do modu��w CPAN i innych. Do bardziej skomplikowanych
test�w lepiej u�ywa� modu�u Test::More (zast�puj�cego ten).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
