#
# (*) TTF fonts are taken from http://www.larabiefonts.com, thus we can redistribute
#
Summary:	OpenGL billard game
Name:		foobillard
Version:	3.0a
Release:	%mkrel 7
License:	GPLv2+
Group:		Games/Sports
URL:		http://foobillard.sunsite.dk/
Source0:	http://foobillard.sunsite.dk/dnl/%{name}-%{version}.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
#Patch0:	%{name}-2.7-no_nv_fresnel.patch.bz2
Patch1:		foobillard-3.0-really-disable-nvidia.patch
#Patch2:	foobillard-3.0-fix-chdir.patch.bz2
BuildRequires:	mesaglu-devel
BuildRequires:	mesa-common-devel
BuildRequires:	png-devel
BuildRequires:	zlib-devel
BuildRequires:	libxaw-devel
BuildRequires:	freetype2-devel
Requires:	pulseaudio-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A free OpenGl billard game for linux.

%prep
%setup -q
#%patch0 -p1
%patch1 -p1
#%patch2 -p1

%build
%configure2_5x	\
	--bindir=%{_gamesbindir} \
	--datadir=%{_gamesdatadir} \
	--enable-glut \
	--enable-nvidia=off
%make

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}
%{__install} -m644 %{name}.6 -D %{buildroot}%{_mandir}/man6/%{name}.6


mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=FooBillard
Comment=%{Summary}
Exec=padsp %{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Games-Sports;Game;SportsGame;
EOF

%{__install} -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
%{__install} -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
%{__install} -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_mandir}/man6/%{name}.6*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_gamesbindir}/%{name}
