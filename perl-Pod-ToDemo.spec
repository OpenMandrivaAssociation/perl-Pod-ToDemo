%define modname	Pod-ToDemo
%define modver	1.20110709

Summary:	Writes a demo program from a tutorial POD
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Pod/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Simple)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl-devel

%description
Pod::ToDemo allows you to write POD-only modules that serve as tutorials which
can write out demo programs if you invoke them directly.  That is, while
SDL::Tutorial is a tutorial on writing beginner SDL applications with Perl,
you can invoke it as:

  $ perl -MSDL::Tutorial=sdl_demo.pl -e 1

and it will write a bare-bones demo program called sdl_demo.pl based on the
tutorial.

%prep
%setup -qn %{modname}-%{modver}
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
%{perl_vendorlib}/Pod
%{_mandir}/man3/*

