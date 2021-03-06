# Generated by go2rpm 1
%bcond_without check

# https://github.com/zgoat/zcache
%global goipath         zgo.at/zcache
%global forgeurl        https://github.com/zgoat/zcache
Version:                1.0.0

%gometa

%global common_description %{expand:
An in-memory key:value store/cache (similar to Memcached) library for Go,
suitable for single-machine applications.}

%global golicenses      LICENSE
%global godocs          README.markdown issue-list.markdown

Name:           %{goname}
Release:        1%{?dist}
Summary:        An in-memory key:value store/cache (similar to Memcached) library for Go, suitable for single-machine applications

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/zcache %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.markdown issue-list.markdown
%{_bindir}/*

%gopkgfiles

%changelog
* Sat Sep 19 16:42:23 CEST 2020 Johan Kok <johankok@users.noreply.github.com> - 1.0.0-1
- Bumped to version 1.0.0

* Fri Aug 28 16:50:12 CEST 2020 Johan Kok <johankok@users.noreply.github.com> - 0-0.1.20200828gitdf91dc4
- Initial package

