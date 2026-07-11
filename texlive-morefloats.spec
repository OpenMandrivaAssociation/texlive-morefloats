%global tl_name morefloats
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1a
Release:	%{tl_revision}.1
Summary:	Increase the number of simultaneous LaTeX floats
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/morefloats
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/morefloats.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/morefloats.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/morefloats.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LaTeX can, by default, only cope with 18 outstanding floats; any more,
and you get the error "too many unprocessed floats". This package
releases the limit; TeX itself imposes limits (which are independent of
the help offered by e-TeX). However, if your floats can't be placed
anywhere, extending the number of floats merely delays the arrival of
the inevitable error message.

