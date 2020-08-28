# Generated by go2rpm 1
%bcond_without check

# https://github.com/zgoat/goatcounter
%global goipath         zgo.at/goatcounter
%global forgeurl        https://github.com/zgoat/goatcounter
Version:                1.4.0

%gometa

%global common_description %{expand:
Easy web analytics. No tracking of personal data.}

%global golicenses      LICENSE
%global godocs          docs CHANGELOG.markdown README.markdown\\\
                        db/README.markdown tpl/_backend_sitecode.markdown\\\
                        tpl/api.markdown tpl/gdpr.markdown tpl/why.markdown

Name:           %{goname}
Release:        1%{?dist}
Summary:        Easy web analytics. No tracking of personal data

License:        # FIXME

URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(code.soquee.net/otp)
BuildRequires:  golang(github.com/arp242/geoip2-golang)
BuildRequires:  golang(github.com/boombuler/barcode)
BuildRequires:  golang(github.com/boombuler/barcode/qr)
BuildRequires:  golang(github.com/go-chi/chi)
BuildRequires:  golang(github.com/go-chi/chi/middleware)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/jmoiron/sqlx)
BuildRequires:  golang(github.com/lib/pq)
BuildRequires:  golang(github.com/mattn/go-sqlite3)
BuildRequires:  golang(github.com/monoculum/formam)
BuildRequires:  golang(github.com/teamwork/reload)
BuildRequires:  golang(golang.org/x/crypto/acme)
BuildRequires:  golang(golang.org/x/crypto/acme/autocert)
BuildRequires:  golang(golang.org/x/crypto/bcrypt)
BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)
BuildRequires:  golang(golang.org/x/net/xsrftoken)
BuildRequires:  golang(golang.org/x/sync/singleflight)
BuildRequires:  golang(golang.org/x/tools/go/analysis)
BuildRequires:  golang(golang.org/x/tools/go/analysis/multichecker)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/asmdecl)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/assign)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/atomic)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/atomicalign)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/bools)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/buildtag)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/cgocall)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/composite)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/copylock)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/deepequalerrors)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/errorsas)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/httpresponse)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/ifaceassert)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/inspect)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/loopclosure)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/lostcancel)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/nilfunc)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/nilness)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/printf)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/shift)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/sortslice)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/stdmethods)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/stringintconv)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/structtag)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/testinggoroutine)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/tests)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/unmarshal)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/unreachable)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/unsafeptr)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/unusedresult)
BuildRequires:  golang(golang.org/x/tools/go/ast/inspector)
BuildRequires:  golang(honnef.co/go/tools/code)
BuildRequires:  golang(honnef.co/go/tools/facts)
BuildRequires:  golang(honnef.co/go/tools/simple)
BuildRequires:  golang(honnef.co/go/tools/staticcheck)
BuildRequires:  golang(honnef.co/go/tools/stylecheck)
BuildRequires:  golang(zgo.at/blackmail)
BuildRequires:  golang(zgo.at/errors)
BuildRequires:  golang(zgo.at/gadget)
BuildRequires:  golang(zgo.at/guru)
BuildRequires:  golang(zgo.at/isbot)
BuildRequires:  golang(zgo.at/json)
BuildRequires:  golang(zgo.at/tz)
BuildRequires:  golang(zgo.at/zcache)
BuildRequires:  golang(zgo.at/zdb)
BuildRequires:  golang(zgo.at/zdb/bulk)
BuildRequires:  golang(zgo.at/zhttp)
BuildRequires:  golang(zgo.at/zhttp/ctxkey)
BuildRequires:  golang(zgo.at/zhttp/header)
BuildRequires:  golang(zgo.at/zhttp/ztpl)
BuildRequires:  golang(zgo.at/zhttp/ztpl/tplfunc)
BuildRequires:  golang(zgo.at/zli)
BuildRequires:  golang(zgo.at/zlog)
BuildRequires:  golang(zgo.at/zstd/zcrypto)
BuildRequires:  golang(zgo.at/zstd/zfloat)
BuildRequires:  golang(zgo.at/zstd/zint)
BuildRequires:  golang(zgo.at/zstd/zjson)
BuildRequires:  golang(zgo.at/zstd/zruntime)
BuildRequires:  golang(zgo.at/zstd/zstring)
BuildRequires:  golang(zgo.at/zstd/zsync)
BuildRequires:  golang(zgo.at/zstripe)
BuildRequires:  golang(zgo.at/zvalidate)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/PuerkitoBio/goquery)
BuildRequires:  golang(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  golang(zgo.at/ztest)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%gobuild -o %{gobuilddir}/bin/goatcounter %{goipath}

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
%doc docs CHANGELOG.markdown README.markdown db/README.markdown
%doc tpl/_backend_sitecode.markdown tpl/api.markdown tpl/gdpr.markdown
%doc tpl/why.markdown
%{_bindir}/*

%gopkgfiles

%changelog
* Fri Aug 28 16:21:39 CEST 2020 Johan Kok <johankok@users.noreply.github.com> - 1.4.0-1
- Initial package

