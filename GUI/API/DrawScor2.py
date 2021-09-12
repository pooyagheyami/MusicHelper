#In the name of God
# -*- coding: utf-8 -*-


import wx
import wx.adv
from Config.Init import *


class DrawScore:
    def __init__(self, dc, npg):
        wx.Font.AddPrivateFont(RES_PATH + u"fonts\\Bravura.ttf")
        self.font = wx.Font(19, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL,False,"Bravura",True)
        self.dc = dc
        self.npg = npg
        self.k = 7
        self.p = 30
        self.m = 32
        self.x = 0
        self.y = 0
        

    def DrawPart(self, nPart):
        pass

    def DrawCelf(self, CelfName):
        x1 = self.x + 20
        y1 = self.y 
        if CelfName == 'Treble':
            self.dc.SetFont(self.font)
            self.dc.DrawText(chr(57424),x1,y1)
        pass

    def DrawTimS(self, TimSName):
        pass

    def DrawKeyS(self, KeySName):
        pass

    def DrawNots(self, NotName):
        self.dc.SetFont(self.font)
        self.dc.DrawText(chr(NotName),self.x,self.y)
        
        pass
    def DrawNumb(self, Numbr):
        fnt = wx.Font(11, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL,False,"Arial",True)
        self.dc.SetFont(fnt)
        self.dc.DrawText(Numbr,self.x+50,self.y+35)
        self.dc.DrawLine(0,self.y+50,1500,self.y+50)
        

    def DrawMsur(self, nMsur):
        pass

    def DrawLins(self, nSystm):
        #self.dc.SetPen(wx.PENSTYLE_SOLID)
        x0 = self.x + 20
        y0 = self.y + 28
        for l in range(5):
            self.dc.DrawLine(x0,y0+(self.k*l),x0+nSystm,y0+(self.k*l))
            
        


class MyScore ( wx.ScrolledWindow ):
    def __init__(self, parent, id, size = wx.DefaultSize):
        wx.ScrolledWindow.__init__(self, parent, id, (0, 0), size=size, style=wx.SUNKEN_BORDER)
        self.SetBackgroundColour("WHITE")
        self.SetVirtualSize((3000, 6000))
        self.SetScrollRate(20,20)

        # create a PseudoDC to record our drawing
        self.pdc = wx.adv.PseudoDC()
        self.DoDrawing(self.pdc)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, lambda x:None)
        self.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouse)

    def ConvertEventCoords(self, event):
        xView, yView = self.GetViewStart()
        xDelta, yDelta = self.GetScrollPixelsPerUnit()
        return (event.GetX() + (xView * xDelta),
            event.GetY() + (yView * yDelta))

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
        elif event.Dragging() or event.LeftUp():
            #if self.dragid != -1:
            #    x,y = self.lastpos
            #    dx = event.GetX() - x
            #    dy = event.GetY() - y
            #    r = self.pdc.GetIdBounds(self.dragid)
            #    self.pdc.TranslateId(self.dragid, dx, dy)
            #    r2 = self.pdc.GetIdBounds(self.dragid)
            #    r = r.Union(r2)
            #    r.Inflate(4,4)
            #    self.OffsetRect(r)
            #    self.RefreshRect(r, False)
            #    self.lastpos = (event.GetX(),event.GetY())
            if event.LeftUp():
                self.dragid = -1    

    def OnPaint(self, event):
        # Create a buffered paint DC.  It will create the real
        # wx.PaintDC and then blit the bitmap to it when dc is
        # deleted.
        dc = wx.BufferedPaintDC(self)

        # we need to clear the dc BEFORE calling PrepareDC
        bg = wx.Brush(self.GetBackgroundColour())
        dc.SetBackground(bg)
        dc.Clear()

        self.PrepareDC(dc)

        # create a clipping rect from our position and size
        # and the Update Region
        xv, yv = self.GetViewStart()
        dx, dy = self.GetScrollPixelsPerUnit()
        x, y   = (xv * dx, yv * dy)
        rgn = self.GetUpdateRegion()
        rgn.Offset(x,y)
        r = rgn.GetBox()

        # Draw the saved drawing operations to the dc using the calculated
        # clipping rect
        self.pdc.DrawToDCClipped(dc,r)

    def DoDrawing(self, dc):
        DrSc = DrawScore(dc,1)
        return DrSc
        #DrSc.DrawLins(2500)
        #DrSc.DrawCelf('Treble')
        
