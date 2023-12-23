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


async def main(page: ft.Page):
    if sys.platform == "emscripten": # check if run in Pyodide environment
        import micropip
        await micropip.install("pandas")

    import pandas

    Nvalue_dic = {
            '5': [2500, 3200, 2500, 2000, 2000, 2100, 2250, 2300],
            '10': [1500, 2200, 4500, 2000, 2500, 3000, 3000, 3200]
        }
    
    
    df = pandas.DataFrame.from_dict(Nvalue_dic)

    print(df.loc[0, '5'])
    await page.add_async(ft.Text("Hello, async world!"))

ft.app(main)
