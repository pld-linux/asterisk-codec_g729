# Available x86 optimizations:
# - generic
# - athlon
# - athlon_xp
# - barcelona
# - c3_2
# - c3
# - core2
# - i686
# - k6_3
# - nocona
# - opteron
# - opteron_sse3
# - pentium3m
# - pentium4m
# - pentium_m
# - prescott
%define		x86_32_optim	generic
# Available x86_64 bit optimizations:
# - generic
# - barcelona
# - core2
# - nocona
# - opteron
# - opteron_sse3
%define		x86_64_optim	barcelona

%ifarch %{ix86}
%define		optim %{x86_32_optim}
%endif
%ifarch %{x8664}
%define		optim %{x86_64_optim}
%endif

%define		dl_url	http://downloads.digium.com/pub/telephony/codec_g729/asterisk-%{asterisk_ver}/
%define		asterisk_ver	1.6.2.0
%define		bench_ver		1.0.7
Summary:	Digium G.729 Software Codec for Asterisk
Name:		asterisk-codec_g729
Version:	3.1.4
Release:	1
License:	Proprietary
Group:		Applications/System
Source0:	%{dl_url}/x86-32/codec_g729a-%{asterisk_ver}_%{version}-%{x86_32_optim}_32.tar.gz
# NoSource0-md5:	f5bbea87e2ffa97f8b7f1b59684085b4
NoSource:	0
Source1:	%{dl_url}/x86-64/codec_g729a-%{asterisk_ver}_%{version}-%{x86_64_optim}_64.tar.gz
# NoSource1-md5:	3bb68858e9db40769826de34b5b17a73
NoSource:	1
Source2:	http://downloads.digium.com/pub/telephony/codec_g729/benchg729/x86-32/benchg729-%{bench_ver}-x86_32
# NoSource2-md5:	428a69780df2bba0f17da061e13a3df3
NoSource:	2
Source3:	http://downloads.digium.com/pub/telephony/codec_g729/benchg729/x86-64/benchg729-%{bench_ver}-x86_64
# NoSource3-md5:	dc9a24b54d3a510e77e86773beb300ec
NoSource:	3
URL:		http://store.digium.com/productview.php?product_code=G729CODEC
BuildRequires:	asterisk-devel
Requires:	asterisk >= %{asterisk_ver}
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		moduledir	%{_libdir}/asterisk/modules

# no debug symbols
%define		_enable_debug_packages	0

%description
Digium offers a software implementation of G.729 that is compatible
with Asterisk and is properly licensed from the intellectual property
rights and patent holders.

Please visit the following web address to read more about this product
and to purchase license keys:
http://store.digium.com/productview.php?product_code=G729CODEC

Follow the instructions below to download and install the Digium G.729
Software Codec for Asterisk.

This package is built with '%{optim}' flavor.

%prep
%ifarch %{ix86}
%setup -qT -n codec_g729a-%{asterisk_ver}_%{version}-%{x86_32_optim}_32 -b0
install -p %{SOURCE2} benchg729
%endif
%ifarch %{x8664}
%setup -qT -n codec_g729a-%{asterisk_ver}_%{version}-%{x86_64_optim}_64 -b1
install -p %{SOURCE3} benchg729
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{moduledir}}
install -p codec_g729a.so $RPM_BUILD_ROOT%{moduledir}
install -p benchg729 $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_bindir}/benchg729
%attr(755,root,root) %{moduledir}/codec_g729a.so
