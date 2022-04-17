#!/usr/bin/env python

from iot_automator import node

node_url            = 'https://testnode.webthings.io/'
node_credentials    = {'unm': 'mterrell', 'pwd': 'hello12'}

with node.connect(node_url, node_credentials) as my_node:
    current_temp            = my_node.devices['Weather'].sense('temperature')
    current_brightness      = my_node.devices['Light Sense'].sense('brightness')
    
    if(current_temp > 75 and current_brightness > 1500):
        my_node.devices['Hue Light Strip'].actuate('power', 'off')

