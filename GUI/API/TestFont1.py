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

TestText = """
a b c d e f g h i j k l m n o p q r s t u v w x y z
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
1 2 3 4 5 6 7 8 9 0 ~ ! @ # $ % ^ & * ( ) _ + - = `
\ [ ] , . / ' : " { } < > ? |  
"""
TestText2 = ''
for i in range(40,256):
        TestText2 += chr(i)+' '

TestText3 = u'\ue050\ue01A'

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,440 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		

		self.Text1 = wx.StaticText( self, wx.ID_ANY, TestText3, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text1.Wrap( -1 )

		bSizer2.Add( self.Text1, 0, wx.ALL, 5 )

		self.Text2 = wx.StaticText(self, wx.ID_ANY, '\ue000', wx.DefaultPosition, wx.DefaultSize, 0)
		self.Text2.Wrap(-1)

		bSizer2.Add(self.Text2, 0, wx.ALL, 5)


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button1, 0, wx.ALL, 5 )

		#font = wx.Font(RES_PATH+'fonts\\Bravura.otf')
		#self.fp1 = font

		self.fp1 = wx.FontPickerCtrl( self, wx.ID_ANY, wx.Font( 28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inkpen2 Special Std" ), wx.DefaultPosition, wx.DefaultSize, wx.FNTP_FONTDESC_AS_LABEL )
		self.fp1.SetMaxPointSize( 100 )
		bSizer3.Add( self.fp1, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer3, 0, 0, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.cls )
		self.fp1.Bind( wx.EVT_FONTPICKER_CHANGED, self.chsfnt )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def cls( self, event ):
		q = self.GetParent()
		q.Close()

	def chsfnt( self, event ):
		print(self.fp1.GetSelectedFont())
		font = wx.Font(self.fp1.GetSelectedFont())
		self.Text1.SetFont(self.fp1.GetSelectedFont())
		print(str(u'\u662f'))
		print(font.GetFaceName())
		print(font.GetNativeFontInfo().ToString())
		#font2 = wx.GraphicsFont(RES_PATH+u"\\fonts\\Bravura.ttf")
		wx.Font.AddPrivateFont(RES_PATH+u"fonts\\Bravura.ttf")

		font2 = wx.Font(22, wx.FONTFAMILY_TELETYPE,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL,False,'Bravura',True)

		print(font2)
		print(font2.GetFaceName())
		print(font2.GetNativeFontInfo().ToString())

		self.Text2.SetLabel(chr(57810))
		self.Text2.SetFont(font2)
		print(chr(57810))
		#self.Text1.SetFont(self.fp1)
		self.Layout()
		
		
	

