Name:		texlive-gmutils
Version:	24287
Release:	2
Summary:	Support macros for other packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gmutils
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmutils.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmutils.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
