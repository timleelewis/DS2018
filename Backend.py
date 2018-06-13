from flask import request
from flask import Flask, jsonify
from flask_cors import CORS
import json
import serial
import os
import time
import sqlite3
import datetime






app = Flask(__name__)
CORS(app)
@app.route('/', methods=['POST'])


def create_task():
    temp = request.get_json()
    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    print (temp)
    incomingData = 0
    outgoingData = 0

    try:
        incomingData = temp["data"]
    except KeyError:
        outgoingData = temp["request"]


    
    if incomingData is not 0:
        #Incoming data is in the format, '{"data": [user, tasks, "deadline", "finishedStatus"]}'
        #Time is in the format: "2018-06-12 22:06:13.109845"
        #Tasks should be one long string, separated by commas.
        #finishedStatus is either "True" or "False" only.

        command = """INSERT INTO main (ID, user, tasks, postingTime, deadline, finishedStatus)  VALUES ("{q}", "{u}", "{t}", "{p}", "{d}", "{f}");"""
 
        ID = str((incomingData[4])['taskID']) 
        user = str((incomingData[0])['user']) 
        tasks = (incomingData[1])['tasks']
        postingTime = str(datetime.datetime.now())
        deadline = str((incomingData[2])['deadline'])
        finishedStatus = str((incomingData[3])['finishedStatus'])


        outgoingCommand = command.format( q = ID,
                                          u = user,
                                          t = tasks,
                                          p = postingTime,
                                          d = deadline,
                                          f = finishedStatus)
                                          

        cursor.execute(outgoingCommand)
        connection.commit()
        connection.close()

        return jsonify(ID)

    
    if outgoingData is not 0:
        print(outgoingData)
        selection = """SELECT * FROM main WHERE ID={x};"""
        outSelection = selection.format( x = outgoingData)
        cursor.execute(outSelection)
        output = cursor.fetchone()
        print (output)

        return jsonify(output)
        

        

if __name__ == '__main__':
    app.run(debug=False)


#$ curl -i -H "Content-Type: application/json" -X POST -d '{"item": ["10000", "10001"]}' http://localhost:5000/
#Use local tunnel to access on open internet
