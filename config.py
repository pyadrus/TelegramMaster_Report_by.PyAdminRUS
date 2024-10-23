# -*- coding: utf-8 -*-
import configparser


class ConfigReader:
    """Конфиг файл для gui программы"""

    def __init__(self):
        self.config = configparser.ConfigParser(empty_lines_in_values=False, allow_no_value=True)
        self.config.read('config_gui.ini')

    def get_line_width_button(self):
        """Получение ширины кнопки"""
        return (
            self.config.get('line_width', 'line_width_button', fallback=None)
        )

    def get_line_height_button(self):
        """Получение высоты кнопки"""
        return (
            self.config.get('line_height', 'height_button', fallback=None)
        )

    def project_name(self):
        """Наименование проекта"""
        return (
            self.config.get('project_name', 'project_name', fallback=None)
        )

    def program_version(self):
        """Версия программы"""
        return (
            self.config.get('program_version', 'program_version', fallback=None)
        )

    def date_of_program_change(self):
        """Дата обновления"""
        return (
            self.config.get('date_of_program_change', 'date_of_program_change', fallback=None)
        )

    def window_width(self):
        """Ширина программы"""
        return (
            self.config.get('window_width', 'window_width', fallback=None)
        )

    def window_height(self):
        """Высота программы"""
        return (
            self.config.get('window_height', 'window_height', fallback=None)
        )

    def window_resizable(self):
        """Разрешение на изменение размера программы, если False, то изменение запрещено"""
        return (
            self.config.get('window_resizable', 'window_resizable', fallback=None)
        )


line_width = ConfigReader().get_line_width_button()  # Ширина кнопки
height_button = ConfigReader().get_line_height_button()  # Высота кнопки
project_name = ConfigReader().project_name()  # Наименование проекта
program_version = ConfigReader().program_version()  # Версия программы
date_of_program_change = ConfigReader().date_of_program_change()  # Дата обновления
window_width = ConfigReader().window_width()  # Ширина программы
window_height = ConfigReader().window_height()  # Высота программы
window_resizable = ConfigReader().window_resizable()  # Разрешение на изменение размера программы, если False, то изменение запрещено
