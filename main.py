import flet as ft
import sys

if sys.platform == "emscripten": # check if run in Pyodide environment
    import micropip
    micropip.install("pandas")

import pandas

Nvalue_dic = {
        '5': [2500, 3200, 2500, 2000, 2000, 2100, 2250, 2300],
        '10': [1500, 2200, 4500, 2000, 2500, 3000, 3000, 3200]
    }


df = pandas.DataFrame.from_dict(Nvalue_dic)

print(df.loc[0, '5'])

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align="right", width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main, view=ft.WEB_BROWSER)
