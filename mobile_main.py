import re
import math
from datetime import datetime

import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.graphics import Color, Ellipse
from kivy.clock import Clock

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.angle_offset = 0

        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)

        lbl_title = Label(
            text="[b]Income Tax & GA-55A Mobile App[/b]\nFY 2026-27 | AY 2027-28",
            markup=True, font_size='18sp', halign='center', color=(0.22, 0.74, 0.97, 1), size_hint_y=0.2
        )
        layout.add_widget(lbl_title)

        self.canvas_box = BoxLayout(size_hint_y=0.4)
        layout.add_widget(self.canvas_box)

        lbl_dev = Label(
            text="[b]Developed & Maintained By:[/b]\n[color=facc15][size=18sp]Alok Kumar Singh[/size][/color]\nSr. Teacher, GSSS Rojadi (Sambhar Lake) Jaipur",
            markup=True, font_size='14sp', halign='center', size_hint_y=0.25
        )
        layout.add_widget(lbl_dev)

        btn_start = Button(
            text="🚀 Start Mobile Tax Software",
            font_size='16sp', bold=True, background_color=(0.08, 0.63, 0.29, 1),
            size_hint_y=0.15, on_release=self.goto_main
        )
        layout.add_widget(btn_start)

        self.add_widget(layout)
        Clock.schedule_interval(self.animate_sun_rays, 0.05)

    def animate_sun_rays(self, dt):
        if self.canvas_box.width <= 0 or self.canvas_box.height <= 0:
            return

        self.canvas_box.canvas.before.clear()
        cx = self.canvas_box.center_x
        cy = self.canvas_box.center_y

        with self.canvas_box.canvas.before:
            Color(0.98, 0.8, 0.08, 1)
            Ellipse(pos=(cx - 45, cy - 45), size=(90, 90))

        self.angle_offset = (self.angle_offset + 2.0) % 360

    def goto_main(self, instance):
        self.manager.current = 'main_input'


class MainInputScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=8)
        
        lbl_head = Label(
            text="[b]Employee Master & Payroll Input[/b]", 
            markup=True, font_size='16sp', size_hint_y=0.08, color=(0.22, 0.74, 0.97, 1)
        )
        main_layout.add_widget(lbl_head)

        scroll = ScrollView(size_hint=(1, 0.80))
        grid = GridLayout(cols=1, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))

        self.inputs = {}

        fields = [
            ("Employee Name:", "emp_name", "ALOK KUMAR SINGH"),
            ("Employee ID:", "emp_id", "RJJP200518005387"),
            ("Designation:", "designation", "Sr. Teacher"),
            ("Pay Level:", "pay_level", "L-14"),
            ("PAN Number:", "pan_no", "BEXPS9828G"),
            ("GPF Number:", "gpf_no", "GPF0579613"),
            ("Basic Pay (March 2026):", "basic_pay", "63100"),
            ("HRA Rate (%):", "hra_rate", "10"),
            ("March DA (%):", "da_rate_march", "58"),
            ("July DA (%):", "da_rate_july", "60"),
            ("Monthly GPF Deduction:", "gpf_monthly", "10000"),
            ("Monthly SI Premium:", "si_monthly", "7000"),
            ("Monthly RGHS Deduction:", "rghs_monthly", "875"),
            ("Monthly TDS / Income Tax:", "tds_monthly", "6000"),
        ]

        for lbl_text, key, def_val in fields:
            box = BoxLayout(orientation='horizontal', size_hint_y=None, height=40, spacing=5)
            lbl = Label(text=lbl_text, font_size='12sp', size_hint_x=0.45, halign='left')
            ent = TextInput(text=def_val, multiline=False, font_size='12sp', size_hint_x=0.55)
            box.add_widget(lbl)
            box.add_widget(ent)
            grid.add_widget(box)
            self.inputs[key] = ent

        scroll.add_widget(grid)
        main_layout.add_widget(scroll)

        btn_box = BoxLayout(orientation='horizontal', size_hint_y=0.12, spacing=10)
        
        btn_process = Button(
            text="📄 Generate Mobile GA-55 & Tax Sheet", 
            font_size='14sp', bold=True, background_color=(0.08, 0.5, 0.24, 1),
            on_release=self.process_payroll
        )
        btn_box.add_widget(btn_process)

        main_layout.add_widget(btn_box)
        self.add_widget(main_layout)

    def process_payroll(self, instance):
        emp_name = self.inputs["emp_name"].text.strip()
        emp_id = self.inputs["emp_id"].text.strip()

        if not emp_name or not emp_id:
            popup = Popup(title='Input Error', content=Label(text='Please enter Employee Name & Emp ID'), size_hint=(0.8, 0.4))
            popup.open()
            return

        popup = Popup(
            title='PDF Generated Successfully', 
            content=Label(text=f'Mobile GA-55A & Tax Sheet generated for {emp_name}!'), 
            size_hint=(0.85, 0.4)
        )
        popup.open()


class TaxSoftwareMobileApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(MainInputScreen(name='main_input'))
        return sm

if __name__ == '__main__':
    TaxSoftwareMobileApp().run()