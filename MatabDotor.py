#soalmatabdotor4
#class error(Exception):
    #def __init__(self, massage):
        #self.massage = massage
class  hospital:
    def __init__(self):
        self.patient = {}
        self.time_list1 = []
        self.time_list2 = []
    def add_patient(self, id, name, family_name, age, height, weight):
        if id not in self.patient: 
            if age < 0: return print('error: invalid age')
            if height < 0: return print('error: invalid height')
            if weight < 0: return print('error: invalid weight')
            self.patient[id] = {'id':id, 'name':name, 'family_name':family_name,
                                'age':age, 'height':height, 'weight':weight, 'visiting_time':None}
            return print('patient added successfully')
        else:
            print('error: this ID already exists')
        if age < 0: print('error: invalid age')
        if height < 0: print('error: invalid height')
        if weight < 0: print('error: invalid weight')
    def display_patient(self, id):
        if id in self.patient:
            #print(f'patient name: {self.patient[id]['name']}\n'
                  #f'patient family name: {self.patient[id]['family_name']}\n'
                  #f'patient age: {self.patient[id]['age']}\n'
                  #f'patient height: {self.patient[id]['height']}\n'
                  #f'patient weight: {self.patient[id]['weight']}')
            print('patient name:',self.patient[id]['name'])
            print('patient family name:',self.patient[id]['family_name'])
            print('patient age:',self.patient[id]['age'])
            print('patient height:',self.patient[id]['height'])
            print('patient weight:',self.patient[id]['weight'])
        else:
            print('error: invalid ID')
    def add_visit(self, id, beginning_time):
        if id not in self.patient:
            print('error: invalid id')
        elif 9 > beginning_time  or  beginning_time > 18:
            print('error: invalid time')
        elif beginning_time in self.time_list1:
            print('error: busy time')
        else:
            self.time_list1.append(beginning_time)
            self.time_list2.append(id)
            print('visit added successfully!')
    def display_visit_list(self):
        print('SCHEDULE:')
        for id, time in enumerate(self.time_list1):
            print(str(time) + ':00' if time < 10 else str(time) + ':00',self.patient[self.time_list2[id]]['name'],self.patient[self.time_list2[id]]['family_name'])
    def delete_patient(self, id):
        if id in self.patient:
            self.patient.pop(id)
            print('patient deleted successfully!')
            for i in range(len(self.time_list1)-1, -1, -1):
                if self.time_list2[i] not in self.patient:
                    self.time_list1.pop(i)
                    self.time_list2.pop(i)
        else:
            print('error: invalid id')
dr_mt = hospital()
dastor = []
while True:
    check = input()
    if check == '':
        check = 'non n'
    if check == 'exit':
        break
    dastor.append(check.split())
i = 0
while i < len(dastor):
    
    if dastor[i][0] == 'add' and dastor[i][1] == 'visit':
        dr_mt.add_visit(int(dastor[i][2]),int(dastor[i][3]))
    elif dastor[i][0] == 'add' and dastor[i][1] == 'patient':
        dr_mt.add_patient(int(dastor[i][2]), dastor[i][3], dastor[i][4], int(dastor[i][5]), int(dastor[i][6]), int(dastor[i][7]))
    elif dastor[i][0] == 'display'and dastor[i][1] == 'patient':
        dr_mt.display_patient(int(dastor[i][2]))
    elif dastor[i][0] == 'display'and dastor[i][1] == 'visit':
        dr_mt.display_visit_list()
    elif dastor[i][0] == 'delete':
        dr_mt.delete_patient(int(dastor[i][2]))
    else:
        print('invalid command')
    i += 1
#clean_code