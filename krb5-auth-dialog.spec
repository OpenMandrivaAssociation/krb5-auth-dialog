%define build_heimdal 0
%{?_with_heimdal: %{expand: %%global build_heimdal 1}}

%define _disable_ld_no_undefined 1

Summary:	Kerberos 5 authentication dialog
Name:		krb5-auth-dialog
Version:	43.0
Release:	1
License:	GPLv2+
Group:		System/Base
URL:		http://www.redhat.com/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires: meson
BuildRequires: itstool
BuildRequires: flex
BuildRequires: bison
BuildRequires: GConf2
BuildRequires: pkgconfig(gnome-doc-utils)
BuildRequires: intltool
BuildRequires: cap-devel
BuildRequires: pam-devel
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(gconf-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
#BuildRequires: pkgconfig(libnm-glib)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(gcr-3)
%if %build_heimdal
BuildRequires: heimdal-devel
%else
BuildRequires: krb5-devel
%endif
buildrequires: scrollkeeper

%description
This package contains a dialog that warns the user when their Kerberos
tickets are about to expire and lets them renew them.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc README AUTHORS NEWS
#{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_bindir}/krb5-auth-dialog
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/libka-plugin-afs.*
%{_libdir}/%{name}/plugins/libka-plugin-dummy.*
%{_libdir}/%{name}/plugins/libka-plugin-pam.*
%{_libdir}/%{name}/plugins/libka-plugin-gnomelock.so
#{_datadir}/krb5-auth-dialog/
%{_datadir}/icons/hicolor/*/status/*
%{_datadir}/GConf/gsettings/org.gnome.KrbAuthDialog.convert
%{_datadir}/appdata/krb5-auth-dialog.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.KrbAuthDialog.gschema.xml
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/xdg/autostart/krb5-auth-dialog.desktop
%{_datadir}/applications/krb5-auth-dialog.desktop
%{_datadir}/dbus-1/services/org.gnome.KrbAuthDialog.service



%changelog
* Sat Feb 25 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.2.1-1
+ Revision: 780703
- new version 3.2.1
- cleaned up spec
- converted BRs to pkgconfig provides

* Sun May 22 2011 Funda Wang <fwang@mandriva.org> 0.17-3
+ Revision: 677118
- rebuild to add gconf2 as req

* Sat Apr 30 2011 Funda Wang <fwang@mandriva.org> 0.17-2
+ Revision: 661049
- fix build

* Sun Sep 12 2010 Götz Waschk <waschk@mandriva.org> 0.17-1mdv2011.0
+ Revision: 577679
- new version
- update file list

* Sun Jul 11 2010 Götz Waschk <waschk@mandriva.org> 0.16-1mdv2011.0
+ Revision: 551160
- update build deps
- new version
- update file list

* Sat Apr 03 2010 Götz Waschk <waschk@mandriva.org> 0.15-1mdv2010.1
+ Revision: 530891
- update to new version 0.15

* Fri Nov 06 2009 Götz Waschk <waschk@mandriva.org> 0.14-1mdv2010.1
+ Revision: 460893
- update to new version 0.14

* Mon Sep 28 2009 Götz Waschk <waschk@mandriva.org> 0.13-1mdv2010.0
+ Revision: 450667
- new version
- drop patch

* Sun Aug 30 2009 Götz Waschk <waschk@mandriva.org> 0.12-3mdv2010.0
+ Revision: 422661
- fix crash in preferences

* Tue Jul 28 2009 Götz Waschk <waschk@mandriva.org> 0.12-2mdv2010.0
+ Revision: 401522
- disable networkmanager support
- update file list

* Mon Jul 13 2009 Götz Waschk <waschk@mandriva.org> 0.12-1mdv2010.0
+ Revision: 395619
- update to new version 0.12

* Mon Jun 15 2009 Götz Waschk <waschk@mandriva.org> 0.11-1mdv2010.0
+ Revision: 386081
- new version
- update file list
- fix build deps

* Mon May 25 2009 Götz Waschk <waschk@mandriva.org> 0.10-1mdv2010.0
+ Revision: 379704
- drop patches
- new version

* Sun May 03 2009 Götz Waschk <waschk@mandriva.org> 0.9.1-1mdv2010.0
+ Revision: 371156
- new version
- drop patch 1
- new version
- rediff patches 0,3
- add missing file
- update file list
- update build deps

* Mon Jan 12 2009 Götz Waschk <waschk@mandriva.org> 0.8-2mdv2009.1
+ Revision: 328720
- drop patch 1

* Mon Jan 12 2009 Götz Waschk <waschk@mandriva.org> 0.8-1mdv2009.1
+ Revision: 328495
- new version
- update build deps
- fix source URL
- update file list
- rediff patch 1
- drop patch 2
- fix format strings and linking

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

* Mon May 19 2008 David Walluck <walluck@mandriva.org> 0.7-7.1mdv2009.0
+ Revision: 209088
- BuildRequires: libglade2.0-devel
- import krb5-auth-dialog


* Mon Feb 18 2008 Christopher Aillon <caillon@redhat.com> - 0.7-7
- Rebuild to celebrate my birthday (and GCC 4.3)

* Thu Nov  1 2007 Matthias Clasen <mclasen@redhat.com> - 0.7-6
- Fix the Comment field in the desktop file (#344351)

* Mon Oct 22 2007 Christopher Aillon <caillon@redhat.com> - 0.7-5
- Don't start multiple times in KDE (#344991)

* Fri Aug 24 2007 Adam Jackson <ajax@redhat.com> - 0.7-4
- Rebuild for build ID

* Mon Aug 13 2007 Christopher Aillon <caillon@redhat.com> 0.7-3
- Update the license tag

* Thu Mar 15 2007 Karsten Hopp <karsten@redhat.com> 0.7-2
- rebuild with current gtk2 to add png support (#232013)

* Mon Jul 24 2006 Christopher Aillon <caillon@redhat.com> - 0.7-1
- Update to 0.7
- Don't peg the network and CPU when the KDC is unavailable

* Wed Jul 19 2006 John (J5) Palmieri <johnp@redhat.com> - 0.6.cvs20060212-4
- rebuild for dbus 

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.6.cvs20060212-3.1
- rebuild

* Sat Jun 24 2006 Jesse Keating <jkeating@redhat.com> - 0.6.cvs20060212-3
- Add missing BRs perl-XML-Parser, gettext
- Work around no network manager stuff on z900s

* Sun Feb 12 2006 Christopher Aillon <caillon@redhat.com> - 0.6.cvs20060212-1
- Update to latest CVS to get some of Nalin's fixes

* Tue Feb  7 2006 Jesse Keating <jkeating@redhat.com> - 0.6-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Christopher Aillon <caillon@redhat.com> 0.6-1
- Update to 0.6, adding an autostart file

* Fri Dec  9 2005 Jesse Keating <jkeating@redhat.com> - 0.5-2.1
- rebuilt

* Thu Dec  1 2005 John (J5) Palmieri <johnp@redhat.com> - 0.5-2
- rebuild for new dbus

* Tue Nov  8 2005 Christopher Aillon <caillon@redhat.com> 0.5-1
- Update to 0.5

* Tue Nov  1 2005 Christopher Aillon <caillon@redhat.com> 0.4-1
- Update to 0.4

* Mon Oct 31 2005 Christopher Aillon <caillon@redhat.com> 0.3-1
- Update to 0.3, working with newer versions of krb5 and NetworkManager

* Tue Aug 16 2005 David Zeuthen <davidz@redhat.com>
- Rebuilt

* Tue Mar 22 2005 Nalin Dahyabhai <nalin@redhat.com> 0.2-5
- Change Requires: krb5 to krb5-libs, repeat $ -> %% fix for build requirements.

* Tue Mar 22 2005 Dan Williams <dcbw@redhat.com> 0.2-4
- Fix $ -> %% for Requires: krb5 >= ...

* Mon Mar 21 2005 David Zeuthen <davidz@redhat.com> 0.2-3
- Fix up BuildRequires and Requires (#134704)

* Fri Mar  4 2005 David Zeuthen <davidz@redhat.com> 0.2-2
- Rebuild

* Mon Aug 16 2004 GNOME <jrb@redhat.com> - auth-dialog
- Initial build.

