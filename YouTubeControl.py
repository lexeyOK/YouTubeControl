#!/usr/bin/env python3

from flask import Flask, send_file

import keyboard
import os, os.path
app = Flask(__name__)

# path to files
appPath = app.root_path + '/'

@app.route("/")
def Interface():
    return send_file(appPath + 'interface.html')

@app.route("/<name>")
def other(name):
    if not name == '':
    	# keyboard keys 
        if name in 'jklmf':
            keyboard.press_and_release(name)
            print(name)
            return '[{"message":"OK"}]'
        else:
            if os.path.exists(os.path.join(appPath, name)):
                return send_file(appPath + name)
            return '[{"message":"FAIL"}]'
    print('Incorrect capture!')
    return '[{"message":"ERROR"}]'

if __name__ == '__main__':
	# host and port
    app.run(port=8080, host="0.0.0.0", threaded=True)

# if not wokrking properly
# sudo fuser 8080/tcp -k