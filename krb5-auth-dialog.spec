%define libgnomeui_version 2.9.1
%define krb5_version 1.4
%define libnm_version 0.5
%define dbus_version 0.90

Summary: Kerberos 5 authentication dialog
Name: krb5-auth-dialog
Version: 0.7
Release: %mkrel 7.1
License: GPLv2+
Group: System/Base
URL: http://www.redhat.com/
Source0: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libglade2.0-devel
BuildRequires: gnomeui2-devel >= %{libgnomeui_version}
BuildRequires: krb5-devel >= %{krb5_version}
BuildRequires: dbus-devel >= %{dbus_version}
BuildRequires: perl-XML-Parser, gettext
%ifnarch s390 s390x
BuildRequires: NetworkManager-glib-devel >= %{libnm_version}
%endif
#Requires: libgnomeui >= %{libgnomeui_version}
Requires: krb5-libs >= %{krb5_version}

Patch1: krb5-auth-dialog-0.7-sm-disable.patch
Patch2: desktop-file-comment.patch

%description
This package contains a dialog that warns the user when their Kerberos
tickets are about to expire and lets them renew them.

%prep
%setup -q
%patch1 -p1 -b .sm-disable
%patch2 -p1 -b .comment

%build
%configure2_5x
%make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %name

%clean
%{__rm} -rf $RPM_BUILD_ROOT


%files -f %name.lang
%defattr(-,root,root,-)
%doc
%{_bindir}/krb5-auth-dialog
%{_datadir}/krb5-auth-dialog/
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/xdg/autostart/krb5-auth-dialog.desktop


