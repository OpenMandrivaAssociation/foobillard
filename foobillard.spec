#
# (*) TTF fonts are taken from http://www.larabiefonts.com, thus we can redistribute
#
%define	name	foobillard
%define	version	3.0a
%define	release	%mkrel 4
%define	Summary	OpenGL billard game

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://foobillard.sunsite.dk/dnl/%{name}-%{version}.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
#Patch0:	%{name}-2.7-no_nv_fresnel.patch.bz2
Patch1:		foobillard-3.0-really-disable-nvidia.patch
#Patch2:	foobillard-3.0-fix-chdir.patch.bz2
License:	GPL
Group:		Games/Sports
URL:		http://foobillard.sunsite.dk/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	mesaglu-devel mesa-common-devel png-devel zlib-devel libxaw-devel freetype2-devel

%description
A free OpenGl billard game for linux.

%prep
%setup -q
#%patch0 -p1
%patch1 -p1
#%patch2 -p1

%build
%configure	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir} \
		--enable-glut \
		--enable-nvidia=off
%make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{makeinstall_std}
%{__install} -m644 %{name}.6 -D $RPM_BUILD_ROOT%{_mandir}/man6/%{name}.6


mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=FooBillard
Comment=%{Summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Games-Sports;Game;SportsGame;
EOF

%{__install} -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
%{__install} -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
%{__install} -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%post
%update_menus

%postun
%clean_menus

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_mandir}/man6/%{name}.6*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%defattr(755,root,root,755)
%{_gamesbindir}/%{name}


