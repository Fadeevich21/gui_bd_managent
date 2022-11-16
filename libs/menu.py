from libs.service_db import ServiceDB
from libs.query import Query
from typing import List, Tuple


class Menu:

    def __init__(self) -> None:
        self.__db = ServiceDB('database/sql.db')
        
        # self.__db.execute_from_file('src/remove_tables.sql')
        # self.__db.execute_from_file('src/create_tables.sql')
        # self.__db.execute_from_file('src/init_tables.sql')
        self.__query = {}

        self.__menu = list()

    def get_list_names(self) -> List[str]:
        return list(self.__query.values())

    def add_query(self, query: Query):
        self.__query[len(self.__query)] = query.name()
        self.__menu.append(query)

    def get_choose(self, text_choose: str) -> int:
        for k, v in self.__query.items():
            if v == text_choose:
                return int(k)

    def handle(self, choose: int) -> Tuple[List[str], List[str]]:
        if choose > len(self.__menu):
            raise IndexError(f'Ваш выбор {choose} не допустим')

        get_rows_func, columns = lambda: self.__menu[choose].get_rows(self.__db), self.__menu[choose].get_columns()
        rows = get_rows_func()
        return (rows, columns)