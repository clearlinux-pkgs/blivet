#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : blivet
Version  : 3.4.2
Release  : 14
URL      : https://files.pythonhosted.org/packages/b5/40/037c3deb3eaf8e7ca91fa39098947537d62b8038e64ff773f0827786e3f6/blivet-3.4.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/b5/40/037c3deb3eaf8e7ca91fa39098947537d62b8038e64ff773f0827786e3f6/blivet-3.4.2.tar.gz
Summary  : Python module for system storage configuration
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1+
Requires: blivet-data = %{version}-%{release}
Requires: blivet-libexec = %{version}-%{release}
Requires: blivet-license = %{version}-%{release}
Requires: blivet-python = %{version}-%{release}
Requires: blivet-python3 = %{version}-%{release}
Requires: blivet-services = %{version}-%{release}
Requires: pygobject
Requires: pyudev
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pygobject
BuildRequires : pyudev
BuildRequires : six

%description
The python-blivet package is a python module for examining and modifying
storage configuration.

%package data
Summary: data components for the blivet package.
Group: Data

%description data
data components for the blivet package.


%package libexec
Summary: libexec components for the blivet package.
Group: Default
Requires: blivet-license = %{version}-%{release}

%description libexec
libexec components for the blivet package.


%package license
Summary: license components for the blivet package.
Group: Default

%description license
license components for the blivet package.


%package python
Summary: python components for the blivet package.
Group: Default
Requires: blivet-python3 = %{version}-%{release}

%description python
python components for the blivet package.


%package python3
Summary: python3 components for the blivet package.
Group: Default
Requires: python3-core
Provides: pypi(blivet)
Requires: pypi(pyudev)
Requires: pypi(six)

%description python3
python3 components for the blivet package.


%package services
Summary: services components for the blivet package.
Group: Systemd services

%description services
services components for the blivet package.


%prep
%setup -q -n blivet-3.4.2
cd %{_builddir}/blivet-3.4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633019629
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/blivet
cp %{_builddir}/blivet-3.4.2/COPYING %{buildroot}/usr/share/package-licenses/blivet/4cc77b90af91e615a64ae04893fdffa7939db84c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system-services/com.redhat.Blivet0.service

%files libexec
%defattr(-,root,root,-)
/usr/libexec/blivetd

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/blivet/4cc77b90af91e615a64ae04893fdffa7939db84c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/blivet.service
