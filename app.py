from flask import jsonify
import json
import sqlite3
from flask import Flask

app = Flask(__name__)

@app.route("/api/v1/info")
def home_index():
    conn = sqlite3.connect('db')
    api_list=[]
    cursor = conn.execute("SELECT version, buildtime,methods, links from apirelease")
    for row in cursor:
        a_dict = {}
        a_dict['version'] = row[0]
        a_dict['buildtime'] = row[1]
        a_dict['methods'] = row[2]
        a_dict['links'] = row[3]
        api_list.append(a_dict)
    conn.close()
    return jsonify({'api_version' : api_list}),200

@app.route("/api/v1/users", methods=['GET'])
def get_users():
    return list_users()

def list_users():
    conn = sqlite3.connect('db')
    api_list=[]
    cursor = conn.execute("SELECT emailid, full_name, id, password, username from users")
    for row in cursor:
        a_dict = {}
        a_dict['email'] = row[3]
        a_dict['full_name'] = row[0]
        a_dict['id'] = row[2]
        a_dict['password'] = row[1]
        a_dict['username'] = row[4]
        api_list.append(a_dict)
    conn.close()
    return jsonify({'user_list' : api_list}),200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
