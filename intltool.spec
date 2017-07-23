#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE1A701D4C9DE75B5 (dobey.pwns@gmail.com)
#
Name     : intltool
Version  : 0.51.0
Release  : 17
URL      : https://launchpad.net/intltool/trunk/0.51.0/+download/intltool-0.51.0.tar.gz
Source0  : https://launchpad.net/intltool/trunk/0.51.0/+download/intltool-0.51.0.tar.gz
Source99 : https://launchpad.net/intltool/trunk/0.51.0/+download/intltool-0.51.0.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: intltool-bin
Requires: intltool-data
Requires: intltool-doc
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
Requires: intltool-data

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
Requires: intltool-bin
Requires: intltool-data
Provides: intltool-devel

%description dev
dev components for the intltool package.


%package doc
Summary: doc components for the intltool package.
Group: Documentation

%description doc
doc components for the intltool package.


%prep
%setup -q -n intltool-0.51.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1500769620
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1500769620
rm -rf %{buildroot}
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

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man8/*
