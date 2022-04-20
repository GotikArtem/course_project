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
        self.root =tk.Tk()
        self.root.geometry('800x600')
        self.root.resizable(False,False)
        self.button1 = tk.Button(self.root,text='Найти',command=self.findcar)
        self.button2 = tk.Button(self.root,text='Выйти',command=lambda:exit())
       
        self.label1 = tk.Label(self.root, text='Введите стоимость')
        self.label1.config(fg='#12f02f', bg='#000fa0')
        self.label2 = tk.Label(self.root, text='Введите имя входного файла')
        self.label3 = tk.Label(self.root, text='Последний выпущенный авто: ')

        self.vvod1 = tk.Entry(self.root,width = 50)
        self.vvod2 = tk.Entry(self.root,width = 50)
        self.listt = tk.Listbox(self.root, width=50)
        self.nad = tk.Label(self.root,text = 'Коржавин Артём 21Вт-2')

        self.label1.place(x=57, y=20)
        self.label2.place(x=57, y=90)
        self.label3.place(x=57, y=150)

        self.vvod1.place(x=57,y=42)
        self.vvod2.place(x=57,y=112)

        self.listt.place(x=430,y=42)
        self.button1.place(x=430,y=240)
        self.button2.place(x=500,y=240)
        self.nad.place(x=10,y=570)

        self.root.mainloop()

    def findcar(self):
        filename = self.vvod2.get()
        filee = open(filename,'r')
        try:
            price = int(self.vvod1.get())
        except:
            print('Хуйня а не число!')
            return
        else:
            data = filee.readlines()
            data2 = [] 
            for element in data:
                price_check = int(element.split()[-1])
                if price_check <= price:
                    data2.append(element.replace('\n', ''))
            filee.close()
            latest = max(data2, key=lambda x: int(x.split()[-2]))
        for element in data2:
            self.listt.insert(0, element)
        self.label3.config(text='Последний выпущенный авто: '+latest)

app = App()



