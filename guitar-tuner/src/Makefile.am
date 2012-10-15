## Process this file with automake to produce Makefile.in
## Created by Anjuta


uidir = $(pkgdatadir)/ui
ui_DATA = guitar_tuner.ui


## The main script
bin_SCRIPTS = guitar_tuner.py

## Directory where .class files will be installed
guitar_tunerdir = $(pythondir)/guitar_tuner


guitar_tuner_PYTHON = \
	guitar_tuner.py


EXTRA_DIST = $(ui_DATA)


# Remove ui directory on uninstall
uninstall-local:

	-rm -r $(uidir)

	-rm -r $(pkgdatadir)
