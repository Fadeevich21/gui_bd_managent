from libs.service_db import ServiceDB
from abc import ABC, abstractmethod


class Query:

    def __init__(self, name_table: str) -> None:
        self.__name_table = name_table

    # @abstractmethod
    def name(self) -> str:
        return self.__name_table

    # @abstractmethod
    def get_rows(self, service: ServiceDB):
        return service.select \
        (
            tables=[(self.__name_table, '')]
        )


# class QueryDisciplines(Query):

#     def name(self) -> str:
#         return 'Вывод всех пар, которые есть в расписании у группы ВТ-201'

#     def get_rows(self, service: ServiceDB):
#         return service.select \
#         (
#             fields=['disciplines.name'],
#             tables=[('disciplines', '')],
#             condition='DISTINCT',
#             joins=[('schedules', 's', 'disciplines.discipline_id = s.discipline_id'), ('groups', 'g', 'g.group_id = s.group_id')],
#             where=['g.name = \'BT-201\'']
#         )

#     def get_columns(self):
#         return ['Дисциплина']

# class QuerySchedules(Query):

#     def name(self) -> str:
#         return 'Выборка расписания в пятницу у группы ВТ-201'

#     def get_rows(self, service: ServiceDB):
#         return service.select \
#         (
#             fields=['day_week', '(sessions.start_time || \' - \' || sessions.end_time)', 'disciplines.name', 'groups.name', 'teachers.fcs', 'parlours.name'],
#             tables=[('schedules', '')],
#             joins= \
#             [
#                 ('sessions', '', 'schedules.session_id = sessions.session_id'),
#                 ('disciplines', '', 'schedules.discipline_id = disciplines.discipline_id'),
#                 ('groups', '', 'schedules.group_id = groups.group_id'),
#                 ('teachers', '', 'schedules.teacher_id = teachers.teacher_id'),
#                 ('parlours', '', 'schedules.parlour_id = parlours.parlour_id')
#             ],
#             where=['groups.name = \'BT-201\'', 'day_week = \'Friday\''],
#             order_by=['sessions.start_time']
#         )

#     def get_columns(self):
#         return ['день недели', 'время', 'дисциплина', 'группа', 'преподаватель', 'кабинет']

# class QueryLvlSettingsDown(Query):

#     def name(self) -> str:
#         return 'Выборка количественного уровня остепенённости преподавателей по кафедрам'

#     def get_rows(self, service: ServiceDB):
#         return service.select \
#         (
#             fields=['d.name', 'lsd.name', """
#             (
#                 SELECT COUNT(*)
#                 FROM departments_teachers dt
#                 JOIN teachers t on dt.teacher_id = t.teacher_id
#                 WHERE d.department_id = dt.department_id AND lsd.level_setting_down_id = t.level_setting_down_id
#             )"""],
#             tables=[('departments', 'd'), ('levels_setting_down', 'lsd')],
#             order_by=['d.name', 'lsd.name']
#         )

#     def get_columns(self):
#         return ['кафедра', 'уровень остепенённости', 'число преподавателей']

# class QueryDepartments(Query):

#     def name(self) -> str:
#         return 'Кафедра'
    
#     def get_rows(self, service: ServiceDB):
#         return service.select \
#         (
#             tables=[('departments', '')]
#         )
    
#     def get_columns(self):
#         return ['id', 'Название']

# class QueryDepartmentsGroups(Query):

#     def name(self) -> str:
#         return 'Кафедра-группа'
    
#     def get_rows(self, service: ServiceDB):
#         return service.select \
#         (
#             tables=[('departments_groups', '')]
#         )
    
#     def get_columns(self):
#         return None

# class QueryDepartmentsTeachers(Query):

#     def name(self) -> str:
#         return 'Кафедра-преподаватели'
    
#     def get_rows(self, service: ServiceDB):
#         return service.select \
#         (
#             tables=[('departments_teachers', '')]
#         )
    
#     def get_columns(self):
#         return None

# class QueryDisciplines(Query):

#     def name(self) -> str:
#         return 'Предметы'
    
#     def get_rows(self, service: ServiceDB):
#         return service.select \
#         (
#             tables=[('disciplines', '')]
#         )
    
#     def get_columns(self):
#         return None

# class QueryDisciplines(Query):

#     def name(self) -> str:
#         return 'Предметы'
    
#     def get_rows(self, service: ServiceDB):
#         return service.select \
#         (
#             tables=[('disciplines', '')]
#         )
    
#     def get_columns(self):
#         return None
