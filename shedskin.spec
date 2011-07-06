Summary:    An experimental python to c++ compiler
Name:       shedskin
Version:    0.8
Release:    %mkrel 1
Source0:    http://schedskin.googlecode.com/files/shedskin-%version.tgz
License:	GPLv3
Group:		Development/Python
Url:		http://code.google.com/p/shedskin/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-devel

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
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root) 
%doc README.html examples
%_bindir/%name
%{py_sitedir}/%{name}/
%{py_sitedir}/%{name}-%{version}-py%{pyver}.egg-info
