%global srcname twine

Name:           python-%{srcname}
Version:        1.11.0
Release:        1%{?dist}
Summary:        Collection of utilities for interacting with PyPI

License:        ASL 2.0
URL:            https://github.com/pypa/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
# There's a shebang in twine/__main__.py which generates rpmlint warnings.
Patch0:         0001-Remove-shebang-from-__main__.py.patch
BuildArch:      noarch

%description
Twine is a utility for interacting with PyPI.
Currently it only supports registering projects and uploading distributions.


%package -n python2-%{srcname}
Summary:        %{summary}
Requires:       python2-clint
Requires:       python2-pkginfo >= 1.4.2
Requires:       python-tqdn
Requires:       python-requests >= 2.3.0
Requires:       python-requests-toolbelt >= 0.8.0
Requires:       python-setuptools >= 0.7.0
# Test requirements
BuildRequires:  python2-clint
BuildRequires:  python-devel
BuildRequires:  python2-pkginfo >= 1.4.2
BuildRequires:  python-tqdn
BuildRequires:  python-requests >= 2.3.0
BuildRequires:  python-requests-toolbelt >= 0.8.0
BuildRequires:  python-setuptools >= 0.7.0
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Twine is a utility for interacting with PyPI.
Currently it only supports registering projects and uploading distributions.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}
ln -s %{_bindir}/twine %{buildroot}%{_bindir}/twine-%{python2_version}
ln -s %{_bindir}/twine-%{python2_version} %{buildroot}%{_bindir}/twine-2


%check
%{__python2} setup.py test


%files -n python2-%{srcname}
%license LICENSE
%doc README.rst AUTHORS
%{python2_sitelib}/*
%{_bindir}/twine
%{_bindir}/twine-2
%{_bindir}/twine-%{python2_version}


%changelog
* Wed Apr 04 2018 Tristan Cacquera <tdecacqu@redhat.com> - 1.11.0-1
- Bump version to 1.11.0

* Mon Jul 18 2016 Jeremy Cline <jeremy@jcline.org> - 1.7.4-3
- Keep objects.inv to support intersphinx documentation
- Skip building the docs package until python-releases is available

* Mon Jul 18 2016 Jeremy Cline <jeremy@jcline.org> - 1.7.4-2
- Add clint as a build dependency so the tests pass

* Fri Jul 15 2016 Jeremy Cline <jeremy@jcline.org> - 1.7.4-1
- Update to the latest upstream release
- Add clint as a dependency

* Tue Jul 12 2016 Jeremy Cline <jeremy@jcline.org> - 1.6.5-5
- Remove unnecessary shebang in __main__.py that caused rpmlint errors

* Mon Jul 11 2016 Jeremy Cline <jeremy@jcline.org> - 1.6.5-4
- Mark man pages as docs

* Mon Jul 11 2016 Jeremy Cline <jeremy@jcline.org> - 1.6.5-3
- Use python_version macro rather than hardcoding version numbers.

* Fri Jul 08 2016 Jeremy Cline <jeremy@jcline.org> - 1.6.5-2
- Update Source0 url to the <name>-<version>.tar.gz format

* Thu Jun 09 2016 Jeremy Cline <jeremy@jcline.org> - 1.6.5-1
- Initial commit
