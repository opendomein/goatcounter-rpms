# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/zgoat/zdb
%global goipath         zgo.at/zdb
%global forgeurl        https://github.com/zgoat/zdb
%global commit          b3821bce94fee86a3febcd9e588d0d622b782c05

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
BuildRequires:  golang(github.com/jmoiron/sqlx/reflectx)
BuildRequires:  golang(github.com/lib/pq)
BuildRequires:  golang(github.com/mattn/go-sqlite3)
BuildRequires:  golang(io/fs)
BuildRequires:  golang(zgo.at/zstd/zbyte)
BuildRequires:  golang(zgo.at/zstd/zstring)
BuildRequires:  golang(zgo.at/zstd/ztest)

%if %{with check}
# Tests
BuildRequires:  golang(embed)
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
* Thu Jan 07 20:00:31 CET 2021 Johan Kok <johankok@users.noreply.github.com> - 0-0.1.20210107gitb3821bc
- Initial package

