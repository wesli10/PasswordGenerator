import random
import PySimpleGUI as sg
import os


class PassGen:
    def __init__(self):
        # Layout
        sg.theme('Black')
        layout = [
            [sg.Text('Nome', size=(23, 1)),
             sg.Input(key='nome', size=(30, 1))],
            [sg.Text('Quantidade de Caracteres', size=(23, 1)),
             sg.Input(key='tamanho', size=(30, 1))],
            [sg.Output(size=(53, 5))],
            [sg.Button('Gerar Senha')]
        ]
        # Declaração da Janela
        self.janela = sg.Window('Password Generator', layout)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                self.salvar_senha(nova_senha, valores)
                print(nova_senha)

    def gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%*'
        chars = random.choices(char_list, k=int(valores['tamanho']))
        new_pass = ''.join(chars)
        return new_pass

    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a') as file:
            file.write(f"nome: {valores['nome']}, Senha: {nova_senha}{os.linesep}")


gen = PassGen()
gen.Iniciar()
