## Process this file with automake to produce Makefile.in
## Created by Anjuta

SUBDIRS = src 

guitar_tunerdocdir = ${prefix}/doc/guitar_tuner
guitar_tunerdoc_DATA = \
	README\
	COPYING\
	AUTHORS\
	ChangeLog\
	INSTALL\
	NEWS


EXTRA_DIST = $(guitar_tunerdoc_DATA)


# Remove doc directory on uninstall
uninstall-local:
	-rm -r $(guitar_tunerdocdir)
