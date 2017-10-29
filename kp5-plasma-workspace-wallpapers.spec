%define		kdeplasmaver	5.11.2
%define		qtver		5.3.2
%define		kpname		plasma-workspace-wallpapers

Summary:	KDE Plasma Workspace Wallpapers
Name:		kp5-%{kpname}
Version:	5.11.2
Release:	1
License:	LGPL v2.1+
Group:		X11
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	ef9cc5a0e5f030bca9fa0189d378e283
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
