import flet as ft
from flask import Flask
import threading
import os

app = Flask(__name__)

# دالة واجهة التطبيق
def main(page: ft.Page):
    page.title = "Menbr Chat"
    page.theme_mode = ft.ThemeMode.DARK
    
    username_field = ft.TextField(label="Username", width=300)
    
    def go_to_chat(e):
        page.clean()
        page.add(ft.Text("تم الدخول بنجاح!"))
        page.update()

    page.add(
        ft.Column([
            ft.Text("Menbr Chat", size=30),
            username_field,
            ft.ElevatedButton("دخول", on_click=go_to_chat)
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

@app.route('/')
def home():
    return "Menbr Chat Server is running! The app is configured."

# تشغيل سيرفر Flask
if __name__ == "__main__":
    # تشغيل تطبيق Flet في خلفية مستقلة (اختياري)
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
