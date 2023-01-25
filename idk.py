from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.app import MDApp 
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from kivymd.uix.bottomnavigation import *
import subprocess, code
KVMD="""
Screen:
    MDBottomNavigation:
    	#panel_color: "#ff0000"
    	selected_color_background: "#ff8000"
    	
    	MDBottomNavigationItem:
    		name: "screen 1"
    		text: "Home"
    		icon: "home"
			MDIcon:
				icon: "Python.png"
				size: 400, 400
				pos: 300, 600
			MDLabel:
				text: 'Python3'
	  		  pos : 60,640
	  		  font_style: "H6"
	        MDLabel:
	            text: "Python version 3.9.4"
	            pos: 100, 400
    	
    	MDBottomNavigationItem:
    		name: "screen 2"
    		text: "Interpreter"
    		icon: "Interpreter.jpg"
    		MDLabel:
    			text: "Interpreter"
    			pos: 30, 500
    			MDTextField:
    				id: interpret
    				hint_text: ">>> "
    				mode: "rectangle"
    				pos: 30, 550
    				size: 400, 650
    			
    	MDBottomNavigationItem:
    		name: "screen 3"
    		text: "Compiler"
    		icon: "Compiler.jpg"
    		MDLabel:
    			text: "Compiler"
    			pos: 30, 500
    			MDTextField:
    				id: compile
    				hint_text: "# Enter code here"
    				pos: 30, 550
    				size: 400, 650
    			
    	MDBottomNavigationItem:
    		name: "screen 4"
    		text: "Terminal"
    		icon: "Terminal.jpg"
    		MDLabel:
    			text: "Terminal"
    			pos: 30, 500
    			MDTextField:
    				id: terminal
    				pos: 30, 550
    				size: 400, 650
    
"""
class MyScreen(Screen):
    def on_text(self, value, text_field_id):
        if text_field_id == "compile":
            # Save the entered code in a file
            with open('user_code.py', 'a') as f:
                f.write(value)
            # Execute the code using subprocess
            result = subprocess.run(["python", "user_code.py"], capture_output=True)
            # Get the output of the code
            output = result.stdout.decode()
            # Set the text of the text field to the output
            self.ids.compile.text = output
        elif text_field_id == "interpret":
            try:
                # Use the code module to execute the entered code
                output = code.interact(local={'result': value}, banner='Interpreter')
                # Set the text of the text field to the output
                self.ids.interpret.text = output
            except Exception:
                self.ids.interpret.text = str(Exception)
    def execute_command(self):
        command = self.ids.terminal.text
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]
        print(output)

prim_palette= ['Red', 'Blue', 'Orange', 'Purple']
class Python(MDApp):
    def build(self):
        self.theme_cls.primary_palette= "Red"    # Blue or Red or Orange or Purple 
        self.theme_cls.theme_style="Light"           # Light or Dark
        return Builder.load_string(KVMD)
Python().run()
