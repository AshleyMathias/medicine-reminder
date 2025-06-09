import customtkinter as ctk
from tkcalendar import DateEntry
from database import insert_reminder
from tkinter import messagebox

class AddReminderPage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        ctk.CTkLabel(self, text="Add Medicine Reminder", font=("Arial", 22)).grid(row=0, column=0, columnspan=2, pady=20)

        ctk.CTkLabel(self, text="Patient Name:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        self.patient_entry = ctk.CTkEntry(self, width=200)
        self.patient_entry.grid(row=1, column=1, padx=10, pady=5)

        ctk.CTkLabel(self, text="Medicine Name:").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        self.medicine_entry = ctk.CTkEntry(self, width=200)
        self.medicine_entry.grid(row=2, column=1, padx=10, pady=5)

        ctk.CTkLabel(self, text="Dosage:").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        self.dosage_entry = ctk.CTkEntry(self, width=200)
        self.dosage_entry.grid(row=3, column=1, padx=10, pady=5)

        ctk.CTkLabel(self, text="Date:").grid(row=4, column=0, sticky="e", padx=10, pady=5)
        self.date_entry = DateEntry(self, width=17, date_pattern='yyyy-mm-dd')
        self.date_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        ctk.CTkLabel(self, text="Time:").grid(row=5, column=0, sticky="e", padx=10, pady=5)
        time_frame = ctk.CTkFrame(self)
        time_frame.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        self.hour_option = ctk.CTkOptionMenu(time_frame, values=[f"{i:02d}" for i in range(24)])
        self.hour_option.grid(row=0, column=0, padx=(0, 10))
        self.minute_option = ctk.CTkOptionMenu(time_frame, values=[f"{i:02d}" for i in range(0, 60, 5)])
        self.minute_option.grid(row=0, column=1)

        self.submit_btn = ctk.CTkButton(self, text="➕ Add Reminder", command=self.add_reminder_action)
        self.submit_btn.grid(row=6, column=0, columnspan=2, pady=20)

    def add_reminder_action(self):
        patient = self.patient_entry.get()
        medicine = self.medicine_entry.get()
        dosage = self.dosage_entry.get()
        date = self.date_entry.get()
        time = f"{self.hour_option.get()}:{self.minute_option.get()}"

        if not all([patient, medicine, dosage, date, time]):
            messagebox.showerror("Error", "Please fill all fields.")
            return

        insert_reminder(patient, medicine, dosage, date, time)
        messagebox.showinfo("Success", "Reminder added successfully!")

        self.patient_entry.delete(0, 'end')
        self.medicine_entry.delete(0, 'end')
        self.dosage_entry.delete(0, 'end')
