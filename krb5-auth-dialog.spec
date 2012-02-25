%define build_heimdal 0
%{?_with_heimdal: %{expand: %%global build_heimdal 1}}

Summary:	Kerberos 5 authentication dialog
Name:		krb5-auth-dialog
Version:	3.2.1
Release:	1
License:	GPLv2+
Group:		System/Base
URL:		http://www.redhat.com/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires: flex
BuildRequires: GConf2
BuildRequires: gnome-doc-utils
BuildRequires: intltool
BuildRequires: libcap-devel
BuildRequires: pam-devel
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(gconf-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libnm-glib)
BuildRequires: pkgconfig(libnotify)
%if %build_heimdal
BuildRequires: heimdal-devel
%else
BuildRequires: krb5-devel
%endif

%description
This package contains a dialog that warns the user when their Kerberos
tickets are about to expire and lets them renew them.

%prep
%setup -q

%build
%configure2_5x \
	--enable-debug \
	--disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc README AUTHORS NEWS
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_bindir}/krb5-auth-dialog
#{_bindir}/krb5-auth-dialog-preferences
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/libka-plugin-afs.*
%{_libdir}/%{name}/plugins/libka-plugin-dummy.*
%{_libdir}/%{name}/plugins/libka-plugin-pam.*
%{_datadir}/krb5-auth-dialog/
%{_datadir}/icons/hicolor/*/status/*
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/xdg/autostart/krb5-auth-dialog.desktop
#{_datadir}/applications/krb5-auth-dialog-preferences.desktop
%{_datadir}/dbus-1/services/org.gnome.KrbAuthDialog.service

