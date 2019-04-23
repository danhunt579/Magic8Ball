"""
File:	DanHunt8.py
Date:	04.01.19
Author:	DanHunt

- A program that uses a GUI which allows the user to input a question.  The computer will answer the question with one of at least 8 predetermined responses.
"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
import random

class Magic8Ball(EasyFrame):
	"""Sets up the window, user asks a question, the 8 ball answers"""
	def __init__(self):
		"""Sets up the window and the widgets"""
		EasyFrame.__init__(self, title = "Magic 8 Ball, tell me the answer.")
		
		# Set up two panels, one for the image and one for input / output (io)
		imagePanel = self.addPanel(row = 0, column = 0, background = "gray")
		ioPanel = self.addPanel(row = 1, column = 0, background = "black")
		
		# Add image to imagePanel
		imagePane = imagePanel.addLabel(text = "", row = 0, column = 0, sticky = "NSEW")
		# Credit the photo creator
		creditPane = imagePanel.addLabel(text = "By greeblie from US - Instrument Of Evil?", row = 1, column = 0, sticky = "NSEW", background = "gray")
		creditPane2 = imagePanel.addLabel(text = "CC BY 2.0, https://commons.wikimedia.org/w/index.php?curid=48076080", row = 2, column = 0, sticky = "NSEW", background = "gray")
		# Add the image to imagePanel
		self.image = PhotoImage(file = "8ball2.gif")
		imagePane["image"] = self.image
		imagePane["background"] = "gray"
		
		# Add input & ouput
		ioPanel.addLabel(text = "Enter a question.  The magic 8 ball knows all.", row = 0, column = 0, sticky = "NSEW", background = "black", foreground = "green")
		self.question = ioPanel.addTextField(text = "", row = 1, column = 0, sticky = "NSEW")
		ioPanel.addButton(text = "Tell me the answer", row = 2, column = 0, command = self.answer)
		self.echo = ioPanel.addTextField(text = "", row = 3, column = 0, sticky = "NSEW")
		self.response = ioPanel.addTextField(text = "", row = 4, column = 0, sticky = "NSEW")
		
	def answer(self):
		# Assign the user question to a variable
		userQuestion = self.question.getText()
		# If the question is blank, alert the user
		if userQuestion == "":
			self.messageBox(title = "Help", message = "Please enter a question.")
			
		# define 8ball answers in a list
		answers = ["It is certain.", "Reply hazy, try again.", "Don't count on it.", "Signs point to yes.", "Better not tell you now", "Outlook not so good", "Absolutely, yes", "Concentrate harder and ask again.", "Absolutely, no"]
		
		# Echo the question the user has entered
		if userQuestion == "":
			echoText = ""
		else:
			echoText = "You asked: " + userQuestion		
		self.echo.setText(echoText)
		
		# Generate a a random number and use that number to get a string from answers list
		if userQuestion != "":
			x = random.randint(0,8)
			self.response.setText(answers[x])
		
def main():
	Magic8Ball().mainloop()
	
main()
