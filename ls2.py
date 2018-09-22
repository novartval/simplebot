school = [
    {'Class':'11', 'Оценки': [3,4,5,6,4,5]},
    {'Class':'10', 'Оценки': [5,4,5,2,3,4]},
    {'Class':'10', 'Оценки': [5,4,5,2,3,4]},
    {'Class':'10', 'Оценки': [5,4,5,2,3,4]},
    {'Class':'10', 'Оценки': [5,4,5,2,3,4]},
    {'Class':'10', 'Оценки': [5,4,5,2,3,4]},
    {'Class':'9', 'Оценки': [3,4,5,6,3,5]}
]

def mean_assessment_class(school):
    mean_assessments = {}
    for classes in school:
        mean_assessments[classes[u'Class']] = sum(classes[u'Оценки']) / float(len(classes[u'Оценки']))
    return mean_assessments

def mean_assessments_school(school):
    sum_assessments = 0
    cnt_assessments = 0
    for classes in school:
        sum_assessments += sum(classes[u'Оценки'])
        cnt_assessments += len(classes[u'Оценки'])
    return sum_assessments / cnt_assessments


mean_assessments_dict = mean_assessment_class(school)

for key, value in mean_assessments_dict.items():
    print(key,value)

print(mean_assessments_school(school))  




''''

def age_input(age):
    if age < 7:
        print('Пользователь еще в детском саду.')
    elif age >= 7 and age <= 18:
        print('Пользователь учится в школе')
    elif age >= 18 and  age <= 25:
        print('Пользователь учится в вузе')
    else:
        print('Пользователь работает.')

age = int(input('Введите возраст пользователя:'))
alex = age_input(age)

'''

def check_str(first_str,second_str):
    if not isinstance(first_str,str) or not isinstance(second_str, str):
        return 0
    elif first_str == second_str:
        return 1
    elif first_str != second_str and second_str != 'learn':
        if len(first_str) > len(second_str):
            return 2
        else:
            return 'Ни одно условие не будет выполнено'
    elif first_str != second_str:
        if second_str == 'learn':
            return 3

def asking_qwest():
    asking_dict = {'Как ты?':'Неплохо', 'Чем занят?':'учусь',
    'Что будешь делать дальше?':'спать'}

    while True:
        ask = str(input(''))
        if ask in asking_dict:
            print(asking_dict[ask])
        else:
            print('мммммммм, все понятно')

asking_qwest()




