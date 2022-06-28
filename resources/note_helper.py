import os
import json

class NoteHelper():
    # directory for notes (relative to appRoot)
    notesDir = 'my-notes/' # default

    # editor for editing notes
    userEditor = 'nano' # default

    # file format for notes
    notesFormat = '.md' # default
    
    # default content written into file when newly created
    defaultContent = '[//]: # "Feel free to use Markdown!"' # default

    # list of user's notes
    noteList = []

    # application's root path
    appRoot = []


    def __init__(self, appRoot) -> None:
        self.appRoot = appRoot

        if os.path.exists(self.appRoot + '/config.json'):
            with open(self.appRoot + '/config.json', 'r') as configFile:
                config = json.load(configFile)
    
                self.notesDir = config['notesDir']
                self.userEditor = config['userEditor']
                self.notesFormat = config['notesFormat']
                self.defaultContent = config['defaultContent']
    
        else:
            with open(self.appRoot + '/config.json', 'w') as configFile:
                config = {
                    "notesDir": self.appRoot + '/' + self.notesDir,
                    "userEditor": self.userEditor,
                    "notesFormat": self.notesFormat,
                    "defaultContent": self.defaultContent
                }

                json.dump(config, configFile)

        # fetch all notes (or create dir on first use)
        try:
            self.noteList = os.listdir(path=self.notesDir)
        except FileNotFoundError:
            self.noteList = []
            os.mkdir(self.notesDir)
        return
    
    def createNote(self):
        filename = input('Title: ') + self.notesFormat
    
        while self.noteList.count(filename) > 0:
            filename = input('Note already exists! Try different Title: ') + self.notesFormat
    
        os.system('echo \'' + self.defaultContent + '\' >> ' + self.notesDir + filename)
        os.system(self.userEditor + ' ' + self.notesDir + filename)
        return
    
    def openNote(self):
        if len(self.noteList) > 0:
            indexInput = input('Nr.: ')

            while not indexInput.isdigit() or indexInput.isdigit() and int(indexInput) > (len(self.noteList) - 1):
                indexInput = input('Invalid input! Nr.: ')

            os.system(self.userEditor + ' ' + self.notesDir + self.noteList[int(indexInput)])

        else:
            print('You have no notes yet!')
            input('press <return> to continue...')
        return
    
    def deleteNote(self):
        if len(self.noteList) > 0:
            indexInput = input('Nr.: ')

            while not indexInput.isdigit() or indexInput.isdigit() and int(indexInput) > (len(self.noteList) - 1):
                indexInput = input('Invalid input! Nr.: ')

            os.remove(self.notesDir + self.noteList[int(indexInput)])
        else:
            print('You have no notes yet!')
            input('press <return> to continue...')
        return

    def displayMenu(self):
        print('\nwhat can i do for you?')
        print('1 | new note \n2 | open note \n3 | delete note\n0 | quit\n')
        userChoice = input('Choice: ')
    
        if userChoice == '1':
            self.createNote()
            return
    
        elif userChoice == '2':
            self.openNote()
            return
    
        elif userChoice == '3':
            self.deleteNote()
            return
    
        elif userChoice == '0':
            exit(0)
    
        else:
            return
    
