%define libgnomeui_version 2.9.1
%define krb5_version 1.4
%define libnm_version 0.5
%define dbus_version 0.90

Summary: Kerberos 5 authentication dialog
Name: krb5-auth-dialog
Version: 0.10
Release: %mkrel 1
License: GPLv2+
Group: System/Base
URL: http://www.redhat.com/
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libcap-devel
BuildRequires: libglade2.0-devel
BuildRequires: libnotify-devel
BuildRequires: gnomeui2-devel >= %{libgnomeui_version}
BuildRequires: krb5-devel >= %{krb5_version}
BuildRequires: dbus-devel >= %{dbus_version}
BuildRequires: dbus-glib-devel
BuildRequires: intltool
BuildRequires: flex
BuildRequires: NetworkManager-glib-devel >= %{libnm_version}
#Requires: libgnomeui >= %{libgnomeui_version}
Requires: krb5-libs >= %{krb5_version}

%description
This package contains a dialog that warns the user when their Kerberos
tickets are about to expire and lets them renew them.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %name

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%post_install_gconf_schemas %name
%postun
%clean_scrollkeeper
%endif

%preun
%preun_uninstall_gconf_schemas %name


%files -f %name.lang
%defattr(-,root,root,-)
%doc README AUTHORS
%_sysconfdir/gconf/schemas/%name.schemas
%{_bindir}/krb5-auth-dialog
%{_bindir}/krb5-auth-dialog-preferences
%{_datadir}/krb5-auth-dialog/
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/xdg/autostart/krb5-auth-dialog.desktop
%_datadir/applications/krb5-auth-dialog-preferences.desktop
%_datadir/dbus-1/services/org.gnome.KrbAuthDialog.service

