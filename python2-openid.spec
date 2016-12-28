Name:		python2-openid
Version:	2.2.5
Release:	1
Summary:	Python OpenID libraries
Group:		Development/Python
License:	Apache License
URL:		https://github.com/openid/python-openid/releases
Source0:	http://openidenabled.com/files/python-openid/packages/python-openid-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python2-setuptools
BuildRequires:	python2-devel

%description
The OpenID library with batteries included.

Features of the 2.x.x series include:

 * Refined and easy-to-use API.

 * Extensive documentation.

 * Many storage implemetations including file-based, sqlite,
   postgresql, and mysql.

 * Simple examples to help you get started.

 * Licensed under the Apache Software License.

 * Includes a Simple Registration API

 * Versions 1.x.x supports protocol version 1; versions 2.x.x support
   both major OpenID protocol versions transparently


%prep
%setup -qn python-openid-%{version}
find . -type f | xargs chmod a-x

%build
python2 setup.py build

%check
#python admin/runtests

%install
python2 setup.py install \
	--skip-build --root %{buildroot} --record=INSTALLED_FILES

%files
%doc background-associations.txt LICENSE NEWS README examples
%{python2_sitelib}/*

