#!/usr/bin/env python

import requests
import json

GRAFANA_SERVER = 'localhost'
GRAFANA_PORT = '3000'

if __name__ == '__main__':

    create_dashboard = False

    datasource_json = {'name':'ic2017','type':'graphite','url':'http://localhost:80','access':'direct','basicAuth':False, 'isDefault':True}
    request = 'http://'+GRAFANA_SERVER+':'+GRAFANA_PORT+'/api/datasources'

    print ('Creating graphite datasource in grafana '+request+str(datasource_json) )
    try:
        r = requests.post('http://'+GRAFANA_SERVER+':'+GRAFANA_PORT+'/api/datasources', data=datasource_json) 
        print ('Create graphite datasource SUCCESS')
    except Exception as err:
        print ('Error creating grafana datasource!!!'+err)


    request = 'http://'+GRAFANA_SERVER+':'+GRAFANA_PORT+'/api/dashboards/db'
    FILE = './ic2017-sample-dashboard.json'
 

    if create_dashboard:
        print ('Creating dashboard in grafana '+FILE)
        try:
            json_data = open(FILE)
            d = json.load(json_data)
            # this works on galileo but not on VM env
            r = requests.post(request, json=d) 
            # this get http response 422
            #r = requests.post(request, data=d")
            # this gets http response 409
            #r = requests.post(request, data=d, headers="Content-Type: application/json")

            print ('Create dashboard in grafana response: '+str(r))
        except Exception as err:
            print ('Error dashboard in grafana!!!'+err)

