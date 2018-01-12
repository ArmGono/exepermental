from Tkinter import *
import tkFileDialog

def Debuger(textVar, titleOfWin):
  newWin = Toplevel(root, width = 200)
  newWin.title(titleOfWin)
  debugText = Label(newWin, text=textVar)
  debugText.pack()

def copyTextToClipboard(textToCopy):
  root.clipboard_clear()
  root.clipboard_append(textToCopy)


def getImageForumFormated(url):
  forumImageUrl = '[IMG URL="{}"]'.format(url)
  return forumImageUrl + "\n"

def getLinkForumFormated(text, url):
  forumTextUrl = '[LINK="{}" href={}]'.format(text, url)
  return forumTextUrl

def updateText(ev):
  global textbox
  textValue = textbox.get(1.0, END).strip()
  imageUrl = getImageForumFormated(imageBox.get(1.0, END).strip())
  anchoreTextValue = anchoreText.get(1.0, END).strip()
  linkValue = getLinkForumFormated(anchoreTextValue, linkBox.get(1.0, END).strip())
  textValue = imageUrl + textValue.replace(anchoreTextValue, linkValue)
  textbox.delete(1.0, END)
  textbox.insert(1.0, textValue)
  copyTextToClipboard(textValue)

root = Tk()

panelFrame = Frame(root, height = 80, bg = 'gray')
textFrame = Frame(root, height = 340, width = 600)
menubar = Menu(root)
projectMenu = Menu(menubar, tearoff = 0)


panelFrame.pack(side = 'top', fill = 'x')
textFrame.pack(side = 'bottom', fill = 'both', expand = 1)

textbox = Text(textFrame, font='Arial 14', wrap='word')
scrollbar = Scrollbar(textFrame)

scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set

textbox.pack(side = 'left', fill = 'both', expand = 1)
scrollbar.pack(side = 'right', fill = 'y')

imageBox = Text(panelFrame, font='Arial 14')
linkBox  = Text(panelFrame, font='Arial 14')
anchoreText  = Text(panelFrame, font='Arial 14')
updateBtn = Button(panelFrame, text = 'Update')

updateBtn.bind("<Button-1>", updateText)


imageBox.place(x = 10 , y = 30, width=170, height = 25)
linkBox.place(x = 190 , y = 30, width=150, height = 25)
anchoreText.place(x = 350 , y = 30, width=150, height = 25)
updateBtn.place(x = 600, y = 30, width = 80, height = 25)

Label(panelFrame, text='Image url').place(x = 10, y = 10)
Label(panelFrame, text='Anchore url').place(x = 190, y = 10)
Label(panelFrame, text='Anchore text').place(x = 350, y = 10)


projectMenu.add_command(label="Project forum", command='setProject')
menubar.add_cascade(label="Select project", menu=projectMenu)
root.config(menu=menubar)
root.mainloop()
