#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : configparser
Version  : 3.5.0b2
Release  : 4
URL      : https://pypi.python.org/packages/source/c/configparser/configparser-3.5.0b2.tar.gz
Source0  : https://pypi.python.org/packages/source/c/configparser/configparser-3.5.0b2.tar.gz
Summary  : This library brings the updated configparser from Python 3.5 to Python 2.6-3.5.
Group    : Development/Tools
License  : MIT
Requires: configparser-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
============
configparser
============
The ancient ``ConfigParser`` module available in the standard library 2.x has
seen a major update in Python 3.2. This is a backport of those changes so that
they can be used directly in Python 2.6 - 3.5.

%package python
Summary: python components for the configparser package.
Group: Default

%description python
python components for the configparser package.


%prep
%setup -q -n configparser-3.5.0b2

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
