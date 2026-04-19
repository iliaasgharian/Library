import LibraryDataAdapter
import model
import sqlite3
import tkinter as tk


connection = sqlite3.connect("NewLibrary.db")
cursor = connection.cursor()

model.Book.books = LibraryDataAdapter.BookDataAdapter.get_all()
s = LibraryDataAdapter.AuthorDataAdapter.search("")

root = tk.Tk()
root.geometry("500x600")
edit_mode = False


def save():
    global edit_mode
    v1 = input1.get()
    v2 = input2.get()
    v3 = input3.get()
    if edit_mode == False:
        if v1 != "" and v2 != "" and v3 != "":
            a1 = model.Author(None, v1, v2, v3)
            a2 = LibraryDataAdapter.AuthorDataAdapter.insert(a1)
            update_listbox()

            input1.delete(0, tk.END)
            input2.delete(0, tk.END)
            input3.delete(0, tk.END)
            edit_mode = False
            lb.selection_clear(0, tk.END)
            button2.config(text="Save")

        else:
            pass
    elif edit_mode == True:
        if v1 != "" and v2 != "" and v3 != "":
            selected_indices = lb.curselection()
            if not selected_indices:
                return

            selected_items = [lb.get(i) for i in selected_indices]
            s1 = selected_items[0].split(",")
            s2 = s1[0].split("id: ")
            id1 = int(s2[1])
            s = LibraryDataAdapter.AuthorDataAdapter.update(id1, v1, v2, v3)
            update_listbox()

            input1.delete(0, tk.END)
            input2.delete(0, tk.END)
            input3.delete(0, tk.END)
            edit_mode = False
            lb.selection_clear(0, tk.END)
            button2.config(text="Save")


def clear():
    global edit_mode
    input1.delete(0, tk.END)
    input2.delete(0, tk.END)
    input3.delete(0, tk.END)
    edit_mode = False
    lb.selection_clear(0, tk.END)
    button2.config(text="Save")


def update_listbox():
    lb.delete(0, tk.END)
    s = LibraryDataAdapter.AuthorDataAdapter.search("")
    for i in s:
        lb.insert(
            tk.END, f"id: {i.id}, name: {i.name}, birthdate: {i.birthdate}, nationality: {i.nationality}")


def print_selected_items(event=None):
    global edit_mode
    selected_indices = lb.curselection()
    if not selected_indices:
        return

    selected_items = [lb.get(i) for i in selected_indices]
    print("Selected items:", selected_items)
    s1 = selected_items[0].split(",")
    s2 = s1[0].split("id: ")
    id1 = int(s2[1])

    properties = LibraryDataAdapter.AuthorDataAdapter.get_one(id1)
    for i in properties:
        id1 = i.id
        name1 = i.name
        birthdate1 = i.birthdate
        nationality1 = i.nationality

    input1.delete(0, tk.END)
    input2.delete(0, tk.END)
    input3.delete(0, tk.END)
    input1.insert(0, name1)
    input2.insert(0, birthdate1)
    input3.insert(0, nationality1)
    button2.config(text="Edit")
    edit_mode = True


root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_rowconfigure(7, weight=1)
root.grid_rowconfigure(8, weight=1)
root.grid_rowconfigure(9, weight=1)
root.grid_rowconfigure(10, weight=20)
root.grid_rowconfigure(11, weight=1)
root.grid_rowconfigure(12, weight=20)
root.grid_rowconfigure(13, weight=1)
root.grid_rowconfigure(14, weight=1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=3)
root.grid_columnconfigure(3, weight=1)

text1 = tk.Label(root, text="name :")
text1.grid(row=2, column=1)
input1 = tk.Entry(root)
input1.grid(row=2, column=2, sticky="nsew")

text2 = tk.Label(root, text="birthdate :")
text2.grid(row=4, column=1)
input2 = tk.Entry(root)
input2.grid(row=4, column=2, sticky="nsew")

text3 = tk.Label(root, text="nationality :")
text3.grid(row=6, column=1)
input3 = tk.Entry(root)
input3.grid(row=6, column=2, sticky="nsew")

button1 = tk.Button(root, text="Clear", bg="#FF8C00",
                    fg="white", command=clear, )
button1.grid(row=9, column=1, sticky="nsew")

button2 = tk.Button(root, text="Save", bg="#1b5fc4",
                    fg="white", activebackground="white", command=save)
button2.grid(row=9, column=2, sticky="nsew")

text_frame = tk.Frame(root)
text_frame.grid(row=10, column=1, columnspan=4,
                sticky="nsew", padx=(0, 30), pady=5)

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lb = tk.Listbox(text_frame, font=("Courier New", 8),
                yscrollcommand=scrollbar.set,)
lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=lb.yview)

update_listbox()


lb.bind('<<ListboxSelect>>', lambda event: print_selected_items())

root.mainloop()
