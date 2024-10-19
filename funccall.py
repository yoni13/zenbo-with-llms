import time
from control_zenbo import domain, sdk, host
def get_time():
    return time.strftime("%I:%M %p")

def get_date():
    return time.strftime("%Y-%m-%d")

def get_location():
    return "Hsinchu,Taiwan"

def add(num1:int, num2:int):
    return num1 + num2

def multiply(num1:int, num2:int):
    return num1 * num2

def change_expression(expression:str):
   """
   Changes the expression of Zenbo
   :params expression: expression of Zenbo,allowed expressions include 
HIDEFACE
INTERESTED
DOUBTING
PROUD
DEFAULT
HAPPY
EXPECTING
SHOCKED
QUESTIONING
IMPATIENT
CONFIDENT
ACTIVE
PLEASED
HELPLESS
SERIOUS
WORRIED
PRETENDING
LAZY
AWARE_RIGHT
TIRED
SHY
INNOCENT
SINGING
AWARE_LEFT
DEFAULT_STILL
PREVIOUS
EXPECTING_ADV
IMPATIENT_ADV
PLEASED_ADV
SHOCKED_ADV
TIRED_ADV
DEFAULT_ADV
WORRIED_ADV
QUESTIONING_ADV
PRETENDING_ADV
INTERESTED_ADV
SHY_ADV
CONFIDENT_ADV
HAPPY_ADV
LAZY_ADV
ACTIVE_ADV
SINGING_ADV
DOUBTING_ADV
AWARE_RIGHT_ADV
AWARE_LEFT_ADV
HELPLESS_ADV
SERIOUS_ADV
INNOCENT_ADV
PROUD_ADV
   """
   ZenboAllowedExpressions = [
    "HIDEFACE", "INTERESTED", "DOUBTING", "PROUD", "DEFAULT", "HAPPY", "EXPECTING", 
    "SHOCKED", "QUESTIONING", "IMPATIENT", "CONFIDENT", "ACTIVE", "PLEASED", 
    "HELPLESS", "SERIOUS", "WORRIED", "PRETENDING", "LAZY", "AWARE_RIGHT", "TIRED", 
    "SHY", "INNOCENT", "SINGING", "AWARE_LEFT", "DEFAULT_STILL", "PREVIOUS", 
    "EXPECTING_ADV", "IMPATIENT_ADV", "PLEASED_ADV", "SHOCKED_ADV", "TIRED_ADV", 
    "DEFAULT_ADV", "WORRIED_ADV", "QUESTIONING_ADV", "PRETENDING_ADV", 
    "INTERESTED_ADV", "SHY_ADV", "CONFIDENT_ADV", "HAPPY_ADV", "LAZY_ADV", 
    "ACTIVE_ADV", "SINGING_ADV", "DOUBTING_ADV", "AWARE_RIGHT_ADV", 
    "AWARE_LEFT_ADV", "HELPLESS_ADV", "SERIOUS_ADV", "INNOCENT_ADV", "PROUD_ADV"
   ]

   if expression not in ZenboAllowedExpressions:
      raise ValueError(f"The following expression {expression} is not allowed!"

   sdk.robot.set_expression(expression)
