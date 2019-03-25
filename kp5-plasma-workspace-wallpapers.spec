%define		kdeplasmaver	5.15.3
%define		qtver		5.9.0
%define		kpname		plasma-workspace-wallpapers

Summary:	KDE Plasma Workspace Wallpapers
Name:		kp5-%{kpname}
Version:	5.15.3
Release:	1
License:	LGPL v2.1+
Group:		X11
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	7006c1d844dd8d23fa6c4e18af645860
URL:		http://www.kde.org/
BuildRequires:	cmake >= 2.8.12
BuildRequires:	ninja
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
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/wallpapers/Autumn
%{_datadir}/wallpapers/BytheWater
%{_datadir}/wallpapers/ColdRipple
%{_datadir}/wallpapers/ColorfulCups
%{_datadir}/wallpapers/DarkestHour
%{_datadir}/wallpapers/EveningGlow
%{_datadir}/wallpapers/FallenLeaf
%{_datadir}/wallpapers/FlyingKonqui
%{_datadir}/wallpapers/Grey
%{_datadir}/wallpapers/Kite
%{_datadir}/wallpapers/OneStandsOut
%{_datadir}/wallpapers/PastelHills
%{_datadir}/wallpapers/Path
%{_datadir}/wallpapers/Canopee
%{_datadir}/wallpapers/Cascade
%{_datadir}/wallpapers/Kokkini
%{_datadir}/wallpapers/Opal
%{_datadir}/wallpapers/summer_1am
