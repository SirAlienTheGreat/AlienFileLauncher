import gi
import random
import subprocess
from gi.repository import GLib
from listfiles import listfiles

currentdirectory = "/hdd/Anime"
CurrentRow=0
CurrentColumn=0

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def NewWindow():
    class MyWindow(Gtk.Window):
        global currentdirectory
        global CurrentRow
        global CurrentColumn
        
        def __init__(self):
            global currentdirectory
            global CurrentRow
            global CurrentColumn
            Gtk.Window.__init__(self, title=currentdirectory)
            

            grid = Gtk.Grid()
            #grid.widget.set_hexpand()
            self.add(grid)

            itemsincurrentdirectory = listfiles(currentdirectory)
            numberOfButtons = len(itemsincurrentdirectory)

            NumberOfRows=5
            NumberOfColumns=int(round(numberOfButtons/NumberOfRows)+1)

            
            def newbutton(y):
                global CurrentRow
                global CurrentColumn
                global currentdirectory

                buttontext = label=itemsincurrentdirectory[y]
                maxlinesize = 20
                if len(buttontext) >= maxlinesize:
                    if len(buttontext) >= 2* maxlinesize:
                        buttontext = buttontext[:maxlinesize-1] + '\n' + buttontext[maxlinesize-1:((2*maxlinesize)-1)] + '\n' + buttontext[((2*maxlinesize)-1):]
                    else:
                        buttontext = buttontext[:maxlinesize-1] + '\n' + buttontext[maxlinesize-1:]
                
                
                self.button = Gtk.Button(buttontext)
                #self.button.modify_font(Pango.FontDescription("Arial"))
                self.button.connect("clicked", self.on_button_clicked, itemsincurrentdirectory[y])
                self.button.set_hexpand(True)
                self.button.set_vexpand(True)
                #self.add(self.button)
                #grid.add(self.button)
                #print("new button at:", str(CurrentRow), str(CurrentColumn))
                grid.attach(self.button, CurrentRow, CurrentColumn, 1, 1)
                if CurrentRow >= NumberOfRows:
                    CurrentRow = 0
                    CurrentColumn = CurrentColumn + 1
                else:
                    CurrentRow = CurrentRow + 1
                                         
            for x in range(numberOfButtons):
                newbutton(x)

        def on_button_clicked(self, widget, data):
            global currentdirectory
            global CurrentRow
            global CurrentColumn
            print(data)
            suffix = data[len(data)-4]+data[len(data)-3]+data[len(data)-2]+data[len(data)-1]
            if suffix == ".mkv" or suffix == ".mp4":
                subprocess.call(["vlc", currentdirectory + "/"  + data])
            else:                
                currentdirectory = currentdirectory + "/" + data
                print(currentdirectory)
                self.destroy()
                CurrentRow=0
                CurrentColumn=0
                NewWindow()
    win = MyWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
NewWindow()
