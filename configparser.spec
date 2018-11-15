#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : configparser
Version  : 3.5.0
Release  : 34
URL      : https://files.pythonhosted.org/packages/7c/69/c2ce7e91c89dc073eb1aa74c0621c3eefbffe8216b3f9af9d3885265c01c/configparser-3.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/7c/69/c2ce7e91c89dc073eb1aa74c0621c3eefbffe8216b3f9af9d3885265c01c/configparser-3.5.0.tar.gz
Summary  : This library brings the updated configparser from Python 3.5 to Python 2.6-3.5.
Group    : Development/Tools
License  : MIT
Requires: configparser-python = %{version}-%{release}
Requires: configparser-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils23
BuildRequires : buildreq-distutils3
BuildRequires : setuptools-legacypython

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
Requires: configparser-python3 = %{version}-%{release}

%description python
python components for the configparser package.


%package python3
Summary: python3 components for the configparser package.
Group: Default
Requires: python3-core

%description python3
python3 components for the configparser package.


%prep
%setup -q -n configparser-3.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542243053
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1542243053
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
