import pandas as pd
import numpy as np

def r_file(name_file_inp):
    dataframe=pd.read_csv(name_file_inp)
    df=pd.DataFrame(dataframe)
    return(dataframe,df)
def w_file(name_file_out,df_out):
    df_out.to_csv(name_file_out,encoding='utf-8-sig',index=False)   
def value_int(title_in,line_lesson,value_lesson):
    inp_name_lesson=df_in[title_in]
    # line_lesson = 1
    # value_lesson='Bài 3: Gõ các dấu sắc, huyền, hỏi, ngã, nặngnew'
    inp_name_lesson[int(line_lesson)]=value_lesson
        
if __name__=="__main__":
    name_file_inp='D:/python/theodoipm_v2/theodoiphongmay.csv'
    name_file_out=r'D:/python/theodoipm_v2/theodoiphongmay_new.csv'
    dataframe,df_in=r_file(name_file_inp)
    
    title_in=input('nhập cột cần ghi ')
    line_lesson=input('nhập dòng')
    value_lesson=input('nhap ten bai:')
    value_int(title_in,line_lesson,value_lesson)
    # df_in.iat[1, 4]='hello0000'
    # inp_name_lesson=df_in['Bài dạy']
    # line_lesson = 1
    # new_lesson='Bài 3: Gõ các dấu sắc, huyền, hỏi, ngã, nặngnew'
    # inp_name_lesson[int(line_lesson)]=new_lesson
    
    
    
    
    w_file(name_file_out,df_in)
    print(df_in)
    