import flet as ft
from flet import AppBar, ElevatedButton, Text, View
from flet.core.colors import Colors
from flet.core.container import Container
from flet.core.cupertino_button import CupertinoButton
from flet.core.dropdown import Option
from flet.core.image import Image


def main(page: ft.Page):
    # Configuração da página
    page.title = 'Simulador de aposentadoria'
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.LIGHT
    page.bgcolor = Colors.BLACK12
    page.window.width = 375
    page.window.height = 667

    # Definição de funções
    def gerar_rotas(e):
        # Construir layout
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    img,

                    ElevatedButton(text="Simular aposentadoria", width=355, style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10)), color=Colors.BLACK, bgcolor=Colors.YELLOW_500,
                                   on_click=lambda _: page.go("/simular_aposentadoria")),

                    ElevatedButton(text="Regras de aposentadoria", width=355, style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10)), color=Colors.YELLOW_500, bgcolor=Colors.BLACK12,
                                   on_click=lambda _: page.go("/regras")),

                ],
            )
        )
        if page.route == "/simular_aposentadoria":
            page.views.append(
                View(
                    "/simular_aposentadoria",
                    [
                        AppBar(title=Text("Simular aposentadoria"), bgcolor=Colors.GREEN_800),

                        idade,
                        genero,
                        tempo_contribuicao,
                        media_salarial,
                        tipo_aposentadoria,
                        alerta,

                        CupertinoButton(
                            content=ft.Text("Simular Aposentadoria"),
                            bgcolor=Colors.GREEN_800,
                            color=Colors.YELLOW_500,
                            opacity_on_click=0.3,
                            on_click=lambda _: verifica_campos(e),
                        )
                    ]
                )
            )
        elif page.route == "/regras":
            page.views.append(
                View(
                    "/regras",
                    [
                        AppBar(title=Text("Regras de aposentadoria"), bgcolor=Colors.GREEN_800),
                        regras
                    ]
                )
            )

        elif page.route == "/resultado":
            simular_aposentadoria()
            page.views.append(
                View(
                    "/resultado",
                    [
                        AppBar(title=Text("Resultado"), bgcolor=Colors.GREEN_800),
                        mensagem

                    ]
                )
            )

        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    def verifica_campos(e):
        try:
            int(media_salarial.value)
            int(idade.value)
            int(tempo_contribuicao.value)

            if genero.value is None or media_salarial.error or idade.error  or tempo_contribuicao.error or tipo_aposentadoria.value is None:
                raise ValueError
            else:
                page.go('/resultado')
        except ValueError:
            print('')
            alerta.value = 'Preencha os campos corretamente'
            page.update()

    def limpar_alerta(e):
        alerta.value = ''
        page.update()

    def simular_aposentadoria():
        try:
            if tipo_aposentadoria == "idade":
                if genero == "Fem":
                    if int(idade.value) >= 62:
                        if int(tempo_contribuicao.value) < 15:
                            mensagem.value = "Você poderá se aposentar assim que completar 15 anos de contribuição"
                        elif int(tempo_contribuicao.value) >= 15:
                            mensagem.value = "Você já pode se aposentar"
                    elif int(idade.value) < 62:
                        if int(tempo_contribuicao.value) >= 30:
                            mensagem.value = "Tente se aposentar por tempo de contribuição"
                        elif int(tempo_contribuicao.value) >= 15:
                            mensagem.value = "Você não pode se aposentar por idade, mas já possui o tempo de contribuição necessário"
                        else:
                            mensagem.value = "Você só pode se aposentar depois de completar 62 anos e ter 15 anos de contribuição"
                elif genero == "Masc":
                    if int(idade.value) >= 65:
                        if int(tempo_contribuicao.value) < 15:
                            mensagem.value = "Você poderá se aposentar assim que completar 15 anos de contribuição"
                        elif int(tempo_contribuicao.value) >= 15:
                            mensagem.value = "Você já pode se aposentar"
                    elif int(idade.value) < 65:
                        if int(tempo_contribuicao.value) >= 35:
                            mensagem.value = "Tente se aposentar por tempo de contribuição"
                        elif int(tempo_contribuicao.value) >= 15:
                            mensagem.value = "Você não pode se aposentar por idade, mas já possui o tempo de contribuição necessário"
                        else:
                            mensagem.value = "Você só pode se aposentar depois de completar 65 anos e ter 15 anos de contribuição"
            elif tipo_aposentadoria == "tempo":
                if genero == "Fem":
                    if int(tempo_contribuicao.value) >= 30:
                        mensagem.value = "Você já pode se aposentar por tempo de contribuição"
                    elif int(tempo_contribuicao.value) < 30:
                        mensagem.value = "Você não pode se aposentar ainda"
                if genero == "Masc":
                    if int(tempo_contribuicao.value) >= 35:
                        mensagem.value = "Você já pode se aposentar por tempo de contribuição"
                    elif int(tempo_contribuicao.value) < 35:
                        mensagem.value = "Você não pode se aposentar ainda"
            page.update()
        except ValueError:
            alerta.value = 'Preencha todos os campos'



    # Criação de componentes7
    img = ft.Image(
        src="assets/logo.png",
        width=365,
        height=520,
    )
    # logo = ft.Row(width=img.width, height=img.height, wrap=False)

    regras = ft.Text("\n Aposentadoria por Idade:\n- Homens: 65 anos de idade e pelo menos 15 anos de contribuição.\n"
                     "- Mulheres: 62 anos de idade e pelo menos 15 anos de contribuição.\n \n Aposentadoria por Tempo de Contribuição:\n"
                     "- Homens: 35 anos de contribuição. \n- Mulheres: 30 anos de contribuição. \n \n Valor Estimado do Benefício: \n "
                     "O valor da aposentadoria será uma média de 60% da média salarial informada,"
                     " acrescido de 2% por ano que exceder o tempo mínimo de contribuição.")

    alerta = ft.Text("")

    mensagem = ft.Text("")

    idade = ft.TextField(label='Idade', hint_text='Idade em anos. EX: 58')
    genero = ft.Dropdown(
        label='Gênero', width=page.window.width,
        options=[Option(key="Masc", text="Masculino"), Option(key="Fem", text="Feminino")])

    tempo_contribuicao = ft.TextField(label='Tempo de contribuição',
                                      hint_text='Tempo de contribuição em anos. EX: 14')
    media_salarial = ft.TextField(label='Média salarial',
                                  hint_text='Média salarial de pelo menos os últimos cinco anos de contribuição. EX: $1580')
    tipo_aposentadoria = ft.Dropdown(
        label='Categoria de aposentadoria', hint_text='Escolha uma opção', width=page.window.width,
        options=[Option(key="tempo", text="Tempo de contribuição"), Option(key='idade', text="Por idade")])

    page.on_route_change = gerar_rotas
    page.go(page.route)
    page.on_view_pop = voltar

ft.app(main)
