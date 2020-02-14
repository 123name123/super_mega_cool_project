from mainForm import Ui_MainWindow
import sys
import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.start.clicked.connect(self.run_start)

    def run_start(self):
        try:
            dol = int(self.dol.text())
            shir = int(self.shir.text())
            map_request = f"http://static-maps.yandex.ru/1.x/?ll={shir},{dol}&spn=0.2,0.2&l=map"
            response = requests.get(map_request)
            self.map_file = "map.png"
            with open(self.map_file, "wb") as file:
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
