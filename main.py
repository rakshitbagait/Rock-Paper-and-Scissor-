from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import random

class RPS(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x600")
        self.config(bg="red")

        self.player_score =0
        self.comp_score =0
        self.rock_img = Image.open("fist.png").resize((60,60))
        self.resized_rock = ImageTk.PhotoImage(self.rock_img)

        self.paper_img = Image.open("paper.png").resize((60,60))
        self.resized_paper = ImageTk.PhotoImage(self.paper_img)

        self.scissors_img = Image.open("scissors.png").resize((60,60))
        self.resized_scissors = ImageTk.PhotoImage(self.scissors_img)


        self.rock_button = Button(image=self.resized_rock,bd=0,background="red",activebackground="white",command=lambda:self.players_hand(self.resize_rock))
        self.rock_button.place(x=50,y=500)
        
        self.paper_button = Button(image=self.resized_paper,bd=0,background="red",activebackground="white",command=lambda:self.players_hand(self.resize_paper))
        self.paper_button.place(x=150,y=500)

                
        self.scissors_button = Button(image=self.resized_scissors,bd=0,background="red",activebackground="white",command=lambda:self.players_hand(self.resize_scissors))
        self.scissors_button.place(x=250,y=500)

        self.you_label = Label(text=f"You:{self.player_score}",background="red",font=("Arial",20,"bold"))
        self.you_label.place(x= 150,y=450)

        self.computer_label = Label(text=f"Computer:{self.comp_score}",background="red",font=("Arial",20,"bold"))
        self.computer_label.place(x=130,y=20)
        self.rock = Image.open("fist.png").resize((100,100))
        self.resize_rock = ImageTk.PhotoImage(self.rock)

        self.paper = Image.open("paper.png").resize((100,100))
        self.resize_paper = ImageTk.PhotoImage(self.paper)

        self.scissors = Image.open("scissors.png").resize((100,100))
        self.resize_scissors = ImageTk.PhotoImage(self.scissors)
        self.computer_gesture = Label(image=self.resize_paper,height=120,width=120,bg="white")
        self.computer_gesture.place(x=150,y=100)
        self.player_gesture = Label(image=self.resize_paper,height=120,width=120,bg="white")
        self.player_gesture.place(x=150,y=300)
        self.choices = (self.resize_scissors,self.resize_rock,self.resize_paper)

        self.result_label = Label(text="Begin",background="red",font=("Arial",12))
        self.result_label.place(x=50,y=250,height=20,width=300)
    def players_hand(self,user_choices):
        self.computer_choice = random.choice(self.choices)

        self.player_gesture.config(image=user_choices)
        self.computer_gesture.config(image=self.computer_choice)


        if user_choices == self.computer_choice:
            self.result_label.config(text="Tie")
        

            
        elif (user_choices == self.resize_rock and self.computer_choice == self.resize_scissors) or \
             (user_choices == self.resize_scissors and self.computer_choice == self.resize_paper) or \
             (user_choices == self.resize_paper and self.computer_choice == self.resize_rock):
            self.result_label.config(text="You Win !")
            self.player_score +=1
            self.you_label.config(text=f"You:{self.player_score}")
        else:
            self.result_label.config(text="Computer win")
            self.comp_score +=1
            self.computer_label.config(text=f"Computer:{self.comp_score  }")

        if self.player_score ==3:
            self.result_label.config(text="You won the game")
            show_message = messagebox.askquestion("game over","You won the game! Do you want to play again")
      
            if show_message == "yes":
                self.player_score = 0
                self.you_label.config(text=f"You:{self.player_score}")
                self.comp_score = 0
                self.computer_label.config(text=f"Computer:{self.comp_score  }")  
            else :
                self.quit()
        elif self.comp_score==3:
            self.result_label.config(text="computer won the game")
            show_message = messagebox.askquestion("game over","Computer won the game! Do you want to play again")

            if show_message == "yes":
                self.player_score = 0
                self.you_label.config(text=f"You:{self.player_score}")
                self.comp_score = 0
                self.computer_label.config(text=f"Computer:{self.comp_score  }")
            else:
                self.quit()

        
            
app = RPS()
app.mainloop()