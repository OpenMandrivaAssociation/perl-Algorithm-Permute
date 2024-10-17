%define upstream_name    Algorithm-Permute
%define upstream_version 0.12

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	7

Summary:    Handy and fast permutation with OO interface
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Algorithm/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This handy module makes performing permutation in Perl easy and fast,
although perhaps its algorithm is not the fastest on the earth. It supports
permutation r of n objects where 0 < r <= n. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.120.0-5
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.120.0-4
+ Revision: 680448
- mass rebuild

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.120.0-3mdv2011.0
+ Revision: 555417
- rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-2mdv2010.0
+ Revision: 405952
- force rebuild
- rebuild using %%perl_convert_version
- fixed license field

* Fri Feb 20 2009 Jérôme Quelin <jquelin@mandriva.org> 0.12-1mdv2009.1
+ Revision: 343337
- import perl-Algorithm-Permute


* Fri Feb 20 2009 cpan2dist 0.12-1mdv
- initial mdv release, generated with cpan2dist

