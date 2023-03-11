#FIXME: without this link fails on znver1
%ifarch %{ix86}
%global optflags %{optflags} -O2
%endif

Summary:	GPS mapping and management tool
Name:		qmapshack
Version:	1.16.1
Release:	7
Group:		Communications
License:	GPLv3+
URL:		https://github.com/Maproom/qmapshack/wiki
Source0:	https://github.com/Maproom/qmapshack/archive/V_%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(alglib)
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
BuildRequires:  pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	qt5-assistant
BuildRequires:	routino-devel

Requires:	proj-data

Recommends:	routino
Recommends:	qmaptool

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
%license LICENSE
%doc changelog.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/QMapShack.png
%{_datadir}/pixmaps/QMapShack.png
%{_datadir}/applications/%{name}.desktop
%{_docdir}/HTML/QMSHelp.q??
%{_mandir}/man1/%{name}.*

#---------------------------------------------------------------------------

%package -n qmaptool
Summary:	Create raster maps from paper map scans
Requires:	gdal

%description -n qmaptool
This is a tool to create raster maps from paper map scans. QMapTool can be
considered as a front-end to the well-known GDAL package. It complements
QMapShack.

%files -n qmaptool
%{_bindir}/qmaptool
%{_bindir}/qmt_*
%{_datadir}/qmaptool/
%{_datadir}/qmt_rgb2pct/translations/*qm
%{_datadir}/icons/hicolor/*/apps/QMapTool.png
%{_datadir}/pixmaps/QMapTool.png
%{_datadir}/applications/qmaptool.desktop
%{_datadir}/doc/HTML/QMTHelp.q??
%{_mandir}/man1/qmaptool.*
%{_mandir}/man1/qmt_*.*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-V_%{version}

# remove bundled libs
rm -fr 3rdparty/alglib

%build
%cmake \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-G Ninja
%ninja_build

%install
%ninja_install -C build

