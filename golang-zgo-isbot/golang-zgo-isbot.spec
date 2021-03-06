# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/zgoat/isbot
%global goipath         zgo.at/isbot
%global forgeurl        https://github.com/zgoat/isbot
%global commit          d1f89ea3798604effab59c20be0a6b9818386beb

%gometa

%global common_description %{expand:
Go library to detect HTTP bots.}

%global golicenses      LICENSE
%global godocs          README.markdown

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Go library to detect HTTP bots

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

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
%doc README.markdown
%{_bindir}/*

%gopkgfiles

%changelog
* Sun Jun 27 11:56:40 CEST 2021 Johan Kok <johankok@users.noreply.github.com> - 0-0.1.20210627gitd1f89ea
- Initial package

