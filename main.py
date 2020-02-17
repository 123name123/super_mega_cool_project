import sys

import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow

from mainForm import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.flag = 0
        self.setStyleSheet("""background-color: #ffe5b4""")
        self.input.setStyleSheet("""background-color: #ffffff""")
        self.input.setStyleSheet("""background-color: #ffffff""")
        self.input.setStyleSheet("""background-color: #ffffff""")
        self.chng_map.setStyleSheet("""background-color: #ffffff""")
        self.search.setStyleSheet("""background-color: #ffffff""")
        self.search_del.setStyleSheet("""background-color: #ffffff""")

    def initUI(self):
        self.checkBox.stateChanged.connect(self.chcng_post)
        self.search.clicked.connect(self.run_search)
        self.chng_map.clicked.connect(self.map_chng)
        self.search_del.clicked.connect(self.del_search)
        self.dest_num = 1
        self.addres = None
        self.dest_list = [0.002, 0.005, 0.02, 0.05, 0.1, 0.3, 0.5, 1, 3, 5, 11, 15, 40]
        self.shir_ch = 37
        self.dol_ch = 55
        self.metka_pos_ch = None
        self.metka_pos_dol = None
        self.map = 'map'

    def chcng_post(self):
        if not self.addres:
            return
        if self.checkBox.isChecked():
            self.adress.setText(f'Полный адрес: {self.addres}, {self.post_code}')
        else:
            self.adress.setText(f'Полный адрес: {self.addres}')

    def run_search(self):
        toponym_to_find = self.input.text()
        geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
        geocoder_params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": toponym_to_find,
            "format": "json"}
        response = requests.get(geocoder_api_server, params=geocoder_params)
        if not response:
            return
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
        self.addres = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
        try:
            self.post_code = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"][
                "postal_code"]
        except Exception:
            self.post_code = '----'
        if self.checkBox.isChecked():
            self.adress.setText(f'Полный адрес: {self.addres}, {self.post_code}')
        else:
            self.adress.setText(f'Полный адрес: {self.addres}')
        self.shir_ch, self.dol_ch = toponym["Point"]["pos"].split()
        self.shir_ch, self.dol_ch = float(self.shir_ch), float(self.dol_ch)
        self.metka_pos_ch, self.metka_pos_dol = self.shir_ch, self.dol_ch

        self.run_start()

    def del_search(self):
        self.input.clear()
        self.metka_pos_ch, self.metka_pos_dol = -333, -333
        self.run_start()
        self.adress.setText('')

    def map_chng(self):
        if self.map == 'map':
            self.map = 'sat'
        elif self.map == 'sat':
            self.map = 'skl'
        elif self.map == 'skl':
            self.map = 'map'
        self.run_start()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            if self.dest_num < len(self.dest_list) - 1:
                self.dest_num += 1
            self.run_start()
        elif event.key() == Qt.Key_PageDown:
            if self.dest_num >= 1:
                self.dest_num -= 1
            self.run_start()
        elif event.key() == Qt.Key_Up:
            self.dol_ch += self.dest_list[self.dest_num]
            self.run_start()
        elif event.key() == Qt.Key_Down:
            self.dol_ch -= self.dest_list[self.dest_num]
            self.run_start()
        elif event.key() == Qt.Key_Right:
            self.shir_ch += self.dest_list[self.dest_num]
            self.run_start()
        elif event.key() == Qt.Key_Left:
            self.shir_ch -= self.dest_list[self.dest_num]
            self.run_start()
        elif event.key() == Qt.Key_M:
            self.map_chng()

    def mousePressEvent(self, event):
        if self.our_map.x() <= event.x() <= self.our_map.x() + 650 and \
                self.our_map.y() <= event.y() <= self.our_map.y() + 450:
            self.shir_ch = self.shir_ch - (334 - event.x()) * self.dest_list[self.dest_num] / 230
            self.dol_ch = self.dol_ch + (236 - event.y()) * self.dest_list[self.dest_num] / 430
            self.metka_pos_ch, self.metka_pos_dol = self.shir_ch, self.dol_ch

            geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
            geocoder_params = {
                "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
                "geocode": ' '.join([str(self.shir_ch), str(self.dol_ch)]),
                "format": "json"}
            response = requests.get(geocoder_api_server, params=geocoder_params)
            if not response:
                return
            json_response = response.json()
            toponym = json_response["response"]["GeoObjectCollection"][
                "featureMember"][0]["GeoObject"]
            self.addres = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
            try:
                self.post_code = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"][
                    "postal_code"]
            except Exception:
                self.post_code = '----'
            if self.checkBox.isChecked():
                self.adress.setText(f'Полный адрес: {self.addres}, {self.post_code}')
            else:
                self.adress.setText(f'Полный адрес: {self.addres}')

            self.run_start()

    def run_start(self):
        try:
            self.our_map.setFocus()
            dest = self.dest_list[self.dest_num]
            map_request = f"http://static-maps.yandex.ru/1.x/?" \
                          f"ll={self.shir_ch},{self.dol_ch}&spn" \
                          f"={dest},{dest}&l={self.map}&size=650,450" \
                          f"&pt={self.metka_pos_ch},{self.metka_pos_dol}"
            response = requests.get(map_request)
            if self.map == 'sat':
                self.map_file = "map.jpg"
            else:
                self.map_file = "map.png"
            with open(self.map_file, "wb") as file:
                if 'error' in str(response.content):
                    return
                file.write(response.content)
            self.pixmap = QPixmap(self.map_file)
            self.our_map.setPixmap(self.pixmap)
        except Exception:
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
