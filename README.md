# NoPyntroChecker
A small python script used for verifying the contents of a game file using the No-Intro database.
## Why is this needed?
No-Intro's testimony explains it pretty well [here](https://no-intro.org/).

**TL;DR:** Preservation is important, and it is very common to see ROM dumps that are tampered with for various reasons. This script makes checking your ROM dumps easy and encourages people to search for those "original/unmodified dumps".
## How does it work?
Once you run the script, it does the following below:
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

**KEEP IN MIND:** This script does not know which files are ROMs and which are not. If you input a file that isn't a ROM, it will still try to check it (which will most likely return no matches, for obvious reasons).

## FAQ
#### "I have a ROM that runs on my console/emulator fine with no issues, and your script said no matches!"
And that is most likely the releaser's intent. Groups that release ROM dumps often look for less noticable things they can take out of/add to ROMs, whether that be to conserve space or "enhance the user's experience" in some form. **CLARIFICATION: This program is _NOT_ meant for verifying that your ROM is real, but rather that it is the original/unmodified dump.**
#### "I am confident that my ROM is unmodified, but your script still said no matches!"
Aw shucks. Most likely one of two things happened:
1. You were checking a lot of files at once, and you got a temp-ban. This is because sending lots of POST requests to No-Intro's database will cause it to think you are spamming or trying to DDOS them. No worries! These bans are usually over within a couple hours, and you can go right back to checking your dumps! If you are really impatient, you can also use a VPN or proxy and check them on that connection until you are unbanned.
2. No-Intro's database API is changed or updated. The site has stayed pretty consistent on how it functioned for years, but this is bound to potentially happen at one point or another. If it does happen, it will make the script completely unusable until updated. This is sadly not something I can avoid.
