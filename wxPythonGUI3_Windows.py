#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# set_size.py
import os
import wx
import time

#This class will walk the image directory of the repo and give a filename for each image avail in a matrix
class imageGetter():
	def __init__(self):
		self.imageFilePaths = []

		self.getImgs()
		self.createWindowsImgPaths()

	def getImgs(self):
		currPath = os.path.dirname(os.path.realpath(__file__))
		print(currPath)
		imgPath = currPath + "\Images"
		print(imgPath)
		self.imageFiles = []
		for (_, _, filenames) in os.walk(imgPath):
			self.imageFiles.extend(filenames)
			break
	def createImgPaths(self):
		self.imageFilePaths = []
		for i in range(len(self.imageFiles)):
			self.imageFilePaths.append( "./Images/"+self.imageFiles[i])
			print(self.imageFilePaths[i])
	def createWindowsImgPaths(self):

		for i in range(len(self.imageFiles)):
			self.imageFilePaths.append( "C:/Users/agcod/Documents/MethodSystemsRepo/AstronomyDisplay/Images/"+self.imageFiles[i])
			print(self.imageFilePaths[i])
#C:/Users/agcod/Documents/MethodSystemsRepo/AstronomyDisplay

class textPanel(wx.Panel):
	def __init__(self, parent):
		(self.screenWidth, self.screenHeight) = wx.GetDisplaySize()	
		wx.Panel.__init__(self, parent=parent, size = (self.screenWidth/2,self.screenHeight))

		self.SetBackgroundColour((0,0,0))
		self.messageLine1 = "Next Astronomy Night"
		self.nextDate = "on 11/13/2018"
		self.nextTime = "at 6:00PM"
		self.nextLocation = "at the ECS Lawn"
		self.createTextWidgets()

	def createTextWidgets(self):
		#Define general text font, size is the first argument
		font0 = wx.Font(46, wx.DECORATIVE,wx.NORMAL, wx.NORMAL)
		font1 = wx.Font(28, wx.DECORATIVE,wx.NORMAL, wx.NORMAL)

		#These are basically text boxes, color and font set individually
		messageLine1ST = wx.StaticText(self, label= self.messageLine1, style = wx.ALIGN_CENTRE_HORIZONTAL)
		messageLine1ST.SetForegroundColour((255,255,255)) # set text color
		messageLine1ST.SetFont(font0)

		dateLabelST = wx.StaticText(self, label=self.nextDate, style = wx.ALIGN_CENTRE_HORIZONTAL)
		dateLabelST.SetForegroundColour((255,255,255)) # set text color
		dateLabelST.SetFont(font1)

		timeLabelST = wx.StaticText(self, label=self.nextTime, style =wx.ALIGN_CENTRE_HORIZONTAL)
		timeLabelST.SetForegroundColour((255,255,255)) # set text color
		timeLabelST.SetFont(font1)

		locationLabelST = wx.StaticText(self, label=self.nextLocation, style =wx.ALIGN_CENTRE_HORIZONTAL)
		locationLabelST.SetForegroundColour((255,255,255)) # set text color
		locationLabelST.SetFont(font1)

		#create a vertical sizer, Everything added to this sizer will be distributed vertically
		self.vertSizer = wx.BoxSizer(wx.VERTICAL)
		self.horizSizerLine1 = wx.BoxSizer(wx.HORIZONTAL)
		self.horizSizerLine2 = wx.BoxSizer(wx.HORIZONTAL)
		self.horizSizerLine3 = wx.BoxSizer(wx.HORIZONTAL)
		self.horizSizerLine4 = wx.BoxSizer(wx.HORIZONTAL)

		#Stretch spacer is just a black zone, order of add matters
		#two spaces at the top
		self.vertSizer.AddStretchSpacer()
		self.vertSizer.AddStretchSpacer()

		#message text 
		self.horizSizerLine1.AddStretchSpacer()
		self.horizSizerLine1.Add(messageLine1ST,0, wx.EXPAND,border=10)
		self.horizSizerLine1.AddStretchSpacer()

		self.vertSizer.Add(self.horizSizerLine1,0,wx.EXPAND,5)

		self.vertSizer.AddStretchSpacer()
		#Next date as set above
		self.horizSizerLine2.AddStretchSpacer()
		self.horizSizerLine2.Add(dateLabelST,0, wx.EXPAND,border=10)
		self.horizSizerLine2.AddStretchSpacer()

		self.vertSizer.Add(self.horizSizerLine2,0, wx.EXPAND, 5)

		self.vertSizer.AddStretchSpacer()

		self.horizSizerLine3.AddStretchSpacer()
		self.horizSizerLine3.Add(timeLabelST,0, wx.EXPAND,border=10)
		self.horizSizerLine3.AddStretchSpacer()

		self.vertSizer.Add(self.horizSizerLine3,0, wx.EXPAND, 5)

		self.vertSizer.AddStretchSpacer()

		self.horizSizerLine4.AddStretchSpacer()
		self.horizSizerLine4.Add(locationLabelST,0, wx.EXPAND,border=10)
		self.horizSizerLine4.AddStretchSpacer()

		self.vertSizer.Add(self.horizSizerLine4,0, wx.EXPAND, 5)

		self.vertSizer.AddStretchSpacer()
		self.vertSizer.AddStretchSpacer()
	
		#Finally add the spacer to the panel
		self.SetSizer(self.vertSizer)

class imagePanel(wx.Panel):
	def __init__(self, parent):
		self.imgToShow = 0
		(self.screenWidth, self.screenHeight) = wx.GetDisplaySize()	
		wx.Panel.__init__(self, parent=parent,size = (self.screenWidth/2,self.screenHeight) )
	
#		self.imageFile = 
		#Register all images here in list
		self.imageFile = ["C:/Users/agcod/Documents/MethodSystemsRepo/AstronomyDisplay/Images/Attendance.jpg", \
					"C:/Users/agcod/Documents/MethodSystemsRepo/AstronomyDisplay/Images/EclipseImage.jpg",\
					"C:/Users/agcod/Documents/MethodSystemsRepo/AstronomyDisplay/Images/LookingUp.jpg",\
					"C:/Users/agcod/Documents/MethodSystemsRepo/AstronomyDisplay/Images/StudentView.jpg"\
					]
		self.numImages = len(self.imageFile)

		self.createImageWidgets()
#Path for windows
#C:\Users\agcod\Documents\MethodSystemsRepo\AstronomyDisplay\Images\Attendance.jpg

	def createImageWidgets(self):
		for i in range(0,numImages):
			imgDisplay[i] = wx.Image(self.imageFile[self.imgToShow],wx.BITMAP_TYPE_ANY)

			self.imageCtrl[i] = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(imgDisplay))

			imgDisplay[i] = imgDisplay.Scale(self.screenWidth/2,self.screenHeight)
			self.imageCtrl.SetBitmap(wx.Bitmap(imgDisplay))
		#self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
		#self.Layout()
	def changeImageCount(self):
		#if at the max value then set it to zero, else increment by one
		if self.imgToShow == (self.numImages - 1):
			self.imgToShow = 0
		else:
			self.imgToShow += 1
	def resetImgCount(self):
		self.imgToShow = 0
	def switchImage(self):



class SlideShow(wx.Frame):
	def __init__(self, redirect=False, filename=None):
		self.frameStyle = ( wx.NO_BORDER)
		wx.Frame.__init__(self, None, wx.ID_ANY, style= self.frameStyle)
		(self.screenWidth, self.screenHeight) = wx.GetDisplaySize()	

		self.imageGetter = imageGetter()
#		print(self.imageGetter.imageFiles[0])
		
		cursor = wx.Cursor(wx.CURSOR_BLANK) 
		# set the cursor for the window 
		self.SetCursor(cursor) 

		self.SetSize(self.screenWidth/2,self.screenHeight)

		self.SetBackgroundColour('black')
		self.imgSwitchCounter = 0

		self.textPanel = textPanel(self)
		#call this to force sizers to fit
		self.textPanel.Layout()
#		self.textPanel.Hide()
		self.imagePanel = imagePanel(self)
		self.imagePanel.Layout()
		self.imagePanel.Hide()

		#define here how long to spend on each image
		self.msPerImage = 3000
		
		#The astronomy night display will show for the msperimage x the number of images  then switch to the images
		#After viewing all images it will switch back
		self.panelSwitchTime = self.msPerImage*self.imagePanel.numImages

		self.switchCountBuffer = 0		

		self.timerText = wx.Timer(self)
		self.timerImages = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.switchPanels,self.timerText)
		self.Bind(wx.EVT_TIMER, self.switchImages,self.timerImages)

		self.timerText.Start(self.panelSwitchTime)
		self.timerImages.Start(self.panelSwitchTime/self.imagePanel.numImages)
		
	def switchPanels(self, event):
#		print("panel Switch, curr img:")
#		print(self.imagePanel.imgToShow)
		self.imagePanel.imgToShow = 0
		#Whenever we call switch panels we switch between text and images
		if self.textPanel.IsShown():
			self.textPanel.Hide()
			self.imagePanel.Show()
		else:
			self.textPanel.Show()
			self.imagePanel.Hide()
		self.Layout()

	def switchImages(self, event):
		#Everytime this event is triggered add one to the counter
		self.switchCountBuffer +=1
#		print(self.switchCountBuffer)

#if we're on the text panel do not switch images to save processor
#if were switching from the text panel also do not switch, switch one early or it flashes
		if (self.switchCountBuffer <= self.imagePanel.numImages and self.switchCountBuffer != self.imagePanel.numImages-1):
			a=1

#Switch the image to the first one tick before the panel switches to prevent flashing
		elif(self.switchCountBuffer == self.imagePanel.numImages-1):
#			print("switching to zero")
			self.imagePanel.resetImgCount()
			self.imagePanel.createImageWidgets()
			self.Layout()

#While on images switch an image until we've gone through them all
		elif (self.switchCountBuffer > self.imagePanel.numImages and self.switchCountBuffer < self.imagePanel.numImages*2):

			self.imagePanel.changeImageCount()
#			print("switching image, showing:")
#			print(self.imagePanel.imgToShow)
			self.imagePanel.switchImage()
			self.Layout()
#when switching back to text panel do not change the image, but reset the counter to restart the loop
		else:
#			print("no switch, reset 0")
			self.switchCountBuffer = 0
		
if __name__ == '__main__':
	#instantiate our frame class
#	imageGetter = imageGetter()

	app = wx.App(False)
	frame = SlideShow()
	frame.Show()
	#Run it as the mainloop
#	frame.switchPanels()

	app.MainLoop()
