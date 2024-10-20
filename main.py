import flet as ft
from loguru import logger

logger.add("user_settings/log/log.log", rotation="2 MB", compression="zip")  # Логирование программы

project_name = "TelegramMaster_Report_by.PyAdminRUS"
program_version = "0.0.1"
date_of_program_change = "21.10.2024"


def main(page: ft.Page):
    page.title = f"{project_name}: {program_version} (Дата изменения {date_of_program_change})"
    page.window.width = 650 # Ширина
    page.window.height = 550 # Высота
    page.window.resizable = False
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
                              ft.Row([ft.ElevatedButton(width=615, height=30, text="Подключение аккаунтов",
                                                        on_click=lambda _: page.go("/connecting_accounts")),
                                      ]),
                              ft.Row([ft.ElevatedButton(width=615, height=30, text="Настройки",
                                                        on_click=lambda _: page.go("/settings")),
                                      ]),

                              ft.Row([ft.ElevatedButton(width=615, height=30, text="Отправка жалоб",
                                                        on_click=lambda _: page.go("/submitting_complaints")),
                                      ]),

                          ]), ]))
        # ______________________________________________________________________________________________________________
        if page.route == "/connecting_accounts":  # Подключение аккаунтов
            try:
                pass
            except Exception as e:
                logger.exception(f"Ошибка: {e}")

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

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
