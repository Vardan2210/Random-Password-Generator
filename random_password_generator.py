import random
from tkinter import *
from tkinter import messagebox
def numbers_pass(password):
    number=random.randint(0,10)
    number=str(number)
    password=password+number
    return password
def words_pass(listofwords,password):
    word_index=random.randint(0, 466550)
    word= listofwords[word_index].rstrip("\n")
    password=password+word
    return password
def alpha_pass(listofalpha, password):
    alpha_index=random.randint(0,32)
    alpha=listofalpha[alpha_index].rstrip("\n")
    password=password+alpha
    return password

word_file= open("words.txt", "r")
alpha_file=open("alphanumericals.txt", "r")
content_word=word_file.readlines()
content_alpha=alpha_file.readlines()
password = ""
for i in range (0,2):
    password=words_pass(content_word, password)
    password=numbers_pass(password)
    password=alpha_pass(content_alpha, password)

window= Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
window.withdraw()

messagebox.showinfo('Password-', password)

window.deiconify()
window.destroy()
window.quit()

word_file.close()
alpha_file.close()