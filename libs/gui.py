from libs.menu import Menu
import libs.query as query
import tkinter as tk
from tkinter import ttk


class Gui(tk.Frame):
    
    def __add_queries(self):
        # self.__menu.add_query(query.QueryDisciplines())
        # self.__menu.add_query(query.QuerySchedules())
        # self.__menu.add_query(query.QueryLvlSettingsDown())
        # self.__menu.add_query(query.QueryDepartments())
        # self.__menu.add_query(query.QueryDepartmentsGroups())
        # self.__menu.add_query(query.QueryDepartmentsTeachers())
        for name_table in ['departments', 'departments_teachers',
                           'departments_groups', 'disciplines',
                           'groups', 'levels_setting_down',
                           'parlours', 'schedules',
                           'sessions', 'teachers']:
            self.__menu.add_query(query.Query(name_table))

    def __init__(self, root: tk.Tk) -> None:
        root.resizable(False, False)
        super().__init__(root)
        self.main_workplace = tk.Frame()
        self.main_workplace.place(x=0, y=0, width=1000, height=600)#side=tk.TOP, fill=tk.X)
        self.__table: ttk.Treeview = None

        self.__menu = Menu()
        self.__add_queries()

        self.__combobox1 = ttk.Combobox(self.main_workplace, values=self.__menu.get_list_names(), state="readonly", width=75, justify='center')
        self.__combobox1.current(0)
        self.__combobox1.place(x=90, y=475, width=200)#pady=10)

        self.__btn_build1 = ttk.Button(self.main_workplace, text='Построить', command=self.show_table)
        self.__btn_build1.place(x=150, y=525)#pady = 10)


        self.__combobox2 = ttk.Combobox(self.main_workplace, values=self.__menu.get_list_names(), state="readonly", width=75, justify='center')
        self.__combobox2.current(0)
        self.__combobox2.place(x=670, y=425, width=200)

        self.__text_field_add_column = tk.Entry(self.main_workplace)
        self.__text_field_add_column.place(x=670, y=465, width=200, height=25)

        self.__btn_build2 = ttk.Button(self.main_workplace, text='Добавить столбец', command=self.add_column)
        self.__btn_build2.place(x=700, y=525)


        self.__combobox3 = ttk.Combobox(self.main_workplace, values=self.__menu.get_list_names(), state="readonly", width=75, justify='center')
        self.__combobox3.current(0)
        self.__combobox3.place(x=400, y=425, width=200)

        self.__text_field_remove_column = tk.Entry(self.main_workplace)
        self.__text_field_remove_column.place(x=400, y=465, width=200, height=25)

        self.__btn_build3 = ttk.Button(self.main_workplace, text='Удалить столбец', command=self.remove_column)
        self.__btn_build3.place(x=430, y=525)

    def add_column(self):
        table_name = self.__combobox3.get()
        request = self.__text_field_add_column.get()
        if request == '':
            return
        
        self.__menu.add_column(table_name, request)
        self.show_table()

    def remove_column(self):
        table_name = self.__combobox2.get()
        column_name = self.__text_field_remove_column.get()
        if column_name == '':
            return
        
        self.__menu.remove_column(table_name, column_name)
        self.show_table()

    def get_choose(self):
        choose_text = self.__combobox1.get()
        choose = self.__menu.get_choose(choose_text)
        return choose

    def show_table(self):
        if self.__table is not None:
            self.__table.destroy()
            self.__scroll_panel_x.destroy()
            self.__scroll_panel_y.destroy()

        self.__table = ttk.Treeview(self.main_workplace, show='headings')
        choose = self.get_choose()
        records, headers = self.__menu.handle(choose)
        self.__table['columns'] = headers
        for header in headers:
            self.__table.heading(header, text=header, anchor='center')
            self.__table.column(header, anchor='center')

        for i in range(len(records)):
            record = records[i]
            if i % 2 == 0:
                self.__table.insert('', tk.END, values=record)
            else:
                self.__table.insert('', tk.END, values=record, tags='gray')
            self.__table.tag_configure('gray', background='#D3D3D3')

        self.__scroll_panel_x = ttk.Scrollbar(self.main_workplace, command=self.__table.xview, orient='horizontal')
        self.__table.configure(xscrollcommand=self.__scroll_panel_x.set)
        self.__scroll_panel_x.place(x=20, y=320, width=950)
        # self.__scroll_panel_x.place(side=tk.BOTTOM, fill=tk.X)

        self.__scroll_panel_y = ttk.Scrollbar(self.main_workplace, command=self.__table.yview)
        self.__table.configure(yscrollcommand=self.__scroll_panel_y.set)
        self.__scroll_panel_y.place(x=970, y=20, height=300)
        # self.__scroll_panel_y.place(side=tk.RIGHT, fill=tk.Y)

        self.__table.place(x=20, y=20, width=950, height=301)
        # self.__table.place(expand=tk.YES, fill=tk.BOTH)
