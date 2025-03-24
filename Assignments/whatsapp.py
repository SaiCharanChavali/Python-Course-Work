num_messages = int(input("Enter the number of messages: "))

chat_data = []
users = set()
user_msg_count = {}

print("\nEnter messages in 'User: Message' format:")
for i in range(num_messages):
    message = input()
    chat_data.append(message)
    user = message.split(":")[0]
    users.add(user)
    user_msg_count[user] = user_msg_count.get(user, 0) + 1

print("\nChoose an option:")
print("1. Total messages")
print("2. Unique users")
print("3. Total words")
print("4. Average words per message")
print("5. Longest message")
print("6. Most active user")
print("7. Message count for a user")
print("8. Most frequent word by a user")
print("9. First and last message of a user")
print("10. Check if user is in chat")
print("11. Common repeated words")
print("12. Messages containing a keyword")
print("13. User with longest average message length")
print("14. Count messages mentioning a user")
print("15. First and last message in chat")
print("16. Remove duplicate messages")
print("17. Commonly used phrases")
print("18. Sort messages alphabetically")
print("19. Display messages in reverse")
print("20. Messages containing emojis")
print("21. Most frequently used word in chat")
print("22. All questions asked")
print("23. Reply ratio between two users")
print("24. Count deleted messages")
print("25. Messages sent after a keyword")
print("26. Exit")

while True:
    choice = int(input("\nEnter choice (1-26): "))

    if choice == 1:
        print("Total messages:", len(chat_data))

    elif choice == 2:
        print("Unique users:", users)

    elif choice == 3:
        total_words = sum(len(msg.split()) for msg in chat_data)
        print("Total words:", total_words)

    elif choice == 4:
        total_words = sum(len(msg.split()) for msg in chat_data)
        avg_words = total_words / len(chat_data) if chat_data else 0
        print("Average words per message:", avg_words)

    elif choice == 5:
        longest_msg = max(chat_data, key=len)
        print("Longest message:", longest_msg)

    elif choice == 6:
        most_active = max(user_msg_count, key=user_msg_count.get)
        print("Most active user:", most_active)

    elif choice == 7:
        name = input("Enter user name: ")
        print(f"{name} sent {user_msg_count.get(name, 0)} messages")

    elif choice == 8:
        name = input("Enter user name: ")
        words = {}
        for msg in chat_data:
            if msg.startswith(name + ":"):
                for word in msg.split():
                    words[word] = words.get(word, 0) + 1
        if words:
            most_common = max(words, key=words.get)
            print(f"Most used word by {name}: {most_common}")
        else:
            print(f"No messages from {name}")

    elif choice == 9:
        name = input("Enter user name: ")
        user_msgs = [msg for msg in chat_data if msg.startswith(name + ":")]
        if user_msgs:
            print("First message:", user_msgs[0])
            print("Last message:", user_msgs[-1])
        else:
            print(f"{name} has not sent any messages.")

    elif choice == 10:
        name = input("Enter user name: ")
        print(f"{name} is {'in' if name in users else 'not in'} the chat")

    elif choice == 11:
        word_count = {}
        for msg in chat_data:
            for word in msg.split():
                word_count[word] = word_count.get(word, 0) + 1
        common_words = [word for word, count in word_count.items() if count > 1]
        print("Common repeated words:", set(common_words))

    elif choice == 12:
        keyword = input("Enter keyword: ")
        matches = [msg for msg in chat_data if keyword in msg]
        print("Messages containing keyword:", matches)

    elif choice == 13:
        avg_length = {user: sum(len(msg) for msg in chat_data if msg.startswith(user + ":")) / user_msg_count[user] for user in users}
        longest_avg_user = max(avg_length, key=avg_length.get)
        print("User with longest average message:", longest_avg_user)

    elif choice == 14:
        name = input("Enter user name: ")
        count = sum(1 for msg in chat_data if name in msg)
        print(f"{name} was mentioned in {count} messages")

    elif choice == 15:
        print("First message:", chat_data[0])
        print("Last message:", chat_data[-1])

    elif choice == 16:
        print("Unique messages:", set(chat_data))

    elif choice == 17:
        print("Feature not implemented in simple version")

    elif choice == 18:
        print("Messages sorted alphabetically:")
        print(sorted(chat_data))

    elif choice == 19:
        print("Messages in reverse order:")
        print(chat_data[::-1])

    elif choice == 20:
        emojis = ["😀", "😂", "😍", "😢", "👍", "🙏"]
        emoji_messages = [msg for msg in chat_data if any(emoji in msg for emoji in emojis)]
        print("Messages containing emojis:", emoji_messages)

    elif choice == 21:
        word_count = {}
        for msg in chat_data:
            for word in msg.split():
                word_count[word] = word_count.get(word, 0) + 1
        most_frequent_word = max(word_count, key=word_count.get)
        print("Most frequently used word:", most_frequent_word)

    elif choice == 22:
        questions = [msg for msg in chat_data if "?" in msg]
        print("Questions asked in chat:", questions)

    elif choice == 23:
        print("Feature not implemented in simple version")

    elif choice == 24:
        count = sum(1 for msg in chat_data if "This message was deleted" in msg)
        print(f"Deleted messages count: {count}")

    elif choice == 25:
        keyword = input("Enter keyword: ")
        if keyword in " ".join(chat_data):
            index = next((i for i, msg in enumerate(chat_data) if keyword in msg), None)
            print("Messages after keyword:", chat_data[index+1:])
        else:
            print("Keyword not found in chat")

    elif choice == 26:
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Enter a number between 1-26.")
