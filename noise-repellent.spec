
# no actual releases since October 2017, homepage suggest building from git
%define commit 60167c09fc51242101a041c9d6642bc92fdabcbb
%define timestamp 20180917

Summary:	An lv2 plugin for broadband noise reduction
Name:		noise-repellent
Version:	0.1.4.%{timestamp}
Release:	1
License:	GPL v3
Group:		Applications
Source0:	https://github.com/lucianodato/noise-repellent/archive/%{commit}/%{name}-%{version}.tar.gz
# Source0-md5:	cf34c73b4494f15549c6c4fe5e4a068b
Patch0:		lv2_dir.patch
URL:		https://github.com/lucianodato/noise-repellent
BuildRequires:	fftw3-devel
BuildRequires:	lv2-devel
BuildRequires:	meson
BuildRequires:	ninja
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprovfiles	%{_libdir}/lv2

%description
An lv2 plug-in for broadband noise reduction.

Features:
- Spectral gating and spectral subtraction suppression rule
- Adaptive and manual noise thresholds estimation
- Adjustable noise floor
- Adjustable offset of thresholds to perform over-subtraction
- Time smoothing and a masking estimation to reduce artifacts
- Basic onset detector to avoid transients suppression
- Whitening of the noise floor to mask artifacts and to recover higher
  frequencies
- Option to listen to the residual signal
- Soft bypass
- Noise profile saved with the session

%package lv2
Summary:	An lv2 plugin for broadband noise reduction
Group:		Applications

%description lv2
An lv2 plug-in for broadband noise reduction.

Features:
- Spectral gating and spectral subtraction suppression rule
- Adaptive and manual noise thresholds estimation
- Adjustable noise floor
- Adjustable offset of thresholds to perform over-subtraction
- Time smoothing and a masking estimation to reduce artifacts
- Basic onset detector to avoid transients suppression
- Whitening of the noise floor to mask artifacts and to recover higher
  frequencies
- Option to listen to the residual signal
- Soft bypass
- Noise profile saved with the session

%prep
%setup -qn %{name}-%{commit}

%patch0 -p1

%build

%meson build

%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files lv2
%defattr(644,root,root,755)
%doc README.md
%dir %{_libdir}/lv2/nrepel.lv2
%{_libdir}/lv2/nrepel.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/nrepel.lv2/*.so
BuildRequires:  rpmbuild(macros) >= 1.726

