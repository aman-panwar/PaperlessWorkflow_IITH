from Model.email_manager import EmailManager
from Model.user import User
from Model.form import Form
import time

# ids = ["cs20btech11004@iith.ac.in", "cs20btech11060@iith.ac.in", "es20btech11035@iith.ac.in", "es20btech11026@iith.ac.in"]
# for id in ids:
#     u =User(id)
#     u.set_notification_frequency("DAILY")
#     u.save_to_db()
#     print("saved to db ",id) 

print('caller started')
u =  User('cs20btech11004@iith.ac.in')
print('user created')
u.send_notification("Another test email")

while True:
    print("in caller")
    time.sleep(5)