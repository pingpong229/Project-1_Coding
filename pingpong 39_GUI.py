import tkinter as tk
from tkinter import messagebox

def calculate_volume():
    try:
        width = float(width_entry.get())
        length = float(length_entry.get())
        height = float(height_entry.get())
        
        if width <= 0 or length <= 0 or height <= 0:
            messagebox.showerror("Error", "กรุณากรอกค่าที่เป็นบวก")
            return
        
        volume = (width * length * height) / 1_000_000
        result_label.config(text=f"ปริมาตร: {volume:.6f} ลูกบาศก์เมตร")
    except ValueError:
        messagebox.showerror("Error", "กรุณากรอกตัวเลขที่ถูกต้อง")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("🟣 CUBIC METER CALCULATOR 🟣")
root.geometry("300x250")
root.configure(bg="#D8BFD8")  # ตั้งค่าสีม่วงพาสเทล

# ส่วนของ Label และ Entry
width_label = tk.Label(root, text="ความกว้าง (cm):", bg="#D8BFD8")
width_label.pack()
width_entry = tk.Entry(root)
width_entry.pack()

length_label = tk.Label(root, text="ความยาว (cm):", bg="#D8BFD8")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

height_label = tk.Label(root, text="ความสูง (cm):", bg="#D8BFD8")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

# ปุ่มคำนวณ
calculate_button = tk.Button(root, text="คำนวณ", command=calculate_volume)
calculate_button.pack(pady=10)

# แสดงผลลัพธ์
result_label = tk.Label(root, text="", bg="#D8BFD8")
result_label.pack()

# เริ่มโปรแกรม
root.mainloop()
