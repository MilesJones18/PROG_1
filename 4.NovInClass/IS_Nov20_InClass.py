'''
GUI Programming Introduction using tkinter

'''

import tkinter
import tkinter.messagebox


'''
Buttons - Typically a square icon that has some dimensions to it that you can click on.
Canvas - A rectangular area that is used to display graphics.
CheckButton - A button that is either on or off, and so on.
'''

'''
def window_pane():
    main_window = tkinter.Tk()

    main_window.title('GUI Program')

    main_window.mainloop()
    pass
'''

class MyGUI():
    def __init__(self):

        self.main_window = tkinter.Tk()
        self.main_window.geometry('400x400')
        self.main_window.eval('tk::PlaceWindow . center')
        self.main_window.title('MY FIRST GUI')
        #Create a window frame, which lets us group widgets together into frames.
        self.left_frame = tkinter.Frame(self.main_window)
        
        self.label = tkinter.Label(self.main_window, text='THIS IS A LABEL', borderwidth=1, relief='solid')
        self.label2 = tkinter.Label(self.main_window, text='Label 2', borderwidth=1, relief='raised')
        self.label3 = tkinter.Label(self.left_frame, text='THIS IS THE LEFT FRAME')

        self.label.pack(pady=20)
        self.label2.pack(side='bottom', ipadx=20, pady=20)
        self.label3.pack(padx=20)
        self.left_frame.pack(side='left')
        
        self.my_button = tkinter.Button(self.main_window, text='CLICK ME',)
        self.exit_button = tkinter.Button(self.main_window, text='EXIT', command=self.main_window.destroy)
        
        self.my_button.pack()
        self.exit_button.pack(side='right')

        self.prompt_label = tkinter.Label(self.left_frame, text='Enter your name please')
        self.user_name = tkinter.Entry(self.left_frame, width=10)

        self.prompt_label.pack(side='left')
        self.user_name.pack(side='left')

        self.main_window.mainloop()



if __name__ == "__main__":
    #window_pane()
    MyGUI()