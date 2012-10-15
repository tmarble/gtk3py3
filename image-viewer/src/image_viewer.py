#!/usr/bin/python3
# -*- Mode: python; py-indent-offset: 4; coding: utf-8  -*-
#
# main.py
# Copyright (C) 2012 Tom Marble <tmarble@info9.net>
#
# image-viewer is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# image-viewer is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk, GdkPixbuf, Gdk
import os, sys

class GUI:
    def __init__(self):
        window = Gtk.Window()
        window.set_title ("Image Viewer Demo")
        window.connect_after('destroy', self.destroy)
        box = Gtk.Box()
        box.set_spacing (5)
        box.set_orientation (Gtk.Orientation.VERTICAL)
        window.add (box)
        self.image = Gtk.Image()
        box.pack_start(self.image, False, True, 0)
        button = Gtk.Button ("Open a picture...")
        button.connect_after('clicked', self.on_open_clicked)
        box.pack_start (button, False, False, 0)
        window.show_all()

    def on_open_clicked (self, button):
        dialog = Gtk.FileChooserDialog("Open Image", button.get_toplevel(), 
                                       Gtk.FileChooserAction.OPEN)
        dialog.add_button(Gtk.STOCK_CANCEL, 0)
        dialog.add_button(Gtk.STOCK_OK, 1)
        dialog.set_default_response(1)
        filefilter = Gtk.FileFilter()
        filefilter.add_pixbuf_formats()
        dialog.set_filter(filefilter)
        if dialog.run() == 1:
            self.image.set_from_file(dialog.get_filename())
        dialog.destroy()

    def destroy(window, self):
        Gtk.main_quit()

def main():
    app = GUI()
    Gtk.main()

if __name__ == "__main__":
    sys.exit(main())
