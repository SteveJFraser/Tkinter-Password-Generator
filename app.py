from random import shuffle, randint
import tkinter as tk
import webbrowser

#
# ---- create pwords.txt if not exists ----
with open("pwords.txt", "a+"):
    pass


# ---- open the pwords.txt file for viewing etc ----
def open_text():
    filename = "pwords.txt"
    # os.system(filename)
    webbrowser.open(filename)


# --- open the file and write empty string ---
def clear_txt_file():
    with open("pwords.txt", "w") as clear:
        clear.write("")


# *args is for the key binding that runs this function
def generate_pword(*args):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    choice_list = []
    for _ in range(0, int(number_of_letters.get())):
        choice_list.append(letters[randint(0, len(letters) - 1)])
    for _ in range(0, int(number_of_numbers.get())):
        choice_list.append(numbers[randint(0, len(numbers) - 1)])
    for _ in range(0, int(number_of_symbols.get())):
        choice_list.append(symbols[randint(0, len(symbols) - 1)])

    shuffle(choice_list)
    final_output = ''
    for x in choice_list:
        final_output += x
    output_string = f"------\nWebsite: {website_name.get()}\nPassword: {final_output}\n"
    with open('pwords.txt', 'a') as outfile:
        outfile.write(output_string)


root = tk.Tk()
root.geometry("700x250")
root.title("Password Generator")
# root.iconbitmap("key_password_lock.ico")
website_name = tk.StringVar()
number_of_letters = tk.StringVar()
number_of_symbols = tk.StringVar()
number_of_numbers = tk.StringVar()

top_frame = tk.Frame(root, background="#1e293b")
top_frame.pack(side="top", fill="x")

left_frame = tk.Frame(root, background="#64748b")
left_frame.pack(side="left", expand=True, fill="both")

right_frame = tk.Frame(root, background="#475569")
right_frame.pack(side="right", expand=True, fill="both")
# ------------ Welcome --------------
welcome_label = tk.Label(top_frame,
                         text="Welcome to the PyPassword Generator!",
                         font=("Arial", 20),
                         background="#1e293b",
                         foreground="#e2e8f0", pady=5)
welcome_label.pack()
# ------------ website --------------
website_label = tk.Label(left_frame,
                         text="Enter the name of the website the password is for :",
                         background="#64748b", font=("Arial", 14),
                         justify="right", foreground="#0f172a")
website_label.pack()
website_input = tk.Entry(right_frame,
                         textvariable=website_name,
                         font=("Arial", 14))
website_input.pack()
# ------------ letters -------------
letters_label = tk.Label(left_frame,
                         text="How many Letters would you like: ",
                         background="#64748b",
                         font=("Arial", 14),
                         justify="right", foreground="#0f172a")
letters_label.pack()
letters_input = tk.Entry(right_frame,
                         textvariable=number_of_letters,
                         font=("Arial", 14))
letters_input.pack()
# ---------- symbols -----------
symbol_label = tk.Label(left_frame,
                        text="How many Symbols would you like: ",
                        background="#64748b",
                        font=("Arial", 14),
                        justify="right", foreground="#0f172a")
symbol_label.pack()
symbol_input = tk.Entry(right_frame,
                        textvariable=number_of_symbols,
                        font=("Arial", 14))
symbol_input.pack()
# --------- numbers ------------
number_label = tk.Label(left_frame,
                        text="How many Numbers would you like: ",
                        background="#64748b",
                        font=("Arial", 14),
                        justify="right", foreground="#0f172a")
number_label.pack()
number_input = tk.Entry(right_frame,
                        textvariable=number_of_numbers,
                        font=("Arial", 14))
number_input.pack()
# ------- submit button ---------
sub_btn = tk.Button(right_frame,
                    text="Create Password",
                    command=generate_pword,
                    font=("Arial", 12),
                    width=24,
                    background="#6b7280",
                    foreground="#0f172a")
sub_btn.pack()
# ------- delete passwords from the text file -------
delete_all_passwords = tk.Button(right_frame,
                                 text="Delete all passwords",
                                 command=clear_txt_file,
                                 font=("Arial", 12),
                                 width=24,
                                 background="#6b7280",
                                 foreground="#0f172a")
delete_all_passwords.pack()
# ----- quit button ----
quit_btn = tk.Button(right_frame,
                     text="Quit",
                     command=root.destroy,
                     font=("Arial", 12),
                     width=24,
                     background="#6b7280",
                     foreground="#0f172a")
quit_btn.pack()
# ---- spacer label ----
sp_lab = tk.Label(left_frame, text="", pady=5, background="#64748b")
sp_lab.pack()
# ----- open text file in default text editor -----
open_text_editor = tk.Button(left_frame,
                             text="Open your passwords file",
                             command=open_text,
                             font=("Arial", 12),
                             width=24,
                             background="#6b7280",
                             foreground="#0f172a")
open_text_editor.pack()
# ----- key binding to the enter key -----
root.bind("<Return>", generate_pword)
root.mainloop()