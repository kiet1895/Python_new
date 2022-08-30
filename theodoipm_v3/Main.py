import xlwings as xw
import pandas as pd
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from mainWin import Ui_MainWindow


app=xw.App(visible=False)
wb = xw.Book(r'D:\python\theodoipm_v3\theodoiphongmay.xlsx')  
def r_file(row_colum,value_in):
    sheet_name= wb.sheets
    sheet1 = sheet_name[0]
    sheet1.range(row_colum).value=value_in
    # wb.save()
    # wb.close()
    # app.kill
def addActivate(sheetName,template=None):
    try:
        sht = wb.sheets(sheetName).activate()
    except:
        if template:
            template.sheets["Template"].api.Copy(wb.sheets.active.api)
            sht = wb.sheets["Template"].api.Name = sheetName
        else:
            sht = wb.sheets.add(sheetName)
    return sht

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.pushButton.clicked.connect(self.check_box)
        
    def check_box(self):
        if self.uic.checkBox_1.isChecked() == True:
            r_file('A10','Thứ 3.2.1')
        #     print('yes')
        # else:
        #     print('no')

    def show(self):
        self.main_win.show()





if __name__=='__main__':
    ''''chạy giao diện'''
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    ''''chạy giao diện'''
    ''''kiểm tra check box 1'''
    print(main_win.check_box())
    
    
    # row_colum='A10'
    # value_in='Thứ 3.2'
    # r_file(row_colum,value_in)
    # sheet_name='newsheet'
    # # wb.sheets[1].delete() '''delete sheet'''
    # # wb.sheets.add("trang 2") ''''add new sheet'''
    # addActivate(sheet_name)
    # print(wb.sheets['Trang_tính1'])
    
    wb.save()
    wb.close()
    sys.exit(app.exec())
    
    
