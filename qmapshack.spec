Summary:	GPS mapping and management tool
Name:		qmapshack
Version:	1.10.0
Release:	2
Group:		Communications
License:	GPLv3+
URL:		https://github.com/Maproom/%{name}/wiki
Source0:	https://github.com/Maproom/qmapshack/archive/V_%{version}/%{name}-%{version}.tar.gz
Patch2:		qmapshack-1.3.1-system-routino.diff
Patch3:		qmapshack-1.10-0-includes.patch

BuildRequires:	cmake
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5Script)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	cmake(Qt5UiTools)
BuildRequires:	qt5-designer
BuildRequires:	qt5-linguist
BuildRequires:	qt5-linguist-tools
BuildRequires:	qt5-devel
BuildRequires:	qt5-qttools
BuildRequires:	proj-devel
BuildRequires:	quazip-devel
BuildRequires:	gdal-devel
BuildRequires:	desktop-file-utils
BuildRequires:	routino-devel
BuildRequires:	routino

Requires:	proj
Requires:	gdal
Requires:	routino

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
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/QMapShack.png
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.*
%{_iconsdir}/*/*/*/QMapShack.*

#---------------------------------------------------------------------------

%prep
%autosetup -p1  -n %{name}-V_%{version}
sed -ie 's/quazip5/quazip/' cmake/Modules/FindQuaZip.cmake

%build
%cmake \
	-DBUILD_SHARED_LIBS:BOOL=OFF
	-G ninja
%make_build


%install
%make_install -c build

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

