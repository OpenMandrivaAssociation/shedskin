Summary:    An experimental python to c++ compiler
Name:       shedskin
Version:    0.8
Release:    4
Source0:    http://schedskin.googlecode.com/files/shedskin-%{version}.tgz
License:	GPLv3
Group:		Development/Python
Url:		https://code.google.com/p/shedskin/
BuildRequires:	python-devel
Requires:	pkgconfig(bdw-gc)
BuildArch:	noarch

%description
Shed Skin is an experimental compiler, that can translate pure, but implicitly
statically typed Python (2.4-2.7) programs into optimized C++. It can generate
stand-alone programs or extension modules that can be imported and used in
larger Python programs. 

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}


%files
%doc README.html examples
%{_bindir}/%{name}
%{py_sitedir}/%{name}/
%{py_sitedir}/%{name}-%{version}-py%{py_ver}.egg-info

