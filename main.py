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
    <height>465</height>
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
    <item>
     <widget class="QPushButton" name="btn_create_edit_main">
      <property name="text">
       <string>Создать</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>

'''
template2 =  '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>905</width>
    <height>147</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="btn_create_edit">
    <property name="geometry">
     <rect>
      <x>550</x>
      <y>100</y>
      <width>171</width>
      <height>24</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Создать/Изменить</string>
    </property>
   </widget>
   <widget class="QPushButton" name="btn_close">
    <property name="geometry">
     <rect>
      <x>750</x>
      <y>100</y>
      <width>111</width>
      <height>24</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Отмена</string>
    </property>
   </widget>
   <widget class="QWidget" name="layoutWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>20</y>
      <width>852</width>
      <height>54</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <layout class="QVBoxLayout" name="verticalLayout">
       <item>
        <widget class="QLabel" name="label">
         <property name="font">
          <font>
           <pointsize>13</pointsize>
          </font>
         </property>
         <property name="text">
          <string>Название сорта</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLineEdit" name="name_sort"/>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_2">
       <item>
        <widget class="QLabel" name="label_2">
         <property name="font">
          <font>
           <pointsize>13</pointsize>
          </font>
         </property>
         <property name="text">
          <string>Степень обжарки</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLineEdit" name="step_obz"/>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_3">
       <item>
        <widget class="QLabel" name="label_3">
         <property name="font">
          <font>
           <pointsize>13</pointsize>
          </font>
         </property>
         <property name="text">
          <string>Молотый/в зернах</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLineEdit" name="molot_zern"/>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_4">
       <item>
        <widget class="QLabel" name="label_4">
         <property name="font">
          <font>
           <pointsize>13</pointsize>
          </font>
         </property>
         <property name="text">
          <string>Описание вкуса</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLineEdit" name="vkus"/>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_5">
       <item>
        <widget class="QLabel" name="label_5">
         <property name="font">
          <font>
           <pointsize>13</pointsize>
          </font>
         </property>
         <property name="text">
          <string>Цена</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLineEdit" name="price"/>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_6">
       <item>
        <widget class="QLabel" name="label_6">
         <property name="font">
          <font>
           <pointsize>13</pointsize>
          </font>
         </property>
         <property name="text">
          <string>Объем упаковки</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLineEdit" name="obem"/>
       </item>
      </layout>
     </item>
    </layout>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

class TableCoffe(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.con = sqlite3.connect('coffee.sqlite')
        self.btn_create_edit_main.clicked.connect(self.create_edit)
        self.tableWidget.cellDoubleClicked.connect(self.on_cell_double_clicked)
        self.show_items()

    def show_items(self):
        cur = self.con.cursor()
        res = cur.execute('select * from coffee').fetchall()
        self.tableWidget.setRowCount(len(res))
        for n, i in enumerate(res):
            for col, j in enumerate(i):
                self.tableWidget.setItem(n, col, QTableWidgetItem(str(j)))

    def create_edit(self):
        self.coffe = CreateCoffe()
        self.coffe.show()

    def on_cell_double_clicked(self, row, column):
        print(self.tableWidget.item(row, 0))
        self.coffe = CreateCoffe(id=self.tableWidget.item(row, 0).text())
        self.coffe.show()


class CreateCoffe(QMainWindow):
    def __init__(self, id=''):
        super().__init__()
        f = io.StringIO(template2)
        uic.loadUi(f, self)
        self.id = id
        self.btn_close.clicked.connect(self.close)
        self.btn_create_edit.clicked.connect(self.create_edit_coffe)
        self.con = sqlite3.connect('coffee.sqlite')

    def create_edit_coffe(self):
        text_edit = [self.name_sort.text(), self.step_obz.text(), self.molot_zern.text(),
                     self.vkus.text(), self.price.text(), self.obem.text()]
        for text in text_edit:
            if not text:
                return

        cur = self.con.cursor()
        if not self.id:
            cur.execute("INSERT INTO coffee (sort_title, degree_of_roasting, ground_or_grains, flavor_description, price, volume_of_packaging) VALUES (?,?,?,?,?,?)", (*text_edit,))
        else:
            cur.execute('UPDATE coffee SET sort_title=?, degree_of_roasting=?, ground_or_grains=?, flavor_description=?, price=?, volume_of_packaging=? WHERE id = ?', (*text_edit, self.id))
        self.con.commit()
        super().close()

    def closeEvent(self, event):
        # Функция вызывается при закрытии окна
        ex.show_items()
        event.accept()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TableCoffe()
    ex.show()
    sys.exit(app.exec())
