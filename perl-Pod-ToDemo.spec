%define upstream_name    Pod-ToDemo
%define upstream_version 1.20110709

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Writes a demo program from a tutorial POD
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Simple)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Pod::ToDemo allows you to write POD-only modules that serve as tutorials which
can write out demo programs if you invoke them directly.  That is, while
SDL::Tutorial is a tutorial on writing beginner SDL applications with Perl,
you can invoke it as:

  $ perl -MSDL::Tutorial=sdl_demo.pl -e 1

and it will write a bare-bones demo program called sdl_demo.pl based on the
tutorial.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
rm -f t/0-signature.t

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Pod


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.201.107.90-3mdv2012.0
+ Revision: 765602
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.201.107.90-1
+ Revision: 690310
- update to new version 1.20110709

* Wed Jun 15 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.201.106.140-1
+ Revision: 685332
- update to new version 1.20110614

* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.201.106.130-1
+ Revision: 684783
- update to new version 1.20110613

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.10.0-2
+ Revision: 667298
- mass rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-1mdv2011.0
+ Revision: 404308
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.01-3mdv2009.1
+ Revision: 351752
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.01-2mdv2009.0
+ Revision: 224000
- rebuild

* Mon Feb 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2008.1
+ Revision: 165074
- import perl-Pod-ToDemo


* Mon Feb 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2008.1
- first mdv release  
