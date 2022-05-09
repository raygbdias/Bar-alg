import json, random, string


with open('db\\db.json', 'r') as db:
    data = json.load(db)


def get_items(content, phrase, quantity):
    def print_db():
        print(f'The {content.lower()} are: ')
        print('=' * 100)
        i = 1
        for item in data[content.title()]:
            print(f'{i}-{item}', end=', ')
            i += 1 #i = i + 1
        print()
        print('=' * 100, end='\n')
        print(f'Choose up to {quantity} {content.lower()}')

    def choice_item():
        choices = []
        for i in range(int(quantity)):
            choice = input(phrase)
            choices.append(choice)

        id = "".join(random.choices(string.ascii_letters + string.digits, k=4))
        dict = {}
        dict[id] = {}
        dict[id][content] = choices
        try:
            with open('db\\user_db.json', 'r+') as user_db:
                user_data = json.load(user_db)
                user_data.update(dict)
                user_db.seek(0)
                json.dump(user_data, user_db, indent=4)
        except FileNotFoundError:
            with open('db\\user_db.json', 'w') as user_db:
                json.dump(dict, user_db, indent=4)
        return choices

    if content == 'cocktails':
        print(phrase)
        print_db()
    else:
        print_db()
        choice_item()


option = input('''1-Voce gostaria de adicionar uma bebida ao app?
2-Voce gostaria de saber qual bebida voce gosta?\n''')

if option == '1':
    get_items('cocktails', "\nType the infos of your cocktails: ")

elif option == '2':
    quantity = input("\nHow many flavours you want to add? ")
    get_items('flavour', "\nWhat are the flavour you like on your cocktails? (Select a number) ", quantity)
    quantity = input("\nHow many types you want to add? ")
    get_items('types', "\nWhat types of cocktails do you enjoy? (Select a number) ", quantity)

#print(list(data['Flavour']))      #convert dict to list to get items






