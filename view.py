import tkinter as tk
from controller import add_contact, view_contacts, update_contact, delete_contact

window = tk.Tk()
window.title("Contact Management System")
window.minsize(width=300, height=150)

# frame_entry = tk.Frame(master=window)
btn_add = tk.Button(master=window, text="Add", command=add_contact)
btn_view = tk.Button(master=window, text="View", command=view_contacts)
btn_edit = tk.Button(master=window, text="Edit", command=update_contact)
btn_delete = tk.Button(master=window, text="Delete", command=delete_contact)

# frame_entry.grid(row=0, column=1)
btn_add.grid(row=0, column=1, padx=180, pady=10)
btn_view.grid(row=1, column=1, padx=180, pady=10)
btn_edit.grid(row=2, column=1, padx=180, pady=10)
btn_delete.grid(row=3, column=1, padx=180, pady=10)


window.mainloop()
