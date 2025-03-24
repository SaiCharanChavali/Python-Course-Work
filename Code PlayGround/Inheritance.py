import tkinter as tk
from tkinter import messagebox

#Base Class - Instagram Story
class InstagramStory:
    def __init__(self, user):
        self.user = user
        self.story_content = ""

    def post_story(self, content):
        self.story_content = content
        return f"{self.user} posted a story: {content}"

#Single Inheritance - Adds Like Feature

class StoryWithLikes(InstagramStory):
    def __init__(self, user):
        super().__init__(user)
        self.likes = 0

    def like_story(self):
        self.likes += 1
        return f"Story liked! Total likes: {self.likes}"

#Single Inheritance - Adds Comments Feature separately
class StoryWithComments(InstagramStory):
    def __init__(self, user):
        super().__init__(user)
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)
        return f"New comment added: {comment}"

#Hierarchical Inheritance - Adds Reaction Feature
class StoryWithReactions(InstagramStory):
    def __init__(self, user):
        super().__init__(user)
        self.reactions = {"😂": 0, "❤": 0, "🔥": 0}

    def react_to_story(self, reaction):
        if reaction in self.reactions:
            self.reactions[reaction] += 1
            return f"Reaction {reaction} added! Total: {self.reactions[reaction]}"
        else:
            return "Invalid reaction!"

#Multiple Inheritance - Combines Likes, Comments, Reactions + Close Friends Feature
class StoryWithCloseFriends(StoryWithLikes, StoryWithComments, StoryWithReactions):
    def __init__(self, user):
        StoryWithLikes.__init__(self, user)  
        StoryWithComments.__init__(self, user)
        StoryWithReactions.__init__(self, user)
        self.close_friends_only = False

    def set_close_friends(self, status):
        self.close_friends_only = status
        mode = "Close Friends" if status else "Public"
        return f"Story visibility set to: {mode}"

#Tkinter UI Setup
root = tk.Tk()
root.title("Instagram Story Simulator")
root.geometry("400x500")
root.configure(bg="#f4f4f4")

# User Object
story = StoryWithCloseFriends("Alice")

#UI Functions
def post_story():
    content = entry_story.get()
    if content.strip():
        result_label.config(text=story.post_story(content))
    else:
        messagebox.showwarning("Warning", "Story content cannot be empty!")

def like_story():
    result_label.config(text=story.like_story())

def add_comment():
    comment = entry_comment.get()
    if comment.strip():
        result_label.config(text=story.add_comment(comment))
    else:
        messagebox.showwarning("Warning", "Comment cannot be empty!")

def toggle_close_friends():
    status = close_friends_var.get()
    result_label.config(text=story.set_close_friends(status))

def react_story(reaction):
    result_label.config(text=story.react_to_story(reaction))

#UI Elements
tk.Label(root, text="Post a Story:", bg="#f4f4f4", font=("Arial", 12)).pack(pady=5)
entry_story = tk.Entry(root, width=40)
entry_story.pack(pady=5)
tk.Button(root, text="Post", command=post_story, bg="#0078D7", fg="white", font=("Arial", 10)).pack(pady=5)

tk.Button(root, text="👍 Like Story", command=like_story, bg="#ffcc00", font=("Arial", 10)).pack(pady=5)

tk.Label(root, text="Add a Comment:", bg="#f4f4f4", font=("Arial", 12)).pack(pady=5)
entry_comment = tk.Entry(root, width=40)
entry_comment.pack(pady=5)
tk.Button(root, text="Comment", command=add_comment, bg="#00cc66", fg="white", font=("Arial", 10)).pack(pady=5)

#Close Friends Toggle
close_friends_var = tk.BooleanVar()
tk.Checkbutton(root, text="Close Friends Only", variable=close_friends_var, command=toggle_close_friends, bg="#f4f4f4", font=("Arial", 10)).pack(pady=5)

#Reactions Buttons
reaction_frame = tk.Frame(root, bg="#f4f4f4")
reaction_frame.pack(pady=10)
tk.Label(root, text="React to Story:", bg="#f4f4f4", font=("Arial", 12)).pack()
tk.Button(reaction_frame, text="😂", command=lambda: react_story("😂"), font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
tk.Button(reaction_frame, text="❤", command=lambda: react_story("❤"), font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
tk.Button(reaction_frame, text="🔥", command=lambda: react_story("🔥"), font=("Arial", 12)).pack(side=tk.LEFT, padx=5)

#Result Label
result_label = tk.Label(root, text="", bg="#f4f4f4", fg="black", font=("Arial", 12))
result_label.pack(pady=10)

# Run the Tkinter Loop
root.mainloop()
