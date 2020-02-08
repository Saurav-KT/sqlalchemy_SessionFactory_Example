import datetime
import json
from api import app
import flask
from datetime import date
from model.log_model import log
from common.base import session_factory
import os

#POST method to write log to database or text file(text log file kept in current working directory)

@app.route("/api/readwritelog/writelog", methods=['POST'])
def writelog():
    req_data = flask.request.get_json(force=True)
    str1 = str(req_data).replace("\'", "\"")
    input_dict = json.loads(str1)
    flag = input_dict[0]["flag"]
    if flag == '1':
        session = session_factory()
        # insert record in database
        for i in input_dict:
            logMsgBody = log(i["logMsg"], date.today(), i["ipAddress"])
            session.add(logMsgBody)
            session.commit()
        session.close()
    else:
        filePath = os.path.abspath("log.txt")
        file1 = open(filePath, "a+")
        for i in input_dict:
            file1.write(i["logMsg"] + '   ' + str(datetime.datetime.now()) + '   ' + i["ipAddress"] + "\n")
        file1.close()

    return flask.jsonify({"msg": "log successfully inserted"})

#POST method to search log in database or text file(text log file kept in current working directory)
@app.route("/api/readwritelog/readlog", methods=['POST'])
def readlog():
    req_data = flask.request.get_json(force=True)
    str1 = str(req_data).replace("\'", "\"")
    input_dict = json.loads(str1)
    flag = input_dict["flag"]
    searchkeyword = input_dict["searchkeyword"]
    searchresult = []

    if flag == '1':
        session = session_factory()
        logs = session.query(log).filter(log.log_description.like('%' + searchkeyword + '%')).all()
        session.close()

    # x = logs.all()
        for x1 in logs:
            searchresult.append({x1.log_description + ' ' + str(x1.log_date) + '  ' + x1.ip_address})

    if flag == '2':
        filePath = os.path.abspath("log.txt")
        with open(filePath, 'r') as searchfile:
            for line in searchfile:
                if searchkeyword in line:
                    searchresult.append(line)

    return str(searchresult)

