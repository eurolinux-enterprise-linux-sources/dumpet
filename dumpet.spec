Name:           dumpet
Version:        2.1
Release:        8%{?dist}
Summary:        A tool to dump and debug bootable CD images
License:        GPLv2+
Group:          Development/Tools
URL:            https://fedorahosted.org/dumpet/
Source0:        https://fedorahosted.org/releases/d/u/dumpet/dumpet-%{version}.tar.bz2
BuildRequires:  popt-devel pkgconfig libxml2-devel

%description
DumpET is a utility to aid in the debugging of bootable CD-ROM images.

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="%{optflags} $(pkg-config --cflags libxml-2.0)"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README TODO COPYING
%attr(644,root,root) %{_mandir}/man1/dumpet.1*
%{_bindir}/dumpet

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 2.1-8
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.1-7
- Mass rebuild 2013-12-27

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 08 2010 Peter Jones <pjones@redhat.com> - 2.1-2
- Rebuild for new libxml2.

* Wed Aug 25 2010 Peter Jones <pjones@redhat.com> - 2.1-1
- Minor fixes (cjwatson)
- Add a man page (cjwatson)

* Fri Oct 16 2009 Peter Jones <pjones@redhat.com> - 2.0-1
- This is the 2.0 release.  It is awesome and adds XML output in order to
  support automated validation of CD images.

* Mon Oct 05 2009 Peter Jones <pjones@redhat.com> - 1.1-1
- Update to dumpet-1.1, which treats CFLAGS reasonably.

* Mon Oct 05 2009 Peter Jones <pjones@redhat.com> - 1.0-1
- First release.

