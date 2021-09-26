#### This project is an example of a telegram bot using python 😁
------------
##### 👨🏻‍💻 About the project
###### This telegram bot project doesn't work alone, normally you use this function in another project, for example for notifications when a site goes down, or something like that.

------------
###### How to create a bot on Telegram?
- Search for the user "BotFather" and click on his start button
- Type /newbot
- Enter your Bot's @
- It will return the "TELEGRAM_TOKEN" in the message "Use this token to access the HTTP API:"
------------
###### How to get my chat_id?
- To find your ID look for the bot: bot (called IDBot), click start and type: /getid
-To find a group chat id add this bot to the group and type:/getgroupid@myidbot

------------
##### Installation

- Python installation is required (Yes, really, you're not looking for a Python API without having python installed, are you?)
- Python min version: 3.8.0
- Enter the project folder in a terminal and run the command 
```
pip3 install -r requirements.txt
```
- Change the environment variables collected earlier in the .env file
- Run the following command to start the application
```
python3 app.py "Here you can type the message"
```
------------
