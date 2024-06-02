from tkinter import *  # Importing Tkinter library for GUI elements
from chat import get_response, bot_name  # Importing chatbot response function and bot name

# Setting up GUI colors and fonts
BG_COLOR = "#1A1A1A"
TEXT_COLOR = "#FFFFFF"
FONT = "Arial 12"
FONT_BOLD = "Arial 12 bold"

class NBAChatApplication:
    # Initializing the main application class
    def __init__(self):
        self.window = Tk()  # Creating the main window
        self._setup_main_window()  # Setting up the main window layout

    def run(self):
        self.window.mainloop()  # Running the main event loop

    def _setup_main_window(self):
        # Setting up the main window properties
        self.window.title("NBA Chatbot")  # Setting the window title
        self.window.resizable(width=True, height=True)  # Allowing the window to be resizable
        self.window.configure(width=470, height=550, bg=BG_COLOR)  # Configuring window size and background color

        # Creating the head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="NBA 2021-2022 InfoBot", font=("Arial", 20, "bold"), pady=10)
        head_label.place(relwidth=1)  # Placing the head label at the top

        # Creating a divider line
        line = Label(self.window, width=450, bg=TEXT_COLOR)
        line.place(relwidth=1, rely=0.07, relheight=0.012)  # Placing the divider line below the head label

        # Setting up the text widget for chat display
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)  # Placing the text widget
        self.text_widget.configure(cursor="arrow", state=DISABLED)  # Disabling the text widget for direct input

        # Creating the bottom label for user input area
        bottom_label = Label(self.window, bg=BG_COLOR, height=80)
        bottom_label.place(relwidth=1, rely=0.825)  # Placing the bottom label

        # Creating the message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)  # Placing the entry box
        self.msg_entry.focus()  # Setting focus to the entry box
        self.msg_entry.bind("<Return>", self._on_enter_pressed)  # Binding the Enter key to message sending

        # Creating the send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=TEXT_COLOR, fg=BG_COLOR,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)  # Placing the send button

    def _on_enter_pressed(self, event):
        # Handling the event when the Enter key is pressed
        msg = self.msg_entry.get()  # Getting the message from the entry box
        self._insert_message(msg, "You")  # Inserting the message into the chat

    def _insert_message(self, msg, sender):
        # Inserting the user and bot messages into the chat window
        if not msg:
            return  # If the message is empty, return

        self.msg_entry.delete(0, END)  # Clearing the entry box
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)  # Enabling the text widget for editing
        self.text_widget.insert(END, msg1)  # Inserting the user's message

        # Getting the response from the chatbot
        bot_response = get_response(msg)

        msg2 = f"{bot_name}: {bot_response}\n\n"
        self.text_widget.insert(END, msg2)  # Inserting the bot's response
        self.text_widget.configure(state=DISABLED)  # Disabling the text widget again

        self.text_widget.see(END)  # Ensuring the latest message is visible

if __name__ == "__main__":
    app = NBAChatApplication()  # Creating an instance of the application
    app.run()  # Running the application