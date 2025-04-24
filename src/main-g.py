import flet as ft
from flet.core.app_bar import AppBar
from flet import AppBar, ElevatedButton, Page, Text, View
from flet.core.colors import Colors
from flet.core.dropdown import Option
from flet.core.textfield import TextField
from rich import align


def main(page: Page):
    page.title = "exemplo de rotas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667


    def gerenciar_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text(''), center_title=True, bgcolor=Colors.PINK),
                    ft.Image(src="src/assets/apo.png", width=350),
                    ElevatedButton(text="Simular aposentadoria", width=page.window.width,
                                   on_click=lambda _: page.go("/simular_aposentadoria")),
                    ElevatedButton(text="Regras aposentadoria", width=page.window.width,
                                   on_click=lambda _: page.go("/regras")),

                ]
            )
        )

        if page.route == "/simular_aposentadoria":
            page.views.append(
                View(
                    "/simular_aposentadoria", [
                        AppBar(title=Text(""), center_title=True, bgcolor=Colors.PINK),
                        Text(value="Simulação aposentadoria"),
                        genero_escolhido,
                        idade,
                        tempo_contribuicao,
                        media_salarial,
                        opcao,
                        ElevatedButton(text="Calcular", on_click=verificar_campos, width=page.window.width),
                        alerta,


                    ],
                    bgcolor=Colors.WHITE,
                )
            )

        if page.route == "/regras":
            page.views.append(
                View(
                    "/regras", [
                        AppBar(title=Text(""), bgcolor="PINK"),
                        Text(value="Regras aposentadoria"),
                        Text(value="As regras de aposentadoria por idade em 2025 são: "
                                   "\n"
                                   "\n"
                                   " Aposentadoria por Idade: \n"
                                   "Homens: 65 anos de idade e pelo menos 15 anos de contribuição. \n"
                                   "Mulheres: 62 anos de idade e pelo menos 15 anos de contribuição.\n "
                                   "\n"
                                   "Aposentadoria por Tempo de Contribuição: \n "
                                   "Homens: 35 anos de contribuição. \n"
                                   "Mulheres: 30 anos de contribuição. \n"
                                   "\n"
                                   "Valor Estimado do Benefício: O valor da aposentadoria será uma média de 60% "
                                   "da média salarial informada, acrescido de 2% por ano que exceder o tempo mínimo "
                                   "de contribuição.")

                    ]
                )
            )
        if page.route == "/resultados":
            calcular_beneficio()
            page.views.append(
                View(
                    '/resultados', [
                        Text('Resultados'),
                        com_aposentadoria,
                        sem_aposentadoria,
                        beneficio,
                        alerta
                    ]
                )
            )

        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    page.on_view_pop = voltar
    page.on_route_change = gerenciar_rotas
    page.go(page.route)

    def verificar_campos(e):
        try:
            int(media_salarial.value)
            int(idade.value)
            int(tempo_contribuicao.value)

            if genero_escolhido.value is None or idade.error or media_salarial.error or tempo_contribuicao.error or opcao.value is None:
                raise ValueError
            else:
                page.go('/resultados')
        except ValueError:
            print('')
            alerta.value = 'Preencha os campos corretamente'
            page.update()

    def limpar_alerta(e):
        alerta.value = ''
        page.update()

    def calcular_beneficio():
        try:
            genero = genero_escolhido.value
            idade_var = int(idade.value)
            salario = int(media_salarial.value)
            tempo_contribuicao_var = int(tempo_contribuicao.value)
            categoria = opcao.value

            if genero == 'masculino':
                if categoria == 'idade':
                    if idade_var >= 65 and tempo_contribuicao_var >= 15:
                        com_aposentadoria.value = 'Você pode se aposentar!'
                        v = salario * (0.6 + 0.02 * (tempo_contribuicao_var - 15))
                        beneficio.value = v
                    elif idade_var < 65 and tempo_contribuicao_var < 15:
                        sem_aposentadoria.value = 'Você não pode se aposentar'
                    elif idade_var < 65 and tempo_contribuicao_var >= 15:
                        sem_aposentadoria.value = 'Você não pode se aposentar'
                    else:
                        sem_aposentadoria.value = 'Você não pode se aposentar'
                else:
                    if tempo_contribuicao_var >= 35:
                        com_aposentadoria.value = 'Você pode se aposentar'
                        v = salario * (0.6 + 0.02 * (tempo_contribuicao_var - 35))
                        beneficio.value = v
                    else:
                        sem_aposentadoria.value = 'Você não pode se aposentar'
            elif genero == 'feminino':
                if categoria == 'idade':
                    if idade_var >= 62 and tempo_contribuicao_var >= 15:
                        com_aposentadoria.value = 'Você pode se aposentar'
                        v = salario * (0.6 + 0.02 * (tempo_contribuicao_var - 15))
                        beneficio.value = v
                    elif idade_var < 62 and tempo_contribuicao_var < 15:
                        sem_aposentadoria.value = 'Você não pode se aposentar'
                    elif idade_var < 62 and tempo_contribuicao_var >= 15:
                        sem_aposentadoria.value = 'Você não pode se aposentar'
                    else:
                        sem_aposentadoria.value = 'Você não pode se aposentar'
                else:
                    if tempo_contribuicao_var >= 30:
                        com_aposentadoria.value = "Você pode se aposentar"
                        v = salario * (0.6 + 0.02 * (tempo_contribuicao_var - 30))
                        beneficio.value = v
                    else:
                        sem_aposentadoria.value = "Você não pode se aposentar"

        except ValueError:
            alerta.value = 'Preencha todos campos'
        page.update()

    idade =  ft.TextField(label='Idade', border_color=Colors.PINK,
                                  border_radius=10, on_click=limpar_alerta)
    tempo_contribuicao = ft.TextField(label='Tempo de contribuição', border_color=Colors.PINK,
                                  border_radius=10, on_click=limpar_alerta)

    genero_escolhido = ft.Dropdown(
        label="Gênero",
        width=page.window.width,
        border_color=Colors.PINK,
        on_change=limpar_alerta,

        options=[
            Option(key='masculino', text='masculino'), Option(key='feminino', text='feminino')],

    )

    media_salarial = ft.TextField(label='Média salarial', border_color=Colors.PINK,
                                  border_radius=10, on_click=limpar_alerta)

    opcao = ft.RadioGroup(on_change=limpar_alerta, content=ft.Row([
        ft.Radio(value='tempo', label="Tempo de contribuição"),
        ft.Radio(value='idade', label="Idade")
    ]))

    alerta = ft.Text(value='', color="pink",)
    sem_aposentadoria = ft.Text(value='', color="pink")
    com_aposentadoria = ft.Text(value='', color="pink")
    beneficio = ft.Text(value='', color="pink")

ft.app(main)