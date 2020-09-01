# Generated by go2rpm 1
%bcond_without check

# https://github.com/zgoat/zdb
%global goipath         zgo.at/zdb
%global forgeurl        https://github.com/zgoat/zdb
%global commit          e9bba7f2acd9e02649c15df05e333f1061a40e54

%gometa

%global common_description %{expand:
Go database stuff.}

%global golicenses      LICENSE
%global godocs          README.markdown

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Go database stuff

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/jmoiron/sqlx)
BuildRequires:  golang(github.com/lib/pq)
BuildRequires:  golang(github.com/mattn/go-sqlite3)
BuildRequires:  golang(zgo.at/zlog)
BuildRequires:  golang(zgo.at/zstd/zbyte)
BuildRequires:  golang(zgo.at/zstd/zfloat)
BuildRequires:  golang(zgo.at/zstd/zint)
BuildRequires:  golang(zgo.at/zstd/zstring)

%if %{with check}
# Tests
BuildRequires:  golang(zgo.at/zstd/ztest)
%endif

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
* Tue Sep 01 08:44:21 CEST 2020 Johan Kok <johankok@users.noreply.github.com> - 0-0.1.20200901gite9bba7f
- Initial package

