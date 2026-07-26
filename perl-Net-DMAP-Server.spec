%define upstream_name    Net-DMAP-Server
Name:		perl-%{upstream_name}
Version:	0.05
Release:	6

Summary:	Base class for D[A-Z]AP servers
License:	Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Net-DMAP-Server
Source0:	https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Net-DMAP-Server-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Net::DAAP::DMAP)
BuildRequires:	perl(Net::Rendezvous::Publish)
BuildRequires:	perl(POE::Component::Server::HTTP)
BuildArch:	noarch

%description
A base class for D[A-Z]AP servers.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std
rm -rf %{buildroot}%{perl_vendorarch}

%files
%defattr(-, root, root, 0755)
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 404090
- rebuild using %0.05 Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.05-4mdv2009.0
+ Revision: 258009
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.05-3mdv2009.0
+ Revision: 246062
- rebuild

* Sun Mar 23 2008 Stefan van der Eijk <stefan@mandriva.org> 0.05-1mdv2008.1
+ Revision: 189545
- import perl-Net-DMAP-Server


