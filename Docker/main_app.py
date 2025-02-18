from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class DataCollectionForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        # Tehsil Dropdown
        self.add_widget(Label(text="Tehsil:"))
        self.tehsil_spinner = Spinner(
            text='Select Tehsil',
            values=['Tehsil 1', 'Tehsil 2', 'Tehsil 3'],
            size_hint=(None, None),
            size=(200, 44),
            pos_hint={'center_x': 0.5}
        )
        self.add_widget(self.tehsil_spinner)

        # UC Name Dropdown
        self.add_widget(Label(text="UC Name:"))
        self.uc_spinner = Spinner(
            text='Select UC',
            values=['UC 1', 'UC 2', 'UC 3'],
            size_hint=(None, None),
            size=(200, 44),
            pos_hint={'center_x': 0.5}
        )
        self.add_widget(self.uc_spinner)

        # Child Name Input
        self.add_widget(Label(text="Child Name:"))
        self.child_name_input = TextInput(hint_text="Enter Child's Name")
        self.add_widget(self.child_name_input)

        # Submit Button
        self.submit_btn = Button(text="Submit", size_hint=(None, None), size=(200, 50))
        self.submit_btn.bind(on_press=self.submit_form)
        self.add_widget(self.submit_btn)

    def submit_form(self, instance):
        # Collecting input data
        tehsil = self.tehsil_spinner.text
        uc_name = self.uc_spinner.text
        child_name = self.child_name_input.text

        # Displaying a popup with the collected data
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=f"Tehsil: {tehsil}"))
        content.add_widget(Label(text=f"UC Name: {uc_name}"))
        content.add_widget(Label(text=f"Child Name: {child_name}"))

        close_btn = Button(text="Close")
        content.add_widget(close_btn)
        popup = Popup(title='Form Data', content=content, size_hint=(0.8, 0.8))
        close_btn.bind(on_press=popup.dismiss)
        popup.open()

class MobileDataApp(App):
    def build(self):
        return DataCollectionForm()

if __name__ == '__main__':
    MobileDataApp().run()
