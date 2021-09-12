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
import wx.dataview
from Database.PostGet import *

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 668,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		V1 = wx.BoxSizer( wx.VERTICAL )
		MyData = Get(u'Main.db',u'',u'TableShow.sql')

		Field = ['id', 'NoteName', 'Npart', 'Nmesur', 'Nnote', 'Ndur','Dprw','Dnxt','Dsop','Dalt','Dtnr','Dbas']
		i = 0
		self.Col = []

		self.DVLC1 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		for f in Field:
			self.Col.append( self.DVLC1.AppendTextColumn( f, wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE ) )
			i += 1

		V1.Add( self.DVLC1, 1, wx.ALL|wx.EXPAND, 5 )

		print(MyData.SQLtxt)
		Data = MyData.GetFromDbf()
		print(Data)
		for d in Data:
			da = (str(d[0]),d[1],str(d[2]),str(d[3]),str(d[4]),str(d[5]),'','','','','','')
			self.DVLC1.AppendItem(da)
		
		


		self.SetSizer( V1 )
		self.Layout()

	def __del__( self ):
		pass



