# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
from Config.Init import *

from . import DrawScor2 as DS

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 600,550 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		V1 = wx.BoxSizer( wx.VERTICAL )

		#self.SW1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SUNKEN|wx.HSCROLL|wx.VSCROLL )
		#self.SetBackgroundColour("WHITE")
		#self.SetVirtualSize((2000, 2000))
		#self.SW1.SetScrollRate( 20, 20 )
		self.SW1 = DS.MyScore(self,wx.ID_ANY)
		V1.Add( self.SW1, 1, wx.EXPAND |wx.ALL, 5 )

		# create a PseudoDC to record our drawing
		self.SW1.pdc = wx.adv.PseudoDC()
		#self.DoDrawing(self.pdc)
		ch = self.SW1.DoDrawing(self.SW1.pdc)
		m = 57343
		n = 57344
		for i in range(104):
                        ch.x = 0
                        ch.y += 50
                        for j in range(37):
                                ch.x += 35
                                m += 1
                                ch.DrawNots(m)
                        ch.DrawNumb(str(n)+'-'+str(m))
                        n = m


		self.SetSizer( V1 )
		self.Layout()

		#self.Bind(wx.EVT_PAINT, self.OnPaint)
		#self.Bind(wx.EVT_ERASE_BACKGROUND, lambda x:None)
		#self.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouse)

	def __del__( self ):
		pass
	'''

	def ConvertEventCoords(self, event):
		xView, yView = self.GetViewStart()
		xDelta, yDelta = self.GetScrollPixelsPerUnit()
		return (event.GetX() + (xView * xDelta),event.GetY() + (yView * yDelta))

	def OffsetRect(self, r):
		xView, yView = self.GetViewStart()
		xDelta, yDelta = self.GetScrollPixelsPerUnit()
		r.Offset(-(xView*xDelta),-(yView*yDelta))

	def OnMouse(self, event):
		if event.LeftDown():
			x,y = self.ConvertEventCoords(event)
			#l = self.pdc.FindObjectsByBBox(x, y)
			l = self.pdc.FindObjects(x, y, 0)
			for id in l:
				if not self.pdc.GetIdGreyedOut(id):
					self.dragid = id
					self.lastpos = (event.GetX(),event.GetY())
					break
		elif event.RightDown():
			x,y = self.ConvertEventCoords(event)
			#l = self.pdc.FindObjectsByBBox(x, y)
			l = self.pdc.FindObjects(x, y, 0)
			if l:
				self.pdc.SetIdGreyedOut(l[0], not self.pdc.GetIdGreyedOut(l[0]))
				r = self.pdc.GetIdBounds(l[0])
				r.Inflate(4,4)
				self.OffsetRect(r)
				self.RefreshRect(r, False)

	def OnPaint(self, event):
		# Create a buffered paint DC.  It will create the real
		# wx.PaintDC and then blit the bitmap to it when dc is
		# deleted.
		self.dc = wx.BufferedPaintDC(self)

		# we need to clear the dc BEFORE calling PrepareDC
		bg = wx.Brush(self.GetBackgroundColour())
		self.dc.SetBackground(bg)
		self.dc.Clear()
		self.SW1.PrepareDC(self.dc)

		# create a clipping rect from our position and size
		# and the Update Region
		xv, yv = self.SW1.GetViewStart()
		dx, dy = self.SW1.GetScrollPixelsPerUnit()
		x, y   = (xv * dx, yv * dy)
		rgn = self.GetUpdateRegion()
		rgn.Offset(x,y)
		r = rgn.GetBox()

		# Draw the saved drawing operations to the dc using the calculated
		# clipping rect
		self.pdc.DrawToDCClipped(self.dc,r)
		
	def DoDrawing(self, dc):
                wx.Font.AddPrivateFont(RES_PATH + u"fonts\\Bravura.ttf")
                self.font = wx.Font(19, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL,False,"Bravura",True)
                dc.SetFont(self.font)
                j = 61192 - 57344
                x, y = (10,10)
                for c in range(40):
                        dc.DrawText(chr(57344+c),x,y+10)
                        #xView, yView = self.GetViewStart()
                        #print(xView,yView)
                        dc.DrawText(chr(57424+c),x+10,y)
       '''


