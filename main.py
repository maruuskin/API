import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
import requests

longitude, lattitude = '37.6156', '55.7522'
spn = '0.05'


class Img(QWidget):
    def __init__(self):
        super().__init__()
        self.get_img()
        self.label = QLabel(self)
        pixmap = QPixmap('img.jpg')
        self.label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        self.show()

    def get_img(self):
        map_params = {
            "ll": ",".join([longitude, lattitude]),
            "spn": ",".join([spn, spn]),
            "l": "map",
        }
        map_api_server = "http://static-maps.yandex.ru/1.x/"
        response = requests.get(map_api_server, params=map_params)
        print(response)

        with open('img.jpg', 'wb') as file:
            file.write(response.content)


app = QApplication(sys.argv)
ex = Img()
sys.exit(app.exec())
