%define		oname GPU-Viewer

Name:		gpu-viewer
Version:	3.08
Release:	1
Summary:	GPU Info
URL:		https://github.com/arunsivaramanneo/GPU-Viewer
Source0:	https://github.com/arunsivaramanneo/GPU-Viewer/archive/v%{version}/%{oname}-%{version}.tar.gz
License:	GPLv3
Group:		Development/Other
BuildArch:	noarch
BuildRequires:	meson
BuildRequires:	ninja
BuildRequires:	python-pkg-resources
BuildRequires:	imagemagick

Requires: gtk+3
Requires: python-gobject3
Requires: python-gi
Requires: grep
Requires: glxinfo
Requires: vulkan-tools
Requires: xdpyinfo
Requires: mesa-demos
Requires: glxinfo
Requires: eglinfo
Requires: vdpauinfo
Requires: clinfo

%description
A front-end to glxinfo, vulkaninfo, clinfo and es2_info.
This project aims to capture all the important details of 
glxinfo, vulkaninfo and clinfo in a GUI. The project is
being developed using python 3 pygobject with GTK3. All 
the important details are extracted using 
glxinfo/vulkaninfo/clinfo with the combination of grep, 
CAT , AWK commands and displayed in the front-end. 
There is no hard OpenGL Programming involved, until 
glxinfo, vulkaninfo and clinfo works the GPU-viewer will 
also work

%prep
%setup -qn %{oname}-%{version}

%build
%meson
%meson_build

%install
%meson_install

# fix desktop file
sed -i '/Version/d' %{buildroot}%{_datadir}/applications/io.github.arunsivaramanneo.GPUViewer.desktop

# icons install
for x in 16 32 24 48 64 96 128 256; do
convert -resize ${x}x${x} %{buildroot}%{_iconsdir}/hicolor/512x512/apps/io.github.arunsivaramanneo.GPUViewer.png %{name}.png
install -Dm0644 %{name}.png %{buildroot}%{_iconsdir}/hicolor/${x}x${x}/apps/io.github.arunsivaramanneo.GPUViewer.png
done


%files
%doc README.md LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/io.github.arunsivaramanneo.GPUViewer.desktop
%{_datadir}/metainfo/io.github.arunsivaramanneo.GPUViewer.metainfo.xml
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*x*/apps/
