Summary:	Extremely portable, efficient, and specification-compliant Java virtual machine.
Summary(pl):	Przeno¶na i zgodna z specyfikacj± wirtualna maszyna Javy
Name:		sablevm
Version:	1.1.6
Release:	1
License:	LGPL
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	94798274f59d9abbd7d09a1050d608de
URL:		http://sablevm.org/
BuildRequires:	automake
BuildRequires:	libffi-devel
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SableVM is a highly-portable Java virtual machine written in C, and
implementing the Java virtual machine specification, second edition.

%description -l pl
SableVM jest przeno¶n± maszyn± wirtualn± Javy napisan± w C, oraz 
implementuj±c± drugie wydanie specyfikacji maszyny wirtualnej Javy.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so
%{_mandir}/man?/*
