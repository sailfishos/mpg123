Name:           mpg123
Version:        1.25.10
Release:        1
Summary:        Console MPEG audio player and decoder library
License:        LGPLv2
Url:            http://www.mpg123.de/
Source0:        https://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(libpulse)

%description
The mpg123 distribution contains an MPEG 1.0/2.0/2.5 audio player/decoder for
layers 1, 2 and 3 (most commonly MPEG 1.0 Layer 3 aka MP3), as well as re-usable decoding
and output libraries.

%package devel
Summary:        Files to develop against libmpg123
Requires:       libmpg123 = %{version}

%description devel
The mpg123 distribution contains an MPEG 1.0/2.0/2.5 audio player/decoder for
layers 1, 2 and 3 (most commonly MPEG 1.0 Layer 3 aka MP3), as well as re-usable decoding
and output libraries.

%package -n libmpg123
Summary:        MPEG audio decoder library

%description -n libmpg123
MPEG 1.0/2.0/2.5 audio decoder library for layers 1, 2 and 3 (most
commonly MPEG 1.0 Layer 3 aka MP3).

%prep
%autosetup -n %{name}-%{version}/mpg123

%build
%configure \
    --enable-modules=yes \
    --with-module-suffix=.so \
    --with-default-audio=pulse \
%ifarch %{arm32}
    --with-cpu=arm_fpu \
%endif
%ifarch %{ix86}
    --with-cpu=x86 \
%endif
%ifarch x86_64
    --with-cpu=x86-64 \
%endif
%ifarch %{arm64}
    --with-cpu=aarch64 \
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

