#server code this is what would be on the robot
#can be used to read in values that client sends to it
import time
from networktables import NetworkTable

import logging
logging.basicConfig(level=logging.DEBUG)

sd = NetworkTable.getTable("SmartDashboard")
hoodPos= 0
armPos=0
cogX = 0
cogY = 0

#attempt to grab value from server
while True:
    try:
        print('DEF: ' + sd.getString('DEF') + ' POS: ' 
        + sd.getString('POS') + ' HoodPos: ' + str(hoodPos) + ' ArmPos: ' + str(armPos)
        + ' COGX: ' + str(cogX) + ' COGY: ' + str(cogY))
    except KeyError:
        print('DEF: N/A '+ ' POS: N/A' 
        + ' HoodPos: '  + str(hoodPos)+ ' ArmPos: '  + str(armPos)
        + ' COGX: ' + str(cogX) + ' COGY: ' + str(cogY))
    hoodPos = hoodPos+1
    armPos = armPos+1
    cogX=cogX+1
    cogY=cogY+1
    sd.putNumber('HOODPOS',hoodPos)
    sd.putNumber('ARMPOS',armPos)
    sd.putNumber('COG_X',cogX)
    sd.putNumber('COG_Y',cogY)
    time.sleep(.001)