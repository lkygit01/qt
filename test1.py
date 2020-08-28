import PySide2.QtCore
import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui
print(PySide2.__version__)

class Mywidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo welt", "hei maalma", "Hola mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("click me!")
        self.text = QtWidgets.QLabel("hello word")
        self.text.setAlignment(QtCore.Qt.AlignHCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)

    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Mywidget()
    widget.resize(800,600)
    widget.show()

    sys.exit(app.exec_())