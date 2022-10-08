Name:      polybar
Version:   3.6.3
Release:   alt1

Summary:   Beautiful highly customizable status bar, without any shell scripting for X Window System
Group:     Graphical desktop/Other
License:   MIT

Url:       https://github.com/polybar/polybar

Source0:    %name-%version.tar
Source1:    xpp.tar
Source2:    i3ipcpp.tar

# Fixed doc builder
# From python2-module-sphinx => python3-module-sphinx
Patch0:     %name-%version-sphinx-builder.patch

Packager:   Pavel Vasilev <django@altlinux.org>

BuildArch:  x86_64

#  Now is improving clang support
# so in future gcc-c++ will optional
BuildRequires:  gcc-c++ cmake pkg-config
# Tools to build docs/mans
BuildRequires:  python3 python3-module-packaging python3-module-sphinx
# Must have modules
BuildRequires:  libexpat-devel libuuid-devel libbrotli-devel libcairo-devel libcurl-devel jsoncpp-devel
# Optional modules
# Needs to visualise data
# like playing music via 'libmpd'
# or network traffic via 'libnl'
BuildRequires:  libalsa-devel libmpdclient libnl-devel libpulseaudio-devel libmpd-devel libmpdclient-devel libuv-devel
# X Window Extensions
BuildRequires:  libxcb-devel libxcbutil-devel libxcbutil-icccm-devel libxcbutil-image-devel libxcbutil-xrm-devel libxcbutil-cursor-devel xorg-xcbproto-devel libXdmcp-devel libxcb-render-util-devel
# Another extensions
BuildRequires:  libpcre-devel libffi-devel libpixman-devel bzip2-devel i3-devel

%description
Polybar aims to help users build beautiful and highly customizable status bars
for their desktop environment, without the need of having a black belt in
shell scripting.

%prep
%setup
%setup -D -a 1
%setup -D -a 2
# Installing static libraries
mv $PWD/xpp $PWD/lib
mv $PWD/i3ipcpp $PWD/lib
%patch0 -p1

%build
%cmake  \
		-DCMAKE_BUILD_TYPE=Release \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-DBUILD_DOC=on \
		-DBUILD_CONFIG=on \
		-DBUILD_SHELL=off
%cmake_build

%install
%cmake_install

%files
%config  %_sysconfdir/%name/config.ini
# Executable utils
%_bindir/%name
%_bindir/%name-msg
# html manuals
%_docdir/%name/*
# mans
%_mandir/man1/%{name}*
%_mandir/man5/%{name}*

%changelog
* Sat Sep 08 2022 Pavel Vasilev <django@altlinux.org> 3.6.3-alt1
- Initial build
