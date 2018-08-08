import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget,QHBoxLayout,QPushButton,QWidget





class MainForm(QMainWindow):
	def __init__(self,parent=None):
		super(MainForm, self).__init__(parent)
		self.resize(400,200)
		self.status = self.statusBar()
		self.status.showMessage("這是訊息欄",3000)
		self.setWindowTitle('關閉視窗範例說明')
		self.button1 = QPushButton('關閉視窗')
		self.button1.clicked.connect(self.onButtonClick)

		layout = QHBoxLayout()
		layout.addWidget(self.button1)

		main_frame = QWidget()
		main_frame.setLayout(layout)
		self.setCentralWidget(main_frame)


	def onButtonClick(self):
		sender = self.sender()
		print(sender.text() + '被按下了')
		qApp = QApplication.instance()
		qApp.quit()



if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = MainForm()
	win.show()
	sys.exit(app.exec_())

