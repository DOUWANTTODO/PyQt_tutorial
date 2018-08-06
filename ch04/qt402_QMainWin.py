import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon




class MainForm(QMainWindow):
	def __init__(self,parent=None):
		super(MainForm, self).__init__(parent)
		self.resize(400,200)
		self.status = self.statusBar()
		self.status.showMessage("這是訊息欄",3000)
		self.setWindowTitle('PyQt5 Mainwindows 例子')
	


if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setWindowIcon(QIcon("images/cartoon1.ico"))
	win = MainForm()
	win.show()
	sys.exit(app.exec_())

