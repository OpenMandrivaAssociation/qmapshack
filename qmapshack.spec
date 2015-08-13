Name: qmapshack
Version: 1.3.0
Release: 1
Summary: GPS mapping and management tool

Group: Communications
License: GPLv3+
URL: https://bitbucket.org/maproom/qmapshack/wiki/Home
Source0: https://bitbucket.org/maproom/%{name}/downloads/%{name}-%{version}.tar.gz
Patch1:	qmapshack-0.11.0-cmake28.patch
Requires: proj

BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5Sql)
BuildRequires: pkgconfig(Qt5WebKitWidgets)
BuildRequires: qt5-designer
BuildRequires: qt5-linguist
BuildRequires: qt5-linguist-tools
BuildRequires: qt5-devel
BuildRequires: qt5-qttools
BuildRequires: proj-devel
BuildRequires: gdal-devel
BuildRequires: desktop-file-utils


%description
QMapShack provides a versatile tool for GPS maps in GeoTiff format as well as
Garmin's img vector map format. You can also view and edit your GPX tracks.
QMapShack is the successor of QLandkarteGT.

Main features:
- use of several work-spaces
- use several maps on a work-space
- handle data project-oriented
- exchange data with the device by drag-n-drop


%prep
%setup -q
%apply_patches

%build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF ..
%make VERBOSE=1


%install
cd build
%makeinstall_std

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%doc LICENSE changelog.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/QMapShack.png
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.*

