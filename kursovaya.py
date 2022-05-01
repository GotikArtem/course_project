#Список автомобилей не дороже введенной суммы с указанием марки, страны и года выпуска
# марка автомобиля
# Страна
# Год выпуска 
# Стоимость
# Россия 2000 1000000
#Стоимость
#виджеты: кнопка найти и выйти, поля ввода стоимости и имя файла , список доступных вариантов и надпись с именем и фамилией



import tkinter as tk
from tkinter import messagebox # импортируем виджет окна сообщения

# os - модуль для работы с файлами, директориями и др. штуками операционной системы
# path - класс для работы с путями в ос
from os import path


class App: # класс нашего приложения
    def __init__(self): # конструктор, который создает и размещает виджеты на экране приложения, после чего запускает его
        self.root = tk.Tk() # создаем экземпляр класса главного окна под именем переменной root
        self.root.geometry('800x600')
        self.root.resizable(False,False)
        self.button1 = tk.Button(self.root,text='Найти',command=self.__findcar)
        self.button2 = tk.Button(self.root,text='Выйти',command=lambda:exit())
       
        self.label1 = tk.Label(self.root, text='Введите стоимость')
        # self.label1.config(fg='#12f02f', bg='#000fa0')
        self.label2 = tk.Label(self.root, text='Введите имя входного файла')
        self.label3 = tk.Label(self.root, text='Последний выпущенный авто: ')

        self.vvod1 = tk.Entry(self.root,width = 50)
        self.vvod2 = tk.Entry(self.root,width = 50)
        self.listt = tk.Listbox(self.root, width=50)
        self.nad = tk.Label(self.root,text = 'Коржавин Артём 21Вт-2')

        self.label1.place(x=57, y=20)#менеджер геометрии
        self.label2.place(x=57, y=90)
        self.label3.place(x=57, y=150)

        self.vvod1.place(x=57,y=42)
        self.vvod2.place(x=57,y=112)

        self.listt.place(x=430,y=42)
        self.button1.place(x=430,y=240)
        self.button2.place(x=500,y=240)
        self.nad.place(x=10,y=570)

        self.root.mainloop()

    def __validate_data(self, data):
        try:
            for brand, country, year, price in [d.split() for d in data]:
                # метод isalpha проеверяет, что строка чисто буквенная
                # метод isdigit проеверяет, что строка чисто численная
                if not(brand.isalpha() and
                    country.isalpha() and
                    year.isdigit() and
                    price[:-1].isdigit()):
                    messagebox.showerror(message='Неверный формат данных в исходном файле!')
                    return False
            return True
        except ValueError:
            messagebox.showerror(message='Неверный формат данных в исходном файле!')
            return False

    
    def __findcar(self): 
        filename = self.vvod2.get()
        if not path.exists(filename):
            messagebox.showerror(message='Нет такого входного файла!')
            return

        filee = open(filename,'r')
        try:
            price = int(self.vvod1.get())
        except:
            messagebox.showerror(message='Неверный формат числа!')
            return
        else:
            data = filee.readlines() # создает список из строк файла
            if not self.__validate_data(data):
                return
            
            data2 = []
            for element in data:
                price_check = int(element.split()[-1][:-1])
                if price_check <= price:
                    data2.append(element.replace('\n', ''))
            filee.close()

        if not data2:
            self.listt.insert(0, 'Отсутствуют данные по текующим параметрам')
            return

        self.listt.delete(0, 'end')
        latest = max(data2, key=lambda x: int(x.split()[-2]))
        for element in data2:
            self.listt.insert(0, element)
        self.label3.config(text='Последний выпущенный авто: '+latest)

if __name__ == '__main__':
    app = App()