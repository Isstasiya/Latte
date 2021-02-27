import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QPushButton, QMainWindow
from addEditCoffeeForm import Ui_Frames
from TableForm import Ui_Frame


class Example(QMainWindow, Ui_Frame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connection = sqlite3.connect("./data/coffee.sqlite")
        title = self.connection.execute('SELECT * FROM coffees WHERE id = 1').description
        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setHorizontalHeaderLabels(str(i[0]) for i in title)
        self.nk()
        self.pushButton.clicked.connect(self.nm)
        self.pushButton_2.clicked.connect(self.nh)
        self.show()

    def nk(self):
        res = self.connection.cursor().execute(f"""SELECT c.id, c.name_sort, c.degree, t.name_type, c.taste, c.price, c.volume
                                                   FROM coffees c INNER JOIN types t ON t.id = c.type = t.id;""").fetchall()
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()

    def nm(self):
        self.qw = Add()
        self.qw.show()

    def nh(self):
        we = list(set([i.row() for i in self.tableWidget.selectedItems()]))
        er = [self.tableWidget.item(i, 0).text() for i in we]
        if not er:
            print('ERROR!!')
            return
        self.qw = Rewrite()
        self.qw.show()


class Add(QMainWindow, Ui_Frames):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connection = sqlite3.connect("./data/coffee.sqlite")
        self.pushButton.clicked.connect(self.ad)
        res = self.connection.cursor().execute(f"""SELECT * FROM types""").fetchall()
        for i in res:
            self.comboBox.addItem(i[1])
        self.show()

    def ad(self):
        try:
            name = self.lineEdit.text()
            deg = int(self.spinBox.text())
            typ = self.comboBox.currentText()
            typ = self.connection.cursor().execute(f"""SELECT id FROM types WHERE name_type = '{typ}'""").fetchall()[0][0]
            iw = self.connection.cursor().execute(f"""SELECT max(id) FROM coffees""").fetchall()[0][0]
            if iw == None:
                iw = 1
            else:
                iw += 1
            op = self.lineEdit_2.text()
            price = int(self.spinBox_2.text())
            volume = int(self.spinBox_3.text())
            res = self.connection.cursor().execute(f"""INSERT INTO coffees (id, name_sort, degree, type, taste, price, volume) VALUES ({iw}, '{name}', {deg}, {typ}, '{op}', {price}, {volume})""").fetchall()
            self.connection.commit()
            self.connection.close()
            ex.nk()
            self.close()
        except Exception:
            print('ERROR!!')


class Rewrite(QMainWindow, Ui_Frames):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connection = sqlite3.connect("./data/coffee.sqlite")
        self.pushButton.clicked.connect(self.ad)
        res = self.connection.cursor().execute(f"""SELECT name_type FROM types""").fetchall()
        for i in res:
            self.comboBox.addItem(i[0])
        self.show()

    def ad(self):
        try:
            we = list(set([i.row() for i in ex.tableWidget.selectedItems()]))
            er = [ex.tableWidget.item(i, 0).text() for i in we]
            if not er:
                raise Exception
            name = self.lineEdit.text()
            deg = int(self.spinBox.text())
            typ = self.comboBox.currentText()
            typ = self.connection.cursor().execute(f"""SELECT id FROM types WHERE name_type = '{typ}'""").fetchall()[0][0]
            iw = self.connection.cursor().execute(f"""SELECT max(id) FROM coffees""").fetchall()[0][0] + 1
            op = self.lineEdit_2.text()
            price = int(self.spinBox_2.text())
            volume = int(self.spinBox_3.text())
            res = self.connection.cursor().execute(f"""UPDATE coffees SET name_sort='{name}', degree={deg}, type={typ}, taste='{str(op)}', price={price}, volume={volume} WHERE id={int(er[0])}""").fetchall()
            self.connection.commit()
            self.connection.close()
            ex.nk()
            self.close()
        except Exception:
            print('ERROR!!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())