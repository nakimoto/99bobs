# 99 Bottles of Beer on the Wall!

### TABLE OF CONTENTS

* [Overview](#overview)
* [User Guide](#user-guide)
* [The Ups](#the-ups)
* [The Downs](#the-downs)
* [Contact](#contact)
* [User Dialogue](#user-dialogue)

## Overview 
This project consisted of me writing a program that would print the lyrics to "99 Bottles of Beer on the Wall" to the console. I wrote my code in an IDE on my Macbook Pro. After finishing the code, I used my mac terminal (ssh client) to create a local GitHub repository on the command line. 
In order to create this repository, I utilized *git init* to initialize the repository, *git add* to add my files to the local repository, *git commit* to commit my files to my repository, and *git push* to push my files to the remote repository. 
A remote repository is created using *git remote add origin <repository url>* after creating a matching repository on GitHub's website. 
  
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
 
  **double check that your command client can run Python (by ensuring it's installed and checking version type) and make sure your command client's directory is the correct path to execute the program**

In the top level directory of this repository, you will find the README.md (what you're currently reading), the 99bottles.py file, a 99bobs.git folder and the commands.txt that includes a list of commands I used to create the local repository on my terminal. 
For more advanced needs, please see the "99bobs.git" folder in the repository. This folder contains all of the commit data from using git init when I initially created the repository locally. You will be able to see changes, the commit log, configurations, and other information. 
  
 ## The Ups 
The code for this project was very straightforward. The idea is to start with an initialized variable that contains my 99 beer bottles, then I created a while loop in which executions of code can be made so long as there were at least (0) beer bottles on the wall. After each verse of the song, a new amount of beer bottles is required. In order to do this, you can subtract 1 from your initial variable and set it to the original variable name. 
Please check out the documentation in the code and take a look to see the line by line comments. 

One important thing I learned in this project is that GitHub stopped allowing use of developer passwords in order to use command clients to push local repositories. According to documentation, this ended in 2021. Now, you must create an authenticated token to use as your password when working locally. 
I also learned that you have to unhide your .git files manually on your computer to have access to everything inside. In order for me to upload my .git files, I had to make them visible and move the contents to a separate folder. Sometimes this differs between operating systems. This is especially the case on MacOS that has a much bigger requirement for security which can allow you to run into permission issues. 
  
## The Downs
I ran into some issues with connecting my local repository to the on-site repository I created on GitHub's website. I would get error messages stating that the remote repository was already created, but when I would commit and push it would tell me the repository doesn't exist. I found out this is due to me accidentally creating it in the wrong directory. I had a previous project file from a long time ago that interfered with me creating a new one in the same location. It was attempting to push to the wrong remote repository. 
  
## Contact
If you have any questions or need additional assistance, you may email me at nkimotou@gmail.com. 
  
# User Dialogue
## This section of the README is dedicated to customer dialogue as part of the Technical Support Engineer role. 

In this scenario, a user reaches out to the Technical Support team with an issue regarding inability to reach The Mom Project website. 

**User**: Hi Nanami, I have been trying to access The Mom Project website all morning! None of the images load and sometimes I get an error message. I can't log in either. Can you help? 
  
**Technical Support Engineer Nanami**: Hi User, I'll be happy to help you with this issue. Wha sort of device are you using? Is it a desktop computer, laptop, tablet, or smartphone? 
  
**User**: I'm using a smartphone.
  
**Technical Support Engineer Nanami**: What sort of browser are you using? Are you using Safari, Chrome, Firefox, or a different browser? 
  
**User**: I'm using Safari on my iPhone. I tried using Chrome and got the same issue. However, my coworker was able to login from his computer in his home. 
  
**NOTE: Since the coworker is able to access the website and log in, Nanami navigates to the site to check that she can see the website and login. After confirming that the site isn't down, Nanami believes this is a user specific issue. Since the user tried a different browser with the same issue, she can conclude that the issue isn't in the user's cache or cookies for safari, but instead may be a Wi-Fi issue. Nanami presses further about the error message.**

**Technical Support Engineer Nanami**: You mentioned seeing an error message before, do you remember what the error message said? 

**User**: The error said it couldn't connect to the server. 
 
**Technical Support Engineer Nanami**: Can you check your internet connectivity on your iPhone? If you go into settings you will see Wi-Fi. Click that option and check that you are connected to your local Wi-Fi. Otherwise, check if you are connected to your mobile data service provided by your mobile carrier. 
  
**User**: I have checked my Wi-Fi, the connection is on but the strength is very weak! What can be done? 

**Technical Support Engineer Nanami**: We can reset your internet modem and Wi-Fi router to see if that fixes the connectivity issue. Go to the room where both devices are located. Unplug them for five minutes, then plug them back in and allow a few minutes for connectivity to be restored. 
  
**NOTE: Ten minutes have passed.**

**User**: Hi Nanami, my Wi-Fi connectivity is restored and I am able to browse The Mom Project website and login now! Thank you for your help. 
  
**Technical Support Engineer Nanami**: Hi User, I'm happy to hear the issue was resolved. Please reach out if you have any additional questions or concerns. 
  
  
 **NOTE: In this situation, I'm able to ask a series of questions to figure out that this is more of a hardware issue on the user's end instead of a software issue on our end. Asking these questions allows me to reduce the amount of time I will spend figuring out a solution and helps the user get back to their daily life a lot quicker. In the event that this was a login issue that occured with several users on different networks, that would tell me it is an issue on our (The Mom Project) end. We would then initiate a routine for figuring out if our website is down, which aspects are down, how long has it been down, why it is down, how fast can we figure out a solution, etc.**
  


  
