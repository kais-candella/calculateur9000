import tkinter as tk

field_text=""

def add_to_field(sth):
    global field_text
    field_text=field_text+str(sth)
    field.delete("1.0","end")
    field.insert("1.0",field_text)
    
def calculate():
    global field_text
    result=str(eval(field_text))
    field.delete("1.0", "end")
    field.insert("1.0", result)
def clear():
    global field_text
    field_text=""
    field.delete("1.0", "end")

calcul=tk.Tk()
calcul.geometry("300x270")
calcul.title("Calculator9000")
field=tk.Text(calcul,height=2,width=21,font=("Arial",20),background="#d7d7d7")
field.grid(row=1,column=1,columnspan=4)

######################
###    Bouttons    ###
######################

btn_1=tk.Button(calcul,text="1", cursor = "hand2",command=lambda: add_to_field(1),width=5,font=("Arial",15),bg="#a49bb8",)
btn_1.grid(row=4,column=1,)

btn_2=tk.Button(calcul,text="2", cursor = "hand2",command=lambda: add_to_field(2),width=5,font=("Arial",15),bg="#a49bb8")
btn_2.grid(row=4,column=2)

btn_3=tk.Button(calcul,text="3", cursor = "hand2",command=lambda: add_to_field(3),width=5,font=("Arial",15),bg="#a49bb8")
btn_3.grid(row=4,column=3)

btn_4=tk.Button(calcul,text="4", cursor = "hand2",command=lambda: add_to_field(4),width=5,font=("Arial",15),bg="#a49bb8",)
btn_4.grid(row=3,column=1)

btn_5=tk.Button(calcul,text="5", cursor = "hand2",command=lambda: add_to_field(5),width=5,font=("Arial",15),bg="#a49bb8",)
btn_5.grid(row=3,column=2)

btn_6=tk.Button(calcul,text="6", cursor = "hand2",command=lambda: add_to_field(6),width=5,font=("Arial",15),bg="#a49bb8",)
btn_6.grid(row=3,column=3)

btn_7=tk.Button(calcul,text="7", cursor = "hand2",command=lambda: add_to_field(7),width=5,font=("Arial",15),bg="#a49bb8",)
btn_7.grid(row=2,column=1)

btn_8=tk.Button(calcul,text="8", cursor = "hand2",command=lambda: add_to_field(8),width=5,font=("Arial",15),bg="#a49bb8",)
btn_8.grid(row=2,column=2)

btn_9=tk.Button(calcul,text="9", cursor = "hand2",command=lambda: add_to_field(9),width=5,font=("Arial",15),bg="#a49bb8",)
btn_9.grid(row=2,column=3)

btn_0=tk.Button(calcul,text="0", cursor = "hand2",command=lambda: add_to_field(0),width=5,font=("Arial",15),bg="#a49bb8",)
btn_0.grid(row=5,column=1)

######################
# buttons operation ##
######################
btn_plus=tk.Button(calcul,text="+", cursor = "hand2",command=lambda: add_to_field("+"),width=5,font=("Arial",15),bg="grey",)
btn_plus.grid(row=4,column=4)

btn_minus=tk.Button(calcul,text="-", cursor = "hand2",command=lambda: add_to_field("-"),width=5,font=("Arial",15),bg="grey",)
btn_minus.grid(row=5,column=4)

btn_times=tk.Button(calcul,text="*", cursor = "hand2",command=lambda: add_to_field("*"),width=5,font=("Arial",15),bg="grey",)
btn_times.grid(row=3,column=4)

btn_division=tk.Button(calcul,text="/", cursor = "hand2",command=lambda: add_to_field("/"),width=5,font=("Arial",15),bg="grey",)
btn_division.grid(row=2,column=4)

btn_clear=tk.Button(calcul,text="clear", cursor = "hand2",command=lambda: clear(),width=5,font=("Arial",15),bg="grey",)
btn_clear.grid(row=6,column=2)

btn_decimal=tk.Button(calcul,text=".", cursor = "hand2",command=lambda: add_to_field("."),width=5,font=("Arial",15),bg="grey",)
btn_decimal.grid(row=6,column=1,rowspan=2,)

btn_open_parenthesis=tk.Button(calcul,text="(", cursor = "hand2",command=lambda: add_to_field("("),width=5,font=("Arial",15),bg="#a49bb8",)
btn_open_parenthesis.grid(row=5,column=2)

btn_close_parenthesis=tk.Button(calcul,text=")", cursor = "hand2",command=lambda: add_to_field(")"),width=5,font=("Arial",15),bg="#a49bb8",)
btn_close_parenthesis.grid(row=5,column=3)

btn_equal=tk.Button(calcul,text="=", cursor = "hand2",command=lambda: calculate(),width=13,font=("Arial",15),bg="grey",)
btn_equal.grid(row=6,column=3,columnspan=2)

calcul.mainloop()