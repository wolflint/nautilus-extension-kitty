#!/usr/bin/env python3
from gi import require_version
require_version('Gtk', '3.0')
require_version('Nautilus', '3.0')

from gi.repository import Nautilus, GObject
import os, subprocess

PROCESSNAME = 'kitty'

class KittyExtension(Nautilus.MenuProvider, GObject.GObject):
    def __init__(self):
        pass

    def launch_kitty(self, menu: Nautilus.MenuItem, files):
        path = '.'
        args = '--working-directory'

        for file in files:
            dirpath = file.get_location().get_path()
            if os.path.isdir(dirpath) and os.path.exists(dirpath):
                path = dirpath

        subprocess.Popen([PROCESSNAME, args, path], shell=False)

    def get_file_items(self, window, files):
        item = Nautilus.MenuItem(
            name="KittyOpen",
            label="Open in Kitty",
            tip="Opens the current folder in kitty"
        )
        item.connect('activate', self.launch_kitty, files)
        return [item]

    def get_background_items(self, window, file_):
        item = Nautilus.MenuItem(
            name="KittyOpenBackGround",
            label="Open in Kitty",
            tip="Opens the current folder in kitty"
        )
        item.connect('activate', self.launch_kitty, [file_])
        return [item]
