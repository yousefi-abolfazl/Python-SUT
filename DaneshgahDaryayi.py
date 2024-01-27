#DaneshgahDaryayi
class University:
    def __init__(self):
        self.course = {}
        self.student = {}
        self.log = {}
    def Add_Student(self, type, id, name, password):
        if type != 'S' and type != 'P':
            return print('invalid type')
        try: 
             id = int(id)
        except:
            return print('invalid id')
        if len(name.split()) > 1:
            return print('invalid name')
        if len(password.split()) > 1 or len(password) < 5:
            return print('invalid password')
        special_char = ['*','.','!','@','$','%','^','&','(',')']
        run = False
        for letter in password:
            if letter in special_char:
                run = True
                break
        if run == False:
            return print('invalid password')
        for id_inf in self.student.keys():
            if str(id_inf) == str(id):
                return print('id already exists')
        self.student[str(id)] = [type, name, password, []]   #OOOOOO
        self.log[str(id)] = False
        return print('signed up successfully!')
    def Login_Student(self, id, password):
        for i, info in self.student.items():
            if id == i:
                if password == info[2]:
                    self.log[str(id)] = True
                    if info[0] == 'S':
                        t = 'student menu'
                    else: 
                        t ='professor menu'
                    return print(f'logged in successfully!\nentered {t}')
                else:
                    return print('incorrect password')
        return print('incorrect id')
    def Logout_Student(self):
        num = False
        for id, login in self.log.items():
            if login == True:
                self.log[str(id)] = False
                num = True
        if num:
            return print('logged out successfully!\nentered log in/sign up menu')
        else:
            return print('invalid command')
    def Add_Course(self, course_id, name, capacity):
        if len(name.split()) > 1:
            return print('invalid course name')
        try: 
             course_id = int(course_id)
        except:
            return print('invalid course id')
        try: 
             capacity = int(capacity)
        except:
            return print('invalid course id')
        if str(course_id) in self.course:
            return print('course id already exists')
        self.course[str(course_id)] = [name, capacity, 0]
        return print('course added successfully!')
    def Get_Course(self, course_id):
        for i, l in self.log.items():
            if l == True:
                Id = i
        if course_id not in self.course:
            return print('incorrect course id')
        if course_id in self.student[Id][3]:
            return print('you already have this course')
        if self.course[course_id][1] == self.course[course_id][2]:
            return print('course is full')
        self.course[course_id][2] += 1    
        self.student[Id][3].append(course_id)
        return print('course added successfully!')    
    def Show_Course(self):
        print('course list:')
        for id_course, info_course in self.course.items():
            print(f'{id_course} {info_course[0]} {info_course[2]}/{info_course[1]} ')
uni = University()      
lst_dastor = []
while True:
    str_1 = input().strip()
    for i, w in enumerate(str_1):
        if i == len(str_1)-3:
            break
        if w != ' ' and str_1[i+1] == ' ' and str_1[i+2] == ' ':
            str_1 += 'o_o'
            break
    lst = str_1.split()
    if lst[0] == 'edu' and lst[-2] == 'exit' and lst[-1] == 'edu':
        break
    lst_dastor.append(lst)
i = 0
special_lst = ['edu', 'sign', 'up', '-i', '-n', '-p']
while i < len(lst_dastor):
    if lst_dastor[i][0] == 'edu' and lst_dastor[i][1] == 'current' and lst_dastor[i][-2] == 'menu' and lst_dastor[i][-1] == 'edu': 
        run = False
        for id , log in uni.log.items():
            if log == True:
                run = True
                Id1 = id
                break
        if run:
            if uni.student[Id1][0] == 'S':
                print('student menu')
            else:
                print('professor menu')
        else:
            print('log in/sign up menu')  
    elif lst_dastor[i][0] == 'edu' and lst_dastor[i][1] == 'sign' and lst_dastor[i][2] == 'up' and lst_dastor[i][4] == '-i' and lst_dastor[i][6] == '-n' and lst_dastor[i][8] == '-p' and lst_dastor[i][-1] == 'edu': 
        uni.Add_Student(list(lst_dastor[i][3])[1], lst_dastor[i][5], lst_dastor[i][7], lst_dastor[i][9])
    elif lst_dastor[i][0] == 'edu' and lst_dastor[i][1] == 'add' and lst_dastor[i][2] == 'course' and lst_dastor[i][3] == '-c' and lst_dastor[i][5] == '-i' and lst_dastor[i][7] == '-n' and lst_dastor[i][0] == 'edu':
        uni.Add_Course(lst_dastor[i][6], lst_dastor[i][4], lst_dastor[i][8])
    elif lst_dastor[i][0] == 'edu' and lst_dastor[i][1] == 'show' and lst_dastor[i][2] == 'course' and lst_dastor[i][3] == 'list' and lst_dastor[i][-1] == 'edu':
        uni.Show_Course()
    elif lst_dastor[i][0] == 'edu' and lst_dastor[i][1] == 'log' and lst_dastor[i][2] == 'in' and lst_dastor[i][3] == '-i' and lst_dastor[i][5] == '-p' and lst_dastor[i][-1] == 'edu':
        uni.Login_Student(lst_dastor[i][4], lst_dastor[i][6]) 
    elif lst_dastor[i][0] == 'edu' and lst_dastor[i][1] == 'log' and lst_dastor[i][2] == 'out' and lst_dastor[i][-1] == 'edu':
        uni.Logout_Student()
    elif lst_dastor[i][0] == 'edu' and lst_dastor[i][1] == 'get' and lst_dastor[i][2] == 'course' and lst_dastor[i][3] == '-i' and lst_dastor[i][-1] == 'edu':
        uni.Get_Course(lst_dastor[i][4])
    else:
        run1 = True
        for inx in range(len(lst_dastor[i])-1, -1, -1):
            if inx == 0:
                break
            if inx == len(lst_dastor[i])-1:
                continue
            if lst_dastor[i][inx] not in special_lst and lst_dastor[i][inx +1] not in special_lst and lst_dastor[i][inx-1] in special_lst:
                g = lst_dastor[i].pop(inx)
                try:
                    lst_dastor[i][inx] = g + ' ' + lst_dastor[i][inx]
                    run1 = False
                except:
                    pass
        if run1:
            print('invalid command')
        else:
            i -= 1  
    i += 1
print(uni.log)    
print(lst_dastor)
#clean_code