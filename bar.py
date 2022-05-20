import json, random, string

class Bar():
    def __init__(self, content, phrase, id, quantity=None):
        with open('db\\db.json', 'r') as db:
            self.data = json.load(db)
        self.content = content
        self.phrase = phrase
        self.quantity = quantity
        self.id = id


    def get_items(self):
        def print_db():
            print(f'The {self.content.lower()} are: ')
            print('=' * 100)
            i = 1
            for item in self.data[self.content.title()]:
                print(f'{i}-{item}', end=', ')
                i += 1 #i = i + 1
            print()
            print('=' * 100, end='\n')
            print(f'Choose up to {self.quantity} {self.content.lower()}')

        def choice_item():
            choices = []
            for i in range(int(self.quantity)):
                choice = input(self.phrase)
                choices.append(choice)

            dict = {}
            dict[self.id] = {}
            dict[self.id][self.content] = choices
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

        if self.content == 'cocktails':
            self.cocktails_db = {}
            print(self.phrase)
            i = 1
            for item in self.data[self.content.title()]:
                if item == 'Name':
                    self.name = input(f'{i}-{item}: ')
                    self.cocktails_db[self.name] = {}
                    self.cocktails_db[self.name]['Flavours'] = []
                    self.cocktails_db[self.name]['Types'] = []
                    self.cocktails_db[self.name]['Ingredients'] = []
                    self.cocktails_db[self.name]['Glass'] = []
                else:
                #elif item == 'Flavour':
                    x = 1
                    print('\n')
                    for sub_item in self.data[item]:
                        print(f'{x}-{sub_item}', end=', ')
                        x += 1
                    quantity = input("How many you want to add? ")
                    for option in range(int(quantity)):
                        self.cocktails_db[self.name][item].append(input(f'{i}-{item}: '))

                        #user_flavour = input("Choose a flavour: ")
                        #self.cocktails_db[self.name]['Flavours'].append(user_flavour)
                    try:
                        with open('db\\user_db.json', 'r+') as user_db:
                            user_data = json.load(user_db)
                            user_data.update(self.cocktails_db)
                            user_db.seek(0)
                            json.dump(user_data, user_db, indent=4)
                    except FileNotFoundError:
                            with open('db\\user_db.json', 'w') as user_db:
                                json.dump(self.cocktails_db, user_db, indent=2)

                i += 1 
        else:
            print_db()
            choice_item()



option = input('''1-Voce gostaria de adicionar uma bebida ao app?
2-Voce gostaria de saber qual bebida voce gosta?\n''')

if option == '1':
    Bar("cocktails", "\nType the infos of your cocktails: ", None).get_items()

elif option == '2':
    id = "".join(random.choices(string.ascii_letters + string.digits, k=4))
    quantity = input("\nHow many flavours you want to add? ")
    Bar('flavours', "\nWhat are the flavour you like on your cocktails? (Select a number) ", id, quantity).get_items()
    quantity = input("\nHow many types you want to add? ")
    Bar('types', "\nWhat types of cocktails do you enjoy? (Select a number) ", id, quantity).get_items()

#print(list(data['Flavour']))      #convert dict to list to get items






