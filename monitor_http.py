import os
import re
import time
while True:
    ret = os.popen('netstat -tulnp').read()
    ret = ret.split('\n')
    for i in ret[2:-1]:
        if i.split()[3].split(':')[-1]=='80':
            print('HTTP (TCP/80)服务已经被打开')
            break
    else:
        print('等待一秒重新开始监控')
        time.sleep(1)
        continue
    break