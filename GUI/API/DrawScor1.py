#In the name of God
# -*- coding: utf-8 -*-


import wx
import wx.adv
from Config.Init import *
from music21 import *

class DrawScore:
    def __init__(self, dc, npg):
        wx.Font.AddPrivateFont(RES_PATH + u"fonts\\Bravura.ttf")
        self.font = wx.Font(21, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL,False,"Bravura",True)
        self.dc = dc
        self.npg = npg
        self.k = 7
        self.p = 50
        self.m = 32
        
        self.mergT = 80
        self.mergL = 70

    def DrawKark(self, nChar,x,y,fntsiz):
        myfont = wx.Font(fntsiz,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL,False,"Bravura",True)
        self.dc.SetFont(myfont)
        self.dc.DrawText(chr(nChar),x,y)

    def DrawPart(self, nPart,x,y):
        x0 = x
        y0 = y
        for p in range(nPart):
            x,y = self.DrawLins(1500,x,y)
            self.dc.SetFont(self.font)
            self.dc.DrawText(chr(57392),x,y-25)
            y += 50
               
        self.dc.DrawLine(x0,y0+35,x,y)
            
        pass

    def Draw1Line(self, x, y, x1, y1):
        self.dc.DrawLine(x, y, x1, y1)

    def DrawCelf(self, CelfName,x ,y):
        print(x,y)
        self.dc.SetFont(self.font)
        if CelfName == 'Treble':
            self.dc.DrawText(chr(57424),x,y)
        if CelfName == 'Bass':
            self.dc.DrawText(chr(57442),x,y)
        if CelfName == 'Alto':
            self.dc.DrawText(chr(57436),x,y)
        pass

    def DrawTimS(self, TimSName,x,y):
        timnumb = [57472,57473,57474,57475,57476,57477,57478,57479,57480,57481]
        self.dc.SetFont(self.font)
        S,M = TimSName.split('/')
        self.dc.DrawText(chr(timnumb[int(S)]),x,y-14)
        self.dc.DrawText(chr(timnumb[int(M)]),x,y)
        pass

    def DrawKeyS(self, KeySName,x,y):
        self.dc.SetFont(self.font)
        self.dc.DrawText(chr(57952),x,y)
        pass

    def DrawNots(self, NotName, x, y):       
        self.dc.SetFont(self.font)
        for i in range(9):
            self.dc.DrawText(chr(60576+i),x+22*i,y)
##        self.dc.DrawText(chr(60577),x+80,y-20)
##        self.dc.DrawText(chr(60578),x+100,y)
##        self.dc.DrawText(chr(60579),x+120,y-10)
##        self.dc.DrawText(chr(60580),x+140,y-20)
##        self.dc.DrawText(chr(60581),x+180,y)
##        self.dc.DrawText(chr(60582),x+200,y-10)
##        self.dc.DrawText(chr(60583),x+220,y-20)
##        self.dc.DrawText(chr(60584),x+240,y)
        pass

    def DrawMsur(self, nMsur):
        pass

    def DrawLins(self, nSystm, x, y):
        
        for l in range(5):
            y += self.k*1
            self.dc.DrawLine(x,y,x+nSystm,y)
        print(x,y)    
        return x,y
        


class MyScore ( wx.ScrolledWindow ):
    def __init__(self, parent, id, xmlfd, size = wx.DefaultSize):
        wx.ScrolledWindow.__init__(self, parent, id, (0, 0), size=size, style=wx.SUNKEN_BORDER)
        self.SetBackgroundColour("WHITE")
        self.SetVirtualSize((2000, 2000))
        self.SetScrollRate(20,20)

        # create a PseudoDC to record our drawing
        self.pdc = wx.adv.PseudoDC()
        self.DoDrawing(self.pdc, xmlfd)

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

    def DoDrawing(self, dc, xmlfildata):
        #print(xmlfildata)
        DrSc = DrawScore(dc,1)
        x = xmlfildata
        #print(x[(1,1)][0].nameWithOctave,x[(1,1)][0].duration.quarterLength)
        
        #print(x[(1,1)][1].fullName)
        for m in xmlfildata:
            prt = m[1].partName
            print(prt,'mesure:'+str(m[0]))
            
            for e in xmlfildata[m]:
                print(e,type(e))
                    
        
        #DrSc.DrawLins(2500)
        #DrSc.DrawKark(57344,8,-75,81)
        
        DrSc.Draw1Line(20,34,20,146)
        
        yis = [34,41,48,55,62] #55 is g line
        for y in yis:
            DrSc.Draw1Line(20,y,800,y)

        DrSc.DrawCelf('Treble',28,0)
        DrSc.DrawKeyS('fa minor',56,-7)
        #DrSc.DrawCelf('Bass',56,0)
        DrSc.DrawTimS('6/4',84,0)
        DrSc.DrawNots('',105,0)

        yis2 = [118,125,132,139,146]
        for y in yis2:
            DrSc.Draw1Line(20,y,800,y)
        DrSc.DrawCelf('Bass',28,70)

        
        #DrSc.DrawPart(2,80,70)
        #DrSc.DrawCelf('Treble',85,60)
        #DrSc.DrawNots('',90,60)
        
