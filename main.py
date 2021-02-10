#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright(C] 2021 cGIfl300 <cgifl300@gmail.com>

import json
from time import sleep

from call_internet_website import call_internet_website
from record_csv import record_csv


def main():
    while True:
        shell_stdout = call_internet_website()
        try:
            json_converted = json.loads(shell_stdout)
        except:
            json_converted = json.loads("{\"ping\": 999999, \"download\": 0, \"upload\": 0}")

        ping = int(json_converted['ping'])
        download = int(json_converted['download'] / 1_000_000)
        upload = int(json_converted['upload'] / 1_000_000)

        print(
            f"Votre ping est de {ping} ms, votre upload est de {upload} mbps et votre download est de {download} mbps.")

        record_csv(ping, upload, download)

        sleep(1_800)


if __name__ == '__main__':
    main()
