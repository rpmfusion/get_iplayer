Name:		get_iplayer
Version:	2.80
Release:	4%{?dist}
Summary:	Lists, Records and Streams BBC iPlayer TV and Radio programmes

Group:		Applications/Internet
License:	GPLv3+
URL:		http://github.com/jjl/get_iplayer
Source0:	ftp://ftp.infradead.org/pub/get_iplayer/get_iplayer-%{version}.tar.gz
Source1:	options
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	sed 
BuildRequires:	perl(Cwd) perl(Env) perl(Fcntl) perl(File::Copy) 
BuildRequires:	perl(File::Path) perl(File::stat) perl(Getopt::Long)
BuildRequires:	perl(HTML::Entities) perl(HTTP::Cookies) perl(HTTP::Headers)
BuildRequires:	perl(IO::Seekable) perl(IO::Socket) perl(LWP::ConnCache)
BuildRequires:	perl(LWP::UserAgent) perl(POSIX) perl(Time::Local) perl(URI)
BuildRequires:	perl(HTML::Entities) perl(HTTP::Cookies)
Requires:	rtmpdump ffmpeg id3v2 lame mplayer vlc

%{?filter_setup:
# https://bugzilla.redhat.com/show_bug.cgi?id=734244
%filter_from_requires /perl(Programme.*)/d; /perl(Streamer)/d;
%filter_setup
}

BuildArch:	noarch

%description
get_iplayer is a tool for listing, recording and streaming BBC iPlayer TV 
programmes, and other programmes via 3rd-party plugins.

%prep
%setup -q

%build
./get_iplayer --manpage=get_iplayer.1 || :

%install
rm -rf $RPM_BUILD_ROOT
install -p -D -m0755 get_iplayer $RPM_BUILD_ROOT%{_bindir}/get_iplayer
install -p -D -m0644 get_iplayer.1 $RPM_BUILD_ROOT%{_mandir}/man1/get_iplayer.1
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
%doc README.txt

%changelog
* Mon Aug 29 2011 David Woodhouse <dwmw2@infradead.org> 2.80-4
- conditionalise %%filter_setup properly.

* Mon Aug 29 2011 David Woodhouse <dwmw2@infradead.org> 2.80-3
- Make the requires filtering work in rpmfusion build system

* Mon Aug 29 2011 David Woodhouse <dwmw2@infradead.org> 2.80-2
- Remove superfluous perl requires

* Mon Aug 29 2011 David Woodhouse <dwmw2@infradead.org> 2.80-1
- Update to 2.80
- Add 'packagemanager yum' to options file (#1270)

* Sun Jan 09 2011 David Woodhouse <dwmw2@infradead.org> 2.79-1
- Update to 2.79

* Fri May 28 2010 David Woodhouse <dwmw2@infradead.org> 2.78-1
- Update to 2.78 (proper fix for Akamai).

* Wed May 26 2010 David Woodhouse <dwmw2@infradead.org> 2.77-3
- Add all necessary perl BuildRequires so we can generate man page

* Wed May 26 2010 David Woodhouse <dwmw2@infradead.org> 2.77-2
- BR perl(HTML::Entities) for man page

* Wed May 26 2010 David Woodhouse <dwmw2@infradead.org> 2.77-1
- Update to 2.77 (fix Limelight and Akamai RTMP downloads).

* Tue Apr 20 2010 David Woodhouse <dwmw2@infradead.org> 2.76-1
- Initial package
