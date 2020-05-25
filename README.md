# NoPyntroChecker
A small python script used for verifying the contents of a game file using the No-Intro database.
## Why is this needed?
No-Intro's testimony explains it pretty well [here](https://no-intro.org/).

**TL;DR:** Preservation is important, and it is very common to see ROM dumps that are tampered with for various reasons. This script makes checking your ROM dumps easy and encourages people to search for those "perfect dumps".
## How does it work?
After you select a game file/enter your game file's filepath, this script utilizes python's hashlib and request libraries and does the following:
1. Generates an MD5 hash from the file.
2. Sends a POST request to the No-Intro database with the generated hash.
3. Analyzes data received from request for any game titles.
4. Returns results based on analysis.
## Requirements
Python 3+, an active internet connection, and your choice of game files. That's it. Just make sure the game file you are checking is for a console that has been indexed by No-Intro (list of supported consoles in the drop-down shown below [here](https://datomatic.no-intro.org/)).

![nopyntrochecker](https://raw.githubusercontent.com/dvcky/NoPyntroChecker/master/nopyntrochecker.png)
## Usage
Pretty simple, just download the NoPyntroChecker repository [here](https://github.com/dduckyy/NoPyntroChecker/archive/master.zip) and extract the "nopyntrochecker.py" file from the repository's zip file to your preferred location. As long as you have Python installed, you should be able to run it from your terminal. Usage below: 
```
py nopyntrochecker.py /path/to/file/filename.filetype
```
Once you press enter, the script will check to make sure you only added 1 argument, and then make sure your file actually exists. If those requirements are met, the script will run as described in ["How does it work?"](#how-does-it-work).
**KEEP IN MIND:** This script does not know what files are ROMs and what are not. If you put in a file that isn't a ROM, it will still try to check it (which will most likely return no matches for obvious reasons).
