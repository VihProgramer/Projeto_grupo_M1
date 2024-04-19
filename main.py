from time import sleep
import flet as ft
from src.script import input_de_dados, escrever_csv, contar_respostas, respostas, total_masculino, total_feminino
from src.view import *

data = []

def main(page: ft.Page):
    page.title = "PROJETO EM GRUPO M01 - QUERO OS DADOS NA MINHA MESA!"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_min_height = 1280
    page.window_height = 1280
    page.window_min_width = 720
    page.window_width = 720

    banner_title = ft.Stack([
        ft.Text(
            spans=[
                ft.TextSpan(
                    "SQUAD 6",
                    ft.TextStyle(
                        size=130,
                        weight=ft.FontWeight.BOLD,
                        foreground=ft.Paint(
                            ft.colors.INVERSE_SURFACE,
                            stroke_width=6,
                            stroke_join=ft.StrokeJoin.ROUND,
                            style=ft.PaintingStyle.STROKE,
                        )
                    )
                )
            ]
        ),
        ft.Text(
            spans=[
                ft.TextSpan(
                    "SQUAD 6",
                    ft.TextStyle(
                        size=130,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.GREY_300,
                    ),
                ),
            ],
        ),
    ])

    banner = ft.Container(
        banner_title,
        image_src=f"src/view/bg_banner.jpeg",
        image_fit=ft.ImageFit.COVER,
        alignment=ft.alignment.center,
        width=max,
        height=ft.AdaptiveControl,
        border_radius=10,
        margin=ft.margin.only(bottom=50),
        border=ft.border.all(1, ft.colors.INVERSE_SURFACE),
        blur=ft.Blur(50,50,tile_mode=ft.BlurTileMode.REPEATED),
    )

    c1 = ft.Container(
        ft.Icon(name=ft.icons.CHECK_CIRCLE_OUTLINED, color=ft.colors.ON_INVERSE_SURFACE),
        alignment=ft.alignment.center,
        width=50,
        height=50,
        bgcolor=ft.colors.GREEN_500,
        border_radius=50
    )

    c2 = ft.Container(
        ft.Icon(name=ft.icons.ERROR_OUTLINE, color=ft.colors.ON_INVERSE_SURFACE),
        alignment=ft.alignment.center,
        width=50,
        height=50,
        bgcolor=ft.colors.RED_500,
        border_radius=50
    )

    def grafico(to_y_sim, to_y_nao, to_y_nao_sei, title):
        return ft.BarChart(
            bar_groups=[
                ft.BarChartGroup(
                    x=0,
                    bar_rods=[
                        ft.BarChartRod(
                            from_y=0,
                            to_y=to_y_sim,
                            width=40,
                            color=ft.colors.GREEN,
                            tooltip="SIM",
                            border_radius=0,
                        ),
                    ],
                ),
                ft.BarChartGroup(
                    x=1,
                    bar_rods=[
                        ft.BarChartRod(
                            from_y=0,
                            to_y=to_y_nao,
                            width=40,
                            color=ft.colors.RED,
                            tooltip="NÃO",
                            border_radius=0,
                        ),
                    ],
                ),
                ft.BarChartGroup(
                    x=2,
                    bar_rods=[
                        ft.BarChartRod(
                            from_y=0,
                            to_y=to_y_nao_sei,
                            width=40,
                            color=ft.colors.YELLOW,
                            tooltip="NÃO SEI",
                            tooltip_style=ft.colors.AMBER,
                            border_radius=0,
                        ),
                    ],
                ),
            ],
            border=ft.border.all(1, ft.colors.ON_SURFACE),
            left_axis=ft.ChartAxis(
                labels_size=40, title=ft.Text(title), title_size=40
            ),
            bottom_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        value=0, label=ft.Container(ft.Text("SIM"), padding=10)
                    ),
                    ft.ChartAxisLabel(
                        value=1, label=ft.Container(ft.Text("NÃO"), padding=10)
                    ),
                    ft.ChartAxisLabel(
                        value=2, label=ft.Container(ft.Text("NÃO SEI"), padding=10)
                    ),
                ],
                labels_size=40,
            ),
            horizontal_grid_lines=ft.ChartGridLines(
                color=ft.colors.GREY_300, width=1, dash_pattern=[3, 3]
            ),
            tooltip_bgcolor=ft.colors.with_opacity(0.5, ft.colors.GREY_300),
            max_y=110,
            interactive=True,
            # expand=True,
        )
    
    salvo = ft.Text("ARQUIVO GERADO COM SUCESSO!", style=ft.TextThemeStyle.HEADLINE_SMALL)

    falha = ft.Text("FALHA AO GERAR O ARQUIVO!", style=ft.TextThemeStyle.HEADLINE_SMALL)


    check = ft.AnimatedSwitcher(
        c1,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
    )

    error = ft.AnimatedSwitcher(
        c2,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
    )

    def exibir_alerta(titulo, mensagem, console):
        alertar = ft.AlertDialog(
            title=ft.Text(titulo), content=ft.Text(mensagem), on_dismiss=lambda e: print(console)
        )
        return alertar
    
    def confirmar_encerramento(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()
        return


    def fechar_app(e):
        page.window_close()
        return

    def fechar_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = False
        page.update()
    
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Por favor confirme"),
        content=ft.Text("Tem certeza que deseja encerrar a aplicação"),
        actions=[
            ft.TextButton("Sim", on_click=fechar_app),
            ft.TextButton("Não", on_click=fechar_modal),
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )


    def close_app_idade(e):
        if idade.value == "00":
            page.window_close()
        return

    def gerar_csv(e):
        global data
        pb = ft.ProgressBar( height=10, width=400)

        try:
            escrever_csv(data)
            page.clean()
            page.add(ft.Column([ft.Text("Gerando CSV..."), pb, ft.Text("Aguarde um momento...")]))
            page.update()
            
            for i in range(0, 15):
                pb.value = i * 0.08
                sleep(0.125)
                page.update()
            
            page.clean()
            page.add(check, salvo, button_inicio)
            page.update()   
        except:
            page.clean()
            
            page.add(error, falha, button_inicio)
            
            page.update()

    def salvar_respostas(e):
        global data
        entrevistado = input_de_dados(
            genero.value, idade.value, pergunta_1.value, pergunta_2.value, pergunta_3.value, pergunta_4.value, pergunta_extra_1.value, pergunta_extra_2.value
        )
        if entrevistado:
            data.append(
                [entrevistado.genero, entrevistado.idade, entrevistado.resposta_1, entrevistado.resposta_2, entrevistado.resposta_3, entrevistado.resposta_4,entrevistado.resposta_extra_1,entrevistado.resposta_extra_2, entrevistado.data_hora.strftime("%d/%m/%Y")]
            )
            limpaTela()

        else:
            alertar = exibir_alerta("Atenção!","Preencha todos os campos corretamente!", "")
            page.dialog = alertar
            alertar.open = True
            page.update()

    def limpaTela():
        try:
            genero.value = ''
            idade.value = ''
            pergunta_1.value = ''
            pergunta_2.value = ''
            pergunta_3.value = ''
            pergunta_4.value = ''
            pergunta_extra_1.value = ''
            pergunta_extra_2.value = ''
            alertar = exibir_alerta("Obrigado!","Suas respostas foram salvas com sucesso!", "")
            page.dialog = alertar
            alertar.open = True
            page.update()

        except Exception as e:
            print(f"Erro: {e}")
            return False
        
    def mostrar_grafico(e):
        global total_masculino, total_feminino, respostas
        print(data)
        contar_respostas(data)


        row_graficos = ft.Column(controls=[
            grafico(respostas["Resposta 1"]["SIM"], respostas["Resposta 1"]["NÃO"], respostas["Resposta 1"]["NÃO SEI"], 'Pergunta 1'),
            grafico(respostas["Resposta 2"]["SIM"], respostas["Resposta 2"]["NÃO"], respostas["Resposta 2"]["NÃO SEI"], 'Pergunta 2'),
            grafico(respostas["Resposta 3"]["SIM"], respostas["Resposta 3"]["NÃO"], respostas["Resposta 3"]["NÃO SEI"], 'Pergunta 3'),
            grafico(respostas["Resposta 4"]["SIM"], respostas["Resposta 4"]["NÃO"], respostas["Resposta 4"]["NÃO SEI"], 'Pergunta 4'),
            grafico(respostas["Resposta 5"]["SIM"], respostas["Resposta 5"]["NÃO"], respostas["Resposta 5"]["NÃO SEI"], 'Pergunta 5'),
            grafico(respostas["Resposta 6"]["SIM"], respostas["Resposta 6"]["NÃO"], respostas["Resposta 6"]["NÃO SEI"], 'Pergunta 6')
        ], width=page.window_width)

        row_graficos = ft.ResponsiveRow([
                ft.Container(
                    grafico(respostas["Resposta 1"]["SIM"], respostas["Resposta 1"]["NÃO"], respostas["Resposta 1"]["NÃO SEI"], 'Pergunta 1'),
                    padding=5,
                    col={"sm": 6, "md": 4, "xl": 6},
                ),
                ft.Container(
                    grafico(respostas["Resposta 2"]["SIM"], respostas["Resposta 2"]["NÃO"], respostas["Resposta 2"]["NÃO SEI"], 'Pergunta 2'),
                    padding=5,
                    col={"sm": 6, "md": 4, "xl": 6},
                ),
                ft.Container(
                    grafico(respostas["Resposta 3"]["SIM"], respostas["Resposta 3"]["NÃO"], respostas["Resposta 3"]["NÃO SEI"], 'Pergunta 3'),
                    padding=5,
                    col={"sm": 6, "md": 4, "xl": 6},
                ),
                ft.Container( 
                    grafico(respostas["Resposta 4"]["SIM"], respostas["Resposta 4"]["NÃO"], respostas["Resposta 4"]["NÃO SEI"], 'Pergunta 4'),
                    padding=5,
                    col={"sm": 6, "md": 4, "xl": 6},
                ),
                ft.Container(
                    grafico(respostas["Resposta 5"]["SIM"], respostas["Resposta 5"]["NÃO"], respostas["Resposta 5"]["NÃO SEI"], 'Pergunta 5'),
                    padding=5,
                    col={"sm": 6, "md": 4, "xl": 6},
                ),
                ft.Container( 
                    grafico(respostas["Resposta 6"]["SIM"], respostas["Resposta 6"]["NÃO"], respostas["Resposta 6"]["NÃO SEI"], 'Pergunta 6'),
                    padding=5,
                    col={"sm": 6, "md": 4, "xl": 6},
                ),
            ]
        )

        
        page.clean()
        page.add(row_graficos)
        page.add(button_inicio)
        page.update()



    genero = ft.TextField(label="Qual o seu gênero?")
    
    idade = ft.TextField(label="Qual a sua idade?", on_change=close_app_idade)
    
    pergunta_1 = ft.Dropdown(
        label="Você atualmente possui assinatura em uma plataforma de streaming de vídeo?",
        hint_text="Resposta",
        options=[
            ft.dropdown.Option("SIM"),
            ft.dropdown.Option("NÃO"),
            ft.dropdown.Option("NÃO SEI"),
        ],   
    )
    
    pergunta_2 = ft.Dropdown(
        label="Você acha que a variedade de conteúdo oferecida por essas plataformas influenciam na sua decisão de assinar ou cancelar uma assinatura?",
        hint_text="Resposta",
        options=[
            ft.dropdown.Option("SIM"),
            ft.dropdown.Option("NÃO"),
            ft.dropdown.Option("NÃO SEI"),
        ],   
    )
    
    pergunta_3 = ft.Dropdown(
        label="Você utiliza plataformas de streaming para assistir conteúdo educacional ou informativo?",
        hint_text="Resposta",
        options=[
            ft.dropdown.Option("SIM"),
            ft.dropdown.Option("NÃO"),
            ft.dropdown.Option("NÃO SEI"),
        ],   
    )
    
    pergunta_4 = ft.Dropdown(
        label="Você acredita que as plataformas de streaming estão substituindo gradualmente a TV tradicional como principal fonte de entretenimento?",
        hint_text="Resposta",
        options=[
            ft.dropdown.Option("SIM"),
            ft.dropdown.Option("NÃO"),
            ft.dropdown.Option("NÃO SEI"),
        ],
    )

    pergunta_extra_1 = ft.Dropdown(
        label="Você acompanha as novidades e lançamentos de conteúdo nas plataformas de streaming que assina?",
        hint_text="Resposta",
        options=[
            ft.dropdown.Option("SIM"),
            ft.dropdown.Option("NÃO"),
            ft.dropdown.Option("NÃO SEI"),
        ],
    )
    pergunta_extra_2 = ft.Dropdown(
        label="Você costuma assistir a conteúdo em plataformas de streaming enquanto realiza outras atividades, como trabalhar ou fazer exercícios?",
        hint_text="Resposta",
        options=[
            ft.dropdown.Option("SIM"),
            ft.dropdown.Option("NÃO"),
            ft.dropdown.Option("NÃO SEI"),
        ],
    )

    row_perguntas = ft.ResponsiveRow([
        ft.Container(
            genero,
            padding=5,
            col={"sm": 12, "md": 4, "xl": 6},
        ),
        ft.Container(
            idade,
            padding=5,
            col={"sm": 12, "md": 4, "xl": 6},
        ),
        ft.Container(
            pergunta_1,
            padding=5,
            col={"sm": 12, "md": 4, "xl": 6},
        ),
        ft.Container(
            pergunta_2,
            padding=5,
            col={"sm": 12, "md": 4, "xl": 6},
        ),
        ft.Container(
            pergunta_3,
            padding=5,
            col={"sm": 12, "md": 4, "xl": 6},
        ),
        ft.Container( 
            pergunta_4,
            padding=5,
            col={"sm": 12, "md": 4, "xl": 6},
        ),
        ft.Container(
            pergunta_extra_1,
            padding=5,
            col={"sm": 12, "md": 4, "xl": 6},
        ),
        ft.Container( 
            pergunta_extra_2,
            padding=5,
            col={"sm": 12, "md": 4, "xl": 6},
        ),
    ])

    def voltar_inicio(e):
        page.clean()
        container = ft.Container(content=row1, padding=30, width=max, height=max)
        page.add(container)
        page.update

    button_salvar_respostas = ft.ElevatedButton(text="Salvar Respostas", on_click=salvar_respostas, icon='save', color=ft.colors.ON_SURFACE)
    button_gerar_csv = ft.ElevatedButton(text="Gerar CSV", on_click=gerar_csv, icon='sync', color=ft.colors.ON_SURFACE)
    button_mostrar_grafico = ft.ElevatedButton(text="Gráfico", on_click=mostrar_grafico, icon='REMOVE_RED_EYE', color=ft.colors.ON_SURFACE)
    button_fechar_app = ft.ElevatedButton(text="Fechar", on_click=confirmar_encerramento, icon='close', color=ft.colors.ON_SURFACE)
    button_inicio = ft.ElevatedButton(text="Início", on_click=voltar_inicio, icon='home', color=ft.colors.ON_SURFACE)

    row_buttons = ft.Row(controls=[
        button_salvar_respostas,
        button_gerar_csv,
        button_mostrar_grafico,
        button_fechar_app,
    ], wrap=True, width=page.window_width, col={"sm": 12, "md": 4, "xl": 6})

    row1 = ft.Row(controls=[
        banner,
        row_perguntas,
        row_buttons
    ], wrap=True, width=max)
    
    
    container = ft.Container(content=row1, padding=30, width=max, height=max)

    page.add(container)
    
    
    
ft.app(target=main)

