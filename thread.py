# 4CHAN IMAGE DOWNLOADER
# @author   tonerqq
# @date     23 Jan 2021

import re
import subprocess as sp
import urllib

# get thread link from user and download source code
thread_link = raw_input(" ENTER 4CHAN THREAD LINK : ")

# download thread source code
page_code = sp.check_output("curl " + str(thread_link), shell=True)

# find all numbers in source code
raw_nums = re.findall('[0-9]+', str(page_code))
raw_nums = set(raw_nums)
# find all desirable JPG numbers and download them
for i in raw_nums:
    if (len(str(i)) == 13 and str(i)[1] == "6"):
        url = "https://i.4cdn.org/wg/" + str(i) + ".jpg"
        print(" DOWNLOADING " + url + " ...")
        urllib.urlretrieve(url, (str(i) + ".jpg"))
