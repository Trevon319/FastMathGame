import time
from tkinter import *
from PIL import ImageTk,Image
import random

main_window = Tk()
main_window.attributes('-fullscreen',True)
main_window.configure(background='#fffce8')
logo = ImageTk.PhotoImage(Image.open(r'C:\Users\goode\OneDrive\Pictures\FastMathCirc.png'))
counter = 0
correct = 0
wrong = 0





def countdown():
    #create StringVar to allow changes to the text within the label
    displayed = StringVar()

    #what the label will display for the countdown
    countdown = ['3','2','1', 'GO!!!']

    #Initialize the label to show 3 (start of the countdown
    displayed.set(countdown[0])

    #Label to display countdown
    count_label = Label(main_window, textvariable=displayed,pady=400,width=25,font=('Times New Roman',50),bg='#fffce8')
    count_label.pack()

    #start countdown
    for num in countdown:
        displayed.set(num)
        count_label.update()
        time.sleep(1)
    #close out the countdown frame
    count_label.pack_forget()


class Addition:
    def __int__(self):
        self.screen = Frame
        self.equation = Label
        self.submit_btn = Button
        self.user_answr = Entry

    def load_screen(self):
        self.op1 = random.randint(0, 9)
        self.op2 = random.randint(0, 9)
        print('check1')
        self.operands = StringVar()
        self.operands.set(f'  {self.op1}\n + {self.op2}\n--------')
        self.screen = Frame(main_window)
        self.screen.pack()
        self.equation = Label(self.screen,textvariable=self.operands)
        self.equation.pack()
        self.user_answr = Entry(self.screen,width=25)
        self.user_answr.pack()
        self.submit_btn = Button(self.screen,text='Enter',width=15,command=lambda : self.get_answer(self.operands))
        self.submit_btn.pack()

    def get_answer(self,operands):
        global counter
        global correct
        global wrong
        ansr = int(self.user_answr.get())
        self.user_answr.delete(0, END)
        cor_answer = self.op1 + self.op2
        if ansr == int(cor_answer):
            print('Correct')
            correct+=1
        else:
            wrong+=1

        self.op1 = random.randint(0,9)
        self.op2 = random.randint(0,9)
        operands.set(f'  {self.op1}\n + {self.op2}\n--------')
        print(ansr)
        print(cor_answer)
        counter+=1
        if counter == 3:
            self.close_screen()
            score_frame = Frame(main_window)
            score_frame.pack()
            Label(score_frame, text=f'You got {correct} answers correct and {wrong} answers wrong',width=50).pack()
            counter = 0
            wrong = 0
            correct = 0
            Button(score_frame,text='continue', command=lambda : [self.close_score(score_frame), start.load_screen(option)]).pack()



    def close_screen(self):
        self.screen.pack_forget()

    def close_score(self,screen):
        screen.pack_forget()













def button_pressed(selected):

    if selected.get() == 'Addition':
        play = Addition()
        play.load_screen()


class startScreen:
    def __int__(self):
        global logo
        self.start_frame = Frame
        self.logo_frame = Label
        self.quit_button = Button
        self.start_button = Button

    def load_screen(self, option_menu):

        self.start_frame = Frame(main_window, bg='#fffce8')
        self.start_frame.pack()
        self.logo_frame = Label(self.start_frame, image=logo,bg='#fffce8')
        self.logo_frame.pack()
        self.quit_button = Button(self.start_frame,text="QUIT", command=main_window.destroy).pack()
        self.start_button = Button(self.start_frame,text="START PLAYING",command=lambda : [self.close_screen(), option_menu.load_screen()]).pack()

    def close_screen(self):
        self.start_frame.pack_forget()


class optionScreen:
    def __int__(self):
        self.option_frame = Frame
        self.menu = OptionMenu
        self.select = Button

    def load_screen(self):
        self.option_frame = Frame(main_window,bg='#fffce8',pady=300)
        self.option_frame.pack()
        options = ['Addition', 'Subtraction', 'Multiplication', 'Division']
        option_list = StringVar()
        option_list.set(options[0])
        self.menu = OptionMenu(self.option_frame, option_list, *options)
        self.menu.configure(width=100,height=5,bg='#d65c68')
        self.menu.pack()

        self.select =Button(self.option_frame, text='CONTINUE',width=50, command=lambda: [self.close_screen(self.option_frame), countdown(), button_pressed(option_list)]).pack()

    def close_screen(self,frame):
        frame.pack_forget()







if __name__ == '__main__':

    option = optionScreen()
    start = startScreen()
    start.load_screen(option)

    main_window.mainloop()
