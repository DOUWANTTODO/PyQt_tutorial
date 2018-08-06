import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget





class MainForm(QMainWindow):
	def __init__(self,parent=None):
		super(MainForm, self).__init__(parent)
		self.resize(400,200)
		self.status = self.statusBar()
		self.status.showMessage("這是訊息欄",3000)
		self.setWindowTitle('將窗口放在中心')
		# 放置中心
		self.center()
	def center(self):
		screen = QDesktopWidget().screenGeometry()

		size = self.geometry()
		#print(screen)
		#print(size)
		self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
	


if __name__ == '__main__':
	app = QApplication(sys.argv)
	
	win = MainForm()
	win.show()
	sys.exit(app.exec_())

