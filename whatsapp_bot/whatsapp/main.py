import subprocess
file = subprocess.Popen("C:\\Users\\ikira\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
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
    pt.typewrite("\n" , interval=.01)


#Processes response
def process_response(message):
    random_no = random.randrange(10)

    if "?" in str(message).lower():
        return "Don't ask me any questions!!"
    elif "hey" in str(message).lower():
        return "Hey! what's up?"
    elif "bye" in str(message).lower():
        return "Bubyee! Have A Great Day!!"
    elif "hi" in str(message).lower():
        return "Hey! what's up?"
    elif "tell me about your self" in str(message).lower():
        return " I'm KIRAN KUMAR from CSE 5th Sem"
    elif "tell me about yourself" in str(message).lower():
        return " I'm KIRAN KUMAR from CSE 5th Sem"
    elif "tell me about your clg" in str(message).lower():
        return "Well! I study in GSKSJTI it's located in KR Circle, It's built by Sir M VISVESHWARAYA"
    elif "good morning" in str(message).lower():
        return " GOOD MORNING , I hope you have a ridiculously amazing day!"
    elif "good afternoon" in str(message).lower():
        return " GOOD NOON , I hope you have a ridiculously amazing day!"
    elif "ga" in str(message).lower():
        return " GOOD NOON , I hope you have a ridiculously amazing day!"
    elif "gm" in str(message).lower():
        return " GOOD MORNING , I hope you have a ridiculously amazing day!"
    elif "gn" in str(message).lower():
        return " Nighty night let bugs bite!"
    elif "gn" in str(message).lower():
        return " GOOD NIGHT  SWEET DREAMS"
    elif "okay" in str(message).lower():
        return "yea cool"
    elif "ok" in str(message).lower():
        return "yea cool"
    elif "uta aitha?" in str(message).lower():
        return "hu nimdu?"
    elif "uta aytha?" in str(message).lower():
        return "hu nimdu?"
    elif "aithu" in str(message).lower():
        return "yen thinde?"
    elif "aythu" in str(message).lower():
        return "yen thinde?"
    elif "aytu" in str(message).lower():
        return "yen thinde?"
    elif "nin yen thinde?" in str(message).lower():
        return "ntg special!!"
    elif "thank you" in str(message).lower():
        return "My pleasure"
    elif "what are you doing?" in str(message).lower():
        return "Nothing much , what about you?"
    elif "wyd" in str(message).lower():
        return "Nothing much , what about you?"
    elif "what you doing?" in str(message).lower():
        return "Nothing much , what about you?"
    elif "thanks" in str(message).lower():
        return "My pleasure"
    elif "what are you doing" in str(message).lower():
        return "Nothing much , what about you?"
    elif "wyd?" in str(message).lower():
        return "Nothing much , what about you?"
    elif "what you doing" in str(message).lower():
        return "Nothing much , what about you?"
    elif "nothing" in str(message).lower():
        return "I'm kinda bored"
    elif "good" in str(message).lower():
        return "Great!! then?"
    elif "helu" in str(message).lower():
        return "Yenilla nine helbeku"
    else:
        if random_no == 0:
            return "That's cool"
        elif random_no == 1:
            return " mmmm then?"
        elif random_no == 2:
            return "sure"
        elif random_no == 3:
            return "Great!"
        elif random_no == 4:
            return "Looks interesting!"
        elif random_no == 5:
            return "Yea ok"
        else:
            return "hu"



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
        except(Exception):
            print(" No new other users with new messages located")
        
        if pt.pixelMatchesColor(int(x + 112), int(y -47),(255,255,255), tolerance=10):
            processed_message = process_response(get_message())
            post_response(processed_message)
            
        else:
            print("No new messages yet....")

        sleep(3)
            

check_for_new_messages()












