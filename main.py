import sqlite3
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from ui_addEditCoffeeForm import Ui_MainWindow as UiAddCoffe
from ui_main import Ui_MainWindow as UiMain


class TableCoffe(QMainWindow, UiMain):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect('data\\coffee.sqlite')
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
        """При двойном нажатии на ячейку таблицы можно будет изменить данные о ее содержимом"""
        self.coffe = CreateCoffe(id_coffe=self.tableWidget.item(row, 0).text())
        self.coffe.show()


class CreateCoffe(QMainWindow, UiAddCoffe):
    def __init__(self, id_coffe=''):
        super().__init__()
        self.setupUi(self)
        self.id = id_coffe
        self.btn_close.clicked.connect(self.close)
        self.btn_create_edit.clicked.connect(self.create_edit_coffe)
        self.con = sqlite3.connect('data\\coffee.sqlite')

    def create_edit_coffe(self):
        text_edit = [self.name_sort.text(), self.step_obz.text(), self.molot_zern.text(),
                     self.vkus.text(), self.price.text(), self.obem.text()]
        for text in text_edit:
            if not text:
                return

        cur = self.con.cursor()
        if not self.id:
            cur.execute("INSERT INTO coffee (sort_title, degree_of_roasting, ground_or_grains, "
                        "flavor_description, price, volume_of_packaging) VALUES (?,?,?,?,?,?)", (*text_edit,))
        else:
            cur.execute('UPDATE coffee SET sort_title=?, degree_of_roasting=?, ground_or_grains=?, '
                        'flavor_description=?, price=?, volume_of_packaging=? WHERE id = ?', (*text_edit, self.id))
        self.con.commit()
        super().close()

    def closeEvent(self, event):
        ex.show_items()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TableCoffe()
    ex.show()
    sys.exit(app.exec())
