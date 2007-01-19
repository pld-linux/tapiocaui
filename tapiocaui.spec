Summary:	A framework for Voice over IP (VoIP) and Instant Messaging (IM)
Name:		tapiocaui
Version:	0.3.9.1
Release:	0.1
License:	GPL
Group:		Networking/Instant messaging
Source0:	http://dl.sourceforge.net/tapioca-voip/%{name}-%{version}.tar.gz
# Source0-md5:	2b0fc6997e793784763fe23c81a4986f
URL:		http://tapioca-voip.sourceforge.net/wiki/index.php/Tapioca
BuildRequires:	dbus-devel 
BuildRequires:	gtk+2-devel 
BuildRequires:	glib2-devel 
BuildRequires:	hal-devel 
BuildRequires:	libfarsight-devel 
BuildRequires:	libxml2-devel
BuildRequires:	tapioca-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tapioca is a framework for Voice over IP (VoIP) and 
Instant Messaging (IM). Its main goal is to provide 
an easy way for developing and using VoIP and IM 
services in any kind of application. It was designed 
to be cross-platform, lightweight, thread-safe, having 
mobile devices and applications in mind.

	Tapioca's main goals are:
	
 * Create a solution that integrates all components 
used by VoIP and IM applications in a single, reliable 
and easy to use framework, which is able to work on different 
platforms.

 * Spare resources, providing central services for multiple 
applications. Eg.: The control of all incoming and outgoing SIP 
requests are managed by the SIP service, avoiding the creation of
 one SIP stack and allocation of a network port for each SIP-based 
application.

 * Reduce the overhead of control layers and library dependencies. 

%prep
%setup -q

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
%{_datadir}/tapiocaui/*.glade
