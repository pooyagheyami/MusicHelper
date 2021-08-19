#In the name of GOD
#please put your code under here
# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.py as py

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		VS = wx.BoxSizer( wx.VERTICAL )
		win = py.shell.Shell(self)
		VS.Add( win, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( VS )
		self.Layout()

	def __del__( self ):
		pass


