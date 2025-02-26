import tkinter as tk
from tkinter import messagebox

def calculate_volume():
    try:
        width = float(entry_width.get())
        length = float(entry_length.get())
        height = float(entry_height.get())
        volume = (width * length * height) / 1_000_000
        label_result.config(text=f"Volume: {volume:.6f} cubic meters")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Create main window
root = tk.Tk()
root.title("Pink Volume Calculator")
root.geometry("400x300")
root.configure(bg="#FFC0CB")

# Title Label
label_title = tk.Label(root, text="Cubic Meters", font=("Arial", 20, "bold"), bg="#FFC0CB")
label_title.pack(pady=10)

# Input Fields
frame = tk.Frame(root, bg="#FFC0CB")
frame.pack(pady=10)

labels = ["Width (cm):", "Length (cm):", "Height (cm):"]
entries = []

for i, text in enumerate(labels):
    tk.Label(frame, text=text, font=("Arial", 12), bg="#FFC0CB").grid(row=i, column=0, padx=5, pady=5, sticky="w")
    entry = tk.Entry(frame, font=("Arial", 12))
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

entry_width, entry_length, entry_height = entries

# Calculate Button
btn_calculate = tk.Button(root, text="Calculate Volume", font=("Arial", 12), command=calculate_volume, bg="#FF69B4", fg="white")
btn_calculate.pack(pady=10)

# Result Label
label_result = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#FFC0CB")
label_result.pack(pady=10)

# Run the GUI
root.mainloop()
