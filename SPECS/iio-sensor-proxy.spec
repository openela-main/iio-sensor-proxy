Name:           iio-sensor-proxy
Version:        2.4
Release:        3%{?dist}
Summary:        IIO accelerometer sensor to input device proxy

License:        GPLv3+
URL:            https://github.com/hadess/iio-sensor-proxy
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  systemd
%{?systemd_requires}

%description
%{summary}.

%package docs
Summary:        Documentation for %{name}
BuildArch:      noarch

%description docs
This package contains the documentation for %{name}.

%prep
%autosetup

%build
%configure \
  --disable-silent-rules \
  --enable-gtk-doc       \
  --disable-gtk-tests    \ # not really interested in sample progs
  %{nil}
%make_build

%install
%make_install

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license COPYING
%doc README
%{_bindir}/monitor-sensor
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
%{_udevrulesdir}/*-%{name}.rules
%{_sysconfdir}/dbus-1/system.d/net.hadess.SensorProxy.conf

%files docs
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%{_datadir}/gtk-doc/html/%{name}/

%changelog
* Sun Feb 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.4-3
- Add BuildRequires: make/gcc

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 02 2017 Bastien Nocera <bnocera@redhat.com> - 2.4-1
+ iio-sensor-proxy-2.4-1
- Update to 2.4

* Wed Sep 20 2017 Bastien Nocera <bnocera@redhat.com> - 2.3-1
+ iio-sensor-proxy-2.3-1
- Update to 2.3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2-1
- Update to 2.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.1-1
- Update to 2.1

* Mon Dec 12 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.0-1
- Update to 2.0

* Fri Nov 18 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.3-2
- Don't use hwdb update macro
- Trivial fixes

* Sat Sep 17 2016 Bastien Nocera <bnocera@redhat.com> - 1.3-1
- Update to 1.3

* Tue Sep 06 2016 Bastien Nocera <bnocera@redhat.com> - 1.2-1
- Update to 1.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 23 2015 Igor Gnatenko <ignatenko@src.gnome.org> - 1.1-1
- Update to 1.1
- Add -docs subpackage

* Tue Jun 23 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0-6
- Fix udev rule (RHBZ #1234744)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0-4
- use real license (GPLv3+)

* Sun May 24 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0-3
- Fix license tag
- Disable silent building

* Sat May 23 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0-2
- Use _udevrules dir instead of custom detecting rules dir

* Sat May 23 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0-1
- Initial package
