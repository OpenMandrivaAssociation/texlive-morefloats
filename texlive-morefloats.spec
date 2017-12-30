# revision 25232
# category Package
# catalog-ctan /macros/latex/contrib/morefloats
# catalog-date 2012-01-29 16:01:54 +0100
# catalog-license lppl1.3
# catalog-version 1.0f
Name:		texlive-morefloats
Version:	1.0h
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0f-1
+ Revision: 770227
- Update to latest upstream package

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0e-2
+ Revision: 754104
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0e-1
+ Revision: 719060
- texlive-morefloats
- texlive-morefloats
- texlive-morefloats
- texlive-morefloats

