#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : configparser
Version  : 3.5.0.b2
Release  : 15
URL      : http://pypi.debian.net/configparser/configparser-3.5.0b2.tar.gz
Source0  : http://pypi.debian.net/configparser/configparser-3.5.0b2.tar.gz
Summary  : This library brings the updated configparser from Python 3.5 to Python 2.6-3.5.
Group    : Development/Tools
License  : MIT
Requires: configparser-legacypython
Requires: configparser-python3
Requires: configparser-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
configparser
        ============
        
        The ancient ``ConfigParser`` module available in the standard library 2.x has
        seen a major update in Python 3.2. This is a backport of those changes so that
        they can be used directly in Python 2.6 - 3.5.
        
        To use the ``configparser`` backport instead of the built-in version on both

%package legacypython
Summary: legacypython components for the configparser package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the configparser package.


%package python
Summary: python components for the configparser package.
Group: Default
Requires: configparser-legacypython
Requires: configparser-python3

%description python
python components for the configparser package.


%package python3
Summary: python3 components for the configparser package.
Group: Default
Requires: python3-core

%description python3
python3 components for the configparser package.


%prep
%setup -q -n configparser-3.5.0b2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507151886
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1507151886
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
