# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/zgoat/zli
%global goipath         zgo.at/zli
%global forgeurl        https://github.com/zgoat/zli
%global commit          33768b083e81082ab73961cc6399bb355e7a02fb

%gometa

%global common_description %{expand:
A Go library for writing CLI programs. It includes flag parsing, colour escape
codes, and various helpful utility functions, and makes testing fairly easy.}

%global golicenses      LICENSE
%global godocs          README.markdown flag.markdown

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        A Go library for writing CLI programs. It includes flag parsing, colour escape codes, and various helpful utility functions, and makes testing fairly easy

License:        # FIXME

URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/sys/unix)

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
%doc README.markdown flag.markdown
%{_bindir}/*

%gopkgfiles

%changelog
* Thu Jan 07 20:03:56 CET 2021 Johan Kok <johankok@users.noreply.github.com> - 0-0.1.20210107git33768b0
- Initial package

