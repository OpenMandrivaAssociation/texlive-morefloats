# revision 23341
# category Package
# catalog-ctan /macros/latex/contrib/morefloats
# catalog-date 2011-07-10 20:11:03 +0200
# catalog-license lppl1.3
# catalog-version 1.0e
Name:		texlive-morefloats
Version:	1.0e
Release:	1
Summary:	Increase the number of simultaneous LaTeX floats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/morefloats
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/morefloats.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/morefloats.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/morefloats.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
LaTeX can, by default, only cope with 18 outstanding floats;
any more, and you get the error "too many unprocessed floats".
This package releases the limit; TeX itself imposes limits
(which are independent of the help offered by e-TeX). However,
if your floats can't be placed anywhere, extending the number
of floats merely delays the arrival of the inevitable error
message.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
