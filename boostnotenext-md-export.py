#!/usr/bin/env python
import os
import sys
import json
import glob

usage = '''usage: boostnotnext-md-export storageFolder1 ... storageFolderN [OPTIONS]
options:
  -t,         include trash notes.
  -h --help,  show help.
'''

storageFolders = {arg for arg in sys.argv[1:] if arg[0] != '-'}

if not storageFolders or '-h' in sys.argv or '--help' in sys.argv:
    print(usage)
    sys.exit()

if '-t' in sys.argv:
    exportTrash = True
else:
    exportTrash = False


def getNoteData(path):
    with open(path, mode='r') as jsonFile:
        data = json.load(jsonFile)
    return data


def getPath(outFolder, noteData):
    path = noteData['folderPathname']
    if path != '/':
        path = path + '/'

    fileName = noteData['title'].strip()

    if not fileName:
        # title was left empty basically
        fileName = noteData['_id']
        print('Note with empty title found. Renaming as ' + outFolder + path + fileName + '.md')

    return outFolder + path + fileName + '.md'


def writeNote(noteData):
    with open(getPath(outFolder, noteData), "w") as file:
        file.write(noteData['content'])


for inFolder in storageFolders:
    outFolder = 'exported_' + inFolder

    notes = glob.glob(f'{inFolder}/notes/*.json')
    if not notes:
        print('Folder', inFolder, 'is not a storage Folder.')

    for note in notes:
        noteData = getNoteData(note)
        if not noteData['trashed'] or exportTrash:
            os.makedirs(outFolder + noteData['folderPathname'], exist_ok=True)
            writeNote(noteData)
