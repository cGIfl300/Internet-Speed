# Copyright(C] 2021 cGIfl300 <cgifl300@gmail.com>

from datetime import datetime


def record_csv(ping, upload, download):
    with open("data\history.csv", "a") as my_file:
        my_file.write(f"{datetime.now()},{ping},{upload},{download}\n")
    my_file.close()
