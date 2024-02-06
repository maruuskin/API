import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QComboBox
import requests


class Img(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.combobox = QComboBox(self)
        self.combobox.addItems(['схема', 'спутник', 'гибрид'])
        self.combobox.currentTextChanged.connect(self.show_img)
        self.map = 'map'
        self.spn = '0.05'
        self.longitude, self.lattitude = '37.6156', '55.7522'
        self.show_img()
        self.show()

    def show_img(self):
        print(self.combobox.currentText())
        # if self.combobox.currentText() == 'схема':
        #     self.map = 'map'
        # elif self.combobox.currentText() == 'спутник':
        #     self.map = 'satellite'
        # elif self.combobox.currentText() == 'гибрид':
        #     self.map = 'hybrid'
        map_params = {
            "ll": ",".join([self.longitude, self.lattitude]),
            "spn": ",".join([self.spn, self.spn]),
            "l": self.map,
        }
        map_api_server = "http://static-maps.yandex.ru/1.x/"
        response = requests.get(map_api_server, params=map_params)
        print(response)
        with open('img.jpg', 'wb') as file:
            file.write(response.content)
        pixmap = QPixmap('img.jpg')
        self.label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            self.spn = str(float(self.spn) + 0.01)
            self.show_img()
        if event.key() == Qt.Key_Right:
            self.longitude = str(float(self.spn) + float(self.longitude))
            self.show_img()


app = QApplication(sys.argv)
ex = Img()
sys.exit(app.exec())
