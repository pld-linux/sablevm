Summary:	Extremely portable, efficient, and specification-compliant Java virtual machine.
Summary(pl):	Przenośna i zgodna z specyfikacją wirtualna maszyna Javy
Name:		sablevm
Version:	1.1.8
Release:	1
License:	LGPL
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/sablevm/%{name}-%{version}.tar.gz
# Source0-md5:	f9ed65b7d7bc685d05a50882f3c4fc97
URL:		http://sablevm.org/
BuildRequires:	automake
BuildRequires:	libffi-devel
BuildRequires:	libltdl-devel
BuildRequires:	popt-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SableVM is a highly-portable Java virtual machine written in C, and
implementing the Java virtual machine specification, second edition.

%description -l pl
SableVM jest przenośną maszyną wirtualną Javy napisaną w C, oraz 
implementującą drugie wydanie specyfikacji maszyny wirtualnej Javy.

%package devel
Summary:	JNI header files for SableVM library
Summary(pl):	Pliki nagłówkowe JNI dla biblioteki SableVM
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libffi-devel
Requires:	libltdl-devel
Requires:	zlib-devel

%description devel
JNI header files for SableVM library.

%description devel -l pl
Pliki nagłówkowe JNI dla biblioteki SableVM.

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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libsablevm-*.so
%{_mandir}/man?/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsablevm.so
%{_libdir}/libsablevm.la
%{_includedir}/jni*.h
