%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Simple
Summary:	Test::Simple perl module
Summary(pl):	Modu³ perla Test::Simple
Name:		perl-%{pdir}-%{pnam}
Version:	0.41
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-Test-Harness
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

gzip -9nf Changes README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Test
%{_mandir}/man3/*
