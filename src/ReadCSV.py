team_list=['G','DB','T','C','D','S','L','H','E','M','F','Bs']

def NumberOfGames(year):
    if year == 2020 :
        return 120
    else :
        return 143
def translate_team_number(team):
    number=0
    for i_team in team_list :
        if team == i_team :
            return number
        else :
            number=number+1

class ReadCSV:
    def __init__(self, filename, split_tag=','):
        self.f=open(filename,'r')
        self.split_tag=split_tag
        self.read_lines=0
        self.Additional_init()

    def Additional_init(self):
        self.ignore_lines=0
        
    def GetLine(self):
        self.read_lines=self.read_lines+1
        while self.read_lines-1 < self.ignore_lines :
            self.f.readline()
            self.read_lines=self.read_lines+1
        return self.f.readline().split(self.split_tag)

class ReadBaseballSchedule(ReadCSV):
    def Additional_init(self):
        self.ignore_lines=2
        self.number_of_games=0
        self.games_each_team=[0]*12
    def GetFirstLine(self):
        if self.read_lines == 0:
            self.read_lines=self.read_lines+1
            first_list=self.f.readline().split(self.split_tag)
            year=first_list[1]
            self.number_of_games=NumberOfGames(year)

    def GetLine(self):
        if self.read_lines == 0 :
            self.GetFirstLine()
        data_list=super().GetLine()
        if len(data_list) > 3 :
            home_team_number=translate_team_number(data_list[3])
            visitor_team_number=translate_team_number(data_list[4])
            self.games_each_team[home_team_number]+=1
            self.games_each_team[visitor_team_number]+=1
            if self.games_each_team[home_team_number] > self.number_of_games and self.games_each_team[visitor_team_number] > self.number_of_games :
                data_list.append('PostSeason')
            else :
                data_list.append('RegularSeason')
        return data_list
    
if __name__=='__main__':
    year=2018
    RBS=ReadBaseballSchedule('data/NPB_'+str(year)+'.csv')
    new_file=open('data/NPB_'+str(year)+'_update.csv','w')
    csv='Year,'+str(year)+'\n'+'Mon,Day,day_of_the_week,Home,Vistor,Home_Score,Vistor_Score,Game_Type\n'
    
    data_list=RBS.GetLine()
    while len(data_list) > 1 :
        #print(data_list)
        data_list=RBS.GetLine()
        for data in data_list :
            csv += str(data).rstrip('\n')+','
        csv+='\n'
    new_file.write(csv)

