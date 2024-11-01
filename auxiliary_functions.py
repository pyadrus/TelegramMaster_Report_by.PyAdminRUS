# -*- coding: utf-8 -*-
import os
import os.path
import random  # Импортируем модуль random, чтобы генерировать случайное число
import time  # Импортируем модуль time, чтобы работать с временем

from loguru import logger

from sqlite_working_tools import DatabaseHandler


def working_with_accounts(account_folder, new_account_folder) -> None:
    """
    Работа с аккаунтами
    :param account_folder: Исходный путь к файлу
    :param new_account_folder: Путь к новой папке, куда нужно переместить файл
    """
    try:  # Переносим файлы в нужную папку
        os.replace(account_folder, new_account_folder)
    except FileNotFoundError:  # Если в папке нет нужной папки, то создаем ее
        try:
            os.makedirs(new_account_folder)
            os.replace(account_folder, new_account_folder)
        except FileExistsError:  # Если файл уже существует, то удаляем его
            os.remove(account_folder)
    except PermissionError:
        logger.error("Не удалось перенести файлы в нужную папку")
    except Exception as e:
        logger.exception(f"Ошибка: {e}")


async def record_inviting_results(time_range_1: int, time_range_2: int, username: str) -> None:
    """
    Запись результатов inviting, отправка сообщений в базу данных.
    :param time_range_1:  - диапазон времени смены аккаунта
    :param time_range_2:  - диапазон времени смены аккаунта
    :param username: - username аккаунта
    """
    logger.info(f'Удаляем с базы данных username {username[0]}')
    # Открываем базу с аккаунтами и с выставленными лимитами
    await DatabaseHandler().delete_row_db(table="members", column="username", value=username[0])
    # Смена username через случайное количество секунд
    record_and_interrupt(time_range_1, time_range_2)


def record_and_interrupt(time_range_1, time_range_2) -> None:
    """
    Запись данных в базу данных и прерывание выполнения кода.
    :param time_range_1:  - диапазон времени смены аккаунта
    :param time_range_2:  - диапазон времени смены аккаунта
    """
    # Смена аккаунта через случайное количество секунд
    selected_shift_time = random.randrange(int(time_range_1), int(time_range_2))
    logger.info(f"Переход к новому username через {selected_shift_time} секунд")
    time.sleep(selected_shift_time)
