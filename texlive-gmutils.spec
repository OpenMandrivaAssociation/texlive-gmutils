# revision 24287
# category Package
# catalog-ctan /macros/latex/contrib/gmutils
# catalog-date 2011-10-14 16:42:22 +0200
# catalog-license lppl
# catalog-version v0.996
Name:		texlive-gmutils
Version:	v0.996
Release:	1
Summary:	Support macros for other packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gmutils
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmutils.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmutils.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Miscellaneous macros used by others of the author's packages.
Contents of the package: \newgif and other globals; \@ifnextcat
and \@ifXeTeX; \(Re)storeMacro(s) to override redefinitions;
\afterfi and friends; commands from relsize, etc.; "almost an
environment" or redefinition of \begin (\begin* doesn't check
if the argument environment is defined).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gmutils/gmRCS.sty
%{_texmfdistdir}/tex/latex/gmutils/gmampulex.sty
%{_texmfdistdir}/tex/latex/gmutils/gmbase.sty
%{_texmfdistdir}/tex/latex/gmutils/gmcommand.sty
%{_texmfdistdir}/tex/latex/gmutils/gmenvir.sty
%{_texmfdistdir}/tex/latex/gmutils/gmlogos.sty
%{_texmfdistdir}/tex/latex/gmutils/gmmeta.sty
%{_texmfdistdir}/tex/latex/gmutils/gmmw.sty
%{_texmfdistdir}/tex/latex/gmutils/gmnotonlypream.sty
%{_texmfdistdir}/tex/latex/gmutils/gmparts.sty
%{_texmfdistdir}/tex/latex/gmutils/gmrelsize.sty
%{_texmfdistdir}/tex/latex/gmutils/gmtypos.sty
%{_texmfdistdir}/tex/latex/gmutils/gmurl.sty
%{_texmfdistdir}/tex/latex/gmutils/gmutils.sty
%doc %{_texmfdistdir}/doc/latex/gmutils/README
%doc %{_texmfdistdir}/doc/latex/gmutils/gmutils.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
