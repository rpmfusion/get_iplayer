Name:		get_iplayer
Version:	2.76
Release:	1%{?dist}
Summary:	Lists, Records and Streams BBC iPlayer TV and Radio programmes

Group:		Applications/Internet
License:	GPLv3+
URL:		http://github.com/jjl/get_iplayer
# Commit 8f6d751ff6ec689213c4c7f98d660dd273c8fb7c
Source0:	http://download.github.com/jjl-get_iplayer-8f6d751.tar.gz
Source1:	options
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	sed
Requires:	rtmpdump ffmpeg id3v2 lame mplayer vlc

BuildArch:	noarch

%description
get_iplayer is a tool for listing, recording and streaming BBC iPlayer TV 
programmes, and other programmes via 3rd-party plugins.

%prep
%setup -q -n jjl-get_iplayer-8f6d751
sed /PROMETHEUS/Q -i README

%build

%install
rm -rf $RPM_BUILD_ROOT
install -p -D -m0755 get_iplayer $RPM_BUILD_ROOT%{_bindir}/get_iplayer
install -p -D -m0644 man/get_iplayer.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/get_iplayer.1.gz
install -p -D -m0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/get_iplayer/options

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/get_iplayer
%{_mandir}/man1/get_iplayer.1.*
%dir %{_sysconfdir}/get_iplayer
%config(noreplace) %{_sysconfdir}/get_iplayer/options
%doc LICENSE.txt 
%doc README

%changelog
* Tue Apr 20 2010 David Woodhouse <dwmw2@infradead.org> 2.76-1
- Initial package
