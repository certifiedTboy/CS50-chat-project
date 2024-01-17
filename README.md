# CS50 CHAT

#### Video Demo: <a href="https://drive.google.com/file/d/1A-Ce75Kr73Px27p60mNLGdhzryLswjNp/view?usp=sharing">Video Demo</a>

##### Description: A simple chat application built with python Flask framework and Flask-socket.io library

##### Live Demo: <a href="https://cs50-chat-project.onrender.com">Live Demo</a>

<div align="center" id="top"> 
 
  &#xa0;

</div>

<h1 align="center"> CS50 chat (Final project)</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/certifiedTboy/CS50-chat-project?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/certifiedTboy/CS50-chat-project?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/certifiedTboy/CS50-chat-project?color=56BEB8">

</p>

- [Introduction](#Introduction)
- [Technologies](#Technologies)
- [Get Started](#Get-Started)
- [Usage and Functionality](#)

<br>

## Introduction

This is a simple chat aplication built for the CS50x final project with python flask and flasksocketio

## Technologies

The following technologies were used:

- [Python](#Node)
- [Python Flask Framework](#Flask)
- [Flask SocketIo](#)
- [Flask Jinja](#)

## Directory Hierarchy

```
|—— main.py
|—— requirements.txt
|—— static
|    |—— css
|        |—— style.css
|—— templates
|    |—— base.html
|    |—— index.html
|    |—— room.html
```

### Tested Platform

- software
  ```
  OS: Debian unstable (May 2021), Ubuntu LTS
  Python: 3.8.5 (anaconda)
  PyTorch: 1.7.1, 1.8.1
  ```

## Get-Started

```bash
# Clone this project
$ git clone https://github.com/certifiedTboy/CS50-chat-project

# Access
$ cd CS50-chat-project

# Install dependencies
$ pip install -r requirements.txt

# Run the project
$ python main.py (Production server)
$ python main.py (Development server)

# The server will initialize in the http://127.0.0.1:8080
# view on cross-platform on  http://192.168.121.92:8080
# view live production demo on https://cs50-chat-project.onrender.com
```

## Usage and Functionalities

### Backend Logic

The chat application is built using Flask as a web framework and SocketIO for real time communication

The main application logic is contained in the main.py file which is located in the root folder of the application.

The application utlizes session for temporary storage of user information such as the username

On the home page of the application, a user has to choose a unique username of not more than 10 characters and a particular room he or she wants to join.

There are 3 basic rooms made available to avoid complexity.

A room can only accept 10 users at a time. And users are not permitted to use same username in a particular room

### User Interface

A simple HTML template engine called Jinja2 is used to generate dynamic contents.

The user interface is devided into 3 files. With the base.html serving as the main file holding all meta data and semantic structure of the page.

The index.html file is the home page of the application which is where users can choose their unique username and the room they wish to join

An error message is printed on the home page if at all the user is doing anything wrongly or there is a server related error. This error is returned from the root route of the application which is incharge of rendering the home page of the application.

The real chat on the application occurs in the room.html page. The file also contains the javascript logic that handles the DOM manipulation of the page and implementation of Socket.io implementation.

### Future Improvement and Integration.

As it stands currently, the application doesn't really do much than just seding instant messages in a general group.

More improvements that can be done on the application includes

- Integration of a profanity filter that blocks any form of hate speech or vulgar statement against users
- Integration of a private chat functionality where users can send direct messages other than the general group chat
- Users can also have a proper profile picture and profile information to share more information about who they are
- Integration of AI functionality to make conversations more interactive and worthwhile
- Integration of proper authentication system and process in order to ensure person using the platforms are real humans and also to ensure security and safety of other users.
- Integration of database storage to ensure data security, accuracy and persistency.

<a href="#top">Back to top</a>
