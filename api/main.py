from mainForm import Ui_MainWindow
import sys
import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.start.clicked.connect(self.run_start)
        self.dest = 0.2

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            self.dest += 0.1
            self.run_start()
        elif event.key == Qt.Key_PageDown:
            if self.dest > 0.1:
                self.dest -= 0.1
            self.run_start()

    def run_start(self):
        try:
            dol = float(self.dol.text())
            shir = float(self.shir.text())
            map_request = f"http://static-maps.yandex.ru/1.x/?ll={shir},{dol}&spn={self.dest},{self.dest}&l=map"
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
