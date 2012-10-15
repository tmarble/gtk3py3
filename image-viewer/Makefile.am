## Process this file with automake to produce Makefile.in
## Created by Anjuta

SUBDIRS = src 

image_viewerdocdir = ${prefix}/doc/image_viewer
image_viewerdoc_DATA = \
	README\
	COPYING\
	AUTHORS\
	ChangeLog\
	INSTALL\
	NEWS


EXTRA_DIST = $(image_viewerdoc_DATA)

# The desktop files
desktopdir = $(datadir)/applications
desktop_DATA = ImageViewerDemo.desktop

DISTCLEANFILES = aclocal.m4 configure install-sh Makefile.in missing

# Remove doc directory on uninstall
uninstall-local:
	-rm -r $(image_viewerdocdir)
