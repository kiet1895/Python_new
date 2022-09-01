from msilib.schema import CheckBox
from operator import index
import xlwings as xw
import pandas as pd
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from mainWin import Ui_MainWindow


class read_file:
    def __init__(self):
        app = xw.App(visible=False)
        self.wb = xw.Book(r'D:\python\theodoipm_v3\theodoiphongmay.xlsx')
        self.sheet_name = self.wb.sheets

    def r_file(self, row_colum, value_in):
        self.sheet1 = self.sheet_name[0]
        '''v2-chuyển data vào list hoặc tupe rồi dùng vòng lặp để ghi file'''
        # print(self.sheet1)
        # b = MainWindow()
        # cc = b.check_box()
        # print(cc)
        self.sheet1.range(row_colum).value = value_in
        # self.wb.save()
        # self.wb.close()
    # def addActivate(self,sheetName,template=None):
    #     try:
    #         sht = self.wb.sheets(sheetName).activate()
    #     except:
    #         if template:
    #             template.sheets["Template"].api.Copy(wb.sheets.active.api)
    #             sht = self.wb.sheets["Template"].api.Name = sheetName
    #         else:
    #             sht = self.wb.sheets.add(sheetName)
    #     return sht


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.pushButton.clicked.connect(self.check_box)
        self.uic.pushButton.clicked.connect(self.outputstr)
        self.uic.pushButton.clicked.connect(self.check_teacher)
        self.uic.pushButton_2.clicked.connect(self.closeEvent)

    def closeEvent(self):
        msg = QMessageBox()
        msg.setWindowTitle("Thông Báo")
        msg.setText('Bạn có muốn đóng chương trình')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        if msg.exec_() == QMessageBox.Yes:
            sys.exit(app.exec())

    def check_box(self):
        global dem
        dem = dict()
        read = read_file()
        if self.uic.checkBox_1.isChecked() == True:
            read.r_file('A1', 'abc')
            dem[1] = 1
            print('yes 1')
        if self.uic.checkBox_2.isChecked() == True:
            read.r_file('A2', 'abc')
            dem[2] = 2
            print('yes 2')
        if self.uic.checkBox_3.isChecked() == True:
            read.r_file('A3', 'abc')
            dem[3] = 3
            print('yes 3')
        if self.uic.checkBox_4.isChecked() == True:
            read.r_file('A4', 'abc')
            dem[4] = 4
            print('yes 4')
        if self.uic.checkBox_5.isChecked() == True:
            read.r_file('A5', 'abc')
            dem[5] = 5
            print('yes 5')
        if self.uic.checkBox_6.isChecked() == True:
            read.r_file('A6', 'abc')
            dem[6] = 6
            print('yes 6')
        if self.uic.checkBox_7.isChecked() == True:
            read.r_file('A7', 'abc')
            dem[7] = 7
            print('yes 7')
        if self.uic.checkBox_8.isChecked() == True:
            read.r_file('A8', 'abc')
            dem[8] = 8
            print('yes 8')
        if self.uic.checkBox_9.isChecked() == True:
            read.r_file('A9', 'abc')
            dem[9] = 9
            print('yes 9')
        read.wb.save()
        read.wb.close()

    def outputstr(self):
        key_row = list(dem.keys())
        print(key_row)
        read = read_file()
        colum_bai = 'C'
        colum_lop = 'B'
        if self.uic.textEdit.toPlainText() != '':
            a = list((self.uic.textEdit.toPlainText().split(" ")))
            num = 0
            if len(a) == len(key_row):
                for i in range(len(key_row)):
                    read.r_file(colum_lop+str(key_row[i]), "'"+a[num])
                    num += 1
                print('đã ghi tên lớp')
                if self.uic.textEdit_2.toPlainText() != '':
                    for i in range(len(key_row)):
                        read.r_file(colum_bai+str(key_row[i]), self.uic.textEdit_2.toPlainText())
                        print('đã ghi tên bài')
                else:
                    print("chưa ghi tên bài học")
            else:
                print("chưa ghi đầy đủ tên lớp")
        else:
            print("chưa ghi tên lớp")
        read.wb.save()
        read.wb.close()

    def check_teacher(self):
        key_row = list(dem.keys())
        read = read_file()
        colum_teacher= 'D'
        for i in range(len(key_row)):
            if self.uic.radioButton.isChecked() == True:
                read.r_file(colum_teacher+str(key_row[i]), 'Thầy kiệt')
            if self.uic.radioButton_2.isChecked() == True:
                read.r_file(colum_teacher+str(key_row[i]), 'Cô Nguyên')
        
        read.wb.save()
        read.wb.close()
    def show(self):
        self.main_win.show()


if __name__ == '__main__':
    ''''chạy giao diện'''
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    ''''chạy giao diện'''
    # read.wb.save()
    # read.wb.close()
    sys.exit(app.exec())
