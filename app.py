#!/usr/bin/python
#-*- coding: utf-8 -*-

import argparse
import commands
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/fibo', methods=['POST'])
def fibo_fun():
        if request.method == 'POST':
		if str(request.form['num']).isdigit() == False :
			return "Wrong input" + "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><title>Post</title></head><body><form action=\"fibo\" method=\"post\"><p>Put number <input type =\"text\"name=\"num\"</p><input type=\"submit\" value =\"submit\"></form></body></html>"

		n=int( request.form['num'])
		f1 =1 	
		f2 =1 
		fn =0
		
		if n==1:
			fn = f1;
		elif n==2: 	
			fn = f2;
		else:
			for i in range(0,n-2):
				fn = f1+ f2
				f1=f2
				f2=fn

		return "%d" % fn + "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><title>Post</title></head><body><form action=\"fibo\" method=\"post\"><p>Put number <input type =\"text\"name=\"num\"</p><input type=\"submit\" value =\"submit\"></form></body></html>"


	
@app.route('/', methods=['GET'])
def hello_test():
        return "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><title>Post</title></head><body><form action=\"fibo\" method=\"post\"><p>Put number <input type =\"text\"name=\"num\"</p><input type=\"submit\" value =\"submit\"></form></body></html>"

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description="")
        parser.add_argument('--listen-port',  type=str, required=True, help='REST service listen port')
        args = parser.parse_args()
        listen_port = args.listen_port
    except Exception, e:
        print('Error: %s' % str(e))

    ipaddr=commands.getoutput("hostname -I").split()[0]
    print "Starting the service with ip_addr="+ipaddr
    app.run(debug=False,host=ipaddr,port=int(listen_port))
