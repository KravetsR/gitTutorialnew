'''План виконання проекту:
1) Створити вікно
2) Малюємо фон клітинку
3) Привітання з гравцем, описуємо правила гри
4) Створюємо список слів
5) В слові виводимо першу та останню букву
6) Створюємо список букв
7) Створюємо кнопки з буквами
8) Перевіряємо відповідь
9) Малюємо частини тіла '''

from tkinter import *
import random

root = Tk()
root.title("Вгадай слово")
canvas = Canvas(root, width= 700, height= 600)
canvas.pack()

def but():
    y = 0
    while y < 600:
        x = 0
        while x < 700:
            canvas.create_rectangle(x, y, x + 33, y + 27, fill="#DCFFFA", outline="blue")
            x += 33
        y += 27
    canvas.create_line(10, 10, 10, 330, width= 7, fill="blue")
    canvas.create_line(10, 10, 200, 10, width= 7, fill="blue")
    canvas.create_line(10, 60, 80, 10, width= 5, fill="blue")
#but()        
rules = '''Привіт! Давай зіграємо в гру.
Вгадуй слова та залишися в живих =)
Слова на тему: природа '''
canvas.create_text(330, 240, text= rules, fill='red', font=('Georgia', '20'))
#Створюємо слова
words = ['водоспад','антилопа', 'магнолія', 'біологія', 'обліпиха', 'галявина','горобець','барвінок']

def ran():
    but()
    word =random.choice(words)
    a = word[1 : -1]
    slovo = []
    for i in a:
        slovo.append(i)
    a0 = canvas.create_text(282, 40, text= word[0], fill= '#0004FF', font= ('Georgia', '23'))
    a1 = canvas.create_text(315, 40, text= '_' , fill= '#0004FF', font= ('Helvetica', '19'))
    a2 = canvas.create_text(347, 40, text= '_' , fill= '#0004FF', font= ('Helvetica', '19'))
    a3 = canvas.create_text(380, 40, text= '_' , fill= '#0004FF', font= ('Helvetica', '19'))
    a4 = canvas.create_text(412, 40, text= '_' , fill= '#0004FF', font= ('Helvetica', '19'))
    a5 = canvas.create_text(444, 40, text= '_' , fill= '#0004FF', font= ('Helvetica', '19'))
    a6 = canvas.create_text(477, 40, text= '_' , fill= '#0004FF', font= ('Helvetica', '19'))
    a7 = canvas.create_text(510, 40, text= word[-1] , fill= '#0004FF', font= ('Helvetica', '19'))
    list1 = [1, 2, 3, 4, 5, 6]
    abc ='абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    error = []
    win = []

    def alfavit(v):
        ''' добавляє в список вгадані букви'''
        ind_alf = abc.index(v)
        key = abc[ind_alf]
        if v in slovo :
            ind = slovo.index(v)
            add = list1[ind]
            slovo[ind] ='1'

            def kord():
                '''Створює в заданому місці'''
                if add == 1:
                    x, y = 315, 40
                if add == 2:
                    x, y = 347, 40
                if add == 3:
                    x, y = 380, 40
                if add == 4:
                    x, y = 412, 40
                if add == 5:
                    x, y = 444, 40
                if add == 6:
                    x, y = 477, 40
                return x, y

            x, y = kord()
            win.append(v)
            text = canvas.create_text(x, y, text=a[ind], fill ='#0004FF', font=('Helvetica', '19'))
            btn[key]['bg'] = 'green'

            if not v in slovo:
                btn[key]['state'] = 'disabled'
            if v in slovo:
                win.append(v)
                ind2 = slovo.index(v)
                add = list1[ind2]
                x, y =kord()
                canvas.create_text(x, y, text=a[ind2], fill ='#0004FF', font=('Helvetica', '19'))
            if len(win) == 6:
                canvas.create_text(340, 310, text ='Вітаю, ви перемогли', fill ='red', font=('Helvetica', '23'))
                for v in abc:
                    btn[i]['state'] = 'disabled'
        else:
            error.append(v)
            btn[key]['bg']='red'
            btn[key]['state'] = 'disabled'
            
            if len(error) == 1:
                head()
            elif len(error) == 2:   
                body()
            elif len(error) == 3:
                hand_l()
            #elif len(er) == 4:        
                hand_p()
            elif len(error) == 4:
                leg_l()
            #elif len(er) == 6:
                leg_p()
                end()
            root.update()

    btn = {}
    def gen(z, x, y):
        ''' кнопки для букв'''
        btn[z] = Button(root, text=z, width=3, height=1, command= lambda: alfavit(z))
        btn[z].place(x = str(x), y = str(y))        
    x = 265
    y =110
    for i in abc[0:8]:
        gen(i, x, y)
        x = x + 33
    x = 265
    y = 137
    for i in abc[8:16]:
        gen(i, x, y)
        x += 33
    x = 265
    y = 164
    for i in abc[16:24]:
        gen(i, x, y)
        x += 33    
    x = 265
    y = 191
    for i in abc[24:33]:
        gen(i, x, y)
        x += 33   

    def head():
        canvas.create_oval(80, 60, 120, 80, width= 3, fill='#FFD387')
        root.update()    
    def body():
        canvas.create_rectangle(95, 80, 105, 200, width= 3 ,fill='#4B51FF')
        root.update()
    def hand_l():
         canvas.create_line(100, 80, 45, 100, width= 4)
         root.update()   
    def hand_p():
         canvas.create_line(100, 80, 145, 100, width= 4)
         root.update()
    def leg_l():
         canvas.create_line(100, 200, 45, 300, width= 4)
         root.update()
    def leg_p():
         canvas.create_line(100, 200, 145, 300, width= 4)
         canvas.create_line(100, 10, 100, 60, width= 4)
         root.update()
        


    def end():
        canvas.create_text(340, 310, text='Ви програли', fill='red', font=('Helvetica','19'))
        for i in abc:
            btn[i]['state'] = 'disabled'
#Пропонуємо почати гру
button_1 = Button(root, text='Старт гри', width= 12, height= 3, command=lambda: ran())
button_1.place(x = 280, y = 340)
button_1['bg'] = '#FFDB00'





root.mainloop()
