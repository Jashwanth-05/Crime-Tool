import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer
from geopy.geocoders import Nominatim
from CTP import latlog
from CTP import CTM
from CTP import PP,MP,RP
import pandas as pd
from PyQt5.QtWidgets import QFileDialog

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
        self.homebt.clicked.connect(lambda: self.page(HOME))
        self.crimeprediction.clicked.connect(lambda: self.page(PREDICT))
        self.crimematching.clicked.connect(lambda: self.page(MATCHING))
        self.crimerate.clicked.connect(lambda: self.page(RATE))
        self.crimepattern.clicked.connect(lambda: self.page(PATTERN))

        self.predictbt.clicked.connect(self.predict)
    def predict(self):
        area=self.locationcb.currentText()
        datetime= self.dateTimeEdit.dateTime().toPyDateTime()
        latitude, longitude =latlog.lg(area)

        db = pd.DataFrame({
            "year": [datetime.year],
            "month": [datetime.month],
            "day": [datetime.day],
            "hour": [datetime.hour],
            "dayofyear": [datetime.timetuple().tm_yday],
            "week": [datetime.isocalendar()[1]],
            "weekofyear": [datetime.isocalendar()[1]],
            "dayofweek": [datetime.weekday()],
            "weekday": [datetime.weekday()],
            "quarter": [(datetime.month - 1) // 3 + 1],
            "latitude": [latitude],
            "longitude": [longitude]
        }, index=[0])
        X=db.iloc[:,[1,2,3,4,6,10,11]].values
        s=CTM.predict(X)
        text = "<html><body>{}</body></html>"
        self.pcrime.setText(text.format(s))

class Pattern(QDialog):
    def __init__(self, page):
        self.page = page
        self.pp = None
        super(Pattern, self).__init__()
        loadUi("UI/pattern.ui", self)
        self.homebt.clicked.connect(lambda: self.page(HOME))
        self.crimeprediction.clicked.connect(lambda: self.page(PREDICT))
        self.crimematching.clicked.connect(lambda: self.page(MATCHING))
        self.crimerate.clicked.connect(lambda: self.page(RATE))
        self.crimepattern.clicked.connect(lambda: self.page(PATTERN))

        self.select.clicked.connect(self.select_file)
        self.s1.clicked.connect(self.pa1)
        self.s2.clicked.connect(self.pa2)
        self.s3.clicked.connect(self.pa3)
        self.s4.clicked.connect(self.pa4)

    def select_file(self):
        self.options = QFileDialog.Options()
        self.options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)", options=self.options)
        text = "<html><body>{}</body></html>"
        self.pathlabel.setText(text.format(file_name))
        if file_name:
            self.pp = PP.Pattern(file_name)

    def pa1(self):
        if self.pp:
            self.pp.p1()
    def pa2(self):
        if self.pp:
            self.pp.p2()
    def pa3(self):
        if self.pp:
            self.pp.p3()
    def pa4(self):
        if self.pp:
            self.pp.p4()

            


class Matching(QDialog):
    def __init__(self, page):
        self.page = page
        super(Matching, self).__init__()
        loadUi("UI/matching.ui", self)
        self.homebt.clicked.connect(lambda: self.page(HOME))
        self.crimeprediction.clicked.connect(lambda: self.page(PREDICT))
        self.crimematching.clicked.connect(lambda: self.page(MATCHING))
        self.crimerate.clicked.connect(lambda: self.page(RATE))
        self.crimepattern.clicked.connect(lambda: self.page(PATTERN))

        self.addmatch.clicked.connect(self.getdata)

    def getdata(self):
        time=self.dateTimeEdit.dateTime().toPyDateTime()
        time_string = time.strftime('%Y-%m-%d %H:%M')
        area=self.location.currentText()
        acts=self.actsdd.currentText()
        crime=self.crimes.currentText()
        victimid=self.VictimIDLE.text()
        new_entry = {
                    'Timestamp':time_string,
                    'Area':area ,
                    'Acts':acts,
                    'Crime':crime ,
                    'Victim_ID':victimid
                    }
        mp=MP.Matching(new_entry)


class Rate(QDialog):
    def __init__(self, page):
        self.page = page
        super(Rate, self).__init__()
        loadUi("UI/crimerate.ui", self)
        self.homebt.clicked.connect(lambda: self.page(HOME))
        self.crimeprediction.clicked.connect(lambda: self.page(PREDICT))
        self.crimematching.clicked.connect(lambda: self.page(MATCHING))
        self.crimerate.clicked.connect(lambda: self.page(RATE))
        self.crimepattern.clicked.connect(lambda: self.page(PATTERN))
        self.result0.clicked.connect(self.pa1)
        self.result1.clicked.connect(self.pa2)
    def pa1(self):
        self.areas=self.area.currentText()
        RP.p1(self.areas)
    def pa2(self):
        self.crime=self.crimes.currentText()
        RP.p2(self.crime)
            

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
sys.exit(app.exec_())
