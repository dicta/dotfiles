#!/usr/bin/python

import sys
import gtk
import gnomekeyring as gkey

items = gkey.find_items_sync(gkey.ITEM_NETWORK_PASSWORD, 
                             {"server": "gmail", "protocol": "imap" })
if items:
    print items[0].secret
