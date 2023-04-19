from tkinter import *
from tkinter import ttk
 
root = Tk()     # создаем корневой объект - окно
root.title("Создание отзывов")     # устанавливаем заголовок окна
root.geometry("300x800")    # устанавливаем размеры окна
root.resizable(False, False)
root.iconbitmap(default="icon.png")

def create_file():
    
    law_range=law_range_get.get()
    law_range_address=law_range_address_get.get()
    law_number_first=law_number_first_get.get()
    law_number_last=law_number_last_get.get()
    law_number_year=law_number_year_get.get()
    physics=physics_get.get()
    physics_address=physics_address_get.get()
    creditor=creditor_get.get()
    creditor_address=creditor_address_get.get()
    summ=summ_get.get()
    
    print(law_range,law_range_address,law_number_first,law_number_last,law_number_year,physics,physics_address,creditor,creditor_address,summ)



label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)
label["text"] = 'В арбитражный суд:'

law_range_get = ttk.Entry()
law_range_get.pack(anchor=NW, padx=6, pady=6)
#law_range=law_range_get.get()


label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)
label["text"] = 'Его адрес: '

law_range_address_get = ttk.Entry()
law_range_address_get.pack(anchor=NW, padx=6, pady=6)
#law_range_address=law_range_address_get.get()

label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)
label["text"] = 'А'

law_number_first_get = ttk.Entry()
law_number_first_get.pack(anchor=NW, padx=6, pady=6)
#law_number_first=law_number_first_get.get()


label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)
label["text"] = '-'

law_number_last_get = ttk.Entry()
law_number_last_get.pack(anchor=NW, padx=6, pady=6)
#law_number_last=law_number_last_get.get()


label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)
label["text"] = '/'

law_number_year_get = ttk.Entry()
law_number_year_get.pack(anchor=NW, padx=6, pady=6)
#law_number_year=law_number_year_get.get()


label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)
label["text"] = 'ФИО: '

physics_get = ttk.Entry()
physics_get.pack(anchor=NW, padx=6, pady=6)
#physics=physics_get.get()




label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)
label["text"] = 'Место жительства должника: '

physics_address_get = ttk.Entry()
physics_address_get.pack(anchor=NW, padx=6, pady=6)
#physics_address=physics_address_get.get()


label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)
label["text"] = 'Кредитор: '

creditor_get = ttk.Entry()
creditor_get.pack(anchor=NW, padx=6, pady=6)
#creditor=creditor_get.get()


label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)
label["text"] = 'Адрес кредитора: '

creditor_address_get = ttk.Entry()
creditor_address_get.pack(anchor=NW, padx=6, pady=6)
#creditor_address=creditor_address_get.get()


label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)
label["text"] = 'Сумма кредита: '

summ_get = ttk.Entry()
summ_get.pack(anchor=NW, padx=6, pady=6)
#summ=summ_get.get()


btn = ttk.Button(text="Создать документ",command=create_file)
btn.pack(fill=X)


root.mainloop()
