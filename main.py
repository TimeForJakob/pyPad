import os
import json

print('-----------------')
print('| pyPad - Notes |')
print('-----------------\n')

# constants
###########

#notesDir = './my-notes/'  |
#userEditor = 'nano'       | possible customizations (+default values)
#notesFormat = '.md'       |

if os.path.exists('config.json'):
    with open('config.json', 'r') as configFile:
        config = json.load(configFile)

        notesDir = config['notesDir']
        userEditor = config['userEditor']
        notesFormat = config['notesFormat']
else:
    with open('config.json', 'w') as configFile:
            config = {
                    "notesDir": "./my-notes/",
                    "userEditor": "nano",
                    "notesFormat": ".md"
                    }
            json.dump(config, configFile)
            
            notesDir = config['notesDir']
            userEditor = config['userEditor']
            notesFormat = config['notesFormat']

# TODO: remove dev-prints
print('config values: ')
print(notesDir)
print(userEditor)
print(notesFormat)

# functions
###########
def displayMenu():
    print('\nWhat can i do for you?')
    print('1 | new note \n2 | open note \n3 | delete note\n0 | quit\n')
    userChoice = input('Choice: ')

    if userChoice == '1':
        filename = input('Title: ') + notesFormat

        while noteList.count(filename) > 0:
            filename = input('Note already exists! Try different Title: ') + notesFormat

        os.system(userEditor + ' ' + notesDir + filename)
        return

    elif userChoice == '2':
        filename = input('Name: ') + notesFormat
        while noteList.count(filename) == 0:
            filename = input('Note does not exist! Name: ') + notesFormat

        os.system(userEditor + ' ' + notesDir + filename)
        return
    elif userChoice == '3':
        filename = input('Name: ') + notesFormat
        while noteList.count(filename) == 0:
            filename = input('Note does not exist! Name: ') + notesFormat

        os.remove(notesDir + filename)
        return
    elif userChoice == '0':
        exit(0)
    else:
        return

# main
#######

# fetch all notes (or create dir on first use)
try:
    noteList = os.listdir(path=notesDir)
except FileNotFoundError:
    noteList = []
    os.mkdir(notesDir)

# repeat until user quits
while True:

    # print all notes
    print('-\nyour current notes: \n')

    # print the note's names (or no notes message)
    if len(noteList) > 0:
        for item in noteList:
            print('[] ' + item[0:item.find(notesFormat)])
        print('-')
    else:
        print('   no notes yet   ')
        print('-')

    # spawn user interface
    displayMenu()

    # fetch noteList again after user interaction
    noteList = os.listdir(path=notesDir)
