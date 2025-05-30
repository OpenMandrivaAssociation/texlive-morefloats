Name:		texlive-morefloats
Version:	73637
Release:	1
Summary:	Increase the number of simultaneous LaTeX floats
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/morefloats
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/morefloats.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/morefloats.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/morefloats.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LaTeX can, by default, only cope with 18 outstanding floats;
any more, and you get the error "too many unprocessed floats".
This package releases the limit; TeX itself imposes limits
(which are independent of the help offered by e-TeX). However,
if your floats can't be placed anywhere, extending the number
of floats merely delays the arrival of the inevitable error
message.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/morefloats/morefloats.sty
%doc %{_texmfdistdir}/doc/latex/morefloats/README
%doc %{_texmfdistdir}/doc/latex/morefloats/morefloats-example.pdf
%doc %{_texmfdistdir}/doc/latex/morefloats/morefloats-example.tex
%doc %{_texmfdistdir}/doc/latex/morefloats/morefloats.pdf
#- source
%doc %{_texmfdistdir}/source/latex/morefloats/morefloats.drv
%doc %{_texmfdistdir}/source/latex/morefloats/morefloats.dtx
%doc %{_texmfdistdir}/source/latex/morefloats/morefloats.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
