# Available x86 optimizations:
# - athlon_32
# - athlon_xp_32
# - barcelona_32
# - c3_2_32
# - c3_32
# - core2_32
# - generic_32
# - i686_32
# - k6_3_32
# - nocona_32
# - opteron_32
# - opteron_sse3_32
# - pentium3m_32
# - pentium4m_32
# - pentium_m_32
# - prescott_32
%define		x86_optim	generic_32
# Available x86_64 bit optimizations:
# - core2_64
# - generic_64
# - nocona_64
# - opteron_64
# - opteron_sse3_64
%define		x86_64_optim	generic_64

%define		dl_url	http://downloads.digium.com/pub/telephony/codec_g729/asterisk-%{asterisk_ver}/
%define		asterisk_ver	1.6.1
%define		bench_ver		1.0.7
Summary:	Digium G.729 Software Codec for Asterisk
Name:		asterisk-codec_g729
Version:	3.1.4
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	%{dl_url}/x86-32/codec_g729a-%{asterisk_ver}_%{version}-%{x86_optim}.tar.gz
# Source0-md5:	177828ca5ec0b7477883d81dbe74558f
Source1:	%{dl_url}/x86-64/codec_g729a-%{asterisk_ver}_%{version}-%{x86_64_optim}.tar.gz
# Source1-md5:	2e3f13ff76ac7925bf16be920cd71fd0
URL:		http://downloads.digium.com/pub/telephony/codec_g729/
BuildRequires:	asterisk-devel
Requires:	asterisk >= %{asterisk_ver}
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		moduledir	%{_libdir}/asterisk/modules

%description
Digium offers a software implementation of G.729 that is compatible
with Asterisk and is properly licensed from the intellectual property
rights and patent holders.

Please visit the following web address to read more about this product
and to purchase license keys:
http://store.digium.com/productview.php?product_code=G729CODEC

Follow the instructions below to download and install the Digium G.729
Software Codec for Asterisk.

%prep
%ifarch %{ix86}
%define	sno		0
%define	optim	%{x86_optim}
%endif
%ifarch %{x8664}
%define	sno		1
%define	optim	%{x86_64_optim}
%endif
%setup -qT -n codec_g729a-%{asterisk_ver}_%{version}-%{optim} -b%{sno}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{moduledir}
install -p codec_g729a.so $RPM_BUILD_ROOT%{moduledir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{moduledir}/codec_g729a.so