from time import sleep
import sys
sys.path.append("src")

import flet as ft
from script import *


def main(page: ft.Page):
    page.title = "PROJETO EM GRUPO M01 - QUERO OS DADOS NA MINHA MESA!"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

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

    def close_app(e):
        page.window_close()

    def close_app_idade(e):
        if idade.value == "00":
            page.window_close()

    def gerar_csv(e):
        
        pb = ft.ProgressBar( height=10, width=400)

        try:
            escrever_csv()
            page.clean()
            
            page.add(ft.Column([ft.Text("Gerando CSV..."), pb, ft.Text("Aguarde um momento...")]))
            
            page.update()
            
            for i in range(0, 101):
                pb.value = i * 0.01
                sleep(0.1)
                page.update()
            
            page.clean()
            
            page.add(check, salvo)
            
            page.update      
        except:
            page.clean()
            
            page.add(error, falha)
            
            page.update

    def salvar_respostas(e):
        print('Respostas salvas')
        input_de_dados()
        
        
        
    nome = ft.TextField(label="Qual o seu nome?")
    
    idade = ft.TextField(label="Qual a sua idade?", on_change=close_app_idade)
    
    pergunta1 = ft.Dropdown(
        label="Você atualmente possui assinatura em uma plataforma de streaming de vídeo?",
        hint_text="Resposta",
        options=[
            ft.dropdown.Option("SIM"),
            ft.dropdown.Option("NÃO"),
            ft.dropdown.Option("NÃO SEI"),
        ],   
    )
    
    pergunta2 = ft.Dropdown(
        label="Você acha que a variedade de conteúdo oferecida por essas plataformas influenciam na sua decisão de assinar ou cancelar uma assinatura?",
        hint_text="Resposta",
        options=[
            ft.dropdown.Option("SIM"),
            ft.dropdown.Option("NÃO"),
            ft.dropdown.Option("NÃO SEI"),
        ],   
    )
    
    pergunta3 = ft.Dropdown(
        label="Você utiliza plataformas de streaming para assistir conteúdo educacional ou informativo?",
        hint_text="Resposta",
        options=[
            ft.dropdown.Option("SIM"),
            ft.dropdown.Option("NÃO"),
            ft.dropdown.Option("NÃO SEI"),
        ],   
    )
    
    pergunta4 = ft.Dropdown(
        label="Você acredita que as plataformas de streaming estão substituindo gradualmente a TV tradicional como principal fonte de entretenimento?",
        hint_text="Resposta",
        options=[
            ft.dropdown.Option("SIM"),
            ft.dropdown.Option("NÃO"),
            ft.dropdown.Option("NÃO SEI"),
        ],
    )

    texto = ft.Text()
    button_salvar_respostas = ft.ElevatedButton(text="Salvar Respostas", on_click=salvar_respostas)
    button_gerar_csv = ft.ElevatedButton(text="Gerar CSV", on_click=gerar_csv)
    button_fechar_app = ft.ElevatedButton(text="Fechar", on_click=close_app)

    row2 = ft.Row(controls=[
        button_salvar_respostas,
        button_gerar_csv,
        button_fechar_app
    ], wrap=True, width=page.window_width)

    row1 = ft.Row(controls=[
        nome,
        idade,
        pergunta1,
        pergunta2,
        pergunta3,
        pergunta4,
        texto,
        row2
    ], wrap=True, width=page.window_width)
    
    
    container = ft.Container(content=row1, padding=30)

    page.add(container)
    
    page.update()
    
    
ft.app(target=main)

