import tkinter as tk
from tkinter import messagebox, scrolledtext, Checkbutton, IntVar, Toplevel
import subprocess
import threading
import sys

def show_loading():
    global loading_window
    loading_window = Toplevel(root)
    loading_window.title("Loading...")
    loading_window.geometry("300x150")
    loading_window.configure(bg="#2C3E50")
    loading_label = tk.Label(loading_window, text="Scanning...", font=("Arial", 14, "bold"), bg="#2C3E50", fg="white")
    loading_label.pack(expand=True)
    root.update()

def confirm_scan():
    selected_scans = [flag for flag, var in scan_options.items() if var.get() == 1]
    if not selected_scans:
        messagebox.showerror("Error", "You must select at least one scan type.")
        return
    
    target = target_entry.get().strip()
    if not target:
        messagebox.showerror("Error", "Please enter a target IP or URL.")
        return
    
    nmap_command = "nmap " + " ".join(selected_scans) + " " + target
    
    modify_window = Toplevel(root)
    modify_window.title("Modify Scan Command")
    modify_window.geometry("500x200")
    modify_window.configure(bg="#2C3E50")
    
    modify_label = tk.Label(modify_window, text="Modify the Nmap command before execution:", bg="#2C3E50", fg="white")
    modify_label.pack(pady=10)
    
    modify_entry = tk.Entry(modify_window, font=("Arial", 12), width=60)
    modify_entry.pack(pady=5)
    modify_entry.insert(0, nmap_command)
    
    def proceed_with_scan():
        modified_command = modify_entry.get().strip()
        modify_window.destroy()
        threading.Thread(target=run_nmap, args=(modified_command,)).start()
    
    proceed_button = tk.Button(modify_window, text="Proceed", bg="#3498DB", fg="white", command=proceed_with_scan)
    proceed_button.pack(pady=10)

def run_nmap(nmap_command):
    root.withdraw()
    show_loading()
    
    result_window = tk.Tk()
    result_window.title("Scan Results")
    result_window.geometry("700x550")
    result_window.configure(bg="#2C3E50")
    
    result_label = tk.Label(result_window, text="Scan Results", font=("Arial", 14, "bold"), bg="#2C3E50", fg="white")
    result_label.pack(pady=10)
    
    result_text = scrolledtext.ScrolledText(result_window, width=80, height=20, font=("Arial", 10), bg="#ECF0F1")
    result_text.pack(pady=10)
    
    result_text.insert(tk.END, f"Running: {nmap_command}\n\n")
    try:
        result = subprocess.run(nmap_command.split(), capture_output=True, text=True, timeout=300)
        result_text.insert(tk.END, result.stdout + "\n")
        result_text.insert(tk.END, result.stderr + "\n")
    except Exception as e:
        result_text.insert(tk.END, f"Error: {str(e)}\n")
    
    loading_window.destroy()
    
    def restart_scan():
        result_window.destroy()
        root.deiconify()
    
    def exit_program():
        result_window.destroy()
        sys.exit(0)
    
    rescan_button = tk.Button(result_window, text="Re-Scan", font=("Arial", 12, "bold"), bg="#3498DB", fg="white", command=restart_scan)
    rescan_button.pack(side="left", padx=20, pady=10)
    
    exit_button = tk.Button(result_window, text="Exit", font=("Arial", 12, "bold"), bg="#E74C3C", fg="white", command=exit_program)
    exit_button.pack(side="right", padx=20, pady=10)
    
    result_window.mainloop()

def clear_placeholder(event):
    target_entry.delete(0, tk.END)

def main():
    global root, target_entry, scan_options
    
    root = tk.Tk()
    root.title("Nmap GUI Scanner")
    root.geometry("700x600")
    root.configure(bg="#2C3E50")
    root.protocol("WM_DELETE_WINDOW", sys.exit)
    
    title_label = tk.Label(root, text="Nmap Scanner", font=("Arial", 18, "bold"), bg="#2C3E50", fg="white")
    title_label.pack(pady=10)
    
    target_entry = tk.Entry(root, font=("Arial", 14), width=50)
    target_entry.pack(pady=5)
    target_entry.insert(0, "Enter Target IP or URL")
    target_entry.bind("<FocusIn>", clear_placeholder)
    
    scan_frame = tk.Frame(root, bg="#2C3E50")
    scan_frame.pack(pady=10)
    
    scan_types = [
        ("Stealth Scan (-sS)", "TCP Connect Scan (-sT)", "Aggressive Scan (-A)", "OS Detection (-O)"),
        ("Version Detection (-sV)", "Full Port Scan (-p-)", "No Ping (-Pn)", "UDP Scan (-sU)"),
        ("Timing Template 4 (-T4)", "Fast Scan (-F)", "Default Scripts (-sC)", "Service Scan (-sN)")
    ]
    
    scan_options = {}
    for row in scan_types:
        row_frame = tk.Frame(scan_frame, bg="#2C3E50")
        row_frame.pack(fill="x", pady=5)
        for scan_item in row:
            flag = scan_item.split("(")[-1].strip(")")
            scan_options[flag] = IntVar()
            chk = Checkbutton(row_frame, text=scan_item, variable=scan_options[flag], bg="#34495E", fg="white", selectcolor="#2C3E50", font=("Arial", 10))
            chk.pack(side="left", padx=10)
    
    scan_button = tk.Button(root, text="Scan", font=("Arial", 12, "bold"), bg="#E74C3C", fg="white", command=confirm_scan)
    scan_button.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
