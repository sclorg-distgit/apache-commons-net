%global pkg_name apache-commons-net
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}


%global base_name    net
%global short_name   commons-%{base_name}

Name:           %{?scl_prefix}%{pkg_name}
Version:        3.2
Release:        8.6%{?dist}
Summary:        Internet protocol suite Java library
License:        ASL 2.0
URL:            http://commons.apache.org/%{base_name}/
Source0:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}maven-plugin-build-helper
BuildRequires:  %{?scl_prefix}apache-commons-parent >= 26-7
# Test dependency
BuildRequires:  %{?scl_prefix}junit



%description
This is an Internet protocol suite Java library originally developed by
ORO, Inc.  This version supports Finger, Whois, TFTP, Telnet, POP3, FTP,
NNTP, SMTP, and some miscellaneous protocols like Time and Echo as well
as BSD R command support. The purpose of the library is to provide
fundamental protocol access, not higher-level abstractions.

%package javadoc
Summary:    API documentation for %{pkg_name}


%description javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
sed -i 's/\r//' NOTICE.txt LICENSE.txt README RELEASE-NOTES.txt

# This test fails with "Connection timed out"
rm src/test/java/org/apache/commons/net/time/TimeTCPClientTest.java

%mvn_file  : %{short_name} %{pkg_name}
%mvn_alias : org.apache.commons:%{short_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}


%files -f .mfiles
%doc LICENSE.txt NOTICE.txt README RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2-8.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2-8.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2-8.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2-8.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2-8.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2-8.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.2-8
- Mass rebuild 2013-12-27

* Fri Sep 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2-7
- Add BuildRequires on apache-commons-parent >= 26-7

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2-6
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Wed Jun 05 2013 Michal Srb <msrb@redhat.com> - 3.2-5
- Enable tests
- Install README, RELEASE-NOTES.txt files
- Fix BR

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 3.2-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan 16 2013 Michal Srb <msrb@redhat.com> - 3.2-2
- Build with xmvn

* Mon Dec  3 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2-1
- Update to upstream version 3.2

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1-1
- Update to upstream 3.1
- Remove RPM bug workaround
- Remove BR on maven-changes-plugin

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 24 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2-3
- Use maven 3 to build
- Packaging fixes according to latest guidelines

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 10 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2-1
- Replace maven plugins with apache-commons-parent for BR
- Versionless jars and javadocs
- Rebase to latest upstream version

* Thu Jul  8 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.0-6
- Add license to javadoc subpackage

* Thu May 20 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.0-5
- Fix maven depmap JPP name to short_name

* Wed May 19 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.0-4
- Ignore test failure

* Wed May 12 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.0-3
- Rename jakarta-commons-net to apache-commons-net and drop EPOCH
- Build with maven
- Clean up whole spec

* Thu Aug 13 2009 Alexander Kurtakov <akurtako@redhat.com> 0:2.0-2
- Set maven.repo.local.

* Thu Aug 13 2009 Alexander Kurtakov <akurtako@redhat.com> 0:2.0-1
- Update to upstream 2.0.

