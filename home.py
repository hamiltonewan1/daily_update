from kivymd.app import MDApp
from kivy.lang import Builder

kv = """
Screen:
    MDFillRoundFlatIconButton:
        width: 300
        md_bg_color:"#210070"
        text: "           Click for a Metal Song            "
        icon: "guitar-electric"
        radius: [15, 15, 15, 15]
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        on_press:
            app.action_metal_song()
        on_touch_down:
            md_bg_color:"#A569BD"

    MDFillRoundFlatIconButton:
        width: 300
        md_bg_color:"#210070"
        text: "           Click for  a Classical Song            "
        icon: "violin"
        radius: [15, 15, 15, 15]
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        on_press:
            app.action_classical_song()
        on_touch_down:
            md_bg_color:"#A569BD"

    MDFillRoundFlatIconButton:
        width: 300
        md_bg_color:"#210070"
        text: "           Click for a Joke            "
        icon: "microphone-variant"
        radius: [15, 15, 15, 15]
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        on_press:
            app.action_joke()
        on_touch_down:
            md_bg_color:"#A569BD"

    MDFillRoundFlatIconButton:
        width: 300
        md_bg_color:"#210070"
        text: "           Click for a Word            "
        icon: "book-education"
        radius: [15, 15, 15, 15]
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        on_press:
            app.action_word()
        on_touch_down:
            md_bg_color:"#A569BD"

    MDFillRoundFlatIconButton:
        width: 300
        md_bg_color:"#210070"
        text: "           Click for a Fact            "
        icon: "notebook"
        radius: [15, 15, 15, 15]
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        on_press:
            app.action_fact()
        on_touch_down:
            md_bg_color:"#A569BD"
"""


class Main(MDApp):
    def action_metal_song(self):
        import get_metal_song

    def action_classical_song(self):
        import get_classical_song

    def action_joke(self):
        import get_joke

    def action_word(self):
        import get_word

    def action_fact(self):
        import get_fact

    def build(self):
        return Builder.load_string(kv)


Main().run()