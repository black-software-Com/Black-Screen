#!/usr/bin/python3
# Black-Screen v1.0
#

from os import system as command,getlogin
from sys import argv
from webbrowser import open_new_tab
try:
     from PyQt5.QtWidgets import *
     from PyQt5.QtGui import *
     from PyQt5.QtCore import *
     from PyQt5.uic import loadUi

except (pip install PyQtWebEngine):
     command("python -m pip install PyQt5")
     command("python -m pip install pyqt5-tools")
try:
     from PyQt5.QtWebEngineWidgets import QWebEngineView
except (Exception,ImportError,ModuleNotFoundError,):
     command("python -m pip install PyQtWebEngine")
try:
     import pyautogui
except (Exception,ImportError,ModuleNotFoundError,):
     command("python -m pip install pyautogui")
try:
     from PIL import Image
except (Exception,ImportError,ModuleNotFoundError,):
     command("python -m pip install PIL")
class Window(QMainWindow):
     def __init__(self,*args,**kwargs):
          super(Window,self).__init__(*args,**kwargs)
          loadUi("page.ui",self)
          self.setWindowTitle("Black-Screen")
          self.setWindowIcon(QIcon("./Scr/black-screen-icon.png"))
          self.move(500,100)
          self.setFixedSize(891,731)
          layout = QVBoxLayout(self)

          key = QShortcut(QKeySequence("Ctrl+r"),self)
          key.activated.connect(self.take_screen)
          
          toolbar = self.addToolBar("Options")
          toolbar.setMovable(False)
          

          # menu = QMenuBar(self)

          # filemenu = menu.addMenu("File")
          file_m = QAction(QIcon("./Scr/file-explorer-icon.png"),"Open File",self)
          file_m.triggered.connect(self.open_file)
          file_m.setShortcut("Ctrl+o")

          screen_shot = QAction(QIcon("./Scr/camera-icon.png"),"Take Screen Shot",self)
          screen_shot.triggered.connect(self.take_screen)
          screen_shot.setShortcut("Ctrl+r")
          dev_= QAction(QIcon("./Scr/dev-icon.png"),"Development",self)
          dev_.triggered.connect(self.dev)
          dev_.setShortcut("Ctrl+d")
          feedback_ = QAction(QIcon("./Scr/support-icon.jpg"),"Send FeedBack",self)
          feedback_.triggered.connect(self.feedback)
          feedback_.setShortcut("Ctrl+f")

          help_ = QAction(QIcon("./Scr/help-icon.png"),"Help",self)
          help_.triggered.connect(self.help)
          help_.setShortcut("Ctrl+H")
          # filemenu.addAction(file_m)
          # filemenu.addSeparator()

          exit_m = QAction(QIcon("./Scr/exit-icon.png"),"Exit",self)
          exit_m.triggered.connect(self.close)
          exit_m.setShortcut("Alt+F4")
          toolbar.addActions([exit_m,screen_shot,file_m,dev_,feedback_,help_])
          # filemenu.addAction(exit_m)
          self.setLayout(layout)
          self.tks.clicked.connect(self.take_screen)

     def contextMenuEvent(self,event):
        global amenu
        menu_r = QMenu(self)
        black_m = QAction('Black',self)
        black_m.setShortcut('F1')
        black_m.triggered.connect(self.black)
        dev_m = QAction('Dev',self)
        dev_m.triggered.connect(self.dev)
        dev_m.setShortcut('F2')
        about_m = QAction('About',self)
        about_m.setShortcut('F3')
        about_m.triggered.connect(self.about)
        menu_r.addActions([black_m,dev_m,about_m])
        help_m = menu_r.addMenu('Help')
        help_mm = QAction('Help',self)
        help_mm.triggered.connect(self.help)
        help_mm.setShortcut('Ctrl+H')
        send_feedback_m = QAction('Send FeedBack',self)
        send_feedback_m.triggered.connect(self.feedback)
        send_feedback_m.setShortcut('Ctrl+F')
        help_m.addActions([help_mm,send_feedback_m])
        menu_r.addSeparator()
        exit_m = QAction('Exit',self)
        exit_m.setShortcut('Alt+F4')
        exit_m.triggered.connect(self.close)
        menu_r.addAction(exit_m)
        menu_r.addAction(exit_m)
        action = menu_r.exec_(self.mapToGlobal(event.pos()))    
        if action == black_m:
          self.black()
        elif action == dev_m:
            self.dev()
        elif action == about_m:
            self.about()
        elif action == send_feedback_m:
            self.feedback()
        elif action == help_mm:
            self.help()
        elif action == exit_m:
            self.close() 
     def take_screen(self):
          sc = pyautogui.screenshot()
          sc.save("screen.png")
          mess_i = QMessageBox(self)
          mess_i.setWindowTitle("Black-Screen")
          mess_i.setWindowIcon(QIcon("./Scr/file-explorer-logo.png"))
          mess_i.setIcon(QMessageBox.Information)
          mess_i.setText("File: screen.png Saved!")
          mess_i.exec_()
          print("File: screen.png Saved!")

          img = Image.open("screen.png")
          img.show()


     def open_file(self):
          user = getlogin()
          file = QFileDialog.getOpenFileName(self,"Open File",f"C:\\Users\\{user}\\Pictures","All Files (*)")
          img = Image.open(file[0])
          img.show()

     def black(self):
          win = QMainWindow(self)
          win.setWindowTitle("Black-Screen/FeedBack")
          win.setWindowIcon(QIcon("./Scr/support-icon.jpg"))
          win.setGeometry(700,100,700,600)
          win.setFixedSize(700,600)
          browser = QWebEngineView(win)
          browser.setUrl(QUrl("https://black-software-com.github.io/Black-Software/"))
          win.setCentralWidget(browser)
          win.show()

     def dev(self):
          win = QMainWindow(self)
          win.setWindowTitle("Black-Screen/Dev")
          win.setWindowIcon(QIcon("./Scr/dev-icon.png"))
          win.setGeometry(700,100,700,600)
          win.setFixedSize(700,600)
          browser = QWebEngineView(win)
          browser.setUrl(QUrl("https://mrprogrammer2938.github.io/mrprogrammer2938/"))
          win.setCentralWidget(browser)
          win.show()

     def feedback(self):
          win = QMainWindow(self)
          win.setWindowTitle("Black-Screen/FeedBack")
          win.setWindowIcon(QIcon("./Scr/support-icon.jpg"))
          win.setGeometry(700,100,700,600)
          win.setFixedSize(700,600)
          browser = QWebEngineView(win)
          browser.setUrl(QUrl("https://github.com/black-software-Com/Black-Screen/issues"))
          win.setCentralWidget(browser)
          win.show()

     def help(self):
          win = QMainWindow(self)
          win.setWindowTitle("Help")
          win.setWindowIcon(QIcon("./Scr/help-logo.png"))
          win.setGeometry(700,100,700,600)
          win.setFixedSize(700,600)
          browser = QWebEngineView(win)
          browser.setUrl(QUrl("https://black-software-com.github.io/Black-Help/"))
          win.setCentralWidget(browser)
          win.show()

     def about(self):
          pass
def main():
    app = QApplication(argv)
    app.setApplicationName("Black-Screen")
    app.setApplicationDisplayName("Black-Screen")
    app.setApplicationVersion("v1.0")
    window = Window()
    window.show()
    app.exec_()

if __name__ == '__main__':
   main()
