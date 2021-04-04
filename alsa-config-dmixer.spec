Name:		alsa-config-dmixer
Version:	1.0
Release:	1
BuildArch:	noarch
Group:		Sound
Summary:	Sound configuration allowing multiple inputs without PulseAudio
Source0:	99-dmix.conf
License:	Apache-2.0

%description
Sound configuration allowing multiple inputs without PulseAudio

On most systems, PulseAudio handles mixing multiple applications' sound
output into one input a cheap sound chip can handle.

This package contains configuration files for achieving this without
PulseAudio.

It is more lightweight (and therefore better suited for some embedded
devices), less error prone, but also far less powerful (e.g. no
switching between speaker, wired headphone and bluetooth headphone).

%prep

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/alsa/conf.d/
cp %{S:0} %{buildroot}%{_sysconfdir}/alsa/conf.d/

%files
%{_sysconfdir}/alsa/conf.d/99-dmix.conf
