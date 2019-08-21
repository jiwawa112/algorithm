#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import networkx as nx
import random
from matplotlib import pyplot as plt
from string import ascii_uppercase

print(ascii_uppercase)

def generate_random_website():
    return 'www.' + ''.join([random.choice(ascii_uppercase) for _ in range(random.randint(3,10))]) + '.' + random.choice(['com','edu','cn'])

print(generate_random_website())

websites = [generate_random_website() for _ in range(25)]
print(websites)

website_connection = {
    websites[0]:random.sample(websites,10),
    websites[1]:random.sample(websites,5),
    websites[2]:random.sample(websites,5),
    websites[3]:random.sample(websites,7),
    websites[4]:random.sample(websites,2),
    websites[5]:random.sample(websites,1),
}

website_nework = nx.Graph(website_connection)
nx.draw_networkx(website_nework)
plt.show()

print(sorted(nx.pagerank(website_nework).items(),key=lambda x:x[1],reverse=True))

# [('www.EOFTHFYY.edu', 0.19572886276714951), ('www.UIT.cn', 0.1229433334157736), ('www.WWLLS.com', 0.0965417125694492), ('www.LLXGSOI.com', 0.09447518622457413), ('www.WLHJSS.cn', 0.05136697673783967), ('www.ERFYRZHHIG.cn', 0.04781068868300051), ('www.JZZGJVBHG.com', 0.04267597869998222), ('www.WUEXBEM.com', 0.03591750668706452), ('www.MAFDY.cn', 0.035116288038894515), ('www.JEWWUHOLRI.edu', 0.03456108218094015), ('www.ZRFXBWUVU.com', 0.03442658710900506), ('www.LDT.edu', 0.03423966483736224), ('www.ZJFDRAWS.cn', 0.02563695281866467), ('www.GBYHMWZCS.cn', 0.021363902878587533), ('www.NEW.cn', 0.021363902878587533), ('www.IRMHW.cn', 0.021363902878587533), ('www.HYAKILQO.edu', 0.021363902878587533), ('www.MLEDKOOU.cn', 0.021363902878587533), ('www.TRXGMPQX.cn', 0.021176980606944708), ('www.OHGZ.com', 0.02056268423041753)]