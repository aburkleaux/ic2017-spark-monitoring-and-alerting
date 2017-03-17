#!/usr/bin/env python

import requests
import requests
import json

GRAFANA_SERVER = '169.46.172.3'
GRAFANA_PORT = '3000'

if __name__ == '__main__':

    datasource_json = {'name':'ic2017-1','type':'graphite','url':'http://graphite','access':'proxy','basicAuth':False, 'isDefault':True}
    request = 'http://'+GRAFANA_SERVER+':'+GRAFANA_PORT+'/api/datasources'

    print ('Creating graphite datasource in grafana '+request+str(datasource_json) )
    try:
        r = requests.post('http://'+GRAFANA_SERVER+':'+GRAFANA_PORT+'/api/datasources', data=datasource_json) 
        print ('Create graphite datasource SUCCESS')
    except Exception as err:
        print ('Error creating grafana datasource!!!'+err)


    request = 'http://'+GRAFANA_SERVER+':'+GRAFANA_PORT+'/api/dashboards/db'
    FILE = './ic2017-sample-dashboard.json'

    print ('Creating dashboard in grafana '+FILE)
    try:
        json_data = open(FILE)
        d = json.load(json_data)
        r = requests.post(request, json=d) 
        print ('Create dashboard in grafana response: '+str(r))
    except Exception as err:
        print ('Error dashboard in grafana!!!'+err)


