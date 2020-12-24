def max_score_keys(users,user_marks):
    key1=list(users.keys())
    value1 = list(user_marks.values())
    position = []
    position_keys = []
    position_values = []
    if value1.count(max(value1)) >= 2:
        for i in range(len(value1)):
            if value1[i] == max(value1):
                position.append(i)
                position_values.append(value1[i])
        for i in position:
            position_keys.append(key1[i])
        print('Maximum marks scored keys are:',dict(zip(position_keys,position_values)))
    else:
        tp1=key1[value1.index(max(value1))]
        tp2=max(value1)
        print('Maximum marks scored keys are:',dict(zip((tp1,),(tp2,))))

users = {'1' : 'name1','9':'name9','2' : 'name2','3' : 'name3','4':'name4','5':'name5'}
user_marks={'9':70,'1' : 50,'2' : 60,'3' : 70,'4':70,'5':70}
max_score_keys(users,user_marks)
