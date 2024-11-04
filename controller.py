# Model-View
import tkinter as tk
from service import add_contact_service, get_contacts_service, edit_contact_service, remove_contact_service
from tkinter import messagebox


def add_contact():

    global enter_owner_name
    global enter_name
    global enter_phone_number
    global enter_email
    global add_form

    add_form = tk.Tk()
    add_form.title("Add Contact")
    add_form.geometry("280x170")

    frame_entry = tk.Frame(master=add_form)

    label_owner_name = tk.Label(master=frame_entry, text="Owner Name: ")
    enter_owner_name = tk.Entry(master=frame_entry, width=20)

    label_name = tk.Label(master=frame_entry, text="Contact Name: ")
    enter_name = tk.Entry(master=frame_entry, width=20)

    label_phone_number = tk.Label(master=frame_entry, text="Phone Number: ")
    enter_phone_number = tk.Entry(master=frame_entry, width=20)

    label_email = tk.Label(master=frame_entry, text="Email: ")
    enter_email = tk.Entry(master=frame_entry, width=20)

    label_owner_name.grid(row=0, column=0)
    enter_owner_name.grid(row=0, column=1)

    label_name.grid(row=1, column=0)
    enter_name.grid(row=1, column=1)

    label_phone_number.grid(row=2, column=0)
    enter_phone_number.grid(row=2, column=1)

    label_email.grid(row=3, column=0)
    enter_email.grid(row=3, column=1)

    frame_entry.grid(row=0, column=1, pady=5)

    btn_add_contact = tk.Button(
        master=add_form,
        text="Add",
        command=parse_contact_from_view
    )
    btn_add_contact.grid(row=4, column=1, pady=20, padx=10)


def parse_contact_from_view():

    owner_name = enter_owner_name.get()
    name = enter_name.get()
    phone_number = int(enter_phone_number.get())
    email = enter_email.get()
    # print('user: ', owner_name, name, phone_number, email)

    response = add_contact_service(owner_name, name, phone_number, email)

    if response == "A new contact has been added":
        messagebox.showinfo("Notification", "A New Contact Added Successfully")
        add_form.destroy()
    else:
        messagebox.showinfo("Notification", response)


def view_contacts():

    global enter_ownername
    global view_window

    view_window = tk.Tk()
    view_window.title("View Contacts")
    view_window.resizable(width=True, height=True)

    frame_entry = tk.Frame(master=view_window)

    label_ownername = tk.Label(
        master=frame_entry, text="Enter your name to view your contacts: ")
    enter_ownername = tk.Entry(master=frame_entry, width=20)

    label_ownername.grid(row=0, column=0)
    enter_ownername.grid(row=1, column=0)

    frame_entry.grid(row=0, column=1, pady=10, padx=10)

    btn_view_contacts = tk.Button(
        master=view_window,
        text="View",
        command=show_contacts
    )
    btn_view_contacts.grid(row=2, column=1, pady=20, padx=10)


def show_contacts():

    owner_name = enter_ownername.get()
    contacts = get_contacts_service(owner_name)
    if not contacts:
        messagebox.showinfo('Notification', 'No Contacts found for this User')
        view_window.destroy()
        return

    view_win = tk.Tk()
    view_win.title(f"{owner_name} Contacts")
    view_win.resizable(width=True, height=True)

    frame_entry = tk.Frame(master=view_win)
    frame_entry.pack(padx=10, pady=10)

    for index, contact in enumerate(contacts):

        res_name_lbl = tk.Label(master=frame_entry, text="Name: ")
        res_name_lbl.grid(row=index*3, column=0, sticky='w')
        res_name = tk.Label(master=frame_entry, text=contact.name)
        res_name.grid(row=index*3, column=1, sticky='w')

        res_phone_lbl = tk.Label(master=frame_entry, text="Phone Number: ")
        res_phone_lbl.grid(row=index*3 + 1, column=0, sticky='w')
        res_phone = tk.Label(master=frame_entry, text=contact.phone_number)
        res_phone.grid(row=index*3 + 1, column=1, sticky='w')

        res_email_lbl = tk.Label(master=frame_entry, text="Email: ")
        res_email_lbl.grid(row=index*3 + 2, column=0, sticky='w')
        res_email = tk.Label(master=frame_entry, text=contact.email or 'N/A')
        res_email.grid(row=index*3 + 2, column=1, sticky='w')

    view_window.destroy()


def update_contact():

    global enter_ownernamee
    global enter_old_name
    global enter_new_name
    global enter_new_phone_number
    global enter_new_email
    global update_window

    update_window = tk.Tk()
    update_window.title("Update Contact")
    update_window.resizable(width=True, height=True)

    frame_entry = tk.Frame(master=update_window)

    label_ownernamee = tk.Label(master=frame_entry, text="Enter your name: ")
    enter_ownernamee = tk.Entry(master=frame_entry, width=20)

    label_ownernamee.grid(row=0, column=0, sticky="e")
    enter_ownernamee.grid(row=0, column=1)

    label_old_name = tk.Label(
        master=frame_entry, text="Enter old contact name: ")
    enter_old_name = tk.Entry(master=frame_entry, width=20)

    label_old_name.grid(row=1, column=0, sticky="e")
    enter_old_name.grid(row=1, column=1)

    label_new_name = tk.Label(master=frame_entry, text="New Contact Name: ")
    enter_new_name = tk.Entry(master=frame_entry, width=20)

    label_new_phone_number = tk.Label(
        master=frame_entry, text="New Phone Number: ")
    enter_new_phone_number = tk.Entry(master=frame_entry, width=20)

    label_new_email = tk.Label(master=frame_entry, text="New Email: ")
    enter_new_email = tk.Entry(master=frame_entry, width=20)

    label_new_name.grid(row=2, column=0, sticky="e")
    enter_new_name.grid(row=2, column=1)

    label_new_phone_number.grid(row=3, column=0, sticky="e")
    enter_new_phone_number.grid(row=3, column=1)

    label_new_email.grid(row=4, column=0, sticky="e")
    enter_new_email.grid(row=4, column=1)

    frame_entry.grid(row=0, column=0, padx=20, pady=10)

    btn_update_contact = tk.Button(
        master=update_window,
        text="Update",
        command=update_contact_from_service
    )
    btn_update_contact.grid(row=2, column=1, pady=20, padx=10)


def update_contact_from_service():

    owner_name = enter_ownernamee.get()
    old_name = enter_old_name.get()
    new_name = enter_new_name.get()
    new_phone = int(enter_new_phone_number.get())
    new_email = enter_new_email.get()

    response = edit_contact_service(
        owner_name, old_name, new_name, new_phone, new_email)

    if response == "Contact has been updated Successfully":
        messagebox.showinfo("Notification", response)
    else:
        messagebox.showinfo("Notification", response)

    update_window.destroy()


def delete_contact():

    global enter_ownerrnamee
    global enter_contactname

    del_window = tk.Tk()
    del_window.title("Delete Contact")
    del_window.resizable(width=True, height=True)

    frame_entry = tk.Frame(master=del_window)

    label_ownerrnamee = tk.Label(master=frame_entry, text="Enter your name: ")
    enter_ownerrnamee = tk.Entry(master=frame_entry, width=15)

    label_ownerrnamee.grid(row=0, column=0)
    enter_ownerrnamee.grid(row=0, column=1)

    label_contactname = tk.Label(
        master=frame_entry, text="Enter contact name: ")
    enter_contactname = tk.Entry(master=frame_entry, width=15)

    label_contactname.grid(row=1, column=0)
    enter_contactname.grid(row=1, column=1)

    frame_entry.grid(row=0, column=1, pady=5, padx=10)

    btn_del_contact = tk.Button(
        master=del_window,
        text="Delete",
        command=delete_contact_from_service
    )
    btn_del_contact.grid(row=2, column=1, pady=20, padx=10)


def delete_contact_from_service():
    owner_name = enter_ownerrnamee.get()
    contact_name = enter_contactname.get()

    response = remove_contact_service(owner_name, contact_name)

    if response == "Contact is deleted":
        messagebox.showinfo("Notification", response)
    else:
        messagebox.showinfo("Notification", response)
