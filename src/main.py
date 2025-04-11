import flet as ft
from flet.core.dropdown import Option


def main(page: ft.Page):
    # Configuração da página
    page.title = 'Simulador de aposentadoria'
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667

    # Definição de funções
    def aposentadoria():
        if tipo_aposentadoria == "idade":
            if genero == "Fem":
                if int(idade.value) >= 62:
                    if int(tempo_contribuicao.value) < 15:
                        mensagem = "Você poderá se aposentar assim que completar 15 anos de contribuição"
                    elif int(tempo_contribuicao.value) >= 15:
                        mensagem = "Você já pode se aposentar"
                elif int(idade.value) < 62:
                    if int(tempo_contribuicao.value) >= 30:
                        mensagem = "Tente se aposentar por tempo de contribuição"
                    elif int(tempo_contribuicao.value) >= 15:
                        mensagem = "Você não pode se aposentar por idade, mas já possui o tempo de contribuição necessário"
                    else:
                        mensagem = "Você só pode se aposentar depois de completar 62 anos e ter 15 anos de contribuição"
            elif genero == "Masc":
                if int(idade.value) >= 65:
                    if int(tempo_contribuicao.value) < 15:
                        mensagem = "Você poderá se aposentar assim que completar 15 anos de contribuição"
                    elif int(tempo_contribuicao.value) >= 15:
                        mensagem = "Você já pode se aposentar"
                elif int(idade.value) < 65:
                    if int(tempo_contribuicao.value) >= 35:
                        mensagem = "Tente se aposentar por tempo de contribuição"
                    elif int(tempo_contribuicao.value) >= 15:
                        mensagem = "Você não pode se aposentar por idade, mas já possui o tempo de contribuição necessário"
                    else:
                        mensagem = "Você só pode se aposentar depois de completar 65 anos e ter 15 anos de contribuição"
        elif tipo_aposentadoria == "tempo":
            if genero == "Fem":
                if int(tempo_contribuicao.value) >= 30:
                    mensagem = "Você já pode se aposentar por tempo de contribuição"
                elif int(tempo_contribuicao.value) < 30:
                    mensagem = "Você não pode se aposentar ainda"
            if genero == "Masc":
                if int(tempo_contribuicao.value) >= 35:
                    mensagem = "Você já pode se aposentar por tempo de contribuição"
                elif int(tempo_contribuicao.value) < 35:
                    mensagem = "Você não pode se aposentar ainda"
            return mensagem



    # Criação de componentes
    idade = ft.TextField(label='Idade', hint_text='Idade em anos. EX: 58')
    genero = ft.Dropdown(
        label='Gênero', options=[Option(key="Masc", text="Masculino"), Option(key="Fem", text="Feminino")]
    )
    tempo_contribuicao = ft.TextField(label='Tempo de contribuição',
                                      hint_text='Tempo de contribuição em anos. EX: 14')
    media_salarial = ft.TextField(label='Média salarial',
                                  hint_text='Média salarial de pelo menos os últimos cinco anos de contribuição. EX: $1580')
    tipo_aposentadoria = ft.Dropdown(
        label='Categoria de aposentadoria', hint_text='Escolha uma opção',
        options=[Option(key="tempo", text="Tempo de contribuição"), Option(key='idade', text="Por idade")])

    # Construir o layout
    page.add(
        tipo_aposentadoria,
        idade,
        genero,
        tempo_contribuicao,
        media_salarial
    )


ft.app(main)

