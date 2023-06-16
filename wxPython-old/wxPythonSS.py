import os
import wx
 
#wx.app is the main application for wxpython. Only one instance is required but this is what is run
class PhotoCtrl(wx.App):
	#do these things to construct the app
	def __init__(self, redirect=False, filename=None):
		wx.App.__init__(self, redirect, filename)

		#get display size
		(self.screenWidth, self.screenHeight) = wx.GetDisplaySize()

		#define a style for the underlying frame
		frameStyle = ((  wx.NO_BORDER | wx.MAXIMIZE) & ~(wx.SYSTEM_MENU | wx.CAPTION))

		#create a frame instance with the defined style
		#The sizers will lock the frame to the size of the panel defined below
		self.frame = wx.Frame(None, title=' ', style = frameStyle)

		#set the background color of that frame to black
		self.frame.SetBackgroundColour('black')
	
		#create a panel instance with the parent of "frame" this puts a panel within the frame
		self.panel = wx.Panel(self.frame)

		#This is a user value defined to set the max width and height for an image
		self.PhotoMaxWidth = self.screenWidth / 3

		#method to create all widgets
		self.createWidgets()

		#final call to show the frame and all children
		self.frame.Show()

	def createWidgets(self):
		instructions = 'Browse for an image'
		#base image to insert images into
		img = wx.Image(self.PhotoMaxWidth,self.PhotoMaxWidth*(self.screenHeight/self.screenWidth))

		self.imageCtrl = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(img))


		instructLbl = wx.StaticText(self.panel, label=instructions)
		#displays the full image path after selection
		self.photoTxt = wx.TextCtrl(self.panel, size=(200,-1))

		#button to press to find an image
		browseBtn = wx.Button(self.panel, label='Browse')
		#binds method onBrowse to the button press
		browseBtn.Bind(wx.EVT_BUTTON, self.onBrowse)

		#instantiate a box sizer for horizontal and vertical
		self.mainSizer = wx.BoxSizer(wx.VERTICAL)
		self.sizer = wx.BoxSizer(wx.HORIZONTAL)

		#Add all vertical elements to the mainsizer
		#self.mainSizer.Add(wx.StaticLine(self.panel, wx.ID_ANY),0, wx.ALL|wx.EXPAND, 5)
		self.mainSizer.Add(instructLbl, 0, wx.ALL, 5)
		self.mainSizer.Add(self.imageCtrl, 0, wx.ALL, 5)

		#add the file path line and the browse button to one horizontal line
		#self.sizer.Add(self.photoTxt, 0, wx.ALL, 5)
		self.sizer.Add(browseBtn, 0, wx.ALL, 5)  

		#add that horizontal line to the mainsizer
		self.mainSizer.Add(self.sizer, 0, wx.ALL, 5)

		#Set the main sizer as the sizer for the panel
		self.panel.SetSizer(self.mainSizer)

		self.mainSizer.Fit(self.frame)

		self.panel.Layout()

	def onBrowse(self, event):

		#Browse for file, called when browse button is pressed
		wildcard = "JPEG files (*.jpg)|*.jpg"
		#pops up a browse fial dialogue, premade
		dialog = wx.FileDialog(None, "Choose a file",wildcard=wildcard,	style=wx.FD_OPEN)
		# if the ok button is pressed get the path selected and set that as the image path
		if dialog.ShowModal() == wx.ID_OK:
			#if okay is pressed then get the path selected then call the view to show the img
			self.photoTxt.SetValue(dialog.GetPath())
			
			dialog.Destroy() 
			self.onView()
		else :
			#if any other button is pressed just exit.
			return


	def onView(self):
		#get the path chosen by the browse
		filepath = self.photoTxt.GetValue()
		#create an image for the image selected
		img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
		# scale the image, preserving the aspect ratio
		W = img.GetWidth()
		H = img.GetHeight()
		if W > H:
			NewW = self.PhotoMaxWidth
			NewH = self.PhotoMaxWidth * H / W
		else:
			NewH = self.PhotoMaxWidth
			NewW = self.PhotoMaxWidth * W / H
		img = img.Scale(NewW,NewH)
		
		self.imageCtrl.SetBitmap(wx.Bitmap(img))

		#refresh the panel now that an image has been selected
		self.panel.Refresh()

if __name__ == '__main__':
	app = PhotoCtrl()
	app.MainLoop()