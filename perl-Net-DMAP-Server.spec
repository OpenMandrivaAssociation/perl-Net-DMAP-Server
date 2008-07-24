%define realname Net-DMAP-Server

Summary: Base class for D[A-Z]AP servers
Name: perl-Net-DMAP-Server
Version: 0.05
Release: %mkrel 3
License: Artistic
Group: Development/Perl
URL: http://search.cpan.org/dist/Net-DMAP-Server/

Source: http://www.cpan.org/modules/by-module/Net/Net-DMAP-Server-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl-Net-DAAP-DMAP
BuildRequires: perl-Net-Rendezvous-Publish
BuildRequires: perl-POE-Component-Server-HTTP

%description
A base class for D[A-Z]AP servers.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT/%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*
