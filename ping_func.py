import logging
from kamene.all import *
logging.getLogger('kamene.runtime').setLevel(logging.ERROR)
from kamene.all import *
def ping_ret(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        print(ip+' '+'ι!')
    else:
        print(ip+' '+'δΈι!')

ping_ret('1.1.1.2')