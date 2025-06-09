import customtkinter as ctk
import threading
import time
from datetime import datetime
from tkinter import messagebox

from add_reminder import AddReminderPage
from view_reminders import ViewRemindersPage
from database import create_table, connect_db

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("900x550")
app.title("💊 Medicine Reminder App")

sidebar = ctk.CTkFrame(app, width=200)
sidebar.pack(side="left", fill="y")

main_frame = ctk.CTkFrame(app)
main_frame.pack(expand=True, fill="both")

ctk.CTkLabel(sidebar, text="Menu", font=("Arial", 20)).pack(pady=20)
btn_home = ctk.CTkButton(sidebar, text="🏠 Home")
btn_home.pack(pady=10)
btn_add = ctk.CTkButton(sidebar, text="➕ Add Reminder")
btn_add.pack(pady=10)
btn_about = ctk.CTkButton(sidebar, text="ℹ️ About")
btn_about.pack(pady=10)

current_page = None
def show_page(page_class):
    global current_page
    if current_page:
        current_page.destroy()
    current_page = page_class(main_frame)
    current_page.pack(expand=True, fill="both")

btn_home.configure(command=lambda: show_page(ViewRemindersPage))
btn_add.configure(command=lambda: show_page(AddReminderPage))
btn_about.configure(command=lambda: messagebox.showinfo("About", "Medicine Reminder App by Ashley 🚑"))

show_page(ViewRemindersPage)

# Alert checker
def check_reminders_loop():
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT patient_name, medicine_name FROM reminders WHERE date || ' ' || time = ?", (now,))
        due = cur.fetchall()
        conn.close()

        if due:
            for reminder in due:
                patient, medicine = reminder
                messagebox.showinfo("💊 Reminder", f"{patient} needs to take {medicine} now!")

        time.sleep(60)

# DB Setup + Start Reminder Checker
create_table()
threading.Thread(target=check_reminders_loop, daemon=True).start()

app.mainloop()
