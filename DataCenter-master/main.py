

from flask import Flask,render_template,request,send_file,jsonify
from flask_mysqldb import MySQL
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import io

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'student1'

mysql = MySQL(app)

def higher_studies(req,cur):
    if field['x']=='departmentId': 
        if field['year']=='all':
            cur.execute("SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM higher_studies GROUP BY "+field['x'])
        else:
            cur.execute("SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM higher_studies WHERE yearOfJoining="+field['year']+" GROUP BY "+field['x'])        
    elif field['x']=='yearOfPassing':
        if field['dep']=='all':
            cur.execute("SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM higher_studies GROUP BY "+field['x'])
        else:
            cur.execute("SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM higher_studies WHERE departmentId=\""+field['dep']+"\"GROUP BY "+field['x'])
    else: 
        if field['dep']=='all' and field['year']=='all': 
            cur.execute("SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM higher_studies GROUP BY "+field['x'])
        elif field['year']=='all':
            cur.execute("SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM higher_studies WHERE departmentId=\""+field['dep']+"\" GROUP BY "+field['x'])
        elif field['dep']=='all': 
            cur.execute("SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM higher_studies WHERE yearOfJoining="+field["year"]+" GROUP BY "+field['x'])
        else:
            cur.execute("SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM higher_studies WHERE yearOfJoining="+field['year']+" AND departmentId=\""+field['dep']+"\" GROUP BY "+field['x'])

    if req=="graph":
        data=cur.fetchall()
        df=pd.DataFrame(data,columns=[field['x'],'NoOfStu'])
        f, ax = plt.subplots(figsize=(10,5))
        plt.bar(df[field['x']],df['NoOfStu'])
        plt.xticks(fontsize=8, rotation=90)
        ax.set_xlabel(field['x'])
        plt.ylabel('NoOfStu')
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0) 
        return bytes_image
    else:
        rv=cur.fetchall()
        payload = []           
        content = {}
        for result in rv:
            content = {field['x']: result[0], 'NoOfStu': result[1]}
            payload.append(content)
            content = {}
        return payload

@app.route("/")
def root():
    return "Hello, this is a Flask server listening at port 5000!"

field=None

@app.route('/fields',methods=['POST'])
def getFields():
    global field
    field=request.get_json()
    print(field)
    return "Fields initialized successfully"

@app.route('/graph',methods=['GET'])
def graph():
    try:
        cur=mysql.connection.cursor()
        try:
            if field['tab']=='higher_studies':
                bytes_image=higher_studies('graph',cur)
                return send_file(bytes_image,attachment_filename='HS1.png',mimetype='image/png')
            #elif ... to be continued   
        except:
            mysql.connection.commit()
            cur.close()
            return "Fetch error"
    except:   
        return "Cannot connect to database!"

@app.route('/data',methods=['POST'])
def data():
    try:
        cur=mysql.connection.cursor()
        try:
            if field['tab']=='higher_studies':
                payload=higher_studies("data",cur)
                print(payload)   
                return jsonify(payload)
        except:
            mysql.connection.commit()
            cur.close()
            return "Fetch error"
    except:   
        return "Cannot connect to database!"



























































# from flask import Flask,render_template,request,send_file,jsonify
# from flask_mysqldb import MySQL

# app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'student1'
# mysql = MySQL(app)


# @app.route("/")
# def root():
#     return "Hello, this is a Flask server listening at port 5000!"

# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import io
# import seaborn as sns

# field=None

# # @app.route('/fields',methods=['POST'])
# # def getFields():
# #     global field
# #     field=request.get_json()
# #     print(field)
# #     return "Fields initialized successfully"

# # @app.route('/student_ach',methods=['GET'])
# # def plot2():
# #     try:
# #         cur=mysql.connection.cursor()
# #         try:
# #             print(field)
# #             new_x = request.args.get('x')
# #             new_y = request.args.get('y')
# #             print("My Code is this : ",new_x,new_y)
# #             cur.execute("SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM higher_studies GROUP BY "+field['x'])
# #             data=cur.fetchall()
# #             df=pd.DataFrame(data,columns=['Country','NoOfStu'])
# #             f, ax = plt.subplots(figsize=(10,5))
# #             plt.bar(df['Country'],df['NoOfStu'])
# #             plt.xticks(fontsize=8, rotation=90)
# #             plt.xlabel('Country')

# #             plt.ylabel('NoOfStu')
# #             bytes_image = io.BytesIO()
# #             plt.savefig(bytes_image, format='png')
# #             bytes_image.seek(0)
# #             return send_file(bytes_image,attachment_filename='HS1.png',mimetype='image/png')
# #         except:
# #             mysql.connection.commit()
# #             cur.close()
# #             return "Fetch error"
# #     except:   
# #         return "Cannot connect to database!"

# @app.route('/HS2graph',methods=['GET'])
# def plot2():
#     try:
#         cur=mysql.connection.cursor()
#         try:
#             print(field)
#             new_x = request.args.get('x')
#             new_y = request.args.get('y')
#             print("My Code is this : ",new_x,new_y)
#             cur.execute("SELECT "+new_x+",COUNT(usn) AS NoOfStu FROM higher_studies GROUP BY "+new_x)
#             data=cur.fetchall()
#             df=pd.DataFrame(data,columns=['Country','NoOfStu'])
#             f, ax = plt.subplots(figsize=(10,5))
#             plt.bar(df['Country'],df['NoOfStu'])
#             plt.xticks(fontsize=8, rotation=90)
#             plt.xlabel('Country')
#             plt.ylabel('NoOfStu')
#             bytes_image = io.BytesIO()
#             plt.savefig(bytes_image, format='png')
#             bytes_image.seek(0)
#             return send_file(bytes_image,attachment_filename='HS1.png',mimetype='image/png')
#         except:
#             mysql.connection.commit()
#             cur.close()
#             return "Fetch error"
#     except:   
#         return "Cannot connect to database!"

# @app.route('/HS2data',methods=['GET'])
# def data2():
#     try:
#         cur=mysql.connection.cursor()
#         try:
#             # cur.execute("SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM higher_studies GROUP BY "+field['x'])
#             cur.execute("SELECT * FROM higher_studies")
#             rv=cur.fetchall()
#             payload = []           
#             content = {}
#             field_names = [i[0] for i in cur.description]
#             # return jsonify(field_names)
#             # payload.append(field_names)
#             for result in rv:
#                 i=0
#                 while i<len(field_names):
#                     #content[] = {'slno': result[0], 'studentname': result[1],'usn':result[2]}
#                     #payload.append(content)
#                     #content = {}
#                     content[field_names[i]]=result[i]
#                     i+=1
#                 payload.append(content)
#                 content={}
#             return jsonify(payload)
#         except:
#             mysql.connection.commit()
#             cur.close()
#             return "Fetch error"
#     except:   
#         return "Cannot connect to database!"