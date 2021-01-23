# 4CHAN IMAGE DOWNLOADER
# @author   tonerqq
# @date     23 Jan 2021

import re
import os 

# 1609214554461.jpg -- 13 numbers

# get thread link from user and download source code
thread_link = raw_input(" ENTER 4CHAN THREAD LINK : ")
page_code = os.system("curl " + str(thread_link))

# find all numbers in source code
raw_nums = re.findall('[0-9]+', str(page_code))
num_list = []
# find all desirable JPG numbers
for i in raw_nums:
    if (len(str(i)) == 13):
        num_list.append(i)
        print i


