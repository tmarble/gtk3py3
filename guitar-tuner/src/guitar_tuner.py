#!/usr/bin/python
#
# main.py
# Copyright (C) 2012 Tom Marble <tmarble@info9.net>
# 
# guitar-tuner is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# guitar-tuner is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk, GdkPixbuf, Gdk, Gst, GObject
import os, sys


#Comment the first line and uncomment the second before installing
#or making the tarball (alternatively, use project variables)
UI_FILE = "src/guitar_tuner.ui"
#UI_FILE = "/usr/local/share/guitar_tuner/ui/guitar_tuner.ui"


class GUI:
	LENGTH = 500  # time to play sound, in ms
	frequencies = { # Frequencies of the strings, in Hz
		'E': 369.23,
		'A': 440,
		'D': 587.33,
		'G': 783.99,
		'B': 987.77,
		'e': 1318.5
	}

	def __init__(self):
		self.builder = Gtk.Builder()
		self.builder.add_from_file(UI_FILE)
		self.builder.connect_signals(self)
		window = self.builder.get_object('window')
		window.show_all()
		
	def play_sound(self, frequency):
		pipeline = Gst.Pipeline(name='note')
		source = Gst.ElementFactory.make('audiotestsrc', 'src')
		sink = Gst.ElementFactory.make('autoaudiosink', 'output')
		source.set_property('freq', frequency)
		pipeline.add(source)
		pipeline.add(sink)
		source.link(sink)
		pipeline.set_state(Gst.State.PLAYING)
		GObject.timeout_add(self.LENGTH, self.pipeline_stop, pipeline)

	def pipeline_stop(self, pipeline):
		pipeline.set_state(Gst.State.PAUSED)		
		return False
		
	def on_quit(self, button):
		Gtk.main_quit()

	def on_button_clicked (self, button):
		label = button.get_child()
		text = label.get_label()
		self.play_sound (self.frequencies[text])
		
	def destroy(window, self):
		Gtk.main_quit()

def main():
	Gst.init_check(sys.argv)
	app = GUI()
	Gtk.main()
		
if __name__ == "__main__":
    sys.exit(main())
