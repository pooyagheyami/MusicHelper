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
from Config.Init import *

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		V1 = wx.BoxSizer( wx.VERTICAL )

		H1 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt1 = wx.StaticText( self, wx.ID_ANY, u"Character code", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt1.Wrap( -1 )

		H1.Add( self.txt1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.cod = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		H1.Add( self.cod, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.shw = wx.Button( self, wx.ID_ANY, u"Show", wx.DefaultPosition, wx.DefaultSize, 0 )
		H1.Add( self.shw, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.crt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		H1.Add( self.crt, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		V1.Add( H1, 0, wx.EXPAND, 5 )

		H2 = wx.BoxSizer( wx.HORIZONTAL )

		self.Chr = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Chr.Wrap( -1 )

		H2.Add( self.Chr, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		V1.Add( H2, 1, wx.EXPAND, 5 )

		H3 = wx.BoxSizer( wx.HORIZONTAL )

		self.cnl = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		H3.Add( self.cnl, 0, wx.ALL, 5 )

		self.oky = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		H3.Add( self.oky, 0, wx.ALL, 5 )


		V1.Add( H3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( V1 )
		self.Layout()

		# Connect Events
		self.shw.Bind( wx.EVT_BUTTON, self.showit )
		self.cnl.Bind( wx.EVT_BUTTON, self.cnclit )
		self.oky.Bind( wx.EVT_BUTTON, self.okyit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def showit( self, event ):
		icod = self.cod.GetValue()
		wx.Font.AddPrivateFont(RES_PATH + u"fonts\\Bravura.ttf")
		font = wx.Font(19, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL,False,"Bravura",True)
		#font = self.GetFont()
		#font.SetPointSize(24)
		#font.SetWeight(wx.FONTWEIGHT_BOLD)
		mychr = chr(int(icod))
		print(self.crt.GetValue())
		print(font)
		mychr2 = str(self.crt.GetValue())

		self.Chr.SetLabel(str(mychr))
		self.Chr.SetFont(font)
		print(font.GetFaceName())
		print(font.GetEncoding())

		event.Skip()

	def cnclit( self, event ):
		q = self.GetParent()
		q.Close()

		event.Skip()

	def okyit( self, event ):
		j = 61192 - 57344
		event.Skip()
