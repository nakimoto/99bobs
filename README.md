# 99 Bottles of Beer on the Wall!

### TABLE OF CONTENTS

* [Overview](#overview)
* [User Guide](#user-guide)
*  [The Ups](#the-ups)
*  [The Downs](#the-downs)
*  [Contact](#contact)

## Overview 
This project consisted of me writing a program that would print the lyrics to "99 Bottls of Beer on the Wall" to the console. I wrote my code in an IDE on my Macbook Pro. After finishing the code, I used my mac terminal (ssh client) to create a local GitHub repository on the command line. 
In order to create this repository, I utilized *git init* to initialize the repository, *git add* to add my files to the local repository, *git commit* to commit my files to my repository, and *git push* to push my files to the remote repository. 
A remote repository is created using *git remote add origin <repository url>* after creating matching reposiroty on GitHub's website. 
  
## User Guide
The code in the program "99bottles.py" is Python. In order to run this code on your computer, you need an IDE with Python installed, access to a command line/terminal, or you can run it on a Python interpreter for interactive Python. 

### Step One
  Download the .zip file from the repository homepage
### Step Two
  After the .zip file is downloaded, you can uncompress it to open it and access the files inside 
### Step Three 
  After opening, you will be able to access the "99bottles.py" program file. 
  If you have an IDE (such as Intellij IDEA, Eclipse, VSCode, etc.,) you can import the file to your IDE of choice and click compile and run. 
  If you are working on the command line you can place the program files somewhere easy to find (such as the desktop). In your terminal or command client, you should be able to type *python <your file>.py* to run the program/script. 
  
Alternatively, you can also clone the entire repository. This is especially great if you use something like GitKraken or GitHub Desktop.
 
  ** double check that your command client can run Python (by ensuring it's installed and checking version type) and make sure your command client's directory is the correct path to execute the program
  
For more advanced needs, please see the "99bobs.git" folder in the repository. This folder contains all of the commit data from using git init when I initially created the repository locally. You will be able to see changes, the commit log, configurations, and other information. There is also a section in that folder that includes a list of commands I used to create the local repository on my terminal. 
  
 ## The Ups 
The code for this project was very straightforward. The idea is to start with an intiialized variable that contains my 99 beer bottles, then I created a while loop in which executions of code can be made so long as there were at least (0) beer bottles on the wall. After each verse of the song, a new amount of beer bottles is required. In order to do this, you can subtract 1 from your intiial variable and set it to the original variable name. 
Please check out the documentation in the code and take a look to see the line by line comments. 

One important thing I leanred in this project is that GitHub stopped allowing use of developer passwords in order to use command client to push local repositories. According to documentation, this ended in 2021. Now, you must create an authenticated token to use as your password when working locally. 
I also learned that you have to unhide your .git files manually on your computer to have access to everything inside. In order for me to upload my .git files, I had to make them visible and move the contents to a separate folder. Sometimes this differs between operating systems. This is especially the case on MacOS that has a much bigger requirement for security which can allow you to run into permission issues. 
  
## The Downs
I ran into some issues with connecting my local repository to the on-site repository I greated on GitHub's website. I would get error messages stating that the remore repository was already created, but when I would commit and push it would tell me the repository doesn't exist. I found out this is due to me accidentally creating it in the wrong directory. I had a previous project file from a long time ago that interfered with me creating a new one in the same location. It was attempting to push to the wrong remote repository. 
  
# Contact
If you have any questions or need additional assitance, you may email me at nkimotou@gmail.com. 

  
  
  
