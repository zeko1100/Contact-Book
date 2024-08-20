import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactManager:
    def __init__(self, window):
        self.window = window
        self.window.title("Contact Manager")

        # Dictionary to store contacts
        self.contacts = {}

        # Labels and Entry widgets for contact details
        self.name_label = tk.Label(window, text="Name:", font=('Arial', 12))
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.name_entry = tk.Entry(window, width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(window, text="Phone Number:", font=('Arial', 12))
        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.phone_entry = tk.Entry(window, width=30)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label = tk.Label(window, text="Email:", font=('Arial', 12))
        self.email_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.email_entry = tk.Entry(window, width=30)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label = tk.Label(window, text="Address:", font=('Arial', 12))
        self.address_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.address_entry = tk.Entry(window, width=30)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons for various operations
        self.add_button = tk.Button(window, text="Add Contact", command=self.add_contact, width=15)
        self.add_button.grid(row=4, column=0, padx=10, pady=10)

        self.view_button = tk.Button(window, text="View Contacts", command=self.view_contacts, width=15)
        self.view_button.grid(row=4, column=1, padx=10, pady=10)

        self.search_button = tk.Button(window, text="Search Contact", command=self.search_contact, width=15)
        self.search_button.grid(row=5, column=0, padx=10, pady=10)

        self.update_button = tk.Button(window, text="Update Contact", command=self.update_contact, width=15)
        self.update_button.grid(row=5, column=1, padx=10, pady=10)

        self.delete_button = tk.Button(window, text="Delete Contact", command=self.delete_contact, width=15)
        self.delete_button.grid(row=6, column=0, padx=10, pady=10)

        self.quit_button = tk.Button(window, text="Quit", command=window.quit, width=15)
        self.quit_button.grid(row=6, column=1, padx=10, pady=10)

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if name in self.contacts:
            messagebox.showwarning("Duplicate Entry", "A contact with this name already exists.")
            return

        if name and phone:
            self.contacts[name] = {
                "phone": phone,
                "email": email,
                "address": address
            }
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Please fill in both the name and phone number.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Contact List", "No contacts found.")
            return

        contact_list = "\n".join([f"{name}: {details['phone']}" for name, details in self.contacts.items()])
        messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if not search_term:
            return

        found_contacts = [f"{name}: {details['phone']}" for name, details in self.contacts.items()
                          if search_term.lower() in name.lower() or search_term in details['phone']]

        if found_contacts:
            messagebox.showinfo("Search Results", "\n".join(found_contacts))
        else:
            messagebox.showinfo("Search Results", "No matching contacts found.")

    def update_contact(self):
        name = simpledialog.askstring("Update Contact", "Enter the name of the contact to update:")
        if not name or name not in self.contacts:
            messagebox.showwarning("Not Found", "Contact not found.")
            return

        new_phone = simpledialog.askstring("Update Phone", "Enter new phone number:", initialvalue=self.contacts[name]["phone"])
        new_email = simpledialog.askstring("Update Email", "Enter new email:", initialvalue=self.contacts[name]["email"])
        new_address = simpledialog.askstring("Update Address", "Enter new address:", initialvalue=self.contacts[name]["address"])

        if new_phone:
            self.contacts[name]["phone"] = new_phone
        if new_email:
            self.contacts[name]["email"] = new_email
        if new_address:
            self.contacts[name]["address"] = new_address

        messagebox.showinfo("Success", "Contact updated successfully!")

    def delete_contact(self):
        name = simpledialog.askstring("Delete Contact", "Enter the name of the contact to delete:")
        if not name or name not in self.contacts:
            messagebox.showwarning("Not Found", "Contact not found.")
            return

        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete the contact '{name}'?")
        if confirm:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully!")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
