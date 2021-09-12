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
from . import Xmlopen
from . import DrawScor1 as DS

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, filpath, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,456 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )
		
		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.filpath = filpath

		print(self.filpath)
		txt,scor = Xmlopen.xml2dbwrite(self.filpath[0],'main.db')

		self.btn1 = wx.Button( self, wx.ID_ANY, u"Play", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz1.Add( self.btn1, 0, wx.ALL, 5 )

		self.btn2 = wx.Button( self, wx.ID_ANY, u"Pause", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz1.Add( self.btn2, 0, wx.ALL, 5 )

		self.btn3 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz1.Add( self.btn3, 0, wx.ALL, 5 )

		self.btn4 = wx.Button( self, wx.ID_ANY, u"Step", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz1.Add( self.btn4, 0, wx.ALL, 5 )

		self.btn5 = wx.Button( self, wx.ID_ANY, u"ML Show", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz1.Add( self.btn5, 0, wx.ALL, 5 )


		Vsz1.Add( Hsz1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		#self.scorbrd = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.ALWAYS_SHOW_SB|wx.BORDER_RAISED|wx.HSCROLL|wx.VSCROLL )
		#self.scorbrd.SetScrollRate( 20, 20 )
		self.scorbrd = DS.MyScore(self, wx.ID_ANY)
		Vsz2 = wx.BoxSizer( wx.VERTICAL )

		#self.pseudoDC = wx.StaticBitmap( self.scorbrd, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		#Vsz2.Add( self.pseudoDC, 1, wx.ALL|wx.EXPAND, 5 )

		#self.mytxt = wx.TextCtrl(self, wx.ID_ANY, txt, wx.DefaultPosition, wx.DefaultSize, 0)
		#Vsz2.Add( self.mytxt, 1, wx.ALL|wx.EXPAND, 5)


		self.scorbrd.SetSizer( Vsz2 )
		self.scorbrd.Layout()
		Vsz2.Fit( self.scorbrd )
		Vsz1.Add( self.scorbrd, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		Vsz1.Add( bSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( Vsz1 )
		self.Layout()

		# Connect Events
		self.btn1.Bind( wx.EVT_BUTTON, self.play )
		self.btn2.Bind( wx.EVT_BUTTON, self.paus )
		self.btn3.Bind( wx.EVT_BUTTON, self.back)
		self.btn4.Bind( wx.EVT_BUTTON, self.step )
		self.btn5.Bind( wx.EVT_BUTTON, self.mlal )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def play( self, event ):
		event.Skip()

	def paus( self, event ):
		event.Skip()


	def back( self, event ):
		event.Skip()

	def step( self, event ):
		event.Skip()

	def mlal( self, event ):
		event.Skip()


