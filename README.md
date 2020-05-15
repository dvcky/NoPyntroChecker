# NoPyntroChecker
A small python script used for verifying the contents of a game file using the No-Intro database.
## Why is this needed?
No-Intro's testimony explains it pretty well [here](https://no-intro.org/).

**TL;DR:** Preservation is important, and it is very common to see ROM dumps that are tampered with for various reasons. This script makes checking your ROM dumps easy and encourages people to keep the "perfect dumps" around longer.
## How does it work?
After prompting you to input a game file, this script utilizes python's hashlib and request libraries and does the following:
1. Generates an MD5 hash from the file.
2. Sends a POST request to the No-Intro database with the generated hash.
3. Analyzes data received from request for any game titles.
4. Returns results based on analysis.
## Requirements
Python 3+, an active internet connection, and your choice of game files. That's it. Just make sure the game file you are checking is for a console that has been indexed by No-Intro (list of supported consoles in the drop-down shown below [here](https://datomatic.no-intro.org/)).

![alt text](https://raw.githubusercontent.com/dduckyy/NoPyntroChecker/master/nopyntrochecker.png)
## Usage
Pretty simple, just download the NoPyntroChecker repository [here](https://github.com/dduckyy/NoPyntroChecker/archive/master.zip) and extract the "nopyntrochecker.py" file from the repository's zip file to your preferred location. As long as you have Python installed, you should be able to run it directly. The script should immediately prompt you to choose a game file/ROM dump you want to have checked with No-Intro's database. Select your file, and watch the magic happen!
