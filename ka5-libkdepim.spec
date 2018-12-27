%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		libkdepim
Summary:	libkdepim
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	46bd64a4514e05bbfc9821e1efa08435
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Designer-devel
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5UiTools-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-akonadi-contacts-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-search-devel >= %{kdeappsver}
BuildRequires:	ka5-kcalcore-devel >= %{kdeappsver}
BuildRequires:	ka5-kcontacts-devel >= %{kdeappsver}
BuildRequires:	ka5-kldap-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kcmutils-devel >= 5.51.0
BuildRequires:	kf5-kcodecs-devel >= 5.51.0
BuildRequires:	kf5-kcompletion-devel >= 5.51.0
BuildRequires:	kf5-kconfig-devel >= 5.51.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.51.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.51.0
BuildRequires:	kf5-ki18n-devel >= 5.51.0
BuildRequires:	kf5-kiconthemes-devel >= 5.51.0
BuildRequires:	kf5-kio-devel >= 5.51.0
BuildRequires:	kf5-kitemviews-devel >= 5.51.0
BuildRequires:	kf5-kjobwidgets-devel >= 5.51.0
BuildRequires:	kf5-kwallet-devel >= 5.51.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.51.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for common kdepim apps.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname}_qt --with-qm --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}_qt.lang
%defattr(644,root,root,755)
/etc/xdg/libkdepim.categories
/etc/xdg/libkdepim.renamecategories
%attr(755,root,root) %ghost %{_libdir}/libKF5Libkdepim.so.5
%attr(755,root,root) %{_libdir}/libKF5Libkdepim.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5LibkdepimAkonadi.so.5
%attr(755,root,root) %{_libdir}/libKF5LibkdepimAkonadi.so.5.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/kdepimakonadiwidgets.so
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/kdepimwidgets.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_ldap.so
%{_datadir}/dbus-1/interfaces/org.kde.addressbook.service.xml
%{_datadir}/dbus-1/interfaces/org.kde.mailtransport.service.xml
%dir %{_datadir}/kdepimwidgets
%dir %{_datadir}/kdepimwidgets/pics
%{_datadir}/kdepimwidgets/pics/addresseelineedit.png
%{_datadir}/kdepimwidgets/pics/clicklineedit.png
%{_datadir}/kdepimwidgets/pics/kdateedit.png
%{_datadir}/kdepimwidgets/pics/ktimeedit.png
%{_datadir}/kservices5/kcmldap.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/Libkdepim
%{_includedir}/KF5/LibkdepimAkonadi
%{_includedir}/KF5/libkdepim
%{_includedir}/KF5/libkdepim_version.h
%{_includedir}/KF5/libkdepimakonadi
%{_includedir}/KF5/libkdepimakonadi_version.h
%{_libdir}/cmake/KF5Libkdepim
%{_libdir}/cmake/KF5LibkdepimAkonadi
%{_libdir}/cmake/MailTransportDBusService
%attr(755,root,root) %{_libdir}/libKF5Libkdepim.so
%attr(755,root,root) %{_libdir}/libKF5LibkdepimAkonadi.so
%{_libdir}/qt5/mkspecs/modules/qt_Libkdepim.pri
%{_libdir}/qt5/mkspecs/modules/qt_LibkdepimAkonadi.pri
