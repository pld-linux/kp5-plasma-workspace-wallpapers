%define		kdeplasmaver	5.4.0
%define		qtver		5.3.2
%define		kpname		plasma-workspace-wallpapers

Summary:	KDE Plasma Workspace Wallpapers
Name:		kp5-%{kpname}
Version:	5.4.0
Release:	1
License:	LGPL v2.1+
Group:		X11
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	8ad2e9423bd01f7302652fe3a79d2484
URL:		http://www.kde.org/
BuildRequires:	cmake >= 2.8.12
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE Plasma Workspace Wallpapers.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/wallpapers/Alps
%{_datadir}/wallpapers/BlueFlower
%{_datadir}/wallpapers/Dance_of_the_Spirits
%{_datadir}/wallpapers/Fog
%{_datadir}/wallpapers/ForestFog
%{_datadir}/wallpapers/ForestHouse
%{_datadir}/wallpapers/GereatHeron
%{_datadir}/wallpapers/Green_Leaves
%{_datadir}/wallpapers/Grey
%{_datadir}/wallpapers/IndianSummer
%{_datadir}/wallpapers/Landmannalaugar
%{_datadir}/wallpapers/Poppy
%{_datadir}/wallpapers/Spray
%{_datadir}/wallpapers/Sunset
%{_datadir}/wallpapers/Tauplitz
%{_datadir}/wallpapers/WalmendingerHorn
%{_datadir}/wallpapers/Water
%{_datadir}/wallpapers/Whisker_Grass
