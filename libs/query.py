from libs.service_db import ServiceDB
from abc import ABC, abstractmethod


class Query(ABC):

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def get_rows(self, service: ServiceDB):
        pass

    @abstractmethod
    def get_columns(self):
        pass


class QueryDisciplines(Query):

    def name(self) -> str:
        return 'Вывод всех пар, которые есть в расписании у группы ВТ-201'

    def get_rows(self, service: ServiceDB):
        return service.select \
        (
            fields=['disciplines.name'],
            tables=[('disciplines', '')],
            condition='DISTINCT',
            joins=[('schedules', 's', 'disciplines.discipline_id = s.discipline_id'), ('groups', 'g', 'g.group_id = s.group_id')],
            where=['g.name = \'BT-201\'']
        )

    def get_columns(self):
        return ['Дисциплина']

class QuerySchedules(Query):

    def name(self) -> str:
        return 'Выборка расписания в пятницу у группы ВТ-201'

    def get_rows(self, service: ServiceDB):
        return service.select \
        (
            fields=['day_week', '(sessions.start_time || \' - \' || sessions.end_time)', 'disciplines.name', 'groups.name', 'teachers.fcs', 'parlours.name'],
            tables=[('schedules', '')],
            joins= \
            [
                ('sessions', '', 'schedules.session_id = sessions.session_id'),
                ('disciplines', '', 'schedules.discipline_id = disciplines.discipline_id'),
                ('groups', '', 'schedules.group_id = groups.group_id'),
                ('teachers', '', 'schedules.teacher_id = teachers.teacher_id'),
                ('parlours', '', 'schedules.parlour_id = parlours.parlour_id')
            ],
            where=['groups.name = \'BT-201\'', 'day_week = \'Friday\''],
            order_by=['sessions.start_time']
        )

    def get_columns(self):
        return ['день недели', 'время', 'дисциплина', 'группа', 'преподаватель', 'кабинет']

class QueryLvlSettingsDown(Query):

    def name(self) -> str:
        return 'Выборка количественного уровня остепенённости преподавателей по кафедрам'

    def get_rows(self, service: ServiceDB):
        return service.select \
        (
            fields=['d.name', 'lsd.name', """
            (
                SELECT COUNT(*)
                FROM departments_teachers dt
                JOIN teachers t on dt.teacher_id = t.teacher_id
                WHERE d.department_id = dt.department_id AND lsd.level_setting_down_id = t.level_setting_down_id
            )"""],
            tables=[('departments', 'd'), ('levels_setting_down', 'lsd')],
            order_by=['d.name', 'lsd.name']
        )

    def get_columns(self):
        return ['кафедра', 'уровень остепенённости', 'число преподавателей']