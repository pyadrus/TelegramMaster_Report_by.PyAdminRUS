import flet as ft
from loguru import logger

from TGConnect import TGConnect
from config import (line_width, height_button, project_name, program_version, date_of_program_change, window_width,
                    window_height, window_resizable)
from gui_menu import account_connection_menu

logger.add("user_settings/log/log.log", rotation="2 MB", compression="zip")  # Логирование программы


def main(page: ft.Page):
    page.title = f"{project_name}: {program_version} (Дата изменения {date_of_program_change})"
    page.window.width = window_width  # Ширина
    page.window.height = window_height  # Высота
    page.window.resizable = window_resizable  # Разрешение изменения размера окна
    logger.info(f"Program version: {program_version}. Date of change: {date_of_program_change}")

    async def route_change(route):
        page.views.clear()
        # Меню "Главное меню"
        page.views.append(
            ft.View("/", [ft.AppBar(title=ft.Text("Главное меню"),
                                    bgcolor=ft.colors.SURFACE_VARIANT),
                          ft.Text(spans=[ft.TextSpan(
                              f"{project_name}",
                              ft.TextStyle(
                                  size=25,
                                  weight=ft.FontWeight.BOLD,
                                  foreground=ft.Paint(
                                      gradient=ft.PaintLinearGradient((0, 20), (150, 20), [ft.colors.PINK,
                                                                                           ft.colors.PURPLE])), ), ), ], ),
                          ft.Text(disabled=False,
                                  spans=[ft.TextSpan('Аккаунт  Telegram: '),
                                         ft.TextSpan("https://t.me/PyAdminRU",
                                                     ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                                                     url="https://t.me/PyAdminRU", ), ], ),
                          ft.Text(disabled=False,
                                  spans=[ft.TextSpan("Канал Telegram: "),
                                         ft.TextSpan("https://t.me/master_tg_d",
                                                     ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                                                     url="https://t.me/master_tg_d", ), ], ),
                          ft.Column([  # Добавляет все чекбоксы и кнопку на страницу (page) в виде колонок.
                              ft.ElevatedButton(width=line_width, height=height_button,
                                                text="Подключение аккаунтов",
                                                on_click=lambda _: page.go("/connecting_accounts")),
                              ft.ElevatedButton(width=line_width, height=height_button, text="Настройки",
                                                on_click=lambda _: page.go("/settings")),
                              ft.ElevatedButton(width=line_width, height=height_button, text="Отправка жалоб",
                                                on_click=lambda _: page.go("/submitting_complaints")),
                              ft.ElevatedButton(width=line_width, height=height_button, text="Документация",
                                                on_click=lambda _: page.go("/documentation")),

                          ]), ]))
        # ______________________________________________________________________________________________________________
        if page.route == "/connecting_accounts":  # Подключение аккаунтов
            try:
                await account_connection_menu(page)
            except Exception as e:
                logger.exception(f"Ошибка: {e}")

        elif page.route == "/connecting_accounts_by_number":  # Подключение аккаунтов по номеру телефона
            try:
                await TGConnect().connecting_number_accounts(page, 'report', 'жалоб')
            except Exception as e:
                logger.exception(f"Ошибка: {e}")

        elif page.route == "/connecting_accounts_by_session":  # Подключение session аккаунтов
            try:
                await TGConnect().connecting_session_accounts(page, 'report', 'жалоб')
            except Exception as e:
                logger.exception(f"Ошибка: {e}")

        # ______________________________________________________________________________________________________________
        elif page.route == "/settings":  # Настройки
            try:
                pass
            except Exception as e:
                logger.exception(f"Ошибка: {e}")

        elif page.route == "/submitting_complaints":  # Отправка жалоб
            try:
                pass
            except Exception as e:
                logger.exception(f"Ошибка: {e}")

        elif page.route == "/documentation":  # ДокумЫЫЫентация
            try:
                pass
            except Exception as e:
                logger.exception(f"Ошибка: {e}")

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
