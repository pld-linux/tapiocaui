# TODO: descs for tapiocaui, not copy of tapioca descs
Summary:	A framework for Voice over IP (VoIP) and Instant Messaging (IM)
Summary(pl):	Szkielet do VoIP (Voice over IP) i IM (Instant Messaging)
Name:		tapiocaui
Version:	0.3.9
Release:	0.1
License:	GPL
Group:		Networking/Instant messaging
Source0:	http://dl.sourceforge.net/tapioca-voip/%{name}-%{version}.tar.gz
# Source0-md5:	aab56e42ca10b312ba0ca2e416b72374
Patch0:		%{name}-farsight.patch
URL:		http://tapioca-voip.sourceforge.net/wiki/index.php/Tapioca
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	dbus-devel
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	glib2-devel
BuildRequires:	libfarsight-devel >= 0.1
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	tapioca-libs-devel >= 0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tapioca is a framework for Voice over IP (VoIP) and Instant Messaging
(IM). Its main goal is to provide an easy way for developing and using
VoIP and IM services in any kind of application. It was designed to be
cross-platform, lightweight, thread-safe, having mobile devices and
applications in mind.

Tapioca's main goals are:
 - Create a solution that integrates all components used by VoIP and
   IM applications in a single, reliable and easy to use framework,
   which is able to work on different platforms.
 - Spare resources, providing central services for multiple
   applications. Eg.: The control of all incoming and outgoing SIP
   requests are managed by the SIP service, avoiding the creation of
   one SIP stack and allocation of a network port for each SIP-based
   application.
- Reduce the overhead of control layers and library dependencies.

%description -l pl
Tapioca to szkielet do VoIP (Voice over IP) i IM (Instant Messaging,
czyli komunikator�w). G��wnym jego celem jest zapewnienie �atwego
sposobu tworzenia i u�ywania us�ug VoIP i IM w dowolnym rodzaju
aplikacji. Zosta� zaprojektowany jako wieloplatformowy, lekki,
bezpieczny dla w�tk�w, a tak�e z my�l� o urz�dzeniach i aplikacjach
przeno�nych.

G��wne cele projektu Tapioca to:
 - stworzenie rozwi�zania integruj�cego wszystkie komponenty u�ywane
   przez aplikacje VoIP i IM w pojedynczym, pewnym i �atwym w u�yciu
   szkielecie, nadaj�cym si� do wykorzystania na r�nych platformach
 - oszcz�dno�� zasob�w poprzez udost�pnienie centralnych us�ug dla
   wielu aplikacji; na przyk�ad: sterowanie wszystkimi przychodz�cymi
   i wychodz�cymi ��daniami SIP jest obs�ugiwane przez us�ug� SIP, co
   zapobiega tworzeniu jednego stosu SIP i przydzielania portu
   sieciowego dla ka�dej aplikacji opartej na SIP
 - ograniczenie narzutu warstw steruj�cych i zale�no�ci bibliotek

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/tapiocaui.desktop
%{_pixmapsdir}/*.png
%{_pixmapsdir}/tapiocaui
%{_datadir}/tapiocaui
