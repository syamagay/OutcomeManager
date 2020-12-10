import sys
import os

sys.path.append(os.getcwd())
from src import pyH1F

def main(year, month):
    print(year)
    print(os.getcwd())
    datafile_path="/Users/syamagay/Project/OutcomeManagement/outcome/"
    filename = str(year)+'{0:02d}'.format(int(month))+"-表1.csv"

    filepath = datafile_path+filename
    with open(filepath,'r') as f:
        line = f.readline() # 1行を文字列として読み込む(改行文字も含まれる)
        while line:
            buf_list = line.split(',')
            print(buf_list[0])
            line = f.readline()
    

if __name__=="__main__" :
    args = sys.argv
    if len(args) < 3 :
        print("Arguments are not enough!")
        print(args[0]+" <year> <month>")
    else :
        main(args[1],args[2])
    
