#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  disks.py - Disk chooser
#  
#  Copyright 2013 Ikey Doherty <ikey@solusos.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#
import gi.repository
from gi.repository import Gtk
from basepage import BasePage

class DiskPage(BasePage):

    def __init__(self, installer):
        BasePage.__init__(self)
        self.installer = installer

    def prepare(self):
        self.installer.can_go_back(True)
        self.installer.can_go_forward(True)
        
    def get_title(self):
        return _("Where should we install?")

    def get_name(self):
        return "disks"

    def get_icon_name(self):
        return "drive-harddisk-system-symbolic"

    def get_primary_answer(self):
        return "Not yet implemented"
