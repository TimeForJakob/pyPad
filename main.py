import os
import json

print('-----------------')
print('| pyPad - Notes |')
print('-----------------')

# constants
###########

# directory for notes
notesDir = '' # def: './my-notes/'

# editor for editing notes
userEditor = '' # def: 'nano'

# file format for notes
notesFormat = '' # def: '.md'

# default content written into file when newly created
defaultContent = '' # def: '[//]: # "Feel free to use Markdown!"'


# functions
###########
def setupConfig():
    # accessing global constants
    global notesDir
    global userEditor
    global notesFormat
    global defaultContent

    if os.path.exists('config.json'):
        with open('config.json', 'r') as configFile:
            config = json.load(configFile)

            notesDir = config['notesDir']
            userEditor = config['userEditor']
            notesFormat = config['notesFormat']
            defaultContent = config['defaultContent']

    else:
        with open('config.json', 'w') as configFile:
            config = {
                    "notesDir": "./my-notes/",
                    "userEditor": "nano",
                    "notesFormat": ".md",
                    "defaultContent": '[//]: # "Feel free to use Markdown!"'
                    }
            json.dump(config, configFile)
            
            notesDir = config['notesDir']
            userEditor = config['userEditor']
            notesFormat = config['notesFormat']
            defaultContent = config['defaultContent']

def displayMenu():
    print('\nwhat can i do for you?')
    print('1 | new note \n2 | open note \n3 | delete note\n0 | quit\n')
    userChoice = input('Choice: ')

    if userChoice == '1':
        filename = input('Title: ') + notesFormat

        while noteList.count(filename) > 0:
            filename = input('Note already exists! Try different Title: ') + notesFormat

        os.system('echo \'' + defaultContent + '\' >> ' + notesDir + filename)
        os.system(userEditor + ' ' + notesDir + filename)
        return

    elif userChoice == '2':
        if len(noteList) > 0:
            indexInput = input('Nr.: ')

            while not indexInput.isdigit() or indexInput.isdigit() and int(indexInput) > (len(noteList) - 1):
                indexInput = input('Invalid input! Nr.: ')

            os.system(userEditor + ' ' + notesDir + noteList[int(indexInput)])

        else:
            print('You have no notes yet!')
            input('press <return> to continue...')
        return

    elif userChoice == '3':
        if len(noteList) > 0:
            indexInput = input('Nr.: ')

            while not indexInput.isdigit() or indexInput.isdigit() and int(indexInput) > (len(noteList) - 1):
                indexInput = input('Invalid input! Nr.: ')

            os.remove(notesDir + noteList[int(indexInput)])
        else:
            print('You have no notes yet!')
            input('press <return> to continue...')
        return

    elif userChoice == '0':
        exit(0)

    else:
        return

# main
#######

# setup config
setupConfig()

# fetch all notes (or create dir on first use)
try:
    noteList = os.listdir(path=notesDir)
except FileNotFoundError:
    noteList = []
    os.mkdir(notesDir)

# repeat until user quits
while True:

    # print all notes
    print('\nyour current notes: ')
    print('-------------------')

    # print the note's names (or no notes message)
    if len(noteList) > 0:
        for i, noteItem in enumerate(noteList):
            print('[' + str(i) + '] ' + noteItem[0:noteItem.find(notesFormat)])
        print('-')
    else:
        print('   no notes yet   ')
        print('-')

    # spawn user interface
    displayMenu()

    # fetch noteList again after user interaction
    noteList = os.listdir(path=notesDir)
