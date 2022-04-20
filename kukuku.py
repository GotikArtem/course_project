#Список автомобилей не дороже введенной суммы с указанием марки, страны и года выпуска
# марка автомобиля
# Страна
# Год выпуска 
# Стоимость
# Россия 2000 1000000
#Стоимость
#виджеты: кнопка найти и выйти, поля ввода стоимости и имя файла , список доступных вариантов и надпись с именем и фамилией
import tkinter as tk

class App:
    def __init__(self):
        root =tk.Tk()
        root.geometry('800x600')
        root.resizable(False,False)
        
        button1 = tk.Button(root,text='Найти',command=findcar)
        button2 = tk.Button(root,text='Выйти',command=lambda:exit())
        
        vvod1 = tk.Entry(root,width = 50)
        vvod2 = tk.Entry(root,width = 50)
        
        listt = tk.Listbox(root)
        nad = tk.Label(root,text = 'Коржавин Артём 21Вт-2')

        vvod1.place(x=57,y=42)
        vvod2.place(x=57,y=112)
        listt.place(x=130,y=42)
        button1.place(x=130,y=400)
        button2.place(x=180,y=400)
        nad.place(x=10,y=750)

        root.mainloop()
    def findcar(self):
        filee = open('Dann','r')
        prize = int(self.vvod2.get())
        data = filee.readlines()
        data2 = [] 
        for i in range(len(filee)):
            fille[i] = filee[i].split()
            prise = filee[i][2]
            if prise <= prize:
                s = ' '.join(filee[i])
                data2.append(s)
        filee.close()
        name = self.vvod1.get()
        fille = open(name,'w')
        for l in data2:
            self.listt.insert(0,l)
            fille.write(l+'\n')
        fille.close()




