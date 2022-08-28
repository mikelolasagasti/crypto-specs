# Generated by go2rpm 1.8.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/cloudflare/circl
%global goipath         github.com/cloudflare/circl
Version:                1.2.0

%gometa

%global common_description %{expand:
CIRCL: Cloudflare Interoperable Reusable Cryptographic Library.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        CIRCL: Cloudflare Interoperable Reusable Cryptographic Library

License:        BSD-3-Clause
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
