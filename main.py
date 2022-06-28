import os
import resources

print('-----------------')
print('| pyPad - Notes |')
print('-----------------')

# main
#######

# init NoteHelper lib
noteHelper = resources.NoteHelper(os.path.dirname(__file__))

# repeat until user quits
while True:

    # print all notes
    print('\nyour current notes: ')
    print('-------------------')

    # print the note's names (or no notes message)
    if len(noteHelper.noteList) > 0:
        for i, noteItem in enumerate(noteHelper.noteList):
            print('[' + str(i) + '] ' + noteItem[0:noteItem.find(noteHelper.notesFormat)])
        print('-')
    else:
        print('   no notes yet   ')
        print('-')

    # spawn user interface
    noteHelper.displayMenu()

    # fetch noteList again after user interaction
    noteHelper.noteList = os.listdir(path=noteHelper.notesDir)
