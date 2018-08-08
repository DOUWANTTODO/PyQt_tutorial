import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip
from PyQt5.QtGui import QFont

class winform(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		QToolTip.setFont(QFont('SansSerif', 10))
		self.setToolTip('這是氣泡提示')
		self.setGeometry(200,300,400,400)
		self.setWindowTitle('氣泡提示demo')


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = winform()
	win.show()
	sys.exit(app.exec_())
