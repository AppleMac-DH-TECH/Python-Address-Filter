import os
import pandas as pd
from pandas import DataFrame

cleaned = []

def train(src_xlsx_path: str):
    df = pd.read_excel(src_xlsx_path, sheet_name="Sheet1")
    
    global cleaned
    
    for id in range(len(df)):
        src_addr = df.at[id, 'EMP LOCATION']
        dst_addr = df.at[id, 'CLEANED ADDRESS']
        inx = 0
        while src_addr[inx] == ' ':
            inx += 1
        src_addr = src_addr[inx:]
        inx = 0
        while dst_addr[inx] == ' ':
            inx += 1
        dst_addr = dst_addr[inx:]
        # print(src_addr)
        # print(dst_addr)
        
        diff_str = ''
        j = 0
        for i in src_addr:
            if j >= len(dst_addr):
                break
            if i == dst_addr[j]:
                if diff_str != '' and diff_str not in cleaned:
                    cleaned.append(diff_str)
                    print(diff_str)
                    diff_str = ''
                j += 1
            else:
                diff_str += i
        
                
    print(cleaned)

def filter(src_addr: str):
    
    global cleaned
    
    dst_addr = src_addr
    
    if not len(cleaned):
        print("first training!")
        return ''
    
    for item in cleaned:
        dst_addr = dst_addr.replace(item, '')
    
    return dst_addr
    

if __name__ == "__main__":
    train_xlsx_path = os.getcwd() + "\\address_sample_ 2.xlsx"
    src_addr_path = os.getcwd() + "\\input.xlsx"
    train(train_xlsx_path)
    
    df = pd.read_excel(src_addr_path, sheet_name="Sheet1")
    
    dst_addr_list = []
    
    for id in range(len(df)):
        src_addr = df.at[id, 'EMP LOCATION']
        dst_addr = filter(src_addr)
        if dst_addr != '':
            dst_addr_list.append(dst_addr)

    df = DataFrame(dst_addr_list, columns=['CLEANED ADDRESS'])
    df.to_excel("output.xlsx", sheet_name='Sheet1')