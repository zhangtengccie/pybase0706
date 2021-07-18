#第一题
# import os
# import re
# import time
#
#
# while True:
#     try:
#         netstat_result = os.popen(' netstat -tulnp').read()
#         finded_tcp80 = False
#         for netstat in netstat_result.split('\n')[2:-1]:
#             re_result = re.match(r'tcp\s+\d+\s+\d+\s+\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:80\s+'
#                                  r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\*\s+LISTEN\s+\d+/.*'
#                                  ,netstat)
#             if re_result:
#                 print('HTTP (TCP/80)服务已经被打开')
#                 finded_tcp80 = True
#                 break
#         if finded_tcp80:
#             break
#         print('等待1秒后重新开始监控！')
#         time.sleep(1)
#     except KeyboardInterrupt:
#         print('接收到管理员ctrl+c~')
#         print('程序退出')
#         break
#第二题
# 非函数实现
# List1 = ['aaa',111,(4,5),2.01]
# List2 = ['bbb',333,3.14,(4,5)]
#
# for x in List1:
#     if x in List2:
#         print(f'{x} in List1 and List2')
#     else:
#         print(f'{x} only in  List1')

# for x in List1:
#     print(f'{x} in List1 and List2') if x in List2 else print(f'{x} only in  List1')

# 函数实现
# def find_same(l1,l2):
#     for x in l1:
#         print(f'{x} in List1 and List2') if x in l2 else print(f'{x} only in  List1')
# find_same(List1,List2)

#第三题
import logging
from kamene.all import *
from kamene.layers.inet import ICMP,IP

logging.getLogger('kamene.runtime').setLevel(logging.ERROR)


def ping_ret(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return ip,True
    else:
        return ip,False

ping_pong = ping_ret('1.1.1.25')
if ping_pong[1]:
    print(f'{ping_pong[0]} 通')
else:
    print(f'{ping_pong[0]} 不通')