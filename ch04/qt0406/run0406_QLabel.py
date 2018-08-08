import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel

from qt0406_QLabel import Ui_Form


class mainwin(QMainWindow, Ui_Form):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.label_4.linkActivated.connect( link_clicked )
		self.label_2.linkActivated.connect( link_hovered )


def link_hovered(self):
    print('滑鼠滑過這個標籤')

def link_clicked(self):
    print('開啟網頁去蝦皮')


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = mainwin()
	win.show()
	sys.exit(app.exec_())