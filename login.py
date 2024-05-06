from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage

class Tela_Login (App):
    def build(self):
        Window.clearcolor[1,1,1,1]

        layout = FloatLayout()
        
        icon_login = AsyncImage(source='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYIVzk5YNtb9B9KuWbVrWQTCpzxq3iY3eQn7xzw2VKfw&s',  pos_hint={'center_x':0.10, 'center_y':0.10})
        self.input_login = TextInput(hint_text='Login: ', pos_hint={'center_x':0.8, 'center_y':0.8}, color=[0,0,0,1])
        self.input_senha = TextInput(hint_text='Senha: ', pos_hint={'center_x':0.6, 'center_y':0.6}, color=[0,0,0,1])

        botao_entrar = Button(text='Entrar', size_hint=(None, None), size=(150,100), pos_hint={'center_x': 0.4, 'center_y': 0.4}, on_press = self.entrar)
        botao_cadastrar = Button(text='Cadastrar', size_hint=(None, None), size=(150,100), pos_hint={'center_x': 0.2, 'center_y': 0.2}, on_press = self.cadastrar)

        self.label_cadastrar = Label(color=[0,0,0,1])
        self.label_entrar = Label(color=[0,0,0,1])

        layout.add_widget(icon_login)
        layout.add_widget(self.input_login)
        layout.add_widget(self.input_senha)
        layout.add_widget(botao_cadastrar)
        layout.add_widget(botao_entrar)
        layout.add_widget(self.label_cadastrar)
        layout.add_widget(self.label_entrar)

        return layout

    def cadastrar(self, instance):
        login = self.input_login.text
        mensagem = f'O Login {login} foi cadastrado'
        self.label_cadastrar.text = mensagem
    
    def entrar(self, instance):
        login = self.input_login.text
        mensagem = f'O Login {login} entrou no sistema'
        self.label_entrar.text = mensagem

Tela_Login().run()
    
    

