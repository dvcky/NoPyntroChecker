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
Python 3+ and your choice of game files. That's it. Just make sure the game file you are checking is for a console that has been indexed by No-Intro (list of supported consoles here).
## Installation
To be finished
