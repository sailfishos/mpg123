Name:           mpg123
Version:        1.25.10
Release:        1
Summary:        Console MPEG audio player and decoder library
License:        LGPL-2.1-only
Group:          Productivity/Multimedia/Sound/Players
Url:            http://www.mpg123.de/
Source0:        https://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(libpulse)
%ifarch %{ix86} x86_64
BuildRequires:  yasm
%endif

%description
The mpg123 distribution contains an MPEG 1.0/2.0/2.5 audio player/decoder for
layers 1, 2 and 3 (most commonly MPEG 1.0 Layer 3 aka MP3), as well as re-usable decoding
and output libraries.

%package devel
Summary:        Files to develop against libmpg123
Group:          Development/Languages/C and C++
Requires:       libmpg123 = %{version}

%description devel
The mpg123 distribution contains an MPEG 1.0/2.0/2.5 audio player/decoder for
layers 1, 2 and 3 (most commonly MPEG 1.0 Layer 3 aka MP3), as well as re-usable decoding
and output libraries.

%package -n libmpg123
Summary:        MPEG audio decoder library
Group:          System/Libraries

%description -n libmpg123
MPEG 1.0/2.0/2.5 audio decoder library for layers 1, 2 and 3 (most
commonly MPEG 1.0 Layer 3 aka MP3).

%prep
%setup -q -n %{name}-%{version}/mpg123

%build
%configure \
    --enable-modules=yes \
    --with-module-suffix=.so \
    --with-default-audio=pulse \
%ifarch armv7hl
    --with-cpu=arm_fpu \
%endif
%ifarch %{ix86} x86_64
    --enable-yasm=yes \
%endif

make %{?_smp_mflags}

%install
%make_install

%post   -n libmpg123 -p /sbin/ldconfig
%postun -n libmpg123 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_bindir}/mpg123
%{_bindir}/mpg123-id3dump
%{_bindir}/mpg123-strip
%{_bindir}/out123
%{_mandir}/man1/mpg123.1*
%{_mandir}/man1/out123.1*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/output_dummy.so
%{_libdir}/%{name}/output_oss.so
%{_libdir}/%{name}/output_pulse.so

%files -n libmpg123
%defattr(-,root,root)
%doc COPYING
%{_libdir}/libmpg123.so.*
%{_libdir}/libout123.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/libmpg123.so
%{_libdir}/libout123.so
%{_libdir}/pkgconfig/libmpg123.pc
%{_libdir}/pkgconfig/libout123.pc
%{_includedir}/fmt123.h
%{_includedir}/mpg123.h
%{_includedir}/out123.h

