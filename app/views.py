from IoTThings.settings import TIME_ZONE
from django.shortcuts import render
import requests
import json
#from django.http import HttpResponse

# Create your views here.
def templates(request):

    json_data =  requests.get('https://thingspeak.com/channels/1293177/feed.json').text
    json_loaded = json.loads (json_data)
    context = {}

    info = json_loaded['feeds'][-8:]
    leitura   = []
    vento     = []
    uv        = []
    nivel_mar = [] 

    for j in range(len(info)):
        leitura.append(info[j]['created_at'])
        vento.append(info[j]['field7'])
        uv.append(info[j]['field8'])
        nivel_mar.append(info[j]['field4'])

    return render(request, 'index.html', {'leituras' : leitura, 'ventos' : vento, 'uvs' : uv, 'niveis' : nivel_mar})
