import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
rcParams['font.family'] =['Hiragino Sans']

class pyH1F:
    def __init__(self,bin,min,max):
        self.bin=bin
        self.min=min
        self.max=max

        self.value_name=[]
        self.bin_width=(max-min)/bin
        self.value_list=[0]*bin
        self.total_entry=0

        self.value_max=0
        self.title='test'
        self.x_label=''
        self.y_label=''

        self.integral=0
        self.y_range=[0,0,0]
        
    def SetTitle(self,tit):
        if ';' in tit :
            tit_list=tit.split(';')
            self.title=tit_list[0]
            self.x_label=tit_list[1]
            self.y_label=tit_list[2]
        else :
            self.title=tit
    def SetYRange(self,y_min, y_max):
        self.y_range[0]=1
        self.y_range[1]=y_min
        self.y_range[2]=y_max
        
    def Fill_string(self,name,value=1):
        i=0
        name_exist=0
        name_number=0
        for vname in self.value_name:
            if vname == name :
                name_exist=1
                name_number=i
            i=i+1
        if name_exist == 0 :
            name_number=i
            self.value_name.append(name)
            if len(self.value_name) > self.bin :
                self.value_list.append(0)
                self.bin = self.bin+1
                self.max = self.max+1
        self.Fill(name_number,value)
    def Fill(self,num,value=1):
        if num >= self.min and num < self.max :
            bin_width=(self.max-self.min)/(self.bin)
            bin_num=int(num/bin_width)
        
            self.value_list[bin_num]=self.value_list[bin_num]+value
            self.total_entry=self.total_entry+value
            self.integral = self.integral + num*value
            
            if self.value_list[bin_num] > self.value_max :
                self.value_max=self.value_list[bin_num]
    def Draw(self, option='hist', fname=''):
        if len(self.value_name) > 0 :
            self.value_list, self.value_name = self.ValueSort(self.value_list, self.value_name)
        if not fname == '':
            fig = plt.figure()
        
        first_text = 'total entry = '+str(self.total_entry)
        if option == 'text' :
            print('=============== Result ======================')
            for i_bin in range(0,self.bin):
                text='Value = '
                
                if len(self.value_name) > i_bin :
                    text += self.value_name[i_bin]
                else :
                    text += str(i_bin)
                text += ", "+str(self.value_list[i_bin])+", "+str(round(self.value_list[i_bin]/self.total_entry*100,2))+'%'
                print(text)
        elif option == 'pie' :
            data_list = np.array(self.value_list)
            plt.title('total = '+str(self.total_entry))
            plt.pie(data_list, labels=self.value_name, counterclock=False, startangle=90, autopct="%1.1f%%", pctdistance=0.7)

        elif option == 'hist' :
            if len(self.value_name) == 0 :
                for i in range(0,self.bin) :
                    self.value_name.append(self.bin_width*i)
                x_list=np.array(self.value_name)
            else :
                x_list=self.value_name
            if self.y_range[0] == 1:
                plt.ylim(self.y_range[1], self.y_range[2])
            plotted_data=np.array(self.value_list)
            plt.bar(x_list,plotted_data,width=self.bin_width)
            plt.xticks(rotation=90, size='small')
            plt.subplots_adjust(left=0.12, right=0.95, bottom=0.2, top=0.90)
            plt.title(self.title, fontsize=20)
            plt.xlabel(self.x_label)
            plt.ylabel(self.y_label)

            plt.text(x_list[-1],self.value_max,'Total : '+str(self.total_entry)+'\n Integral : '+str(self.integral)+'\n Average : '+str(float(self.integral)/float(self.total_entry)),ha='right',va='top')
            #print(x_list)
            #print(plotted_data)

        if not fname == '':
            fig.savefig(fname)
            plt.close(fig)

    def ValueSort(self, list_a, list_b):
        olist_a=[]
        olist_b=[]
        i=0

        for va in list_a :
            io=0
            temp_i=len(olist_a)
            for ova in olist_a :
                if va > ova :
                    temp_i=io
                    break
                io=io+1
            olist_a=self.SortList(olist_a, temp_i)
            olist_b=self.SortList(olist_b, temp_i)
            olist_a[temp_i] = va
            olist_b[temp_i] = list_b[i]
            i=i+1
            #print(olist_a)
            #print(olist_b)
        return olist_a, olist_b
    
    def SortList(self, old_list, number):
        new_list=[]
        i=0
        if len(old_list) == 0:
            new_list.append(0)
        for o_v in old_list :
            if i == number :
                new_list.append(0)
            new_list.append(o_v)
            i=i+1
        if len(old_list) == number and not len(old_list) == 0 :
            new_list.append(0)

        return new_list
        
if __name__=='__main__' :
    p=pyH1F(10,0,100)
    p.Fill(5)
    p.Fill(100)
    p.Draw('hist','test.png')
        
