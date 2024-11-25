import io
import sys
import sqlite3

from PyQt6 import uic
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QColor, QPainter, QPolygonF
from PyQt6.QtWidgets import QApplication, QMainWindow, QColorDialog, QTableWidgetItem
from math import sin, cos, pi


template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>952</width>
    <height>441</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QTableWidget" name="tableWidget">
      <attribute name="horizontalHeaderCascadingSectionResizes">
       <bool>false</bool>
      </attribute>
      <attribute name="horizontalHeaderShowSortIndicator" stdset="0">
       <bool>false</bool>
      </attribute>
      <attribute name="horizontalHeaderStretchLastSection">
       <bool>true</bool>
      </attribute>
      <attribute name="verticalHeaderCascadingSectionResizes">
       <bool>false</bool>
      </attribute>
      <attribute name="verticalHeaderShowSortIndicator" stdset="0">
       <bool>false</bool>
      </attribute>
      <attribute name="verticalHeaderStretchLastSection">
       <bool>false</bool>
      </attribute>
      <column>
       <property name="text">
        <string>ID</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>Название сорта</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>Степень обжарки</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string> Молотый/в зернах</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>Описание вкуса</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>Цена</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>Объем упаковки</string>
       </property>
      </column>
     </widget>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class NoTSquare(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.con = sqlite3.connect('coffee.sqlite')
        self.show_items()

    def show_items(self):
        cur = self.con.cursor()
        res = cur.execute('select * from coffee').fetchall()
        self.tableWidget.setRowCount(len(res))
        for n, i in enumerate(res):
            for col, j in enumerate(i):
                self.tableWidget.setItem(n, col, QTableWidgetItem(str(j)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NoTSquare()
    ex.show()
    sys.exit(app.exec())
