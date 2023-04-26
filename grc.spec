Name:           grc
Version:        %{tag}
Release:        1%{?dist}
Summary:        Generic Colouriser

License:        GPL
URL:            http://melkor.dnp.fmph.uniba.sk/~garabik/grc.html
Source0:        https://github.com/kriipke/grc/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

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

%post
if command -v zsh &>/dev/null; then
  printf '%s\n' "Would you like to have grc configured system-wide in your shell configuration: /etc/zshrc?" \
      "If you don't you'll have to manually add the following line to your shell somewhere to use grc: " \
      "  [[ -s "/etc/profile.d/grc.sh" ]] && source /etc/grc.sh"
  
  read -p "Let this script configure your /etc/zshrc? [Y|n] " -n 1 -r

  if [[ ! $REPLY =~ ^[Yy]$ ]]; then
      exit 1
  fi

  echo '[[ -s "/etc/grc.zsh" ]] && source /etc/grc.zsh' >> /etc/zshrc

else
  cat <<EOF
  ENSURE YOU HAVE THE FOLLOWING CONFIGUIRATION IN PLACE TO USE GRC:
  
  Bash..............................................................
  
  To set aliases for supported commands, append to your `~/.bashrc`:
  
      GRC_ALIASES=true
      [[ -s "/etc/profile.d/grc.sh" ]] && source /etc/grc.sh
  
  If the file `/etc/default/grc` exists, it is sourced first, 
  therefore you can place a line saying `GRC_ALIASES=true` there.
  
  ZSH...............................................................
  
  Or for zsh users, append to `~/.zshrc`:
  
      [[ -s "/etc/grc.zsh" ]] && source /etc/grc.zsh
  
  FISH..............................................................
  
  Add to `~/.config/fish/config.fish` or in a new file in 
  `~/.config/fish/conf.d/`:
  
      source /usr/local/etc/grc.fish
EOF

fi

%postun
# remove the line added in %post on uninstall
if grep -q '\(source\|.\)\s\/etc\/grc\.zsh' /etc/zshrc; then
    sed -i '/\(source\|.\)\s\/etc\/grc\.zsh/d' /etc/zshrc
fi


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
%doc README.markdown Regexp.txt

%changelog
* Wed Apr 26 2023 Spencer Smolen <mail@kriipke.io>
- Rewrote grc.spec based on https://gtihub.com/garabik/grc/blob/v1.13/grc.spec
