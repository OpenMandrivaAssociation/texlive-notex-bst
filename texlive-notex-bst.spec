%global tl_name notex-bst
%global tl_revision 76790

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A BibTeX style that outputs HTML
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/utils/misc/noTeX.bst
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/notex-bst.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
noTeX.bst produces a number of beautifully formatted HTML P elements
instead of TeX code. It can be used to automatically generate
bibliographies to be served on the web starting from BibTeX files.

