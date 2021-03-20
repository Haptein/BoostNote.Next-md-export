# BoostNote.Next-md-export
Script to export complete BoostnoteNext local storages at once.


```
usage:

python boostnotnext-md-export storageFolder1 ... storageFolderN [OPTIONS]
or (after chmod +x)
./boostnotnext-md-export storageFolder1 ... storageFolderN [OPTIONS]

options:
  -t,         include trash notes.
  -h --help,  show help.
```

The whole markdown directory is recreated, ready for Joplin's import or whatever.
Note: Attachments aren't really supported since I didn't use those, feel free to pr.