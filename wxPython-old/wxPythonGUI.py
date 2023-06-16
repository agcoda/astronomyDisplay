#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# set_size.py
import os
import wx
import time

class SlideShow(wx.App):

	#init is called on class instantiation
	def __init__(self, redirect=False, filename=None):

		#These are the text labels displayed for the screen base
		self.messageLine1 = "Next Astronomy Night"
		self.nextDate = "on 11/11/2018"
		self.nextTime = "at 6:30PM"
		self.nextLocation = "at the ECS Lawn"

		#Create the app 		
		wx.App.__init__(self, redirect, filename)

		#Get the screen width and height with this
		(self.screenWidth, self.screenHeight) = wx.GetDisplaySize()		

		#This style defines the basic way the full container will be drawn 
		frameStyle = ( wx.NO_BORDER)

		#create a base frame to put all widgets into
		self.container = wx.Frame(None,title = ' ', style=frameStyle, size = (self.screenWidth/2,self.screenHeight/2))

		#Within that frame add a panel, this can later be swapped to different images.
		self.textPanel = wx.Panel(self.container, size = (self.screenWidth/2,self.screenHeight/2))
		self.imagePanel = wx.Panel(self.container, size = (self.screenWidth/2,self.screenHeight/2))
		
		#Make the container black
		self.container.SetBackgroundColour('black')

		self.createTextWidgets()
		self.container.Show()



	def createTextWidgets(self):
		#Define general text font, size is the first argument
		font0 = wx.Font(46, wx.DECORATIVE,wx.NORMAL, wx.NORMAL)
		font1 = wx.Font(28, wx.DECORATIVE,wx.NORMAL, wx.NORMAL)

		#These are basically text boxes, color and font set individually
		messageLine1 = wx.StaticText(self.textPanel, label=self.messageLine1, style = wx.ALIGN_CENTRE_HORIZONTAL)
		messageLine1.SetForegroundColour((255,255,255)) # set text color
		messageLine1.SetFont(font0)

		dateLabel = wx.StaticText(self.textPanel, label=self.nextDate, style = wx.ALIGN_CENTRE_HORIZONTAL)
		dateLabel.SetForegroundColour((255,255,255)) # set text color
		dateLabel.SetFont(font1)

		timeLabel = wx.StaticText(self.textPanel, label=self.nextTime, style =wx.ALIGN_CENTRE_HORIZONTAL)
		timeLabel.SetForegroundColour((255,255,255)) # set text color
		timeLabel.SetFont(font1)

		locationLabel = wx.StaticText(self.textPanel, label=self.nextLocation, style =wx.ALIGN_CENTRE_HORIZONTAL)
		locationLabel.SetForegroundColour((255,255,255)) # set text color
		locationLabel.SetFont(font1)

		#create a vertical sizer, Everything added to this sizer will be distributed vertically
		self.vertSizer = wx.BoxSizer(wx.VERTICAL)
		#self.horizSizer = wx.BoxSizer(wx.HORIZONTAL)

		#Stretch spacer is just a black zone, order of add matters
		#two spaces at the top
		self.vertSizer.AddStretchSpacer()
		self.vertSizer.AddStretchSpacer()
		#message text 
		self.vertSizer.Add(messageLine1,0, wx.EXPAND,border=10)

		self.vertSizer.AddStretchSpacer()
		#Next date as set above
		self.vertSizer.Add(dateLabel,0, wx.EXPAND, 5)

		self.vertSizer.AddStretchSpacer()

		self.vertSizer.Add(timeLabel,0, wx.EXPAND, 5)

		self.vertSizer.AddStretchSpacer()

		self.vertSizer.Add(locationLabel,0, wx.EXPAND, 5)

		self.vertSizer.AddStretchSpacer()
		self.vertSizer.AddStretchSpacer()
	
		#Finally add the spacer to the panel
		self.textPanel.SetSizer(self.vertSizer)

		#This will fit the frame to the text, not useful right now
		#self.vertSizer.Fit(self.container)

		#I don't know what this does really
		self.textPanel.Layout()
		#self.imagePanel.Refresh()
	def createImageWidgets(self):


		imageFile = "C:/Users/agcod/Pictures/dnbPics/dnbSchems/blade.jpg"
		imgDisplay = wx.Image(imageFile,wx.BITMAP_TYPE_ANY)

		self.imageCtrl = wx.StaticBitmap(self.imagePanel, wx.ID_ANY, wx.BitmapFromImage(imgDisplay))
#		W = imgDisplay.GetWidth()
#		H = imgDisplay.GetHeight()
#		if W > H:
#			NewW = self.screenWidth
#			NewH = self.screenWidth * H / W
#		else:
#			NewH = self.screenWidth
#			NewW = self.screenWidth * W / H
		imgDisplay = imgDisplay.Scale(self.screenWidth/2,self.screenHeight/2)
		self.imageCtrl.SetBitmap(wx.Bitmap(imgDisplay))
		#self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
		self.imagePanel.Refresh()


#png = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
#wx.StaticBitmap(self, -1, png, (10, 5), (png.GetWidth(), png.GetHeight()))


	

if __name__ == '__main__':
	#instantiate our frame class
	app = SlideShow()
	#Run it as the mainloop
	app.MainLoop()