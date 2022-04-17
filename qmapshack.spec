Summary:	GPS mapping and management tool
Name:		qmapshack
Version:	1.16.1
Release:	1
Group:		Communications
License:	GPLv3+
URL:		https://github.com/Maproom/%{name}/wiki
Source0:	https://github.com/Maproom/qmapshack/archive/V_%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(proj)
BuildRequires:	cmake(QuaZip-Qt5)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Help)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5UiTools)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5WebEngineWidgets)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	pkgconfig(gdal)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	qt5-assistant
BuildRequires:	routino-devel
# unpackaged yet
#BuildRequires: alglib-devel

%description
QMapShack provides a versatile tool for GPS maps in GeoTiff format as well as
Garmin's img vector map format. You can also view and edit your GPX tracks.
QMapShack is the successor of QLandkarteGT.

Main features:
- use of several work-spaces
- use several maps on a work-space
- handle data project-oriented
- exchange data with the device by drag-n-drop

%files
%doc LICENSE changelog.txt
%{_bindir}/*
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop
%{_datadir}/qmaptool/translations/*qm
%{_datadir}/qmt_rgb2pct/translations/*qm
%{_mandir}/man1/*.1*
%{_docdir}/HTML/*qch
%{_docdir}/HTML/*qhc

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-V_%{version}

%build
%cmake \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-G Ninja
%ninja_build

%install
%ninja_install -C build
