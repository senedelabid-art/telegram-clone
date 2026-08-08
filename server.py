import os
import flet as ft
from flask import Flask

app = Flask(__name__)


def main(page: ft.Page):
  page.title = "Menbr Chat"
  page.theme_mode = ft.ThemeMode.DARK

  username_field = ft.TextField(label="Username", width=300)

  def go_to_chat(e):
    page.clean()
    page.add(ft.Text("تم الدخول بنجاح!"))
    page.update()

  page.add(
      ft.Column(
          [
              ft.Text("Menbr Chat", size=30),
              username_field,
              ft.ElevatedButton("دخول", on_click=go_to_chat),
          ],
          alignment=ft.MainAxisAlignment.CENTER,
      )
  )


@app.route("/")
def home():
  return "Menbr Chat Server is running!"


# تشغيل Flet مع Flask ليتوافق مع Render
if __name__ == "__main__":
  port = int(os.environ.get("PORT", 8080))
  # تشغيل Flet في خلفية مستقلة
  import threading

  threading.Thread(
      target=lambda: ft.app(
          target=main, view=ft.AppView.WEB_BROWSER, port=8550
      )
  ).start()
  app.run(host="0.0.0.0", port=port)
