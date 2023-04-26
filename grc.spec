Name:           grc
Version:        1.13
Release:        1%{?dist}
Summary:        Generic Colouriser

License:        GPL
URL:            http://melkor.dnp.fmph.uniba.sk/~garabik/grc.html
Source0:         %{name}-%{version}.tar.gz

BuildRequires: bash
Requires:      python 

%description
Generic Colouriser is yet another colouriser for beautifying your logfiles
or output of commands.

Authors:
--------
    Radovan Garabik <garabik@melkor.dnp.fmph.uniba.sk>

%prep
%setup -q


%install
rm -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}
install -m 755 grcat $RPM_BUILD_ROOT%{_bindir}
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}
install -m 644 %{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}/
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -m 644 %{name}.sh $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/%{name}.sh
install -m 644 %{name}.zsh $RPM_BUILD_ROOT%{_sysconfdir}/
install -m 644 %{name}.fish $RPM_BUILD_ROOT%{_sysconfdir}/
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 colourfiles/conf.* $RPM_BUILD_ROOT/%{_datadir}/%{name}/
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/
install -m 644 grcat.1 $RPM_BUILD_ROOT%{_mandir}/man1/
install -d 755 $RPM_BUILD_ROOT%{_datadir}/zsh/
install -d 755 $RPM_BUILD_ROOT%{_datadir}/zsh/site-functions
install -m 644 _%{name} $RPM_BUILD_ROOT%{_datadir}/zsh/site-functions
%make_install


%files
%{_bindir}/%{name}
%{_bindir}/grcat
%{_sysconfdir}/%{name}.conf
%{_sysconfdir}/profile.d/%{name}.sh
%{_sysconfdir}/%{name}.zsh
%{_sysconfdir}/%{name}.fish
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/conf.*
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man1/grcat.1.gz
%{_datadir}/zsh/site-functions/_%{name}
%license debian/copyright 
%doc README.markdown



%changelog
* Wed Apr 26 2023 Spencer Smolen <mail@kriipke.io>
- Rewrote grc.spec based on https://gtihub.com/garabik/grc/blob/v1.13/grc.spec
