#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Devel-ArgNames
Version  : 0.03
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/N/NU/NUFFIN/Devel-ArgNames-0.03.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NU/NUFFIN/Devel-ArgNames-0.03.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libd/libdevel-argnames-perl/libdevel-argnames-perl_0.03-2.debian.tar.xz
Summary  : ~
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Devel-ArgNames-license = %{version}-%{release}
Requires: perl-Devel-ArgNames-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(PadWalker)

%description
No detailed description available

%package dev
Summary: dev components for the perl-Devel-ArgNames package.
Group: Development
Provides: perl-Devel-ArgNames-devel = %{version}-%{release}
Requires: perl-Devel-ArgNames = %{version}-%{release}

%description dev
dev components for the perl-Devel-ArgNames package.


%package license
Summary: license components for the perl-Devel-ArgNames package.
Group: Default

%description license
license components for the perl-Devel-ArgNames package.


%package perl
Summary: perl components for the perl-Devel-ArgNames package.
Group: Default
Requires: perl-Devel-ArgNames = %{version}-%{release}

%description perl
perl components for the perl-Devel-ArgNames package.


%prep
%setup -q -n Devel-ArgNames-0.03
cd %{_builddir}
tar xf %{_sourcedir}/libdevel-argnames-perl_0.03-2.debian.tar.xz
cd %{_builddir}/Devel-ArgNames-0.03
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Devel-ArgNames-0.03/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Devel-ArgNames
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Devel-ArgNames/1b827b04fc2f893e2ae0c698fb5ca1c544d3ffba
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Devel::ArgNames.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Devel-ArgNames/1b827b04fc2f893e2ae0c698fb5ca1c544d3ffba

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/Devel/ArgNames.pm
