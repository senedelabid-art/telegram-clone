import flet as ft

def main(page: ft.Page):
    page.title = "Menbr Chat"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    # عناصر شاشة تسجيل الدخول
    username_field = ft.TextField(label="Username (@username)", prefix_text="@", width=300)
    password_field = ft.TextField(label="Password", password=True, can_reveal_password=True, width=300)
    
    # عناصر شاشة الدردشة
    chat_list = ft.ListView(expand=True, spacing=10, padding=10)
    message_input = ft.TextField(hint_text="اكتب رسالتك...", expand=True)

    def go_to_chat(e):
        if not username_field.value:
            username_field.error_text = "الرجاء إدخال اسم المستخدم"
            page.update()
            return
        
        # الانتقال لشاشة الدردشة
        page.clean()
        page.vertical_alignment = ft.MainAxisAlignment.START
        
        header = ft.Row([
            ft.Icon(ft.icons.ACCOUNT_CIRCLE, size=40),
            ft.Text(f"@{username_field.value}", size=20, weight=ft.FontWeight.BOLD)
        ], alignment=ft.MainAxisAlignment.START)

        def send_message(e):
            if message_input.value:
                chat_list.controls.append(
                    ft.Row([
                        ft.Container(
                            content=ft.Text(message_input.value, color=ft.colors.WHITE),
                            bgcolor=ft.colors.GREEN_800,
                            padding=10,
                            border_radius=10
                        )
                    ], alignment=ft.MainAxisAlignment.END)
                )
                message_input.value = ""
                page.update()

        send_btn = ft.IconButton(icon=ft.icons.SEND, on_click=send_message, icon_color=ft.colors.GREEN)

        page.add(
            header,
            ft.Divider(),
            chat_list,
            ft.Row([message_input, send_btn])
        )
        page.update()

    # تصميم واجهة الدخول الأساسية
    page.add(
        ft.Column([
            ft.Text("Menbr Chat", size=32, weight=ft.FontWeight.BOLD, color=ft.colors.GREEN),
            ft.Text("تطبيق دردشة شبيه بتليجرام", size=14, color=ft.colors.GREY),
            ft.Container(height=20),
            username_field,
            password_field,
            ft.Container(height=10),
            ft.ElevatedButton("دخول / بدء المحادثة", on_click=go_to_chat, width=300, bgcolor=ft.colors.GREEN, color=ft.colors.WHITE)
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.app(target=main)
