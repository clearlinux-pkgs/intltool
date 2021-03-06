#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE1A701D4C9DE75B5 (dobey.pwns@gmail.com)
#
Name     : intltool
Version  : 0.51.0
Release  : 26
URL      : https://launchpad.net/intltool/trunk/0.51.0/+download/intltool-0.51.0.tar.gz
Source0  : https://launchpad.net/intltool/trunk/0.51.0/+download/intltool-0.51.0.tar.gz
Source1  : https://launchpad.net/intltool/trunk/0.51.0/+download/intltool-0.51.0.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: intltool-bin = %{version}-%{release}
Requires: intltool-data = %{version}-%{release}
Requires: intltool-license = %{version}-%{release}
Requires: intltool-man = %{version}-%{release}
Requires: perl(XML::Parser)
BuildRequires : perl(XML::Parser)
Patch1: perlfixes.patch

%description
===============
these at http://bugs.launchpad.net/intltool on Launchpad. Patches are
also very welcome. See HACKING for more information on submitting patches.

%package bin
Summary: bin components for the intltool package.
Group: Binaries
Requires: intltool-data = %{version}-%{release}
Requires: intltool-license = %{version}-%{release}

%description bin
bin components for the intltool package.


%package data
Summary: data components for the intltool package.
Group: Data

%description data
data components for the intltool package.


%package dev
Summary: dev components for the intltool package.
Group: Development
Requires: intltool-bin = %{version}-%{release}
Requires: intltool-data = %{version}-%{release}
Provides: intltool-devel = %{version}-%{release}
Requires: intltool = %{version}-%{release}

%description dev
dev components for the intltool package.


%package license
Summary: license components for the intltool package.
Group: Default

%description license
license components for the intltool package.


%package man
Summary: man components for the intltool package.
Group: Default

%description man
man components for the intltool package.


%prep
%setup -q -n intltool-0.51.0
cd %{_builddir}/intltool-0.51.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607983720
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1607983720
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/intltool
cp %{_builddir}/intltool-0.51.0/COPYING %{buildroot}/usr/share/package-licenses/intltool/dfac199a7539a404407098a2541b9482279f690d
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/intltool-extract
/usr/bin/intltool-merge
/usr/bin/intltool-prepare
/usr/bin/intltool-update
/usr/bin/intltoolize

%files data
%defattr(-,root,root,-)
/usr/share/intltool/Makefile.in.in

%files dev
%defattr(-,root,root,-)
/usr/share/aclocal/*.m4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/intltool/dfac199a7539a404407098a2541b9482279f690d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/intltool-extract.8
/usr/share/man/man8/intltool-merge.8
/usr/share/man/man8/intltool-prepare.8
/usr/share/man/man8/intltool-update.8
/usr/share/man/man8/intltoolize.8
