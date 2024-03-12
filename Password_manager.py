import tkinter as tk
from tkinter import simpledialog
from cryptography.fernet import Fernet
import json
import base64

class PasswordManagerGUI:
    def __init__(self, master_password):
        self.master_password = master_password
        self.password_manager = PasswordManager(master_password)
        self.password_manager.load_from_file()

        self.root = tk.Tk()
        self.root.title("Password Manager")

        self.website_label = tk.Label(self.root, text="Website:")
        self.website_entry = tk.Entry(self.root)

        self.username_label = tk.Label(self.root, text="Username:")
        self.username_entry = tk.Entry(self.root)

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_entry = tk.Entry(self.root, show="*")

        self.save_button = tk.Button(self.root, text="Save Password", command=self.save_password)
        self.retrieve_button = tk.Button(self.root, text="Retrieve Password", command=self.retrieve_password)

        self.website_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.website_entry.grid(row=0, column=1, padx=5, pady=5)
        self.username_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.username_entry.grid(row=1, column=1, padx=5, pady=5)
        self.password_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.password_entry.grid(row=2, column=1, padx=5, pady=5)

        self.save_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.retrieve_button.grid(row=4, column=0, columnspan=2, pady=10)

    def save_password(self):
        website = self.website_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        if website and username and password:
            self.password_manager.save_password(website, username, password)
            self.clear_entries()

    def retrieve_password(self):
        website = self.website_entry.get()
        username = self.username_entry.get()
        if website and username:
            retrieved_password = self.password_manager.retrieve_password(website, username)
            if retrieved_password:
                self.password_entry.delete(0, tk.END)
                self.password_entry.insert(0, retrieved_password)

    def clear_entries(self):
        self.website_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def run(self):
        self.root.mainloop()


class PasswordManager:
    def __init__(self, master_password):
        self.master_password = master_password
        self.passwords = {}
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def _encrypt(self, data):
        return self.cipher_suite.encrypt(data.encode())

    def _decrypt(self, data):
        return self.cipher_suite.decrypt(data).decode()

    def _save_to_file(self):
        encrypted_data = self._encrypt(json.dumps(self.passwords))
        encoded_data = base64.b64encode(encrypted_data).decode()
        with open('passwords.json', 'w') as file:
            json.dump({'data': encoded_data}, file)

    def load_from_file(self):
        try:
            with open('passwords.json', 'r') as file:
                data = json.load(file)
                encoded_data = data['data']
                encrypted_data = base64.b64decode(encoded_data)
                decrypted_data = self._decrypt(encrypted_data)
                self.passwords = json.loads(decrypted_data)
        except (FileNotFoundError, json.JSONDecodeError):
            pass  # If the file doesn't exist or is not valid JSON, create a new one when saving passwords

if __name__ == "__main__":
    # Use a dialog to securely input the master password
    root = tk.Tk()
    root.withdraw()
    master_password = simpledialog.askstring("Password Manager", "Enter your master password to store it:", show='*')

    if master_password:
        password_manager_gui = PasswordManagerGUI(master_password)
        password_manager_gui.run()  
