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
        
        flo = FloatLayout()
        icon_login = AsyncImage(
            source='https://cdn-icons-png.freepik.com/512/295/295128.png',
            pos=(325, 350),
            size_hint= (.4, .4)
            )

        flo.add_widget(icon_login)
        l1 = Button(
            text="Login", size_hint=(.2, .1),
            pos=(200, 350), color = [1,1,1,1]
        )

        flo.add_widget(l1)

        self.t1 = TextInput(size_hint=(.4, .1), pos=(400, 350))
        flo.add_widget(self.t1)
        
        l2 = Button(
            text="Senha", size_hint=(.2, .1),
            pos=(200, 250),color = [1,1,1,1]
        )
        
        flo.add_widget(l2)

        t2 = TextInput(
            multiline=True, size_hint=(.4, .1), pos=(400, 250)
        )

        flo.add_widget(t2)
        
        b1 = Button(
            text='Entrar', size_hint = (.2, .1),
            pos_hint = {'center_x':.5, 'center_y':.07},
            on_press = self.entrar
        )
        b2 = Button(
            text='Cadastrar', size_hint = (.2, .1),
            pos_hint = {'center_x':.5, 'center_y':.20},
            on_press = self.cadastrar
        )
        
        self.label_cadastrar = Label(
            pos_hint = {'center_x': .50, 'center_y': .30}, 
            color = [1,1,1,1]
        )

        self.label_entrar = Label(
            pos_hint = {'center_x': .50, 'center_y': .30}, 
            color = [1,1,1,1]
        )
        
        flo.add_widget(b1)
        flo.add_widget(b2)
        flo.add_widget(self.label_cadastrar)
        flo.add_widget(self.label_entrar)
        
        return flo

    def cadastrar(self, instance):
        login = self.t1.text
        mensagem = f'O Login {login} foi cadastrado!'
        self.label_cadastrar.text = mensagem
    
    def entrar(self, instance):
        login = self.t1.text
        mensagem = f'O login {login} entrou no sistema!'
        self.label_cadastrar.text = mensagem

      
FloatApp().run()