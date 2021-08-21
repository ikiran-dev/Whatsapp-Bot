
import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)


position1 = pt.locateOnScreen('whatsapp/smile.PNG', confidence=.6)
x = position1[0]
y = position1[1]

# Gets message
def get_message():
     global x, y
    
     position = pt.locateOnScreen('whatsapp/smile.PNG', confidence=.6)
     x = position[0]
     y = position[1]
     pt.moveTo(x,y, duration=.05)
     pt.moveTo(x + 110, y - 70, duration=.5)
     pt.tripleClick()
     pt.rightClick()
     pt.moveRel(12,15)
     pt.click()
     whatsapp_message = pyperclip.paste()
     pt.click()
     print("Message Recieved: " + whatsapp_message)
     return whatsapp_message
     
# Posts
def post_response(message):
    global x, y
    position = pt.locateOnScreen('whatsapp/smile.PNG', confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo( x + 200 , y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01 )
    #pt.typewrite("\n" , interval=.01)


#Processes response
def process_response(message):
    random_no = random.randrange(3)

    if "?" in str(message).lower():
        return "Don't ask me any questions!!"
    elif "hey" in str(message).lower():
        return "Hey! what's up?"
    elif "tell me abt ur self" in str(message).lower():
        return " I'm KIRAN KUMAR from CSE 5th Sem"
    elif "tell me abt ur clg" in str(message).lower():
        return "Well! I study in GSKSJTI it's located in KR Circle, It's built by Sir M VISVESHWARAYA"
    elif "good morning" in str(message).lower():
        return " GOOD MORNING , I hope you have a ridiculously amazing day!"
    elif "gm" in str(message).lower():
        return " GOOD MORNING , I hope you have a ridiculously amazing day!"
    elif "gn" in str(message).lower():
        return " Nighty night let bugs bite!"
    elif "gn" in str(message).lower():
        return " GOOD NIGHT  SWEET DREAMS"
        
        
        
        
    
    else:
        if random_no == 0:
            return "That's cool"
        elif random_no == 1:
            return "PANDA is the best"
        else:
            return " I'm bored can u tell me something thats intersting"



#CHECK FOR NEW MESSAGES
def check_for_new_messages():
    pt.moveTo(x + 110, y -45, duration=.5)


    while True:
        #Continuosly checks for new messages
        try:
            position = pt.locateOnScreen('whatsapp/nm.PNG',confidence=.7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                sleep(.5)
        except(Exception):
            print(" No new other users with new messages located")
        
        if pt.pixelMatchesColor(int(x + 110), int(y -45),(255,255,255), tolerance=22):
            print ("is_white")
            processed_message = process_response(get_message())
            post_response(processed_message)
        else:
            print("No new messages yet....")
            sleep(5)
        





check_for_new_messages()












