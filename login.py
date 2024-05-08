from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.image import AsyncImage

Window.size = (900,500)

class FloatApp(App):
    def build(self):
        Window.clearcolor=(0, 0, 1, 0)
        
        layout_principal = FloatLayout()
        icon_login = AsyncImage(
            source='https://cdn-icons-png.freepik.com/512/295/295128.png',
            pos=(325, 350),
            size_hint= (.4, .4)
            )
        
        layout_principal.add_widget(icon_login)

        label_login = Label(
            text="Login", 
            size_hint=(.2, .1),
            pos=(195, 350),
            color = [1,1,1,1],
            halign = ('center')
        )
        with label_login.canvas.before:
            Color (0.2, 0.5, 0.7, 1),
            Rectangle (
            pos=(200,350),
            size=(200, 60)
            )

        layout_principal.add_widget(label_login)

        self.input_login = TextInput(
            multiline= False,
            size_hint=(.4, .1),
            pos=(400, 350),
            hint_text='Digite o seu login aqui...',
            padding_y=(20)
            )
        
        layout_principal.add_widget(self.input_login)
        
        label_senha = Label(
            text="Senha", 
            size_hint=(.2, .1),
            pos=(195, 250),
            color = [1,1,1,1],
            halign = ('center')
        )
        with label_senha.canvas.before:
            Color (0.2, 0.5, 0.7, 1),
            Rectangle (
            pos=(200,250),
            size=(200, 60)
            )
        
        layout_principal.add_widget(label_senha)

        input_senha = TextInput(
            multiline= False,
            size_hint=(.4, .1),
            pos=(400, 250),
            hint_text='Digite o sua senha aqui...',
            padding_y=(20)
        )

        layout_principal.add_widget(input_senha)
        
        botao_entrar = Button(
            text='Entrar', 
            size_hint = (.2, .1),
            pos_hint = {'center_x':.5,'center_y':.07},
            on_press = self.entrar
        )

        layout_principal.add_widget(botao_entrar)

        botao_cadastrar = Button(
            text='Cadastrar', 
            size_hint = (.2, .1),
            pos_hint = {'center_x':.5, 'center_y':.20},
            on_press = self.cadastrar
        )
        
        layout_principal.add_widget(botao_cadastrar)

        self.label_cadastrar = Label(
            pos_hint = {'center_x': .50, 'center_y': .30}, 
            color = [1,1,1,1]
        )

        layout_principal.add_widget(self.label_cadastrar)

        self.label_entrar = Label(
            pos_hint = {'center_x': .50, 'center_y': .30}, 
            color = [1,1,1,1]
        )
        
        layout_principal.add_widget(self.label_entrar)
        
        return layout_principal

    def cadastrar(self, instance):
        login = self.input_login.text
        mensagem = f'O Login {login} foi cadastrado!'
        self.label_cadastrar.text = mensagem
    
    def entrar(self, instance):
        login = self.input_login.text
        mensagem = f'O Login {login} entrou no sistema!'
        self.label_cadastrar.text = mensagem

      
FloatApp().run()