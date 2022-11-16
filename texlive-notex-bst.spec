Name:		texlive-notex-bst
Version:	42361
Release:	1
Summary:	A BibTeX style that outputs HTML
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/notex-bst
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/notex-bst.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
noTeX.bst produces a number of beautifully formatted HTML P
elements instead of TeX code. It can be used to automatically
generate bibliographies to be served on the web starting from
BibTeX files.

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/bibtex/bst/notex-bst

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
