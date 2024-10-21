# -*- coding: utf-8 -*-
import configparser


class ConfigReader:

    def __init__(self):
        self.config = configparser.ConfigParser(empty_lines_in_values=False, allow_no_value=True)
        self.config.read('config_gui.ini')

    def get_line_width_button(self):
        """Получение ширины кнопки"""
        return (
            self.config.get('line_width', 'line_width_button', fallback=None)
        )

config_reader = ConfigReader()