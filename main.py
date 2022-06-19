import os

print('-----------------')
print('| pyPad - Notes |')
print('-----------------\n')

# functions
###########

def openNote(fileName):
    file = open(fileName, 'rw')
    return file

# main code
###########

# fetch all notes (or create dir on first use)
try:
    noteList = os.listdir(path='./my-notes')
except FileNotFoundError:
    noteList = []
    os.mkdir('./my-notes')

# print all notes
print('your current notes: \n')

if len(noteList) > 0:
    for item in noteList:
        print('- ' + item[0:item.find('.txt')])
else:
    print('- no notes yet -')
