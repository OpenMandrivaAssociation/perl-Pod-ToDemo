%define module   Pod-ToDemo
%define version    1.01
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    writes a demo program from a tutorial POD
Source:     http://www.cpan.org/modules/by-module/Pod/%{module}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{module}
BuildRequires: perl-devel
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::Simple)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Pod::ToDemo allows you to write POD-only modules that serve as tutorials which
can write out demo programs if you invoke them directly.  That is, while
SDL::Tutorial is a tutorial on writing beginner SDL applications with Perl,
you can invoke it as:

  $ perl -MSDL::Tutorial=sdl_demo.pl -e 1

and it will write a bare-bones demo program called sdl_demo.pl based on the
tutorial.

%prep
%setup -q -n %{module}-%{version} 
rm -f t/0-signature.t

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Pod

