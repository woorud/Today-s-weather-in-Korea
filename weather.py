from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QStringListModel
from urllib.request import urlopen

import urllib.request, json
import sys

form_class = loadUiType("weather.ui")[0]

class weather(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.url1 = "http://api.openweathermap.org/data/2.5/weather?id="
        self.appid = input() # 074c4527c3cfdf3ff8baf79bb49455c1
        self.url2 = "&appid={}".format(self.appid)

        file = open("city.list.json", encoding="UTF-8-SIG").read()
        cities = json.loads(file)

        self.nameid = {}
        for city in cities:
            if city["country"] == "KR":
                self.nameid[city["name"]] = city["id"]

        cities = ["Seoul", "Incheon", "Busan", "Gwangju", "Ulsan", "Daejeon", "Daegu", "Jeju-do"]
        model = QStringListModel(cities)
        self.l_city.setModel(model)
        self.selModel = self.l_city.selectionModel()
        self.selModel.selectionChanged.connect(self.selection)

    def selection(self):
        item = self.selModel.selection().indexes()[0]
        # print(item.data())
        # print(self.nameid[item.data()])
        url = self.url1 + str(self.nameid[item.data()]) + self.url2
        # print(url)
        file1 = urllib.request.urlopen(url)
        s = json.loads(file1.read())
        # print(s)


app = QApplication(sys.argv)
myWindow = weather(None)
myWindow.show()
app.exec()
