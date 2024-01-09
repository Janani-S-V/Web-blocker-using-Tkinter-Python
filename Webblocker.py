import tkinter as tk
from tkinter import messagebox
import os

# Path to the hosts file on Windows
hosts_file_path = r"C:\Windows\System32\drivers\etc\hosts"

def block_website(website):
    try:
        with open(hosts_file_path, 'a') as hosts_file:
            hosts_file.write('127.0.0.1 ' + website.strip() + '\n')
        messagebox.showinfo("Success", f"Website {website} blocked successfully")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to block website. Error: {str(e)}")

def unblock_website(website):
    try:
        with open(hosts_file_path, 'r') as hosts_file:
            lines = hosts_file.readlines()
        with open(hosts_file_path, 'w') as hosts_file:
            for line in lines:
                if website.strip() not in line:
                    hosts_file.write(line)
        messagebox.showinfo("Success", f"Website {website} unblocked successfully")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to unblock website. Error: {str(e)}")

def block_from_gui(entry_var):
    website_to_block = entry_var.get().strip()
    block_website(website_to_block)

def unblock_from_gui(entry_var):
    website_to_unblock = entry_var.get().strip()
    unblock_website(website_to_unblock)

def create_gui():
    root = tk.Tk()
    root.title("Website Blocker")

    label_block = tk.Label(root, text="Enter website to block:")
    label_block.pack()

    entry_var_block = tk.StringVar()
    entry_block = tk.Entry(root, textvariable=entry_var_block)
    entry_block.pack()

    block_button = tk.Button(root, text="Block Website", command=lambda: block_from_gui(entry_var_block))
    block_button.pack()

    label_unblock = tk.Label(root, text="Enter website to unblock:")
    label_unblock.pack()

    entry_var_unblock = tk.StringVar()
    entry_unblock = tk.Entry(root, textvariable=entry_var_unblock)
    entry_unblock.pack()

    unblock_button = tk.Button(root, text="Unblock Website", command=lambda: unblock_from_gui(entry_var_unblock))
    unblock_button.pack()

    root.mainloop()

if __name__ == '__main__':
    create_gui()
