import tkinter as tk
from tkinter import ttk
import numpy as np

from bankers import *
from page_rep import *
from diskscheduling import *
from processsynch import *
from memoryalloc import *
from procscheduling import *
from descriptions import *

def main():
    mainwindow = tk.Tk()
    mainwindow.title("OS Simulator")
    mainwindow.minsize(600, 700)

    frame = tk.Frame(mainwindow)
    frame.pack(padx=10, pady=10)
    bankers_btn = tk.Button(frame, text="Banker's Algorithm", command=getinputBankers)
    bankers_btn.pack(side=tk.LEFT)
    CreateToolTip(bankers_btn, text = 'Generates a single safe sequence\n'
                 'Requires matrix input. Press tab to go to next input field faster!')
    desc = tk.Button(frame, text="Summary", command=bankers_desc)
    desc.pack(side=tk.LEFT)


    frame = tk.Frame(mainwindow)
    frame.pack(padx=10, pady=10)
    pagerep_btn = tk.Button(frame, text="Process Scheduling methods", command=scheduling)
    pagerep_btn.pack(side=tk.LEFT)
    CreateToolTip(pagerep_btn, text = 'Generates analysis of process scheduling methods\n'
                 'Gives turnaround time, waiting time, response time, and other statistics\n'
                 'for FCFS, SJF, SRTF, RR, preemptive and non preemptive Priority scheduling.')
    desc = tk.Button(frame, text="Summary", command=proc_desc)
    desc.pack(side=tk.LEFT)


    frame = tk.Frame(mainwindow)
    frame.pack(padx=10, pady=10)
    pagerep_btn = tk.Button(frame, text="Page replacement methods", command=getinputPagerep)
    pagerep_btn.pack(side=tk.LEFT)
    CreateToolTip(pagerep_btn, text = 'Generates analysis of page replacement methods\n'
                 'Gives number of page faults and frame contents for FIFO, LRU and OPTIMAL.')
    desc = tk.Button(frame, text="Summary", command=page_rep_desc)
    desc.pack(side=tk.LEFT)

    frame = tk.Frame(mainwindow)
    frame.pack(padx=10, pady=10)
    pagerep_btn = tk.Button(frame, text="Memory Allocation methods", command=getinputMA)
    pagerep_btn.pack(side=tk.LEFT)
    CreateToolTip(pagerep_btn, text = 'Generates analysis of Memory Allocation methods\n'
                 'Gives fragmentation, block allocation for first fit, best fit and worst fit.')
    desc = tk.Button(frame, text="Summary", command=MemAlloDesc)
    desc.pack(side=tk.LEFT)



    frame = tk.Frame(mainwindow)
    frame.pack(padx=10, pady=10)
    disksched_btn = tk.Button(frame, text="Disk Scheduling methods", command=diskSchedulingMain)
    disksched_btn.pack(side=tk.LEFT)
    CreateToolTip(disksched_btn, text = 'Disk Schedluing Implementation\n'
                 'Output is in textboxes')
    desc = tk.Button(frame, text="Summary", command=disk_desc)
    desc.pack(side=tk.LEFT)

    frame = tk.Frame(mainwindow)
    frame.pack(padx=10, pady=10)
    dinnerp = tk.Button(frame, text="Dining Philosopher", command = dp)
    dinnerp.pack(side=tk.LEFT)
    CreateToolTip(dinnerp, text = 'This is a simulation\n'
                 'Delay of 3 seconds to generate output\n'
                 'Simulates 5 philosophers in the dining philosophers problem')
    desc = tk.Button(frame, text="Summary", command=dining_p_desc)
    desc.pack(side=tk.LEFT)
    
    frame = tk.Frame(mainwindow)
    frame.pack(padx=10, pady=10)
    sleepyb = tk.Button(frame, text="Sleeping Barbers", command = sb)
    sleepyb.pack(side=tk.LEFT)
    CreateToolTip(sleepyb, text = 'This is a simulation\n'
                 'Delay of a few seconds to generate output\n'
                 'Simulates 50 customers and 3 barbers in the sleeping barbers problem')
    desc = tk.Button(frame, text="Summary", command=sleeping_b_desc)
    desc.pack(side=tk.LEFT)

    credits_frame = tk.Frame(mainwindow, background='gray')
    credits_frame.pack(padx=10, pady=10, fill='both', expand=tk.YES)

    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox('all'))

    canvas = tk.Canvas(credits_frame, background='gray')
    canvas.pack(side=tk.LEFT, fill='both', expand=tk.YES)

    scrollbar = tk.Scrollbar(credits_frame, command=canvas.yview)
    scrollbar.pack(side=tk.LEFT, fill='y')

    canvas.configure(yscrollcommand = scrollbar.set)

    canvas.bind('<Configure>', on_configure)


    frame = tk.Frame(canvas, background='gray')
    canvas.create_window((0,0), window=frame, anchor='nw')


    lbl = tk.Label(frame, text="OS Simulator Project", font="-size 30", background='gray')
    lbl.pack()

    tbox = tk.Text(frame, background='gray', wrap=tk.WORD)
    tbox.pack()
    tbox.insert(tk.INSERT, "This project is submitted to Shashidhar sir, Anappa Sir, and \nAnkit Sir, of the Computer Science department of NITK, Surathkal, \nas part of the course requirements for CS255, Operating Systems\n\n")

    tbox.insert(tk.INSERT, "This project is a collection of decision-making algorithms used in \nOperating Systems.\n\nSubmitted by:\n")

    tbox.insert(tk.INSERT, "181CO111: Ashish Reddy\t\t\t  181CO112: Atul Kailas Patil\n181CO113: Bhadra Giri\t\t\t   181CO115: Chethan L Naik\n181CO116: Danish Waseem\t\t\t 181CO118: Dhiraj Lokesh\n \t\t\t   181CO119: Feyaz Baker\n")

    tbox.insert(tk.INSERT, "\nSubmitted on\n28th May 2020\n")

    tbox.config(state='disabled')

    mainwindow.mainloop()

if __name__ == "__main__":
    main()