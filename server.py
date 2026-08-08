import flet as ft


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


ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8080)
