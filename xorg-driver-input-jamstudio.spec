Summary:	X.org input driver for JamStudio devices
Summary(pl):	Sterownik wej�ciowy X.org dla urz�dze� JamStudio
Name:		xorg-driver-input-jamstudio
Version:	1.0.0.5
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/driver/xf86-input-jamstudio-%{version}.tar.bz2
# Source0-md5:	4ea7a20133f637750f72a34b8f7b1b21
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 0.99.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for JamStudio devices. This driver supports the
KB-Gear JamStudio pentablet.

%description -l pl
Sterownik wej�ciowy X.org dla urz�dze� JamStudio. Obs�uguje pentablety
KB-Gear JamStudio.

%prep
%setup -q -n xf86-input-jamstudio-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/input/js_x_drv.so
%{_mandir}/man4/js_x.4*
