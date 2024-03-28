import tkinter as tk
from tkinter import ttk
import pyautogui
import pygetwindow as gw
import time



def generate_string():
    # Retrieve the values from the input boxes
    mid_num = mid_entry.get()
    file_num = file_entry.get()
    county_num = county_combobox.get()
    scanner = scanner_entry.get()
    date = date_entry.get()
    usace = usace_entry.get()
    
    # Format the string as per your requirement
    result_string = f"{mid_num} {file_num} {county_num} {date} HIST {scanner} {usace}"
    
    # Update the entry widget to show the result
    result_entry.delete(0, tk.END)  # Clear existing content
    result_entry.insert(0, result_string)  # Insert the new string
    result_var.set(result_string) 
    
    # Automatically copy the result string to the clipboard
    root.clipboard_clear()
    root.clipboard_append(result_string)

    # Replace 'Your Window Title Here' with the exact title of the Scandall 21 window
    window_title = 'Untitled - ScandAll 21'
    try:
        # Get the window and bring it to the foreground
        window = gw.getWindowsWithTitle(window_title)[0]
        window.activate()
        
        # Wait a moment for the window to become active
        time.sleep(1)
        
        # Now perform the keystrokes
        pyautogui.press('alt')
        pyautogui.press('s')
        pyautogui.press('a')
        pyautogui.press('enter')

    except IndexError:
        print(f"Window with title '{window_title}' not found.")


# Create the main window
root = tk.Tk()
root.title("String Generator")

mid_label = ttk.Label(root, text="Master ID")
mid_label.grid(column=0, row=0, padx=10, pady=10)
mid_entry = ttk.Entry(root,)
mid_entry.grid(column=1, row=0, padx=10, pady=10)
mid_entry.insert(0,'xxx')

# Create and place the labels and entry widgets for inputs
file_label = ttk.Label(root, text="File #")
file_label.grid(column=0, row=1, padx=10, pady=10)
file_entry = ttk.Entry(root)
file_entry.grid(column=1, row=1, padx=10, pady=10)

county_label = ttk.Label(root, text="County #")
county_label.grid(column=0, row=2, padx=10, pady=10)
county_combobox = ttk.Combobox(root, values=['003', '097', '129', '999', '000'])
county_combobox.grid(column=1, row=2, padx=10, pady=10)

date_label = ttk.Label(root, text="Date")
date_label.grid(column=0, row=3, padx=10, pady=10)
date_entry = ttk.Entry(root)
date_entry.grid(column=1, row=3, padx=10, pady=10)

scanner_label = ttk.Label(root, text="Scanner")
scanner_label.grid(column=0, row=4, padx=10, pady=10)
scanner_entry = ttk.Entry(root)
scanner_entry.grid(column=1, row=4, padx=10, pady=10)

usace_label = ttk.Label(root, text="USACE #")
usace_label.grid(column=0, row=5, padx=10, pady=10)
usace_entry = ttk.Entry(root)
usace_entry.grid(column=1, row=5, padx=10, pady=10)

# Create and place the button, when pressed, it will run the generate_string function
generate_button = ttk.Button(root, text="Generate", command= generate_string)
generate_button.grid(column=0, row=6, columnspan=2, pady=10)


result_label = ttk.Label(root, text="Name")
result_label.grid(column=0, row=7, padx=10, pady=10)
# Entry widget to display the result, set to read-only mode
result_entry = ttk.Entry(root)
# To make the Entry widget read-only, we need to create a variable
# and associate it with the widget. The widget will display the value of this variable.
result_var = tk.StringVar()
result_entry.config(textvariable=result_var)
result_entry.grid(column=0, row=7, columnspan=2,pady=10)

# Run the application
root.mainloop()
