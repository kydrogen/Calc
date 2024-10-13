import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation+=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    """
    calcuation  = "10 + 5"
    1. eval("10 + 5") -> 15
    2. str(15) = "15"
    3. assign the variable result = "15"
    """
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field(): 
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root=tk.Tk()
root.geometry("300x275")

text_result = tk.Text(root, width=16, height=2, font=("Arial", 24) )
text_result.grid(columnspan=5)

btn_1 = tk. Button(root, text="1", width=5, font=("Arial", 14), command=lambda: add_to_calculation(1) )
btn_1.grid(row=2, column=1 )
root.mainloop()