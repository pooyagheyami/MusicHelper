#In the name of GOD
# -*- coding: utf-8 -*-
#!usr/bin/env python

import wx
from  Config.Init import *
import GUI.API.ImpScor1 as pnl

class telframe(wx.Frame):
	def __init__(self,parent):
		wx.Frame.__init__(self,parent,style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE)
		self.parent= parent
		dlg = wx.FileDialog(parent, message="Choose a file",
					defaultDir=os.getcwd(),
					defaultFile="",
					wildcard="Music file(*.*)|*.*",
					style=wx.FD_OPEN | wx.FD_CHANGE_DIR )

		if dlg.ShowModal() ==wx.ID_OK:
			paths = dlg.GetPaths()
			print(paths)

		dlg.Destroy()
		
		self.Pnl = pnl.MyPanel1(self, paths)

	def closeit(self):
		self.Close(True)

def size():
	return (-1,-1)

def main(panel=None ):
	parent =  panel.GetParent()

	frame = telframe(parent )
	frame.SetTitle(u'form')
	frame.SetSize(size())
	frame.Show()

if __name__ == '__main__':
	main()
