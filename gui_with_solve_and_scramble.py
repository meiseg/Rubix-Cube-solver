"""
Install the libraries below 
pip install pyserial
pip install tk

"""
import tkinter as tk
import serial
import random
from cube import cube
from time import sleep


#change this into com# whatever number arduino is shown for you 
port_ard = '/dev/cu.usbserial-14140' 
s = serial.Serial(port=port_ard, baudrate=57600)
senior = cube()
def solution():

    senior.solve()
    write_arduino(senior.sol_ard)

def scramble():
    senior.scramble()
    write_arduino(senior.scam)


def write_arduino(args):
    senior(args)
    s.flush()
    args += "\n"
    
    s.write(bytes(args,"UTF-8"))

button_list = []


m = tk.Tk()
m.configure(bg="black")
steps_mov = tk.DoubleVar()
left = tk.Button(m,text="LEFT",width=25,height=10,command=lambda:write_arduino("L "))
left.grid(row=0, column=0,padx=10,pady=5)
button_list.append(left)
right = tk.Button(m,text="RIGHT",width=25,height=10,command=lambda:write_arduino("R "))
right.grid(row=0, column=1,padx=10,pady=5)
button_list.append(right)
Up = tk.Button(m,text="UP",width=25,height=10,command=lambda:write_arduino("U "))
Up.grid(row=0,column=2,padx=10,pady=5)
button_list.append(Up)
down = tk.Button(m,text="DOWN",width=25,height=10,command=lambda:write_arduino("D "))
down.grid(row=0,column=3,padx=10,pady=5)
button_list.append(down)
front = tk.Button(m,text="FRONT",width=25,height=10,command=lambda:write_arduino("F "))
front.grid(row=0,column=4,padx=10,pady=5)
button_list.append(front)
back = tk.Button(m,text="BACK",width=25,height=10,command=lambda:write_arduino("B "))
back.grid(row=0,column=5,padx=10,pady=5)
button_list.append(back)


#prime buttons 
left_prime = tk.Button(m,text="LEFT PRIME",width=25,height=10,command=lambda:write_arduino("L'"))
left_prime.grid(row=1,column=0,padx=10,pady=5)
button_list.append(left_prime)
right_prime = tk.Button(m,text="RIGHT PRIME",width=25,height=10,command=lambda:write_arduino("R'"))
right_prime.grid(row=1,column=1,padx=10,pady=5)
button_list.append(right_prime)
upper_prime = tk.Button(m,text="UP PRIME",width=25,height=10,command=lambda:write_arduino("U'"))
upper_prime.grid(row=1,column=2,padx=10,pady=5)
button_list.append(upper_prime)
down_prime = tk.Button(m,text= "DOWN PRIME",width=25,height=10,command=lambda:write_arduino("D'"))
down_prime.grid(row=1,column=3,padx=10,pady=5)
button_list.append(down_prime)
front_prime = tk.Button(m,text="FRONT PRIME",width=25,height=10,command=lambda:write_arduino("F'"))
front_prime.grid(row=1,column=4,padx=10,pady=5)
button_list.append(front_prime)
back_prime = tk.Button(m,text="BACK PRIME",width=25,height=10,command=lambda:write_arduino("B'"))
back_prime.grid(row=1,column=5,padx=10,pady=5)
button_list.append(back_prime)


stepps = tk.Scale(m,variable=steps_mov,from_= 45, to=55,orient="horizontal")
scam = tk.Button(m,text="SCRAMBLE",height=10,width=25,command=scramble)
scam.grid(row=2,column=2,pady=50)
button_list.append(scam)
sol = tk.Button(m, text="SOLVE", height=10, width=25,command=solution)
sol.grid(row=2, column=3,pady=50)
button_list.append(sol)


for i in button_list:
    i.configure(font=("Arial",14),height=5,width=13)


m.mainloop()