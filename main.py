import os
import subprocess
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import platform

# ตั้งค่าขนาดหน้าต่าง Widget ลอยเล็กๆ ใน Android
Window.size = (280, 200)

class NetCutterWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 8

        # Header
        self.add_widget(Label(
            text='🔥 FF NET-CUTTER INJECTED', 
            font_size='14sp', 
            bold=True,
            color=(0.93, 0.27, 0.27, 1)
        ))

        # Status Label
        self.status_label = Label(
            text='STATUS: ONLINE', 
            font_size='12sp',
            bold=True,
            color=(0.13, 0.77, 0.36, 1)
        )
        self.add_widget(self.status_label)

        # ปุ่มตัดเน็ต
        btn_cut = Button(
            text='🔴 ตัดเน็ตทันที (CUT)',
            background_color=(0.93, 0.27, 0.27, 1),
            font_size='13sp',
            bold=True
        )
        btn_cut.bind(on_press=self.cut_net)
        self.add_widget(btn_cut)

        # ปุ่มต่อเน็ต
        btn_on = Button(
            text='🟢 ต่อเน็ตคืน (RESTORE)',
            background_color=(0.13, 0.77, 0.36, 1),
            font_size='13sp',
            bold=True
        )
        btn_on.bind(on_press=self.restore_net)
        self.add_widget(btn_on)

    def run_cmd(self, cmd):
        """ส่งคำสั่ง Shell เข้าไปใน Android OS ของ BlueStacks"""
        try:
            if platform == 'android':
                os.system(cmd)
            else:
                print(f"[Simulation] Executing: {cmd}")
        except Exception as e:
            print(f"Error: {e}")

    def cut_net(self, instance):
        # สั่งปิดเน็ตผ่าน Internal Android Shell
        self.run_cmd("su -c 'svc data disable' || svc data disable")
        self.run_cmd("su -c 'svc wifi disable' || svc wifi disable")
        self.status_label.text = "STATUS: 🔴 CUT (เน็ตดับ)"
        self.status_label.color = (0.93, 0.27, 0.27, 1)

    def restore_net(self, instance):
        # สั่งเปิดเน็ตคืน
        self.run_cmd("su -c 'svc data enable' || svc data enable")
        self.run_cmd("su -c 'svc wifi enable' || svc wifi enable")
        self.status_label.text = "STATUS: 🟢 ONLINE (เน็ตปกติ)"
        self.status_label.color = (0.13, 0.77, 0.36, 1)

class NetCutterApp(App):
    def build(self):
        return NetCutterWidget()

if __name__ == '__main__':
    NetCutterApp().run()
