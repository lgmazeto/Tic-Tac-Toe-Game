from tkinter import *
from tkinter import messagebox

xscore = 0
oscore = 0
count = 0
player = 'X'
marks = list()
win = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
       (0, 3, 6), (1, 4, 7), (2, 5, 8),
       (0, 4, 8), (2, 4, 6)]


def _changeValue():
    global player
    if player == 'X':
        player = '0'
        _winner('X')
    else:
        player = 'X'
        _winner('0')


def _click(b):
    global player, count

    if b['text'] == '':
        b['text'] = player
        count += 1
        _changeValue()
    else:
        messagebox.showerror('Tic-Tac-Toe Game', 'This place was already selected.\n'
                                                 'Please choose another...')

    if count == 9:
        messagebox.showinfo('Tic-Tac-Toe Game', 'DRAW!\n')
        _restart()


def _winner(letter):
    global marks, player
    global xscore, oscore
    marks.clear()
    buttonsRestartValue = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    for b in buttonsRestartValue:
        marks.append(b['text'])
    for w in win:
        x = w[0]
        y = w[1]
        z = w[2]
        if marks[x] == letter and marks[y] == letter and marks[z] == letter:
            if letter == 'X':
                xscore += 1
                scoreX.configure(text='X = ' + str(xscore) + ' points')
            else:
                oscore += 1
                scoreO.configure(text='O = ' + str(oscore) + ' points')
            messagebox.showinfo('Tic-Tac-Toe Game', 'CONGRATULATIONS PLAYER ' + letter + ' WINS!')
            _restart()


def _restart():
    cont = messagebox.askquestion('Tic-Tac-Toe Game', 'Do you wanna play again?')
    if cont == 'yes':
        global count
        if count > 0:
            count = 0
        buttonsRestartValue = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
        for b in buttonsRestartValue:
            b['text'] = ''
    else:
        messagebox.showinfo('Tic-Tac-Toe Game', 'Ok, see you letter, we are closing the application.')
        root.destroy()


root = Tk()
# Window
root.title('Tic-Tac-Toe')
root.iconbitmap('assets/Ico_tic_tac_toe.ico')

# Refresh and grid
refresh = Button(root, text='Refresh', width=6, pady=5, command=_restart)
refresh.grid(row=3, column=1)

# Score and grid
scoreX = Label(root, text='X = ' + str(xscore) + ' points')
scoreX.grid(row=3, column=0)
scoreO = Label(root, text='O = ' + str(oscore) + ' points')
scoreO.grid(row=3, column=2)

# Buttons
b1 = Button(root, text='', font=('Helvetica', 20, 'bold'), width=6, height=3, bg='SystemButtonFace', command=lambda: _click(b1))
b2 = Button(root, text='', font=('Helvetica', 20, 'bold'), width=6, height=3, bg='SystemButtonFace', command=lambda: _click(b2))
b3 = Button(root, text='', font=('Helvetica', 20, 'bold'), width=6, height=3, bg='SystemButtonFace', command=lambda: _click(b3))

b4 = Button(root, text='', font=('Helvetica', 20, 'bold'), width=6, height=3, bg='SystemButtonFace', command=lambda: _click(b4))
b5 = Button(root, text='', font=('Helvetica', 20, 'bold'), width=6, height=3, bg='SystemButtonFace', command=lambda: _click(b5))
b6 = Button(root, text='', font=('Helvetica', 20, 'bold'), width=6, height=3, bg='SystemButtonFace', command=lambda: _click(b6))

b7 = Button(root, text='', font=('Helvetica', 20, 'bold'), width=6, height=3, bg='SystemButtonFace', command=lambda: _click(b7))
b8 = Button(root, text='', font=('Helvetica', 20, 'bold'), width=6, height=3, bg='SystemButtonFace', command=lambda: _click(b8))
b9 = Button(root, text='', font=('Helvetica', 20, 'bold'), width=6, height=3, bg='SystemButtonFace', command=lambda: _click(b9))

# Grid
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

root.mainloop()
