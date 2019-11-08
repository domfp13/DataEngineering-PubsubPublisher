#!/usr/bin/env python3
# Created by Enrique Plata

import main

def test():
    """
    simulates how the cloud function is triggered.
    :return:
    {
        'name': 'global/UPS_ALLOCATION/CMCC_Weekly_Carrier_Report_20190830.xlsx',
        'bucket' : 'app-script-data-extraction'
    }
    """
    main.publish_message({'name': 'appusma206_apps/BMO_Disposition/BMO_Disposition_2019_10.csv',
             'bucket' : 'appusma206_apps'}, 'context')

test()