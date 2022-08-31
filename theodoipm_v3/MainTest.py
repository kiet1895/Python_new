from doctest import OutputChecker
from msilib.schema import CheckBox
from operator import index
import xlwings as xw
import pandas as pd
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainWin import Ui_MainWindow


class read_file:
    def __init__(self):
        app = xw.App(visible=False)
        self.wb = xw.Book(r'D:\python\theodoipm_v3\theodoiphongmay.xlsx')
        self.sheet_name = self.wb.sheets
        # print(self.sheet_name[0])
        # self.wb.save()
        # self.wb.close()

    def r_file(self,row_colum,value_in):
        self.sheet1 = self.sheet_name[0]
        '''v2-chuyển data vào list hoặc tupe rồi dùng vòng lặp để ghi file'''
        # print(self.sheet1) 
        # b = MainWindow()
        # cc = b.check_box()
        # print(cc)
        self.sheet1.range(row_colum).value=value_in
        self.wb.save()
        self.wb.close()
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
    def check_box(self):
        global dem
        dem=0
        if self.uic.checkBox_1.isChecked() == True:
            read = read_file()
            read.r_file('A1','abc')
            dem+=1
            print('yes 1')
        if self.uic.checkBox_2.isChecked() == True:
            read = read_file()
            read.r_file('A2','abc')
            dem+=1
            print('yes 2')
        if self.uic.checkBox_3.isChecked() == True:
            read = read_file()
            read.r_file('A3','abc')
            dem+=1
            print('yes 3')
        if self.uic.checkBox_4.isChecked() == True:
            read = read_file()
            read.r_file('A4','abc')
            dem+=1
            print('yes 4')
        if self.uic.checkBox_5.isChecked() == True:
            read = read_file()
            read.r_file('A5','abc')
            dem+=1
            print('yes 5')
        if self.uic.checkBox_6.isChecked() == True:
            read = read_file()
            read.r_file('A6','abc')
            dem+=1
            print('yes 6')
        if self.uic.checkBox_7.isChecked() == True:
            read = read_file()
            read.r_file('A7','abc')
            dem+=1
            print('yes 7')
        if self.uic.checkBox_8.isChecked() == True:
            read = read_file()
            read.r_file('A8','abc')
            dem+=1
            print('yes 8')
        if self.uic.checkBox_9.isChecked() == True:
            read = read_file()
            read.r_file('A9','abc')
            dem+=1
            print('yes 9')
    def outputstr(self):
        colum_bai='B'
        colum_lop='C'
        row_bai=1
        row_lop=1
        if self.uic.textEdit.toPlainText()!='':
            a=list((self.uic.textEdit.toPlainText().split(",")))
            print(a)
            if len(a)==dem:
                for i in a:
                    read = read_file()
                    read.r_file(colum_lop+str(row_lop),"'"+str(i))
                    row_lop+=1
                print('đã ghi tên lớp')
                if self.uic.textEdit_2.toPlainText()!='':
                    for i in range(len(a)):
                        read = read_file()
                        read.r_file(colum_bai+str(row_bai),self.uic.textEdit_2.toPlainText())
                        row_bai+=1
                        print('đã ghi tên bài')
                else:
                    print("chưa ghi tên bài học")
            else: 
                print("chưa ghi đầy đủ tên lớp")
        else:
            print("chưa ghi tên lớp")
            
        # if self.uic.textEdit_2.toPlainText()!='':
        #     for i in range(len(a)):
        #         read = read_file()
        #         read.r_file(colum_bai+str(row_bai),self.uic.textEdit_2.toPlainText())
        #         row_bai+=1
        #         print('đã ghi tên bài')
        # else:
        #     print("chưa ghi tên bài học")
    def show(self):
        self.main_win.show()


if __name__ == '__main__':
    ''''chạy giao diện'''
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    ''''chạy giao diện'''
    # main_win.check_box()
    # read = read_file()
    # read.r_file('A11','abc')
    # row_colum='A10'
    # value_in='Thứ 3.2'
    # r_file(row_colum,value_in)
    # sheet_name='newsheet'
    # # wb.sheets[1].delete() '''delete sheet'''
    # # wb.sheets.add("trang 2") ''''add new sheet'''
    # addActivate(sheet_name)
    # print(wb.sheets['Trang_tính1'])

    sys.exit(app.exec())
