%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Simple
Summary:	Test::Simple Perl module
Summary(cs):	Modul Test::Simple pro Perl
Summary(da):	Perlmodul Test::Simple
Summary(de):	Test::Simple Perl Modul
Summary(es):	Módulo de Perl Test::Simple
Summary(fr):	Module Perl Test::Simple
Summary(it):	Modulo di Perl Test::Simple
Summary(ja):	Test::Simple Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Test::Simple ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Test::Simple
Summary(pl):	Modu³ Perla Test::Simple
Summary(pt):	Módulo de Perl Test::Simple
Summary(pt_BR):	Módulo Perl Test::Simple
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Test::Simple
Summary(sv):	Test::Simple Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Test::Simple
Summary(zh_CN):	Test::Simple Perl Ä£¿é
Name:		perl-%{pdir}-%{pnam}
Version:	0.46
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
To jest bardzo prosty, bardzo podstawowy modu³ do pisania testów
pasuj±cych do modu³ów CPAN i innych. Do bardziej skomplikowanych
testów lepiej u¿ywaæ modu³u Test::More (zastêpuj±cego ten).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_sitelib}/Test/*.pm
%{_mandir}/man3/*
