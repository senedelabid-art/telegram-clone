import flet as ft

def main(page: ft.Page):
    page.title = "Menbr Chat"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    username_field = ft.TextField(label="Username (@username)", prefix_text="@", width=300)
    email_field = ft.TextField(label="Email", width=300)
    password_field = ft.TextField(label="Password", password=True, can_reveal_password=True, width=300)

    def handle_login(e):
        pass

    page.add(
        ft.Column([
            ft.Text("Menbr Chat", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.GREEN),
            ft.Container(height=20),
            username_field,
            email_field,
            password_field,
            ft.ElevatedButton("دخول / انشاء حساب", on_click=handle_login, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.app(target=main)
