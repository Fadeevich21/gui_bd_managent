from libs.menu import Menu
import libs.query as query
import tkinter as tk
from tkinter import ttk


class Gui(tk.Frame):
    
    def __add_queries(self):
        self.__menu.add_query(query.QueryDisciplines())
        self.__menu.add_query(query.QuerySchedules())
        self.__menu.add_query(query.QueryLvlSettingsDown())

    def __init__(self, root) -> None:
        super().__init__(root)

        self.main_workplace = tk.Frame()
        self.main_workplace.pack(side=tk.TOP, fill=tk.X)
        self.__table: ttk.Treeview = None

        self.__menu = Menu()
        self.__add_queries()

        self.__combobox = ttk.Combobox(self.main_workplace, values=self.__menu.get_list_names(), state="readonly", width=75, justify='center')
        self.__combobox.current(0)
        self.__combobox.pack(pady=10)
        

        self.__btn_build = ttk.Button(self.main_workplace, text='Построить', command=self.show_table)
        self.__btn_build.pack(pady = 10)


    def get_choose(self):
        choose_text = self.__combobox.get()
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
        self.__scroll_panel_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.__scroll_panel_y = ttk.Scrollbar(self.main_workplace, command=self.__table.yview)
        self.__table.configure(yscrollcommand=self.__scroll_panel_y.set)
        self.__scroll_panel_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.__table.pack(expand=tk.YES, fill=tk.BOTH)