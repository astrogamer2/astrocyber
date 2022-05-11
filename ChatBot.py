import json
import random
import re
import urllib.request
import requests
import sys
from datetime import datetime

#time
now = datetime.now()

current_time = now.strftime("%H:%M:%S")
current_time2,current_time1,current_time3 = current_time.split(":")
def f(x):
    if (x > 4) and (x <= 8):
        return 'Early in the Morning'
    elif (x > 8) and (x <= 12 ):
        return 'in the Morning'
    elif (x > 12) and (x <= 16):
        return'in the Noon'
    elif (x > 16) and (x <= 20) :
        return 'in the Evening'
    elif (x > 20) and (x <= 24):
        return'in the Night'
    elif (x <= 4):
        return'in Late Night'

def f2(x):
  if (x > 12) and (x <= 20) :
        return 'Evening'
  elif (x > 4) and (x <= 12 ):
        return 'Morning'


int_time = int(current_time2)
ampm = f(int_time)
if int_time > 12:
  int_time = int(current_time2)
  current_time2 = int_time - 12

mn = f2(int_time)

if "0" in current_time1:
  if current_time1[0] == "0":
    cr,current_time1 = current_time1.replace("0", ":")

elif not "0" in current_time1:
  if not current_time1[0] == "0":
    current_time10 = current_time1
    current_time1 = f":{current_time10}"

print(f"good {mn} sir its {current_time2}{current_time1} {ampm}")

data = []

id_save = []


def listToString(s): 
    
    str1 = " "
  
    return (str1.join(s))

def replace(string1, object, obj2):
    return string1.replace(obj2, object)

cb = " <ChatBot> "

id = input(f"{cb}Input User Name : ")

cpu = " <CPU> "


for loop in range(100):
  reconizer.adjust_for_ambient_noise(sr.Microphone(), duration = 0.1)
  audio = reconizer.listen(sr.Microphone())
  user_input = reconizer.recognize_google(sr.Microphone())
  user_input = user_input.lower()


  if "rename" in user_input:
    if user_input[0:7] == "rename":
      inp_id = replace(user_input, "", "rename ")
      speeker.say(f"renamed {id} to {inp_id}")
      id = f'{inp_id}'

  id_save.append(id)
  
  if user_input == "discord":
    server_invite = replace(user_input, "", "discord ")
    r = f"\n{cb}{server_invite} : https://discord.com/invite/" + server_invite
    print(r)

  if "dc" in user_input:
    if user_input[0] == "dc":
      server_invite = replace(user_input, "", "dc ")
      r = f"\n{cb}{server_invite} : https://discord.com/invite/" + server_invite
      print(r)

  
  if user_input == "ids":
    print(f"{cpu}IDs Made Till Now Are : ")
    for ids in id_save:
      print(f"   {ids}")

  if user_input == "$TextBook":
    text = input(f"{cb}STD : ")
    print(f"{cb}https://byjus.com/ncert-books/#ncert-books-class-{text}")
  
  if user_input == "$YT":
    YT_inp = input(f"\n{cb}YouTube Video : ")

    YT_int = YT_inp.isspace()
    if YT_int == False or True:
      YT_inp = replace(YT_inp, "-", " ")

    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + YT_inp)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    print(f"\n{cb}https://www.youtube.com/watch?v=" + video_ids[0])

  
  if user_input == "$help":
    print(f"\n{cb}How May I Help You!!")

  if user_input == "$add":
    command_prompt = input(f"\n{cpu}Add Commands : ")
    data.append(command_prompt)

  if user_input == "$remove":
    command_prompt2 = input(f"\n{cpu}Remove Commands : ")
    for messages in data:
      data_raw3 = messages
      Input2,Output2 = data_raw3.split(":")
      if command_prompt2 == Input2:
        pos = data.index(f"{Input2}:{Output2}")
        data.pop(pos)
      elif command_prompt2 == Output2:
        pos = data.index(f"{Input2}:{Output2}")
        data.pop(pos)
      elif command_prompt2 == (f"{Input2}:{Output2}"):
        pos = data.index(f"{Input2}:{Output2}")
        data.pop(pos)

  if user_input == "$Google":
    Search = input(f"\n{cb}Find : ")
    Search_refined = replace(Search,"+"," ")
    print(f"\n{cb}https://www.google.com/search?q={Search_refined}")

  if user_input == "$FireFox":
    Search = input(f"\n{cb}Find : ")
    Search_refined = replace(Search,"+"," ")
    print(f"\n{cb}https://www.google.com/search?client=firefox-b-d&q={Search_refined}")

  if user_input == "$MicrosoftEdge":
    Search = input(f"\n{cb}Find : ")
    Search_refined = replace(Search,"+"," ")
    print(f"\n{cb}https://www.bing.com/search?q={Search_refined}")

  if user_input == "$Edge":
    Search = input(f"\n{cb}Find : ")
    Search_refined = replace(Search,"+"," ")

  if user_input == "$E-Mail":
    op = ["Gmail" , "Outlook" , "ProtonMail" , "iCloud Mail" , "Yahoo"]
    print(f"\n{cb}Y/N")
    for ops in op:
      ask = input(f"\n{cb} {ops}? : ")
      if ask == "Y":
        G = f"\n{cb}https://mail.google.com/mail/u/0/?tab=#inbox"
        out = f"\n{cb}https://outlook.live.com/mail/0/inbox?tab="
        pro = f"\n{cb}https://mail.protonmail.com/u/0/inbox"
        I = f"\n{cb}https://www.icloud.com/mail/u/0/inbox"
        yah = f"\n{cb}https://mail.yahoo.com/mail/u/0/inbox"
        if ops == "Gmail":
          print(G)
        elif ops == "Outlook":
          print(out)
        elif ops == "ProtonMail":
          print(pro)
        elif ops == "iCloud Mail":
          print(I)
        elif ops == "Yahoo":
          print(yah)
        elif ops == None:
          print(f"\n\n{cb}ERROR 404 : No Mail Found\n")
        break
  
  if user_input == "$Spotify":
    Search = input(f"\n{cb}Music : ")
    Search_refined = replace(Search,"%20"," ")
    print(f"\n{cb}https://open.spotify.com/search/{Search_refined}")

  
  if user_input == "$Custom":
    for raw in data:
      data_raw = raw
      data_output = replace(data_raw,"  Output : ",":")
      print(f"{cb}CUSTOM COMMANDS : ")
      print(f"\n        [Input : {data_output}]")

  for message in data:
    data_raw2 = message
    Input,Output = data_raw2.split(":")
    if user_input == Input:
      print(f"\n{cb}{Output}")
      

