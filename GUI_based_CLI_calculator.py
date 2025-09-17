import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        
        # Entry widget to display results
        self.entry = tk.Entry(root, width=20, font=('Arial', 14), bd=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Button layout
        button_layout = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]
        
        # Create and place buttons
        for (text, row, col) in button_layout:
            if text == '=':
                btn = tk.Button(root, text=text, width=5, height=2, 
                              font=('Arial', 12), command=self.calculate)
            elif text == 'C':
                btn = tk.Button(root, text=text, width=5, height=2, 
                              font=('Arial', 12), command=self.clear)
            else:
                btn = tk.Button(root, text=text, width=5, height=2, 
                              font=('Arial', 12), 
                              command=lambda x=text: self.add_to_expression(x))
            btn.grid(row=row, column=col, padx=5, pady=5)
    
    def add_to_expression(self, value):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current + value)
    
    def clear(self):
        self.entry.delete(0, tk.END)
    
    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except:
            messagebox.showerror("Error", "Invalid Expression")
            self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()