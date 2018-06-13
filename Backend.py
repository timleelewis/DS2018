from flask import request
from flask import Flask, jsonify
import serial
import os
import time
import sqlite3
import datetime





queryCounter = 0

app = Flask(__name__)
@app.route('/', methods=['POST'])


def create_task():
    global queryCounter
    task = (request.json["data"])
    print(task)
    #Incoming data is in the format, '{"data": [user, tasks, "deadline", "finishedStatus"]}'
    #Time is in the format: "2018-06-12 19:59:03.327762"
    #Tasks should be one long string, separated by commas.
    #finishedStatus is either "True" or "False" only.

    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()


    command = """INSERT INTO main (queryNum, user, tasks, postingTime, deadline, finishedStatus)  VALUES ("{q}", "{u}", "{t}", "{p}", "{d}", "{f}");"""

    #queryNum serves as an ID for each thing
    
    queryNum = str(queryCounter) 
    user = str(incomingData[0]) 
    tasks = incomingData[1]
    postingTime = str(datetime.datetime.now())
    deadline = str(incomingData[2])
    finishedStatus = str(incomingData[3])


    outgoingCommand = command.format( q = queryNum,
                                      u = user,
                                      t = tasks,
                                      p = postingTime,
                                      d = deadline,
                                      f = finishedStatus)
                                      

    print (outgoingCommand)
    cursor.execute(outgoingCommand)
    queryCounter = queryCounter + 1
    connection.commit()
    connection.close()

    
    return jsonify("thanks")

if __name__ == '__main__':
    app.run(debug=False)


#$ curl -i -H "Content-Type: application/json" -X POST -d '{"item": ["10000", "10001"]}' http://localhost:5000/
#Use local tunnel to access on open internet
