import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer

def page(Page):
    index = widget.indexOf(Page)
    widget.setCurrentIndex(index)

class MyApp(QDialog):
    def __init__(self, page):
        self.page = page
        super(MyApp, self).__init__()
        loadUi("UI/Opening.ui", self)
        timer = QTimer(self)
        timeout_duration = 4000
        timer.singleShot(timeout_duration, lambda: self.page(HOME))


class Home(QDialog):
    def __init__(self, page):
        self.page = page
        super(Home, self).__init__()
        loadUi("UI/project.ui", self)
        self.crimeprediction.clicked.connect(lambda: self.page(PREDICT))
        self.crimematching.clicked.connect(lambda: self.page(MATCHING))
        self.crimerate.clicked.connect(lambda: self.page(RATE))
        self.crimepattern.clicked.connect(lambda: self.page(PATTERN))


class Predict(QDialog):
    def __init__(self, page):
        self.page = page
        super(Predict, self).__init__()
        loadUi("UI/prediction.ui", self)
        self.crimeprediction.clicked.connect(lambda: self.page(PREDICT))
        self.crimematching.clicked.connect(lambda: self.page(MATCHING))
        self.crimerate.clicked.connect(lambda: self.page(RATE))
        self.crimepattern.clicked.connect(lambda: self.page(PATTERN))


class Pattern(QDialog):
    def __init__(self, page):
        self.page = page
        super(Pattern, self).__init__()
        loadUi("UI/pattern.ui", self)
        self.crimeprediction.clicked.connect(lambda: self.page(PREDICT))
        self.crimematching.clicked.connect(lambda: self.page(MATCHING))
        self.crimerate.clicked.connect(lambda: self.page(RATE))
        self.crimepattern.clicked.connect(lambda: self.page(PATTERN))


class Matching(QDialog):
    def __init__(self, page):
        self.page = page
        super(Matching, self).__init__()
        loadUi("UI/matching.ui", self)
        self.crimeprediction.clicked.connect(lambda: self.page(PREDICT))
        self.crimematching.clicked.connect(lambda: self.page(MATCHING))
        self.crimerate.clicked.connect(lambda: self.page(RATE))
        self.crimepattern.clicked.connect(lambda: self.page(PATTERN))


class Rate(QDialog):
    def __init__(self, page):
        self.page = page
        super(Rate, self).__init__()
        loadUi("UI/crimerate.ui", self)
        self.crimeprediction.clicked.connect(lambda: self.page(PREDICT))
        self.crimematching.clicked.connect(lambda: self.page(MATCHING))
        self.crimerate.clicked.connect(lambda: self.page(RATE))
        self.crimepattern.clicked.connect(lambda: self.page(PATTERN))


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = MyApp(page)
widget.addWidget(mainwindow)
widget.setFixedWidth(1366)
widget.setFixedHeight(768)
widget.show()
HOME = Home(page)
PREDICT = Predict(page)
PATTERN = Pattern(page)
MATCHING = Matching(page)
RATE = Rate(page)
widget.addWidget(HOME)
widget.addWidget(PREDICT)
widget.addWidget(PATTERN)
widget.addWidget(MATCHING)
widget.addWidget(RATE)
app.exec_()
