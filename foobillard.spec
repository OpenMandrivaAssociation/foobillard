#
# (*) TTF fonts are taken from http://www.larabiefonts.com, thus we can redistribute
#
Summary:	OpenGL billard game
Name:		foobillard
Version:	3.0a
Release:	%mkrel 8
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
Comment=%{summary}
Exec=padsp %{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;SportsGame;
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


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 3.0a-8mdv2011.0
+ Revision: 610740
- rebuild

* Sat May 01 2010 Funda Wang <fwang@mandriva.org> 3.0a-7mdv2010.1
+ Revision: 541466
- fix desktop file

* Sun Aug 30 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 3.0a-7mdv2010.0
+ Revision: 422648
- execute foobillard with psdsp, to get sound back (mdvbz #52483)
- spec file clean

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 3.0a-6mdv2009.0
+ Revision: 245302
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 3.0a-4mdv2008.1
+ Revision: 136417
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Sat Dec 02 2006 Olivier Blin <oblin@mandriva.com> 3.0a-4mdv2007.0
+ Revision: 89977
- buildrequire freetype2-devel

  + Emmanuel Andry <eandry@mandriva.org>
    - xdg menu
      fix buildrequires
    - Import foobillard

* Tue Dec 27 2005 Lenny Cartier <lenny@mandriva.com> 3.0a-3mdk
- rebuild

* Fri Aug 27 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 3.0a-2mdk
- rebuild for new menu
- drop packager tag

* Fri Jul 30 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 3.0a-1mdk
- 3.0a
- drop P0 (merged upstream)

* Sat Apr 24 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 3.0-1mdk
- 3.0
- really disable nvidia (P1)
- fix problem with foobillard not changing to datadir before running (P2)
- add menu item with icons
- install man page
- fix buildrequires (lib64..)

