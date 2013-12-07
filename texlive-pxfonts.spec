# revision 15878
# category Package
# catalog-ctan /fonts/pxfonts
# catalog-date 2009-01-15 09:33:18 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-pxfonts
Version:	20090115
Release:	4
Summary:	Palatino-like fonts in support of mathematics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/pxfonts
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxfonts.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxfonts.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Pxfonts supplies virtual text roman fonts using Adobe Palatino
(or URWPalladioL) with some modified and additional text
symbols in the OT1, T1, and TS1 encodings; maths alphabets
using Palatino/Palladio; maths fonts providing all the symbols
of the Computer Modern and AMS fonts, including all the Greek
capital letters from CMR; and additional maths fonts of various
other symbols. The set is complemented by a sans-serif set of
text fonts, based on Helvetica/NimbusSanL, and a monospace set
derived from the parallel TX font set. All the fonts are in
Type 1 format (AFM and PFB files), and are supported by TeX
metrics (VF and TFM files) and macros for use with LaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxbex.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxbexa.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxbmia.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxbsy.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxbsya.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxbsyb.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxbsyc.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxex.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxexa.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxmia.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxsy.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxsya.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxsyb.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxsyc.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/rpcxb.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/rpcxbi.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/rpcxi.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/rpcxr.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/rpxb.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/rpxbi.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/rpxbmi.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/rpxbsc.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/rpxi.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/rpxmi.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/rpxr.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/rpxsc.afm
%{_texmfdistdir}/fonts/map/dvips/pxfonts/pxfonts.map
%{_texmfdistdir}/fonts/map/dvips/pxfonts/pxr.map
%{_texmfdistdir}/fonts/map/dvips/pxfonts/pxr1.map
%{_texmfdistdir}/fonts/map/dvips/pxfonts/pxr2.map
%{_texmfdistdir}/fonts/map/dvips/pxfonts/pxr3.map
%{_texmfdistdir}/fonts/tfm/public/pxfonts/p1xb.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/p1xbi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/p1xbsc.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/p1xbsl.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/p1xi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/p1xr.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/p1xsc.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/p1xsl.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pcxb.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pcxbi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pcxbsl.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pcxi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pcxr.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pcxsl.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxb.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxbex.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxbexa.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxbi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxbmi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxbmi1.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxbmia.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxbsc.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxbsl.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxbsy.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxbsya.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxbsyb.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxbsyc.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxex.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxexa.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxmi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxmi1.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxmia.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxr.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxsc.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxsl.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxsy.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxsya.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxsyb.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxsyc.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpcxb.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpcxbi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpcxbsl.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpcxi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpcxr.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpcxsl.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxb.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxbi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxbmi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxbsc.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxbsl.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxmi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxpplb.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxpplbi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxpplbo.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxpplr.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxpplri.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxpplro.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxr.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxsc.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxsl.tfm
%{_texmfdistdir}/fonts/type1/public/pxfonts/pxbex.pfb
%{_texmfdistdir}/fonts/type1/public/pxfonts/pxbexa.pfb
%{_texmfdistdir}/fonts/type1/public/pxfonts/pxbmia.pfb
%{_texmfdistdir}/fonts/type1/public/pxfonts/pxbsy.pfb
%{_texmfdistdir}/fonts/type1/public/pxfonts/pxbsya.pfb
%{_texmfdistdir}/fonts/type1/public/pxfonts/pxbsyb.pfb
%{_texmfdistdir}/fonts/type1/public/pxfonts/pxbsyc.pfb
%{_texmfdistdir}/fonts/type1/public/pxfonts/pxex.pfb
%{_texmfdistdir}/fonts/type1/public/pxfonts/pxexa.pfb
%{_texmfdistdir}/fonts/type1/public/pxfonts/pxmia.pfb
%{_texmfdistdir}/fonts/type1/public/pxfonts/pxsy.pfb
%{_texmfdistdir}/fonts/type1/public/pxfonts/pxsya.pfb
%{_texmfdistdir}/fonts/type1/public/pxfonts/pxsyb.pfb
%{_texmfdistdir}/fonts/type1/public/pxfonts/pxsyc.pfb
%{_texmfdistdir}/fonts/type1/public/pxfonts/rpcxb.pfb
%{_texmfdistdir}/fonts/type1/public/pxfonts/rpcxbi.pfb
%{_texmfdistdir}/fonts/type1/public/pxfonts/rpcxi.pfb
%{_texmfdistdir}/fonts/type1/public/pxfonts/rpcxr.pfb
%{_texmfdistdir}/fonts/type1/public/pxfonts/rpxb.pfb
%{_texmfdistdir}/fonts/type1/public/pxfonts/rpxbi.pfb
%{_texmfdistdir}/fonts/type1/public/pxfonts/rpxbmi.pfb
%{_texmfdistdir}/fonts/type1/public/pxfonts/rpxbsc.pfb
%{_texmfdistdir}/fonts/type1/public/pxfonts/rpxi.pfb
%{_texmfdistdir}/fonts/type1/public/pxfonts/rpxmi.pfb
%{_texmfdistdir}/fonts/type1/public/pxfonts/rpxr.pfb
%{_texmfdistdir}/fonts/type1/public/pxfonts/rpxsc.pfb
%{_texmfdistdir}/fonts/vf/public/pxfonts/p1xb.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/p1xbi.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/p1xbsc.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/p1xbsl.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/p1xi.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/p1xr.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/p1xsc.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/p1xsl.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pcxb.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pcxbi.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pcxbsl.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pcxi.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pcxr.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pcxsl.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pxb.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pxbi.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pxbmi.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pxbmi1.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pxbsc.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pxbsl.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pxi.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pxmi.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pxmi1.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pxr.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pxsc.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pxsl.vf
%{_texmfdistdir}/tex/latex/pxfonts/omlpxmi.fd
%{_texmfdistdir}/tex/latex/pxfonts/omlpxr.fd
%{_texmfdistdir}/tex/latex/pxfonts/omspxr.fd
%{_texmfdistdir}/tex/latex/pxfonts/omspxsy.fd
%{_texmfdistdir}/tex/latex/pxfonts/omxpxex.fd
%{_texmfdistdir}/tex/latex/pxfonts/ot1pxr.fd
%{_texmfdistdir}/tex/latex/pxfonts/ot1pxss.fd
%{_texmfdistdir}/tex/latex/pxfonts/ot1pxtt.fd
%{_texmfdistdir}/tex/latex/pxfonts/pxfonts.sty
%{_texmfdistdir}/tex/latex/pxfonts/t1pxr.fd
%{_texmfdistdir}/tex/latex/pxfonts/t1pxss.fd
%{_texmfdistdir}/tex/latex/pxfonts/t1pxtt.fd
%{_texmfdistdir}/tex/latex/pxfonts/ts1pxr.fd
%{_texmfdistdir}/tex/latex/pxfonts/ts1pxss.fd
%{_texmfdistdir}/tex/latex/pxfonts/ts1pxtt.fd
%{_texmfdistdir}/tex/latex/pxfonts/upxexa.fd
%{_texmfdistdir}/tex/latex/pxfonts/upxmia.fd
%{_texmfdistdir}/tex/latex/pxfonts/upxr.fd
%{_texmfdistdir}/tex/latex/pxfonts/upxss.fd
%{_texmfdistdir}/tex/latex/pxfonts/upxsya.fd
%{_texmfdistdir}/tex/latex/pxfonts/upxsyb.fd
%{_texmfdistdir}/tex/latex/pxfonts/upxsyc.fd
%{_texmfdistdir}/tex/latex/pxfonts/upxtt.fd
%doc %{_texmfdistdir}/doc/fonts/pxfonts/00bug_fix.txt
%doc %{_texmfdistdir}/doc/fonts/pxfonts/COPYRIGHT
%doc %{_texmfdistdir}/doc/fonts/pxfonts/pxfontsdoc.pdf
%doc %{_texmfdistdir}/doc/fonts/pxfonts/pxfontsdoc.tex
%doc %{_texmfdistdir}/doc/fonts/pxfonts/pxfontsdocA4.pdf
%doc %{_texmfdistdir}/doc/fonts/pxfonts/pxfontsdocA4.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090115-2
+ Revision: 755530
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090115-1
+ Revision: 719416
- texlive-pxfonts
- texlive-pxfonts
- texlive-pxfonts
- texlive-pxfonts

