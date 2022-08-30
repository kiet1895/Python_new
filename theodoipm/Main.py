
from unicodedata import name


def r_file(name):
    tup=()
    ds=[]
    name='D:/python/theodoipm/'+name+'.csv'
    with open(name,mode='r',encoding='utf-8-sig') as f:
        while True:
            data = f.readline()
            if data=='': 
                break
            data_list=list(data.strip().split(','))
            # print(data_list)
            ds.append(data_list)
            tup=tuple(ds)
    return(tup)
def w_file(name_file,output):
    name_file='D:/python/theodoipm/'+name_file+'.csv'
    with open(name_file,mode='a',encoding='utf-8-sig') as f:
        f.write(output)
    return  
        
        
        
        
if __name__=="__main__":
    file_in='theodoiphongmay'
    file_out='theodoiphongmay_new'
    r_file=r_file(file_in)
    print(r_file[1])
    new_line='\n'+','.join(r_file[1])
    w_file(file_out,new_line)
    