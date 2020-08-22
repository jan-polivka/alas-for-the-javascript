from flask import Flask
from flask import jsonify
from flask import request
from flask import json
import json

import os #This is for list of files and directories
app = Flask(__name__)


@app.route('/')
def landing():
    with open('landing.html') as f:
        read_data = f.read()
    return read_data
    
@app.route('/test')
def read_file():
    with open('test.html') as f:
        read_data = f.read()
    return read_data

    
@app.route('/form')
def form_file():
    with open('form.txt') as f:
        read_data = f.read()
    return read_data
       
    
    
@app.route('/character', methods=['POST'])
def character():
    print ("test CHARS")
    data = ""
    data_loaded = ""
    sel = request.get_json()
    with open('json_demo.json', 'r') as json_file:
        data = json_file.read()
        data_loaded = json.loads(data)
        

    
    if (data_loaded['character'][sel['tar']]['health'] >= 4):
        data_loaded['character'][sel['tar']]['health'] = 4
    else:
        data_loaded['character'][sel['tar']]['health'] += 1

    
    with open('json_demo.json', 'w') as json_file:
        json.dump(data_loaded, json_file)

    print (data_loaded['character'][sel['tar']])
    return jsonify(data_loaded['character'][sel['tar']])
    
@app.route('/characterNewX', methods=['POST'])
def characterNewX():
    data = request.get_json()
    print (data.get('name', ''))
    data_loaded = ""
    with open('json_demo.json', 'r') as json_file:
        data_loaded = json.loads(json_file.read())
        print (data)
        print (data_loaded['character'])
        data_loaded['character'].append(data)
        
    with open('json_demo.json', 'w') as json_file:
        json.dump(data_loaded, json_file)
    
    return ('', 200)
    
@app.route('/characterHide', methods=['POST'])
def characterHide():
    arr = os.listdir("chars")
    listString = ""
    for member in arr:
        listString += member.replace('.json', '') + ","
    listString = listString[:-1]
    
    return listString
   

@app.route('/characterEx')
def characterEx():
    with open('characterEx.html') as f:
        read_data = f.read()
    return read_data
   
@app.route('/characterLoad', methods=['POST'])
def characterLoad():
    char = request.args.get('char')
    data = ""
    print (char)
    
    with open("chars/" + char + ".json", 'r') as json_file:
        data = json_file.read()
        data = json.loads(data)
    
    print (data)
    return data
    
@app.route('/characterHealthInc', methods=['POST'])
def characterHealthInc():
    char = request.args.get('char')
    data = ""
    print (char)
    
    with open("chars/" + char + ".json", 'r') as json_file:
        data = json_file.read()
        data = json.loads(data)
    
    if (data['health'] >= 4):
        data['health'] = 4
    else:
        data['health'] += 1
    print (data)
    with open("chars/" + char + ".json", 'w') as json_file:
        json.dump(data, json_file)
    return data
    
    
@app.route('/characterHealthDec', methods=['POST'])
def characterHealthDec():
    char = request.args.get('char')
    data = ""
    print (char)
    
    with open("chars/" + char + ".json", 'r') as json_file:
        data = json_file.read()
        data = json.loads(data)
    
    if (data['health'] <= 0):
        data['health'] = 0
    else:
        data['health'] -= 1
    print (data)
    with open("chars/" + char + ".json", 'w') as json_file:
        json.dump(data, json_file)
    return data
    
@app.route('/characterNew')
def characterNew():
    with open('characterNew.html') as f:
        read_data = f.read()
    return read_data
    
@app.route('/characterSave', methods=['POST'])
def characterSave():
    data = request.get_json()
    print (data.get('name', ''))
    data_loaded = ""
    with open('json_demo.json', 'r') as json_file:
        data_loaded = json.loads(json_file.read())
        print (data)
        print (data_loaded['character'])
        data_loaded['character'].append(data)
        
    with open('json_demo.json', 'w') as json_file:
        json.dump(data_loaded, json_file)
    
    return ('', 200)