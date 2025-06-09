import customtkinter as ctk
from database import connect_db

class ViewRemindersPage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        ctk.CTkLabel(self, text="Upcoming Reminders", font=("Arial", 22)).pack(pady=20)
        self.reminders_frame = ctk.CTkScrollableFrame(self, width=600, height=300)
        self.reminders_frame.pack(pady=10)

        self.load_reminders()

    import tkinter as tk

    def delete_reminder(self, reminder_id):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM reminders WHERE id=?", (reminder_id,))
        conn.commit()
        conn.close()
        self.load_reminders()  # Refresh view

    def load_reminders(self):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM reminders ORDER BY date, time")
        rows = cur.fetchall()
        conn.close()

        for widget in self.reminders_frame.winfo_children():
            widget.destroy()

        if rows:
            for row in rows:
                id, patient, medicine, dosage, date, time = row
                frame = ctk.CTkFrame(self.reminders_frame)
                frame.pack(fill="x", pady=5, padx=10)

                text = f"👤 {patient} | 💊 {medicine} | 🧪 {dosage} | 📅 {date} ⏰ {time}"
                ctk.CTkLabel(frame, text=text, anchor="w").pack(side="left", fill="x", expand=True)

                del_btn = ctk.CTkButton(frame, text="Delete", width=70,
                                        command=lambda id=id: self.delete_reminder(id))
                del_btn.pack(side="right", padx=5)

            # For edit, add an edit_btn similarly (needs extra code)
        else:
            ctk.CTkLabel(self.reminders_frame, text="No reminders found.").pack()
