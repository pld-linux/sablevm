
# TODO:
# - Unpackaged files:
# /usr/include/jawt.h
# /usr/include/jawt_md.h
# /usr/lib/sablevm-classpath/libgjsmalsa.la
# /usr/lib/sablevm-classpath/libgtkpeer.la
# /usr/lib/sablevm-classpath/libjavaio.la
# /usr/lib/sablevm-classpath/libjavalang.la
# /usr/lib/sablevm-classpath/libjavalangreflect.la
# /usr/lib/sablevm-classpath/libjavanet.la
# /usr/lib/sablevm-classpath/libjavanio.la
# /usr/lib/sablevm-classpath/libjavautil.la
# /usr/lib/sablevm-classpath/libjawtgnu.la
# /usr/lib/sablevm/bin/jdb
# /usr/lib/security/classpath.security
# /usr/share/sablevm/AUTHORS
# /usr/share/sablevm/LGPL-2.1
# /usr/share/sablevm/LICENSE									

Summary:	Extremely portable, efficient, and specification-compliant Java virtual machine.
Summary(pl):	Przeno¶na i zgodna z specyfikacj± wirtualna maszyna Javy
Name:		sablevm
Version:	1.13
Release:	1
License:	LGPL
Group:		Development/Languages/Java
Source0:	http://sablevm.org/download/release/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d5828200032bfe921dd43e450931e38c
Source1:	http://sablevm.org/download/release/%{version}/%{name}-classpath-%{version}.tar.gz
# Source1-md5:	9476bb7a0ad67c6cfa353d06f094cdce
URL:		http://sablevm.org/
BuildRequires:	automake
BuildRequires:	jikes
BuildRequires:	libffi-devel
BuildRequires:	libltdl-devel
BuildRequires:	popt-devel
BuildRequires:	zlib-devel
Requires:	fastjar
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SableVM is a highly-portable Java virtual machine written in C, and
implementing the Java virtual machine specification, second edition.

%description -l pl
SableVM jest przeno¶n± maszyn± wirtualn± Javy napisan± w C, oraz 
implementuj±c± drugie wydanie specyfikacji maszyny wirtualnej Javy.

%package devel
Summary:	JNI header files for SableVM library
Summary(pl):	Pliki nag³ówkowe JNI dla biblioteki SableVM
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libffi-devel
Requires:	libltdl-devel
Requires:	zlib-devel

%description devel
JNI header files for SableVM library.

%description devel -l pl
Pliki nag³ówkowe JNI dla biblioteki SableVM.

%prep
%setup -q -a 1

%build
cp -f /usr/share/automake/config.sub .
CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti"
%configure
%{__make}

cd %{name}-classpath-%{version}
cp -f /usr/share/automake/config.sub .
CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti"
%configure \
	--with-jikes
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd %{name}-classpath-%{version}

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
%dir %{_libdir}/%{name}-classpath
%attr(755,root,root) %{_libdir}/%{name}-classpath/*.so
%dir %{_datadir}/%{name}-classpath
%{_datadir}/%{name}-classpath/*.jar

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsablevm.so
%{_libdir}/libsablevm.la
%{_includedir}/jni*.h
