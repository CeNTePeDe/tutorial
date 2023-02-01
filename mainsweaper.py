import tkinter as tk
from random import shuffle  # метод для перемешивания коллекции
from tkinter.messagebox import showinfo, showerror


# словарь цветов
colors = {
    0: 'white',
    1: 'blue',
    2: 'green',
    3: '#32CD32',
    4: '#FF1493',
    5: '#48D1CC',
    6: '#DA70D6',
    7: '#CD853F',
    8: '#708090'
}



class MyButton(tk.Button):  # на основе класса button из tkinter


    def __init__(self, master, x, y, number=0, *args, **kwargs):
        super(MyButton, self).__init__(master, width=3, font='Calibri 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False  # отвечает является ли кнопка миной
        self.count_bomb = 0  # подсчет колличество бомб
        self.is_open = False  # данный атрибут отвечает за открытие кнопки, первоначально она открыта



    def __repr__(self):
        return f'MyButton {self.x} {self.y} {self.number} {self.is_mine}'
        # вывод кнопки с координатами и номер кнопки является ли она бомбой



class MineSweeper:
    window = tk.Tk()
    ROW = 7
    COLUMN = 10
    MINES = 10
    IS_GAME_OVER = False
    IS_FIRST_CLICK = True  # парметр заводиться, чтобы при нажатии первый раз игрок не папал на бомбу,

    # а только после компьютер рандомно начал их растовлять



    def __init__(self):
        self.buttons = []
        # count = 1 вырезаем счетчик, тк он дает числа барьерным элемнтам, а эти элементы должны быть нейтральны
        for i in range(MineSweeper.ROW + 2):
            temp = []
            for j in range(MineSweeper.COLUMN + 2):
                btn = MyButton(MineSweeper.window, x=i, y=j)
                btn.config(command=lambda button=btn: self.click(button))
                # функция lambda является провадником для вызова кнопки
                btn.bind('<Button-3>', self.right_click)   # кнопка 3я тк она отвечает за правое нажатие клавиши
                temp.append(btn)
            self.buttons.append(temp)




    def right_click(self, event): # функция обезвреживания бомб
        if MineSweeper.IS_GAME_OVER:
            return
        cur_btn = event.widget
        if cur_btn['state'] == 'normal':
            cur_btn['state'] = 'disabled'
            cur_btn['text'] = '%'
            cur_btn['disabledforeground'] = 'red'
        elif cur_btn['text'] == '%': # данная функция для того чтобы убирать флашки ошибочно поставленые
            cur_btn['text'] = ''
            cur_btn['state'] = 'normal'



    def click(self, clicked_button: MyButton):  # делаем анатацию, работаем с обьектами кнопок
        # print(clicked_button) команда для проверки
        if MineSweeper.IS_GAME_OVER:
            return # команда, для того чтобы после игры не возможно было открывать кнопки
        if MineSweeper.IS_FIRST_CLICK:
            self.create_widgets()  # вызов другого метода для начала игры, инкапсуляция
            self.insert_mines(clicked_button.number)  # ставяться именно сдесь, тк сначала нужно золожить бомбу,
                                                      # а потом распечать
            self.count_mines_in_buttons()  # потом мы подсчитываем бомбы
            self.print_buttons()
            MineSweeper.IS_FIRST_CLICK = False # для того чтобы игровое поле не перезагружалось во время игры
        if clicked_button.is_mine:
            clicked_button.config(text='*', bg='red', disabledforeground='black')
            # последняя функция для черного шрифта
            clicked_button.is_open = True  # тк кнопка открыта
            MineSweeper.IS_GAME_OVER = True  # тк мы кликнули по бомбе, следовательно конец игре
            showinfo('Game Over', 'Вы проиграли')
            for i in range(1, MineSweeper.ROW + 1):  # цикл для обхода всех мин
                for j in range(1, MineSweeper.COLUMN + 1):
                    btn = self.buttons[i][j]
                    if btn.is_mine:
                        btn['text'] = '*'  # для того чтобы поле проигриша показать все мины
        else:
            color = colors.get(clicked_button.count_bomb, 'black')

            if clicked_button.count_bomb:
                clicked_button.config(text=clicked_button.count_bomb, disabledforeground=color)
                clicked_button.is_open = True
            else:
                self.breadth_first_seach(clicked_button)  # метод поиска в ширину
        clicked_button.config(state='disable')
        clicked_button.config(relief=tk.SUNKEN)  # данный параметр показывает, что кнопка нажата
        # сделано для того, чтобы не нажимать на кнопку дважды




    def breadth_first_seach(self, btn: MyButton):
        queue = [btn]  # создаем очередь для поиска в ширину
        while queue:
            cur_btn = queue.pop()
            color = colors.get(cur_btn.count_bomb, 'black')
            if cur_btn.count_bomb:
                cur_btn.config(text=cur_btn.count_bomb, disabledforeground=color)

            else:
                cur_btn.config(text='', disabledforeground=color)
            cur_btn.is_open = True
            cur_btn.config(state='disable')
            cur_btn.config(relief=tk.SUNKEN)

            if cur_btn.count_bomb == 0:
                x, y = cur_btn.x, cur_btn.y
                for dx in [-1, 0, 1]:  # осуществление проверки в поиска ширину
                    for dy in [-1, 0, 1]:
                        # if not abs(dx - dy) == 1:  # взятие по модулю
                        #    continue данные операции убрали тк это не дает просмотр клеток по диогонали

                        next_btn = self.buttons[x + dx][y + dy]
                        # рассматриваем следующую кнопку, далее проверяем добовлять ее в очередь или нет
                        # предпоследняя операция для проверки не является ли кнопка барьерной
                        # последняя операция проверка не находится ли кнопка в списке
                        if not next_btn.is_open and 1 <= next_btn.x <= MineSweeper.ROW and \
                                1 <= next_btn.y <= MineSweeper.COLUMN and next_btn not in queue:
                            # обавляем кнопку после праверки условия, нажатая кнопка уже находиться в списке
                            queue.append(next_btn)




    def reload(self): # метод перезапуска игры
        [child.destroy() for child in self.window.winfo_children()] # генератор списка вызовит destroy
                                                                    # для каждого элемента списка
        self.__init__() # запускаем метод для инициализации
        self.create_widgets() # далее создаем виджеты
        MineSweeper.IS_FIRST_CLICK = True
        MineSweeper.IS_GAME_OVER = False




    def create_settings_win(self): #создани дополнительного окна, для изменения размеров поля и колличество бомб
        win_settings = tk.Toplevel(self.window)
        win_settings.wm_title('Настройки')  # создание название подокна
        # описание каждого окошка
        # описание строк
        tk.Label(win_settings, text='Колличество строк').grid(row=0, column=0)
        row_entry = tk.Entry(win_settings)
        row_entry.insert(0, MineSweeper.ROW)
        row_entry.grid(row=0, column=1, padx=20, pady=20)
        # описание столбцов
        tk.Label(win_settings, text='Колличество колонок').grid(row=1, column=0)
        column_entry = tk.Entry(win_settings)
        column_entry.insert(0, MineSweeper.COLUMN)
        column_entry.grid(row=1, column=1,padx=20, pady=20)
        # описание мин
        tk.Label(win_settings, text='Колличество мин').grid(row=2, column=0)
        mines_entry = tk.Entry(win_settings)
        mines_entry.insert(0, MineSweeper.MINES)
        mines_entry.grid(row=2, column=1, padx=20, pady=20)

        # создание кнопки применить
        save_btn = tk.Button(win_settings, text='Применить',
                  command=lambda: self.change_settings(row_entry, column_entry, mines_entry))
        save_btn.grid(row=3, column=0, columnspan=2,padx=20, pady=20)




    def change_settings(self, row:tk.Entry, column:tk.Entry, mines:tk.Entry):
        #обработка ошибок, у учетом ввода слов в табло
        try:
            int(row.get()), int(column.get()), int(mines.get())
        except ValueError:
            showerror('Ошибка', 'Вы ввели неправельное значение!')


        MineSweeper.ROW = int(row.get())
        MineSweeper.COLUMN = int(column.get())
        MineSweeper.MINES = int(mines.get())
        self.reload()




    def create_widgets(self):
        # Создаем меню
        menubar = tk.Menu(self.window)
        self.window.config(menu=menubar)
        # создание подменю
        settings_menu = tk.Menu(menubar, tearoff=0)  # последний пораметр для убирания штрихов в меню
        settings_menu.add_command(label='Играть', command=self.reload)
        settings_menu.add_command(label='Настройки', command=self.create_settings_win)
        settings_menu.add_command(label='Выход', command=self.window.destroy)
        menubar.add_cascade(label='Файл', menu=settings_menu)
        count = 1
        for i in range(1, MineSweeper.ROW + 1):  # индексы +1 для того чтобы не выводить барьерные кнопки на экран
            for j in range(1, MineSweeper.COLUMN + 1):
                btn = self.buttons[i][j]
                btn.number = count
                btn.grid(row=i, column=j, stick='NWES')  # растягиваем кнопки
                count += 1
        # данные два цикала, для того чтобы кнопки всегда распределялись равномерно, при увеличении размеров экрана
        for i in range(1, MineSweeper.ROW+1):
            tk.Grid.rowconfigure(self.window, i, weight=1)
        for i in range(1, MineSweeper.COLUMN + 1):
            tk.Grid.columnconfigure(self.window, i, weight=1)




    def open_all_buttons(self):  # заполняет внутри кнопок текст
        for i in range(MineSweeper.ROW + 2):
            for j in range(MineSweeper.COLUMN + 2):
                btn = self.buttons[i][j]
                if btn.is_mine:
                    btn.config(text='*', bg='red', disabledforeground='black')
                    # последняя функция для черного шрифта
                elif btn.count_bomb in colors:
                    color = colors.get(btn.count_bomb, 'black')
                    btn.config(text=btn.count_bomb, fg=color)




    def start(self):
        self.create_widgets()  # вызов другого метода для начала игры, инкапсуляция

        # self.open_all_buttons() функция открытия всех кнопок
        # print(self.get_mines_places()) инструкция для проверки индексов для мин
        MineSweeper.window.mainloop()




    def print_buttons(self):
        # for row_btn in self.buttons:  oбащение через self, тк внутри класса
        # print(row_btn) последующие инструкции для более красивого вывода
        for i in range(1, MineSweeper.ROW + 1):
            for j in range(1, MineSweeper.COLUMN + 1):
                btn = self.buttons[i][j]
                if btn.is_mine:
                    print('B', end='')  # для вывода в консоль в виде таблицы
                else:
                    print(btn.count_bomb, end='')
            print()



    # функция вставки бомб
    def insert_mines(self, number: int):  # метод расстановки мин на поле
        index_mines = self.get_mines_places(number)
        print(index_mines)
        for i in range(1, MineSweeper.ROW + 1):  # начало с единицы, для обхода барьерных элементов
            for j in range(1, MineSweeper.COLUMN + 1):  # заканчиваем тоже +1, для обхода
                btn = self.buttons[i][j]  # обращение к кнопке по индекам
                if btn.number in index_mines:
                    btn.is_mine = True



    def count_mines_in_buttons(self):  # метод для подсчета бомб в соседних кнопках
        for i in range(1, MineSweeper.ROW + 1):
            for j in range(1, MineSweeper.COLUMN + 1):
                btn = self.buttons[i][j]
                count_bomb = 0  # счетчик бомб
                if not btn.is_mine:  # сделано для кнопок не являющихся минами
                    for row_dx in [-1, 0, 1]:
                        for col_dx in [-1, 0, 1]:  # приращение
                            neighbour = self.buttons[i + row_dx][j + col_dx]  # получение всех возможных соседей
                            if neighbour.is_mine:
                                count_bomb += 1
                btn.count_bomb = count_bomb



    @staticmethod  # тк в методе нету ссылки на self метод делаем статическим
    def get_mines_places(exclude_number: int):  # те номер который необходимо исключить
        indexes = list(range(1, MineSweeper.COLUMN * MineSweeper.ROW + 1)) # формирование списка из номеров бомб
        indexes.remove(exclude_number) # сдесь удаляем клетку, в котрорую кликаем первый раз
        shuffle(indexes)
        return indexes[:MineSweeper.MINES]


game = MineSweeper()

game.start()
