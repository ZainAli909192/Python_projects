from plyer import notification
import time

num=1;
if __name__ == '__main__':
   while num==1:
       notification.notify(
           title="** Take Rest now **",
           message="Drink water",
           timeout=5)
       time.sleep(40)
       num=0
