# Generated by go2rpm 1
%bcond_without check

# https://github.com/zgoat/zstd
%global goipath         zgo.at/zstd
%global forgeurl        https://github.com/zgoat/zstd
%global commit          ef3212fc7e04f2fa3bcca87f5d472a670f7381db

%gometa

%global common_description %{expand:
A collection of extensions to Go's standard library.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        A collection of extensions to Go's standard library

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

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
* Fri Aug 28 16:04:07 CEST 2020 Johan Kok <johankok@users.noreply.github.com> - 0-0.1.20200828gitef3212f
- Initial package

