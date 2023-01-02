# Messenger Scheduler

A bot that allows you to schedule messages to be sent on Messenger at a later time, as well as providing other functionality such as sending messages to all friends, viewing a list of friends, and canceling scheduled messages.

## Requirements

- A Facebook account and a Facebook Page
- A Facebook App and a Messenger product set up on the Facebook Developer Platform
- A webhook URL to receive and process messages from users
- The `fbchat` and `sqlite3` Python libraries

## Installation

1. Clone the repository to your local machine
2. Install the required libraries by running the following command:
```
pip install fbchat sqlite3
```

3. Set up your Facebook App and Messenger product on the Facebook Developer Platform, and set up a webhook to receive and process messages from users
4. Create a `secrets.py` file in the root directory of the project and add the following variables:
```
EMAIL = "<your email>"
PASSWORD = "<your password>"
APP_ID = "<your app id>"
APP_SECRET = "<your app secret>"
PAGE_ID = "<your page id>"
VERIFY_TOKEN = "<your verify token>"
```

5. Run the `messenger-scheduler.py` file to start the bot
```
python app.py
```

## Usage

1. Send a scheduled message: enter the message, scheduled time (in Unix time), and the ID of the friend to send the message to.
2. Schedule a message for later delivery: enter the message, scheduled time (in Unix time), and the ID of the friend to send the message to. The message will be stored in the database and delivered at the specified time.
3. View a list of scheduled messages: view a list of all scheduled messages, including the ID, friend ID, message, and scheduled time.
4. Cancel a scheduled message: enter the ID of the scheduled message to cancel.
5. Send a message to all friends: enter a message to send to all of your friends on Messenger.
6. View a list of friends: view a list of all of your friends on Messenger, including their name and ID.
7. Quit: exit the program.

## Credits

- [fbchat](https://github.com/carpedm20/fbchat) - A library for interacting with the Facebook Messenger API in Python
- [sqlite3](https://docs.python.org/3/library/sqlite3.html) - A built-in library for working with SQLite databases in Python
