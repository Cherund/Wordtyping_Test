from tkinter import *
from english_words import english_words_lower_set
import random
import time

words_list = list(english_words_lower_set)
typed_words_dict: dict
start_time: float


def start_game():
    global start_time, typed_words_dict
    typed_words_dict = {}
    start_button.pack_forget()
    start_time = time.time()
    typed_word_entry.pack()
    stop_button.pack()
    next_word()


def next_word():
    correct_word = random.choice(words_list)
    text_label.config(text=correct_word)


def add_word(entry):
    typed_word = typed_word_entry.get()
    typed_words_dict[text_label['text']] = typed_word
    typed_word_entry.delete(0, END)
    next_word()


def stop():
    words_per_minute = round((len(typed_words_dict)/(time.time() - start_time)) * 60, 2)
    typos_str = ''

    for word in typed_words_dict:
        if word != typed_words_dict[word]:
            typos_str += f'You typed {typed_words_dict[word]} instead of {word}\n'

    if typos_str == '':
        text_label.config(text=f'You speed is {words_per_minute} words per minute!\n'
                               f'And you did not make any typos!')
    else:
        text_label.config(text=f'You speed is {words_per_minute} words per minute!\n'
                               f'Here is your typos:\n {typos_str}')

    typed_word_entry.pack_forget()
    stop_button.pack_forget()
    typed_word_entry.delete(0, END)
    start_button['text'] = 'Restart'
    start_button.pack()


window = Tk()
window.title('Typing Speed Test')
window.config(pady=20, padx=20)
window.minsize(height=300, width=600)


title_label = Label(text='Typing Speed Test!', font=('Montserrat', 40), pady=20)
title_label.pack()

text_label = Label(text='Your have to type as fast as you can.\n'
                        'After you press the start button the word will appear.\n'
                        'You have to type it in entry field, and press Return to submit it.\n'
                        '',
                   font=('Montserrat', 20), pady=20)
text_label.pack()

start_button = Button(text='Start', command=start_game)
start_button.pack()

typed_word_entry = Entry(width=40)
typed_word_entry.bind('<Return>', add_word)

stop_button = Button(text='Stop', command=stop)
window.mainloop()
