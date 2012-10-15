# Makefile.am

# Prefix bin_ tells where to copy this program
bin_SCRIPTS = gtune3

# the shared files, like UI files
gtune3sharedir = ${prefix}/share/gtune3
gtune3share_DATA = gtune3.ui gtune3.svg

# List of files to be distributed
EXTRA_DIST = $(bin_SCRIPTS) $(gtune3share_DATA)

# The desktop files
desktopdir = $(datadir)/applications
desktop_DATA = gtune3.desktop

DISTCLEANFILES = aclocal.m4 configure install-sh Makefile.in missing

maintainer-clean-generic:
	rm -f *~
