# import sqlite3
import psycopg2
from typing import List, Optional, Tuple


class ServiceDB:

    def __init__(self, path: str) -> None:
        self.__connection = psycopg2.connect(dbname='university_bd', host='localhost', port='5432')
        self.__cursor = self.__connection.cursor()
        # self.__connection: sqlite3.Connection = sqlite3.connect(path)
        # self.__cursor: sqlite3.Cursor = sqlite3.Connection.cursor(self.__connection)

    def execute(self, query: str) -> None:
        try:
            self.__cursor.execute(query)
            self.__connection.commit()
        except:
            print("rollback")
            self.__connection.rollback()

    def execute_from_file(self, filename: str):
        with open(filename, 'r', encoding='utf-8') as file:
            queries = file.read().split(';')
            for query in queries:
                self.execute(query)

    def create_table(self, query: str)-> None:
        self.execute(query)

    def create_table(self,
                     table: str,
                     condition: str = None,
                     fields: Optional[List[str]] = None 
                    ):
        query = f'CREATE TABLE {condition} {table} ({", ".join(fields)});'
        self.create_table(query)

    def insert(self,
               table: str,
               list_items: list[list]
              ):
        query = f'INSERT INTO {table} VALUES '
        for items in list_items:
            query += f'({str(items)}), '
        query = query[:-2] + ';'
        self.execute(query)
        

    def select(self,
               tables: List[Tuple[str, str]],
               condition: Optional[str] = None,
               joins: Optional[List[Tuple[str, str, str]]] = None,
               fields: Optional[List[str]] = None,
               group_by: Optional[List[str]] = None,
               order_by: Optional[List[str]] = None,
               where: Optional[List[str]] = None
              ):
        fields = ['*'] if fields is None else fields
        condition = ' ' if condition is None else condition
        query = f'SELECT {condition} {", ".join(fields)} FROM '
        query += ', '.join([f'{table} {short}' for table, short in tables])
        if joins:
            query += ' JOIN ' + ' JOIN '.join([f'{table}{(" AS " + short) if short else ""} ON {rule}' for table, short, rule in joins])
        if where:
            query += ' WHERE ' + ' AND '.join(where)
        if group_by:
            query += f' GROUP BY {group_by}'
        if order_by:
            query += ' ORDER BY ' + ', '.join(f'{(item[1:] + " DESC") if item.startswith("-") else (item + " ASC")}' for item in order_by)
        query += ';'
        self.__cursor.execute(query)
        result = self.__cursor.fetchall()

        return result


    def add_column(self, table_name: str, 
                   request: str):
        query = f'ALTER TABLE {table_name} ADD COLUMN {request};'
        self.execute(query)

    def remove_column(self, table_name: str, column_name: str):
        query = f'ALTER TABLE {table_name} DROP COLUMN {column_name};'
        self.execute(query)


    def get_columns(self):
        return [desc[0] for desc in self.__cursor.description]
