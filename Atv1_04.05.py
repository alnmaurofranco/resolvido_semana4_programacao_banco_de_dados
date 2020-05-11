users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]

dicionario = [(6, 'M'), (2, 'M'), (1, 'M'), (8, 'F')]

for user in users:
    user["sexo"] = []
    user["idade"] = []

for i, j in dicionario:
    users[i]["sexo"].append(users[j])
    users[j]["sexo"].append(users[i])
    users[i]["idade"].append(users[j])
    users[j]["idade"].append(users[i])

def users_with_sexo (user):
    if (user['sexo'] == 'M'):
        return user['sexo'].append(user['M'])
    elif (user['sexo'] == 'F'):
        return user['sexo'].append(user['F'])


def number_of_users_sexo (user):
    return len(user["sexo"])

def users_with_sexy_equals_masculino (user):
    return user['sexo'] == 'M'
    
def users_with_sexo_equals_feminino (user):
    return user['sexo'] == 'F'

def friends_with_sexo (user):
    return [
        id
        for sexo in user ['sexo']
        for sexos in sexo ['sexo']
        if users_with_sexy_equals_masculino (user, sexos)
        and users_with_sexo_equals_feminino (user, sexos)
    ]
    
print(friends_with_sexo)