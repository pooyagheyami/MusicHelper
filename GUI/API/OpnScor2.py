# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from . import Xmlopen

###########################################################################
## Class MyPanel3
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, filpath, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		V1 = wx.BoxSizer( wx.VERTICAL )

		self.filpath = filpath

		txt, scor = Xmlopen.xml2dbwrite(self.filpath[0],'main.db')
		Xmlopen.xml2dbf2(self.filpath[0],'main.db')

		self.SW1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.SW1.SetScrollRate( 20, 20 )
		V2 = wx.BoxSizer( wx.VERTICAL )

		self.Txt1 = wx.StaticText( self.SW1, wx.ID_ANY, txt, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Txt1.Wrap( 1 )

		V2.Add( self.Txt1, 1, wx.ALL|wx.EXPAND, 5 )

		#self.Txt2 = wx.StaticText( self.SW1, wx.ID_ANY, scor, wx.DefaultPosition, wx.DefaultSize, 0 )
		#self.Txt2.Wrap( 1 )

		#V2.Add( self.Txt2, 1, wx.ALL|wx.EXPAND, 5 )


		self.SW1.SetSizer( V2 )
		self.SW1.Layout()
		V2.Fit( self.SW1 )
		V1.Add( self.SW1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( V1 )
		self.Layout()

	def __del__( self ):
		pass


