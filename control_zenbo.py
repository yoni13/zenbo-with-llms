import pyzenbo
from pyzenbo.modules.dialog_system import RobotFace

# Init zenbo
host = '192.168.0.186'
domain = '' # this value is required from asus servers
sdk = pyzenbo.connect(host)
'''
sdk.robot.set_expression(RobotFace.DEFAULT,timeout=5)
sdk.robot.speak('Hello!I am Zenbo.')
sdk.robot.set_expression(RobotFace.HIDEFACE)
'''
