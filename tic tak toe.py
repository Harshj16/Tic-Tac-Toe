#Basic tic tac toe in python with graphics
#importing modules
from tkinter import *
from tkinter import Tk, Canvas, Frame, BOTH


#making main frame window
tk = Tk()
tk.title("Tik Tac Toe")
tk.geometry("800x1000")
tk.configure(bg = "Black")
tk.iconbitmap('ttt.ico')
bclick = True #variable to switch between X and 0
flag = 0 # Increments if one button is clicked

#Quiting game
def Quit():
    from tkinter import messagebox
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        tk.destroy()
tk.protocol("WM_DELETE_WINDOW", Quit)

'''
use when you want to use play again window
#play again
def play_again():
    play_again = Tk()
    play_again.geometry("300x100")
    play_again.configure(bg = "Black")
    Label(play_again , text = "Do You want to play again " , fg = "White" , bg  = "Black", font=('times',16,'bold')).pack()
    Button(play_again,text = "Play Again" , command = start_game , fg = "Black" , bg = "Light blue" , width = 9 , height = 1 , activebackground = "white",
               font=('times',15,'bold')).place(x=90 , y = 50)
'''
      
#empty entry error
def err_screen():
    def err_delete():
        err.destroy()
    global err
    err = Tk()
    err.geometry('300x100')
    err.title('Warning!!')
    err.iconbitmap('ttt.ico')
    err.configure(background='black')
    Label(err, text='Please Enter Name', fg='white', bg='black', font=('times', 16, ' bold ')).pack()
    Button(err, text='OK', command=err_delete, fg="black", bg="lawn green", width=9, height=1, activebackground="white",
               font=('times', 15, ' bold ')).place(x=90, y=50)
        
#Play game code
def play_game():
    global Entry_player1
    global Entry_player2
    game_window = Tk()
    game_window.title("Tik Tac Toe")
    game_window.geometry("800x300")
    game_window.iconbitmap('ttt.ico')
    game_window.configure(bg = "Black")
    Label_player1 = Label(game_window , text = " 'X' \n Player Name" , bg = "Light Blue" , width = 30 , height  = 3,
                           font=('times', 10, 'italic bold ')).place(x = 10 , y = 20)
    Entry_player1 = Entry(game_window , fg = "Black"  ,font=('times', 30, 'italic bold ') ,
                           width = 20)
    Entry_player1.place(x = 250 , y = 20)
    Label_player2 = Label(game_window , text = " 'O' \n Player Name" , bg = "Light Blue" , height  = 3 , width = 30 ,
                           font=('times', 10, 'italic bold ')).place(x = 10 , y = 120)
    Entry_player2 = Entry(game_window , fg = "Black"  ,font=('times', 30, 'italic bold '),
                           width = 20)
    Entry_player2.place(x = 250 , y = 120)
    play = Button(game_window , text = 'Play Game', bg = "pink" ,fg = "black" ,command = start_game , height = 5 , width = 20 ,
                            font =('times',11,'bold')).place(x = 300 , y = 190)
    game_window.mainloop()
    
#Starting the game while displaying the name
def start_game():
    Ep1 = Entry_player1.get()
    Ep2 = Entry_player2.get()
    if Ep1 == '':     #throws error if entry box is empty
        err_screen()
    elif Ep2 == '':
        err_screen()  #throws error if entry box is empty
    else:
        play_window = Tk()
        play_window.title("Tic Tac Toe")
        play_window.configure(bg = "Black")
        play_window.iconbitmap('ttt.ico')

        #Defining the buttton as disabled at initialization
        def disableButton():
            button1.configure(state=DISABLED)
            button2.configure(state=DISABLED)
            button3.configure(state=DISABLED)
            button4.configure(state=DISABLED)
            button5.configure(state=DISABLED)
            button6.configure(state=DISABLED)
            button7.configure(state=DISABLED)
            button8.configure(state=DISABLED)
            button9.configure(state=DISABLED)
            
        #main game
        #Button click code
        import tkinter.messagebox
        def btnClick(buttons):
            global bclick, flag, Entry_player2 , Entry_player1, Ep1 , Ep2
            Ep1 = Entry_player1.get()
            Ep2 = Entry_player2.get()
            if buttons["text"] == " " and bclick == True:
                buttons["text"] = "X"
                bclick = False
                checkForWin()
                flag += 1
            elif buttons["text"] == " " and bclick == False:
                buttons["text"] = "O"
                bclick = True
                checkForWin()
                flag += 1
            else:
                tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")
        #Check for wins
        #show player1 or player2 is winner
        def checkForWin():
            if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
                button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
                button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
                button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
                button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
                button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
                button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
                button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
                button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
                disableButton()
                tkinter.messagebox.showinfo("Tic-Tac-Toe", Ep1 + "\n Player X \n Wins !:)")
                play_window.destroy()
                
            elif(flag == 8):
                tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")
                play_window.destroy()

            elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
                  button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
                  button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
                  button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
                  button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
                  button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
                  button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
                  button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
                  button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
                  disableButton()
                  tkinter.messagebox.showinfo("Tic-Tac-Toe", Ep2 + "\n Player O \n Wins !:)")
                  play_window.destroy()
                  
                  
        buttons = StringVar()
        #board
        Label(play_window , text = "Player 'X' " , bg = "Sea Green" ,height = 1 , width  = 8,
                                   font=('times', 20, 'italic bold ')).grid(row = 1 ,column = 0)
        Label(play_window , text = Ep1 , bg = "Light Blue" ,height = 1 , width  = 8,
                           font=('times', 20, 'italic bold ')).grid(row = 1 , column = 1, columnspan=8)
        Label(play_window , text = "Player 'O' " , bg = "Sea Green" ,height = 1 , width  = 8,
                           font=('times', 20, 'italic bold ')).grid(row = 2 , column  = 0)
        Label(play_window , text = Ep2 , bg = "Light Blue" ,height = 1 , width  = 8,
                           font=('times', 20, 'italic bold ')).grid(row = 2 , column  = 1, columnspan=8)

        button1 = Button(play_window, text=" ", font='Times 20 bold', bg='Black', fg='white', height=4, width=8, command=lambda: btnClick(button1))
        button1.grid(row=3, column=0)

        button2 = Button(play_window, text=' ', font='Times 20 bold', bg='Black', fg='white', height=4, width=8, command=lambda: btnClick(button2))
        button2.grid(row=3, column=1)

        button3 = Button(play_window, text=' ',font='Times 20 bold', bg='Black', fg='white', height=4, width=8, command=lambda: btnClick(button3))
        button3.grid(row=3, column=2)

        button4 = Button(play_window, text=' ', font='Times 20 bold', bg='Black', fg='white', height=4, width=8, command=lambda: btnClick(button4))
        button4.grid(row=4, column=0)

        button5 = Button(play_window, text=' ', font='Times 20 bold', bg='Black', fg='white', height=4, width=8, command=lambda: btnClick(button5))
        button5.grid(row=4, column=1)

        button6 = Button(play_window, text=' ', font='Times 20 bold', bg='Black', fg='white', height=4, width=8, command=lambda: btnClick(button6))
        button6.grid(row=4, column=2)

        button7 = Button(play_window, text=' ', font='Times 20 bold', bg='Black', fg='white', height=4, width=8, command=lambda: btnClick(button7))
        button7.grid(row=5, column=0)

        button8 = Button(play_window, text=' ', font='Times 20 bold', bg='Black', fg='white', height=4, width=8, command=lambda: btnClick(button8))
        button8.grid(row=5, column=1)

        button9 = Button(play_window, text=' ', font='Times 20 bold', bg='Black', fg='white', height=4, width=8, command=lambda: btnClick(button9))
        button9.grid(row=5, column=2)
        play_window.mainloop()
                
#about game
def about_game():
    def about_destroy():
        about.destroy()
    global about   
    about = Tk()
    about.configure(bg = "Black")
    about.geometry("800x500")
    about.title("Tic Tac Toe")
    about.iconbitmap('ttt.ico')
    message = Label(about ,text="Tic Tac Toe ", bg="slate blue", fg="black", width=50,
                   height=3, font=('times', 35, 'italic bold ')).pack()
    Disp = Label(about,text = "Tic-tac-toe (American English), noughts and crosses (British English), or\n Xs and Os is a paper-and-pencil game for two players,\n X and O, who take turns marking the spaces in a 3×3 grid.\n The player who succeeds in placing three of their marks in a \n horizontal, vertical, or diagonal row is the winner." ,
                   width = 85 , height = 6 , bg = "Black" , fg = "White" ,font = ('times' , 10 , 'italic bold')).place(x= 80 , y = 200)
    about_button = Button(about , text = "Back" , bg = "Dark Orange" , fg = "black" , height = 3 , width = 20  ,command = about_destroy,
                            font =('times',11,'bold')).place(x = 300 , y = 300)

    
    

#making menu
message = Label(tk ,text="Tic Tac Toe ", bg="slate blue", fg="black", width=50,
                   height=3, font=('times', 35, 'italic bold ')).pack()
play_button = Button(text = 'Play Game', bg = "dark orange" ,fg = "black" ,command = play_game , height = 5 , width = 20 , anchor = "center" ,
               font =('times',13,'bold')).place(x = 270 , y = 170)
about = Button(text = 'About Game', bg = "Dark orange" ,fg = "black" ,command = about_game , height = 5 , width = 20 ,
              font =('times',13,'bold')).place(x = 270 , y = 290)
Quit_main = Button(text = 'Quit', bg = "Dark orange" ,fg = "black" ,command = Quit , height = 5 , width = 20 ,
              font =('times',13,'bold')).place(x = 270 , y = 410)
tk.mainloop()