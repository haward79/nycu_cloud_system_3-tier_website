
from flask import Flask
from flask import request
from flask import redirect
from flask import json
from flask_cors import CORS, cross_origin
import mysql.connector


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=['GET',])
@cross_origin()
def get_comments():

    comments = []

    db_con = mysql.connector.connect(user='dbuser', password='nycu_ai', host='192.168.56.4', database='web')
    db_cursor = db_con.cursor()
    db_cursor.execute('SELECT * FROM comments;')
    result = db_cursor.fetchall()

    for comment in result:
        comments.append(comment[1])
    
    db_cursor.close()
    db_con.close()

    return app.response_class(response=json.dumps({'status': 0, 'data': comments}), status=200, mimetype='application/json')


@app.route("/", methods=['POST',])
@cross_origin()
def send_comment():

    comment = request.json['data']

    if len(comment) > 0:
        db_con = mysql.connector.connect(user='dbuser', password='nycu_ai', host='192.168.56.4', database='web')
        db_cursor = db_con.cursor()
        db_cursor.execute('INSERT INTO comments (data) VALUES (%s);', (comment,))
        db_con.commit()
        db_cursor.close()
        db_con.close()

        return app.response_class(response=json.dumps({'status': 0}), status=200, mimetype='application/json')

    else:
        return app.response_class(response=json.dumps({'status': 1, 'msg': 'Comment is blank!'}), status=400, mimetype='application/json')
