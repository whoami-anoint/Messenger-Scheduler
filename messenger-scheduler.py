import os
import time
import fbchat
from fbchat import Client
from fbchat.models import *
import threading
import sqlite3

# Create a new bot
bot = Client("<email>", "<password>")

# Connect to the database
conn = sqlite3.connect("scheduled_messages.db")
cursor = conn.cursor()

# Create the scheduled messages table if it doesn't exist
cursor.execute(
    "CREATE TABLE IF NOT EXISTS scheduled_messages (id INTEGER PRIMARY KEY, friend_id TEXT, message TEXT, scheduled_time REAL)"
)
conn.commit()

# Send a message to a friend at a scheduled time
def send_scheduled_message(friend_id, message, scheduled_time):
    while True:
        current_time = time.time()
        if current_time >= scheduled_time:
            bot.send(Message(text=message), thread_id=friend_id, thread_type=ThreadType.USER)
            break
        else:
            time.sleep(1)

# Schedule a message to be sent at a later time
def schedule_message(friend_id, message, scheduled_time):
    cursor.execute(
        "INSERT INTO scheduled_messages (friend_id, message, scheduled_time) VALUES (?, ?, ?)",
        (friend_id, message, scheduled_time)
    )
    conn.commit()
    print("Message scheduled for delivery at " + str(scheduled_time))

# Get input from the user
def get_input():
    message = input("Enter a message to send: ")
    scheduled_time = float(input("Enter the scheduled time (in Unix time): "))
    friend_id = input("Enter the ID of the friend to send the message to: ")
    return (friend_id, message, scheduled_time)

# Display a menu of options
def display_menu():
    print("1. Send a scheduled message")
    print("2. Schedule a message for later delivery")
    print("3. View a list of scheduled messages")
    print("4. Cancel a scheduled message")
    print("5. Send a message to all friends")
    print("6. View a list of friends")
    print("7. Quit")

# Send a message to all friends
def send_message_to_all_friends(message):
    friends = bot.fetchAllUsers()
    for friend in friends:
        bot.send(Message(text=message), thread_id=friend.uid, thread_type=ThreadType.USER)

# View a list of friends
def view_friend_list():
    friends = bot.fetchAllUsers()
    for friend in friends:
        print(friend.name + " (" + friend.uid + ")")

# View a list of scheduled messages
def view_scheduled_messages():
    cursor.execute("SELECT * FROM scheduled_messages")
    rows = cursor.fetchall()
    for row in rows:
        id = row[0]
        friend_id = row[1]
        message = row[2]
        scheduled_time = row[3]
        print("ID: " + str(id))
        print("Friend ID: " + friend_id)
        print("Message: " + message)
        print("Scheduled Time: " + str(scheduled_time))
        print("---")
        
 # Cancel a scheduled message
def cancel_scheduled_message(message_id):
    cursor.execute("DELETE FROM scheduled_messages WHERE id=?", (message_id,))
    conn.commit()
    print("Scheduled message with ID " + str(message_id) + " cancelled.")

# Main function
def main():
    while True:
        display_menu()
        choice = int(input("Enter a choice: "))
        if choice == 1:
            (friend_id, message, scheduled_time) = get_input()
            send_scheduled_message(friend_id, message, scheduled_time)
        elif choice == 2:
            (friend_id, message, scheduled_time) = get_input()
            schedule_message(friend_id, message, scheduled_time)
        elif choice == 3:
            view_scheduled_messages()
        elif choice == 4:
            message_id = int(input("Enter the ID of the scheduled message to cancel: "))
            cancel_scheduled_message(message_id)
        elif choice == 5:
            message = input("Enter a message to send to all friends: ")
            send_message_to_all_friends(message)
        elif choice == 6:
            view_friend_list()
        elif choice == 7:
            break

# Run the main function
if __name__ == "__main__":
    main()
