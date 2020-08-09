# Generated by go2rpm 1
%bcond_without check

# https://github.com/teamwork/reload
%global goipath         github.com/teamwork/reload
Version:                1.3.2

%gometa

%global common_description %{expand:
Lightweight automatic reloading of Go processes.}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Lightweight automatic reloading of Go processes

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/fsnotify/fsnotify)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Sun Aug 09 11:34:20 CEST 2020 Johan Kok <johankok@users.noreply.github.com> - 1.3.2-1
- Initial package

