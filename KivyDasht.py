import sys
import time
from networktables import NetworkTable
import logging
logging.basicConfig(level=logging.DEBUG)

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.video import Video

class main(GridLayout):
    cols=6
    def __init__(self,**kwargs):
        super(main,self).__init__(**kwargs)
        
        #Defense ToggleButtons
        self.add_widget(Label(text='Defense',size_hint_x=None,size_hint_y=None, width=200,height=50))
		
        self.Nothing = ToggleButton(text='Nothing',group='def',size_hint_x=None,size_hint_y=None, width=100,height=50)
        self.Nothing.bind(on_press=self.sendNothing)
        self.add_widget(self.Nothing)
		
        self.Rockwall = ToggleButton(text='Rockwall',group='def',size_hint_x=None,size_hint_y=None, width=100,height=50)
        self.Rockwall.bind(on_press=self.sendRockwall)
        self.add_widget(self.Rockwall)
        
        self.RoughTerrain = ToggleButton(text='RoughTerrain',group='def',size_hint_x=None,size_hint_y=None, width=100,height=50)
        self.RoughTerrain.bind(on_press=self.sendRoughTerrain)
        self.add_widget(self.RoughTerrain)

        self.Moat = ToggleButton(text='Moat',group='def',size_hint_x=None,size_hint_y=None, width=100,height=50)
        self.Moat.bind(on_press=self.sendMoat)
        self.add_widget(self.Moat)

        self.Ramparts = ToggleButton(text='Ramparts',group='def',size_hint_x=None,size_hint_y=None, width=100,height=50)
        self.Ramparts.bind(on_press=self.sendRamparts)
        self.add_widget(self.Ramparts)

        #Position ToggleButtons
        self.add_widget(Label(text='Position',size_hint_x=None,size_hint_y=None, width=200,height=50))
		
        self.One = ToggleButton(text='1',group='pos',size_hint_x=None,size_hint_y=None, width=100,height=50)
        self.One.bind(on_press=self.sendOne)
        self.add_widget(self.One)
		
        self.Two = ToggleButton(text='2',group='pos',size_hint_x=None,size_hint_y=None, width=100,height=50)
        self.Two.bind(on_press=self.sendTwo)
        self.add_widget(self.Two)
        
        self.Three = ToggleButton(text='3',group='pos',size_hint_x=None,size_hint_y=None, width=100,height=50)
        self.Three.bind(on_press=self.sendThree)
        self.add_widget(self.Three)

        self.Four = ToggleButton(text='4',group='pos',size_hint_x=None,size_hint_y=None, width=100,height=50)
        self.Four.bind(on_press=self.sendFour)
        self.add_widget(self.Four)

        self.Five = ToggleButton(text='5',group='pos',size_hint_x=None,size_hint_y=None, width=100,height=50)
        self.Five.bind(on_press=self.sendFive)
        self.add_widget(self.Five)

        #Sensor Label Displays
        self.add_widget(Label(text='Sensors',size_hint_x=None,size_hint_y=None, width=200,height=50))
         
        self.Hoodlabel = Label(text = 'Hood: N/A',size_hint_x=None,size_hint_y=None, width=100,height=50)
        self.add_widget(self.Hoodlabel)

        self.Armlabel = Label(text = 'Arm: N/A',size_hint_x=None,size_hint_y=None, width=100,height=50)
        self.add_widget(self.Armlabel)

        self.Cogxlabel = Label(text = 'CogX: N/A',size_hint_x=None,size_hint_y=None, width=100,height=50)
        self.add_widget(self.Cogxlabel)

        self.Cogylabel = Label(text = 'CogY: N/A',size_hint_x=None,size_hint_y=None, width=100,height=50)
        self.add_widget(self.Cogylabel)

        self.video = Video(source='http://127.0.0.1:5000/')
        self.add_widget(self.video)

        #Update/Start Button
        self.Update = Button(text='update',size_hint_x=None,size_hint_y=None, width=100,height=50)
        self.Update.bind(on_press=self.startupdate)
        self.add_widget(self.Update)
        
    #Send Defense Selected
    def sendNothing(self,value):
        sd.putString('DEF','2')
		
    def sendRockwall(self,value):
        sd.putString('DEF','3')

    def sendRoughTerrain(self,value):
        sd.putString('DEF','4')

    def sendMoat(self,value):
        sd.putString('DEF','1')

    def sendRamparts(self,value):
        sd.putString('DEF','5')

    #Send Position Selected    
    def sendOne(self,value):
        sd.putString('POS','1')
		
    def sendTwo(self,value):
        sd.putString('POS','2')

    def sendThree(self,value):
        sd.putString('POS','3')

    def sendFour(self,value):
        sd.putString('POS','4')

    def sendFive(self,value):
        sd.putString('POS','5')

    #Start the update 
    def update(self,dt):
        self.Hoodlabel.text = 'Hood: ' + str(sd.getNumber('HOODPOS',217))
        self.Armlabel.text = 'Arm: ' + str(sd.getNumber('ARMPOS',217))
        self.Cogxlabel.text = 'CogX: ' + str(sd.getNumber('COG_X',217))
        self.Cogylabel.text = 'CogY: ' + str(sd.getNumber('COG_Y',217))
        print('updating')
        
    def startupdate(self,value):
        Clock.schedule_interval(self.update, 0.001)
        
class TCDash(App):
    NetworkTable.setIPAddress("127.0.0.1")#for robot will be 10.2.17.2 aka ip of rio
    NetworkTable.setClientMode()
    NetworkTable.initialize()

    sd = NetworkTable.getTable("SmartDashboard")
    
    def build(self):
       return main()

if __name__ == '__main__':
    sd = NetworkTable.getTable("SmartDashboard")
    TCDash().run()
