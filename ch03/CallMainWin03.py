import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWin02 import Ui_Form



class MainForm(QMainWindow, Ui_Form):
	def __init__(self,parent=None):
		super(MainForm, self).__init__(parent)
		self.setupUi(self)
	


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = MainForm()
	win.show()
	sys.exit(app.exec_())
