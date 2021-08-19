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
from music21 import *

###########################################################################
## Class MyPanel2
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,196 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vz = wx.BoxSizer( wx.VERTICAL )
		intro = "Welcom to PyCrust"

		self.Cmdtxt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Vz.Add( self.Cmdtxt, 0, wx.ALL|wx.EXPAND, 5 )

		self.shwlin = wx.StaticText( self, wx.ID_ANY, u"prnt", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.shwlin.Wrap( 1 )

		Vz.Add( self.shwlin, 1, wx.ALL|wx.EXPAND, 5 )

		self.DoIt = wx.Button( self, wx.ID_ANY, u"RunCmd", wx.DefaultPosition, wx.DefaultSize, 0 )
		Vz.Add( self.DoIt, 0, wx.ALL, 5 )


		self.SetSizer( Vz )
		self.Layout()

		# Connect Events
		self.DoIt.Bind( wx.EVT_BUTTON, self.runscrpt )

	def __del__( self ):
		pass

	
	# Virtual event handlers, overide them in your derived class
	def runscrpt( self, event ):
		event.Skip()


