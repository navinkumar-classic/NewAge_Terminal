import customtkinter
import tkinter as tk
from back import *
import keyboard
from data_structures import CQueue
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

#disabling enter key
#key="enter" 
#keyboard.block_key(key)

os.chdir("C:\\Users")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.geometry("780x480")
        self.title("Terminal")
        self.resizable(width=False,height=False)
        

        #fonts
        self.menu_font = ("Robot 9000", 15, 'bold')
        self.text_font = ("Libel Suit Rg", 18, 'bold')
        self.history_text = []
        self.queue = CQueue(5)

        #create tabs
        self.tabs = customtkinter.CTkTabview(self)
        self.tabs.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.tabs.pack(padx = 20, pady = 10,fill = "both",expand = True)
        self.tabs._segmented_button.configure(font=self.menu_font)

        #add tabes
        self.tabs.add("Terminal")
        self.tabs.add("History")

        #create the stuff in terminal tab
        #print the command line: title
        self.cmd_title = customtkinter.CTkTextbox(self.tabs.tab("Terminal"),height = 10,width=8,font = self.menu_font,fg_color="transparent")
        self.cmd_title.pack(fill = "both",padx = 10,pady = 0)
        self.cmd_title.insert("0.0","Command Line: ")
        self.cmd_title.configure(state = "disabled")

        #create a textbox for the command
        self.command = customtkinter.CTkTextbox(self.tabs.tab("Terminal"), height=40, font = self.text_font, activate_scrollbars= False)
        self.command.pack(fill = "both",padx = 10,pady = 5)
        self.command.insert("0.0",text = get_shrt_dir(os.getcwd()) + ">$ ")
        self.command.configure(wrap=None)
        self.command.bind('<Shift_R>',command = self.shift_cycle)
        self.command.bind('<Return>',command = self.Enter_func)
        

        #create the run button
        self.button = customtkinter.CTkButton(self.tabs.tab("Terminal"),text = "Run",command = self.bt_func)
        self.button.place(relx = 0.5,rely = 0.25,anchor = tk.CENTER)
        self.button.configure(font=self.menu_font)

        #create the output textbox
        self.outbox = customtkinter.CTkTextbox(self.tabs.tab("Terminal"), height=600,font = self.text_font)
        self.outbox.pack(fill = "both",padx = 10,pady = 45)
        self.outbox.configure(state = "disabled")

        #creating button for changing system mode
        self.switch_var_1 = customtkinter.StringVar(value = "on")
        self.switch_1 = customtkinter.CTkSwitch(master = self.tabs.tab("Terminal"), text = "App Mode",command = self.switch_appmode
                                                ,variable = self.switch_var_1, onvalue = "on", offvalue = "off",border_color= "transparent")
        self.switch_1.place(relx = 0.7,rely = 0.954,anchor = tk.CENTER)
        self.switch_1.configure(font=self.menu_font)

        #creating button for directory mode
        self.switch_var_2 = customtkinter.StringVar(value = "on")
        self.switch_2 = customtkinter.CTkSwitch(master = self.tabs.tab("Terminal"), text = "Directory Mode",command = self.switch_dirmode
                                                ,variable = self.switch_var_2, onvalue = "on", offvalue = "off",border_color= "transparent")
        self.switch_2.place(relx = 0.25,rely = 0.954,anchor = tk.CENTER)
        self.switch_2.configure(font=self.menu_font)

        #create the stuff in History tab
        #create the history textbox
        self.historybox = customtkinter.CTkTextbox(self.tabs.tab("History"),font = self.text_font)
        self.historybox.pack(fill = "both",padx = 10,pady = 10,expand =True)
        self.historybox.configure(state = "disabled")

    #create a function for run button
    def bt_func(self,event = None):

        #enable these textboxes
        self.historybox.configure(state = "normal")
        self.outbox.configure(state = "normal")

        #clears the historybox and outbox
        self.historybox.delete("0.0","end")
        self.outbox.delete("0.0","end")

        #gets the command calculate the output and print it 
        tex = self.command.get("0.0","end")
        clean = clean_cmd(tex)
        out = run_cmd(clean)
        self.outbox.insert("0.0",text = out)

        #updates queue
        bool = self.queue.enqueue(clean_cmd(tex[:]))
        if bool == False:
            temp = self.queue.dequeue()
            bool_temp = self.queue.enqueue(clean_cmd(tex[:]))

        #updates the command line
        #checks the directory mode and choses the directory 
        if self.switch_var_2.get() == "on": tmp_dir = get_shrt_dir(os.getcwd())
        else: tmp_dir = os.getcwd()
        self.command.delete("0.0","end")
        self.command.insert("0.0",text = tmp_dir + ">$ ")
            

        #updates the history 
        self.history_text.append(tex)
        history_text = ''.join(self.history_text[::-1])
        self.historybox.insert("0.0",text=history_text)

        #disable these textboxes 
        self.historybox.configure(state = "disabled")
        self.outbox.configure(state = "disabled")

    #implements the circular queue with shift key
    def shift_cycle(self,event = None):

        #getting the current command and storing it
        tex = clean_cmd(self.command.get("0.0","end"))
        self.command.delete("0.0","end")

        #dequeing the command in queue and enqueue the current command
        next_cmd = self.queue.dequeue()
        self.queue.enqueue(tex[:])
        if self.switch_var_2.get() == "on": tmp_dir = get_shrt_dir(os.getcwd())
        else: tmp_dir = os.getcwd()
        self.command.insert("0.0",text = tmp_dir + ">$ " + next_cmd)
    
    #binds the run button function to enter and disables new line
    def Enter_func(self,event = None):
        self.bt_func()
        return "break"
    
    #creates the switch function for app mode switch
    def switch_appmode(self,event = None):

        #if the switch mode is on then its dark mode if its off its light mode
        if self.switch_var_1.get() == "on":
            customtkinter.set_appearance_mode("dark")      
        else:
            customtkinter.set_appearance_mode("light")

    #creates the switch function for changing the directory mode
    def switch_dirmode(self,event = None):

        #if the switch is on then get the command and show shorthen the directory
        if self.switch_var_2.get() == "on":
            cln_command = clean_cmd(self.command.get("0.0","end"))
            self.command.delete("0.0","end")
            self.command.insert("0.0",text = get_shrt_dir(os.getcwd()) + ">$ " + cln_command)

        #if the switch is off then get the command and show the full directory
        else:
            cln_command = clean_cmd(self.command.get("0.0","end"))
            self.command.delete("0.0","end")
            self.command.insert("0.0",text = os.getcwd() + ">$ " + cln_command)

def main():
    app = App()
    app.mainloop()

main()
