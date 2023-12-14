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
        self.addition_screen_frame = Frame
        self.equation = Label
        self.submit_btn = Button
        self.user_answer = Entry

    def load_screen(self):
        #create operators that will be random integers 0-9
        self.op1 = random.randint(0, 9)
        self.op2 = random.randint(0, 9)

        #creates variable that will allow the displayed equation to
        #change once the user enters their answer
        self.operands = StringVar()
        self.operands.set(f'  {self.op1}\n + {self.op2}\n--------')#how equation is formatted

        #create frame to hold widgets
        self.addition_screen_frame = Frame(main_window)
        self.addition_screen_frame.pack()

        #creates label to display the equation
        self.equation = Label(self.addition_screen_frame, textvariable=self.operands)
        self.equation.pack()

        #creates entry box for the user to type an answer
        self.user_answer = Entry(self.addition_screen_frame, width=25)
        self.user_answer.pack()

        #creates button that when pressed, calls the (get_answer)function, which checks the user answer and displays a new equation
        self.submit_btn = Button(self.addition_screen_frame, text='Enter', width=15, command=lambda : self.get_answer(self.operands))
        self.submit_btn.pack()

#   Checks user answer
    #updates score
    #displays new equation
    def get_answer(self,operands):
        global counter #tracks number of answers attemted
        global correct #tracks correct answers
        global wrong   #tracks wrong answers

        #gets user answer from entry box
        user_answer = int(self.user_answer.get())

        #clears the entry box
        self.user_answer.delete(0, END)

        #checks if user's answer is correct and updates their score
        correct_answer = self.op1 + self.op2
        if user_answer == int(correct_answer):
            correct+=1
        else:
            wrong+=1

        #gets new numbers to be displayed for next equation
        self.op1 = random.randint(0,9)
        self.op2 = random.randint(0,9)
        operands.set(f'  {self.op1}\n + {self.op2}\n--------')
        counter+=1

        #ends game once x questions have been attempted
        #then displays score
        #continue button takes user back to option screen
        if counter == 3:
            self.close_screen()
            score_frame = Frame(main_window)
            score_frame.pack()
            Label(score_frame, text=f'You got {correct} answers correct and {wrong} answers wrong',width=50).pack()
            counter = 0
            wrong = 0
            correct = 0
            Button(score_frame,text='continue', command=lambda : [self.close_score(score_frame), option.load_screen()]).pack()

    def close_screen(self):
        self.addition_screen_frame.pack_forget()

    def close_score(self,screen):
        screen.pack_forget()


#function takes what the user selected in the option menu as parameter
#Then loads the game mode selected
def option_button_pressed(selected):
    if selected.get() == 'Addition':
        play = Addition()
        play.load_screen()


class startScreen:
    def __int__(self):
        #get game logo
        global logo
        self.start_frame = Frame
        self.logo_frame = Label
        self.quit_button = Button
        self.start_button = Button

    def load_screen(self, option_menu):
        #create frame to hold all starting screen widgets
        self.start_frame = Frame(main_window, bg='#fffce8')
        self.start_frame.pack()

        #create widget to hold the logo
        self.logo_frame = Label(self.start_frame, image=logo,bg='#fffce8')
        self.logo_frame.pack()

        #button to exit the game
        self.quit_button = Button(self.start_frame,text="QUIT", command=main_window.destroy).pack()

        #when start button is pressed, first close the starting screen frame, then load the option menu
        self.start_button = Button(self.start_frame,text="START PLAYING",command=lambda : [self.close_screen(), option_menu.load_screen()]).pack()


    def close_screen(self):
        self.start_frame.pack_forget()


class optionScreen:
    def __int__(self):
        self.option_menu_frame = Frame
        self.menu = OptionMenu
        self.select_mode = Button

    def load_screen(self):
        #create frame to hold option menu widgets
        self.option_menu_frame = Frame(main_window, bg='#fffce8', pady=300)
        self.option_menu_frame.pack()

        #list of game possible game modes
        options = ('Addition', 'Subtraction', 'Multiplication', 'Division')

        #variable to hold game mode options
        option_list = StringVar()
        option_list.set(options[0])

        #creates drop menu with game modes
        self.menu = OptionMenu(self.option_menu_frame, option_list, *options)
        self.menu.configure(width=100,height=5,bg='#d65c68')
        self.menu.pack()

        #When continue button is pressed, 1.close out the option frame
        #2. call the coutdown function
        #3. load the game mode that the user selected
        self.select_mode =Button(self.option_menu_frame, text='CONTINUE', width=50, command=lambda: [self.close_screen(self.option_menu_frame), countdown(), option_button_pressed(option_list)]).pack()

    def close_screen(self,frame):
        frame.pack_forget()







if __name__ == '__main__':
    #create object that will load option screen
    option = optionScreen()

    #create start screen
    start = startScreen()

    #load the start screen which will open the option menu
    start.load_screen(option)

    main_window.mainloop()
