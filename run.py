import time
import numpy as np
from crawler import check_pub_list
from send_email import send_email


pub_list=check_pub_list()
while(1):
    
    new_pub_list=check_pub_list()
    
    if set(new_pub_list).difference(set(pub_list))==set():
        pass
    else:
        send_email()
    
    sleep_time=int(np.random.rand()*1000+3600*4)

    time.sleep(sleep_time)
    
