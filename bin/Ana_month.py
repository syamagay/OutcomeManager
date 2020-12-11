import sys
import os

sys.path.append(os.getcwd())
from src import pyH1F

def read_one_month(year, month):
    #print(year)
    #print(os.getcwd())
    maindir_path="/Users/syamagay/Project/OutcomeManagement/"
    datafile_path=maindir_path+"outcome/"
    pic_dirpath=maindir_path+"picture/"
    filename = str(year)+'{0:02d}'.format(int(month))+"-表1.csv"

    filepath = datafile_path+filename
    
    HistList=[]
    HistTitle_List=[]
    HistList.append(pyH1F.pyH1F(10,0,10))
    HistTitle_List.append('CategoryHist') # distinguish by categories

    HistList.append(pyH1F.pyH1F(10,0,10))
    HistTitle_List.append('ShopHist') # distinguish by shops

    HistList.append(pyH1F.pyH1F(10,0,10))
    HistTitle_List.append('category_const_same') # distinguish by categories and const outcome are treated as the same.

    
    
    with open(filepath,'r') as f:
        line = f.readline() # 1行を文字列として読み込む(改行文字も含まれる)
        data_flag=False
        while line:
            buf_list = line.split(',')
            if data_flag :
                #print(buf_list[0])
                HistList[0].Fill_string(buf_list[2],int(buf_list[3]))
                HistList[1].Fill_string(buf_list[2],int(buf_list[3]))

                # Treat "const" values as the same.
                if buf_list[0]=='const':
                    HistList[2].Fill_string('const',int(buf_list[3]))
                else:
                    HistList[2].Fill_string(buf_list[2],int(buf_list[3]))
            elif buf_list[0]=="Date":
                data_flag = True
            line = f.readline()
        for hist, histname in zip(HistList, HistTitle_List) :
            hist.SetTitle(histname)
            picture_path = pic_dirpath + histname +str(year)+'{0:02d}'.format(int(month))+'.png'
            hist.Draw('hist',picture_path)
        HistList[2].Draw('text')
            
if __name__=="__main__" :
    args = sys.argv
    if len(args) < 3 :
        print("Arguments are not enough!")
        print(args[0]+" <year> <month>")
    else :
        read_one_month(args[1],args[2])
    
