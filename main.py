import flet as ft

def main(page: ft.Page):
    page.title = "Gestor de tareas"
    page.horizontal_alignment = "center"

    tareas = {}
    escribir_tarea = ft.TextField(label="¿Qué hay de nuevo?", border="underline")
    contador = 0

    page.window_max_height = 500
    page.window_max_width = 500
    page.bgcolor = "#ffc2a1"

    lista_tareas = ft.ListView(
        expand=True,
        spacing=10,
        padding=10,
        auto_scroll=False
    )

    def agregar_color(señal):
        ultimo_elemento = list(tareas.keys())[-1]
        tareas[ultimo_elemento].bgcolor = señal.control.icon_color
        page.update()

    color1 = ft.ElevatedButton(icon="circle", text="color", icon_color="#4fa4b8", on_click=agregar_color)
    color2 = ft.ElevatedButton(icon="circle", text="color", icon_color="#63ab3f", on_click=agregar_color)
    color3 = ft.ElevatedButton(icon="circle", text="color", icon_color="#f0b541", on_click=agregar_color)

    def agregar(señal):
        nonlocal contador

        tarea = ft.Container(
            content=ft.Row(controls=[
                ft.Text(value=escribir_tarea.value),
                ft.TextButton(
                    text=str(contador),
                    style=ft.ButtonStyle(
                        color=ft.colors.WHITE,
                        icon_color=ft.colors.BLUE_900
                    ),
                    icon="delete",
                    on_click=eliminar
                )
            ]),
            bgcolor="white",
            border_radius=10,
            padding=ft.padding.only(left=10)
        )

        tareas[str(contador)] = tarea
        lista_tareas.controls.append(tarea)
        escribir_tarea.value = ""
        page.update()
        contador += 1

    def eliminar(señal):
        lista_tareas.controls.remove(tareas[señal.control.text])
        tareas.pop(señal.control.text)
        page.update()

    front = ft.Column(controls=[
        ft.Container(
            content=escribir_tarea,
            bgcolor="#e64539",
            height=70,
            border_radius=10,
            padding=ft.padding.only(left=10, top=10, right=10, bottom=10)
        ),
        ft.Container(
            content=ft.Row(controls=[
                ft.ElevatedButton(text="Agregar", on_click=agregar),
                color1,
                color2,
                color3,
            ]),
            bgcolor="#ff8933",
            height=70,
            border_radius=10,
            padding=ft.padding.only(left=10, top=10, right=10, bottom=10)
        ),
        lista_tareas
    ], expand=True)

    page.add(front)

ft.app(target=main)
