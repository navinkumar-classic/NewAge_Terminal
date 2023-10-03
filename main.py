import customtkinter
import tkinter as tk


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

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
        self.text_font = ("NEOTERIC", 20, 'bold')
        self.history_text = []

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
        self.command = customtkinter.CTkTextbox(self.tabs.tab("Terminal"), height=40,font = self.text_font)
        self.command.pack(fill = "both",padx = 10,pady = 5)
        self.command.insert("0.0","PS C:User\Lenovo$>- ")

        #create the run button
        self.button = customtkinter.CTkButton(self.tabs.tab("Terminal"),text = "Run",command = self.bt_func)
        self.button.place(relx = 0.5,rely = 0.26,anchor = tk.CENTER)
        self.button.configure(font=self.menu_font)

        #create the output textbox
        self.outbox = customtkinter.CTkTextbox(self.tabs.tab("Terminal"), height=600,font = self.text_font)
        self.outbox.pack(fill = "both",padx = 10,pady = 45)
        self.outbox.configure(state = "disabled")

        #create the stuff in History tab
        #create the history textbox
        self.historybox = customtkinter.CTkTextbox(self.tabs.tab("History"),font = self.text_font)
        self.historybox.pack(fill = "both",padx = 10,pady = 10,expand =True)
        self.historybox.configure(state = "disabled")

    #create a function for run button
    def bt_func(self):

        #enable these textboxes
        self.historybox.configure(state = "normal")
        self.outbox.configure(state = "normal")

        #clears the historybox and outbox
        self.historybox.delete("0.0","end")
        self.outbox.delete("0.0","end")

        #gets the command calculate the output and print it 
        tex = self.command.get("0.0","end")
        self.outbox.insert("0.0","executing a random command")

        #updates the command line
        self.command.delete("0.0","end")
        self.command.insert("0.0","PS C:User\Lenovo$>- ")

        #updates the history 
        self.history_text.append(tex)
        history_text = ''.join(self.history_text[::-1])
        self.historybox.insert("0.0",text=history_text)

        #disable these textboxes 
        self.historybox.configure(state = "disabled")
        self.outbox.configure(state = "disabled")

def main():
    app = App()
    app.mainloop()

main()