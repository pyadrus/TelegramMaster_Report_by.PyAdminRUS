import flet as ft

from config import line_width, height_button


async def account_connection_menu(page):
    """Меню подключения аккаунтов"""
    page.views.append(
        ft.View("/account_connection_menu",
                [ft.AppBar(title=ft.Text("Главное меню"),
                           bgcolor=ft.colors.SURFACE_VARIANT),
                 ft.Text(spans=[ft.TextSpan(
                     "Подключение аккаунтов",
                     ft.TextStyle(
                         size=20,
                         weight=ft.FontWeight.BOLD,
                         foreground=ft.Paint(
                             gradient=ft.PaintLinearGradient((0, 20), (150, 20), [ft.colors.PINK,
                                                                                  ft.colors.PURPLE])), ), ), ], ),

                 ft.Column([  # Добавляет все чекбоксы и кнопку на страницу (page) в виде колонок.

                     ft.ElevatedButton(width=line_width, height=height_button,
                                       text="Подключение аккаунтов по номеру телефона",
                                       on_click=lambda _: page.go("/connecting_accounts_by_number")),
                     ft.ElevatedButton(width=line_width, height=height_button, text="Подключение session аккаунтов",
                                       on_click=lambda _: page.go("/connecting_accounts_by_session")),
                 ])]))
