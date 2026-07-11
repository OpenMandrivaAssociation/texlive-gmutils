%global tl_name gmutils
%global tl_revision 24287

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.996
Release:	%{tl_revision}.1
Summary:	Support macros for other packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gmutils
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gmutils.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gmutils.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Miscellaneous macros used by others of the author's packages. Contents
of the package: \newgif and other globals; \@ifnextcat and \@ifXeTeX;
\(Re)storeMacro(s) to override redefinitions; \afterfi and friends;
commands from relsize, etc.; "almost an environment" or redefinition of
\begin (\begin* doesn't check if the argument environment is defined).

