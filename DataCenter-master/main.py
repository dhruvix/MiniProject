

# from flask import Flask,render_template,request,send_file,jsonify
# from flask_mysqldb import MySQL
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import seaborn as sns
# import io

# app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'student1'

# mysql = MySQL(app)

# def higher_studies(req,cur):
#     if field['x']=='departmentId': 
#         if field['year']=='all':
#             cur.execute("SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM higher_studies GROUP BY "+field['x'])
#         else:
#             cur.execute("SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM higher_studies WHERE yearOfJoining="+field['year']+" GROUP BY "+field['x'])        
#     elif field['x']=='yearOfPassing':
#         if field['dep']=='all':
#             cur.execute("SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM higher_studies GROUP BY "+field['x'])
#         else:
#             cur.execute("SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM higher_studies WHERE departmentId=\""+field['dep']+"\"GROUP BY "+field['x'])
#     else: 
#         if field['dep']=='all' and field['year']=='all': 
#             cur.execute("SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM higher_studies GROUP BY "+field['x'])
#         elif field['year']=='all':
#             cur.execute("SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM higher_studies WHERE departmentId=\""+field['dep']+"\" GROUP BY "+field['x'])
#         elif field['dep']=='all': 
#             cur.execute("SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM higher_studies WHERE yearOfJoining="+field["year"]+" GROUP BY "+field['x'])
#         else:
#             cur.execute("SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM higher_studies WHERE yearOfJoining="+field['year']+" AND departmentId=\""+field['dep']+"\" GROUP BY "+field['x'])

#     if req=="graph":
#         data=cur.fetchall()
#         df=pd.DataFrame(data,columns=[field['x'],'NoOfStu'])
#         f, ax = plt.subplots(figsize=(10,5))
#         plt.bar(df[field['x']],df['NoOfStu'])
#         plt.xticks(fontsize=8, rotation=90)
#         ax.set_xlabel(field['x'])
#         plt.ylabel('NoOfStu')
#         bytes_image = io.BytesIO()
#         plt.savefig(bytes_image, format='png')
#         bytes_image.seek(0) 
#         # field=None
#         return bytes_image
#     else:
#         rv=cur.fetchall()
#         payload = []           
#         content = {}
#         for result in rv:
#             content = {field['x']: result[0], 'NoOfStu': result[1]}
#             payload.append(content)
#             content = {}
#         # field=None
#         return payload

# @app.route("/")
# def root():
#     return "Hello, this is a Flask server listening at port 5000!"

# field=None

# @app.route('/fields',methods=['POST'])
# def getFields():
#     global field
#     field=request.get_json()
#     print(field,"Recieved Fields")
#     return "Fields initialized successfully"

# @app.route('/graph',methods=['GET'])
# def graph():
#     try:
#         my_x=request.args['x']
#         my_y = request.args['y']
#         print(my_x,"I'm",my_y)
#         cur=mysql.connection.cursor()
#         try:
#             print("graph:",field)
#             if field['tab']=='higher_studies':
#                 bytes_image=higher_studies('graph',cur)
#                 return send_file(bytes_image,attachment_filename='HS1.png',mimetype='image/png')
#             #elif ... to be continued   
#         except:
#             mysql.connection.commit()
#             cur.close()
#             return "Fetch error"
#     except:   
#         return "Cannot connect to database!"

# @app.route('/data',methods=['POST'])
# def data():
#     try:
#         cur=mysql.connection.cursor()
#         try:
#             if field['tab']=='higher_studies':
#                 payload=higher_studies("data",cur)
#                 print(payload)   
#                 return jsonify(payload)
#         except:
#             mysql.connection.commit()
#             cur.close()
#             return "Fetch error"
#     except:   
#         return "Cannot connect to database!"

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

#Harsha tables (to be included when full set arrives)

#Abhishek tables
def higher_studies(req,cur,field):
    qry="SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM higher_studies "
    if field['x']=='departmentId': 
        if field['year']=='all':
            qry+="GROUP BY "+field['x']
        else:
            qry+="WHERE yearOfJoining="+field['year']+" GROUP BY "+field['x']        
    elif field['x']=='yearOfPassing':
        if field['dep']=='all':
            qry+="GROUP BY "+field['x']
        else:
            qry+="WHERE departmentId=\""+field['dep']+"\"GROUP BY "+field['x']
    else: 
        if field['dep']=='all' and field['year']=='all': 
            qry+="GROUP BY "+field['x']
        elif field['year']=='all':
            qry+="WHERE departmentId=\""+field['dep']+"\" GROUP BY "+field['x']
        elif field['dep']=='all': 
            qry+="WHERE yearOfJoining="+field["year"]+" GROUP BY "+field['x']
        else:
            qry+="WHERE yearOfJoining="+field['year']+" AND departmentId=\""+field['dep']+"\" GROUP BY "+field['x']

    cur.execute(qry)

    if req=="graph":
        data=cur.fetchall()
        df=pd.DataFrame(data,columns=[field['x'],'NoOfStu'])
        f, ax = plt.subplots(figsize=(10,5))
        plt.bar(df[field['x']],df['NoOfStu'])
        plt.xticks(fontsize=8, rotation=90)
        plt.xlabel(field['x'])
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

def competative_exam_details(req,cur,field):
    if field['x']=='departmentId':
        if field['year']=='all':
            qry="SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM competative_exam_details GROUP BY "+field['x']
        else:
            qry="SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM competative_exam_details WHERE yearOfPassing="+field['year']+" GROUP BY "+field['x']
    elif field['x']=='yearOfPassing':
        if field['dep']=='all':
            qry="SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM competative_exam_details GROUP BY "+field['x']
        else:
            qry="SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM competative_exam_details WHERE departmentId=\""+field['dep']+"\" GROUP BY "+field['x']    
    elif field['x']=='qualifyingExam':
        if field['y']=='examScore':
            qry="SELECT "+field['x']+",MAX(CAST("+field['y']+" AS INT)) FROM competative_exam_details " 
            if field['dep']=='all' and field['year']=='all': 
                qry+="GROUP BY "+field['x']
            elif field['year']=='all':
                qry+="WHERE departmentId=\""+field['dep']+"\" GROUP BY "+field['x']
            elif field['dep']=='all': 
                qry+="WHERE yearOfPassing="+field['year']+" GROUP BY "+field['x']
            else:
                qry+="WHERE yearOfPassing="+field['year']+" AND departmentId=\""+field['dep']+"\" GROUP BY "+field['x']
        elif field['y']=='status':
            if field['dep']=='all' and field['year']=='all': 
                qry="(SELECT Q1.qualifyingExam,NoOfQ,COALESCE(NoOfNQ,0) AS NoOfNQ FROM ((SELECT qualifyingExam,COUNT(status) AS NoOfQ FROM competative_exam_details WHERE status=\"qualified\" GROUP BY qualifyingExam) AS Q1) LEFT JOIN ((SELECT qualifyingExam,COUNT(status) AS NoOfNQ FROM competative_exam_details WHERE status=\"not qualified\" GROUP BY qualifyingExam) AS Q2) ON Q1.qualifyingExam=Q2.qualifyingExam) UNION (SELECT Q2.qualifyingExam,COALESCE(NoOfQ,0) AS NoOfQ,NoOfNQ FROM ((SELECT qualifyingExam,COUNT(status) AS NoOfQ FROM competative_exam_details WHERE status=\"qualified\" GROUP BY qualifyingExam) AS Q1) RIGHT JOIN ((SELECT qualifyingExam,COUNT(status) AS NoOfNQ FROM competative_exam_details WHERE status=\"not qualified\" GROUP BY qualifyingExam) AS Q2) ON Q2.qualifyingExam=Q1.qualifyingExam)"
            elif field['year']=='all':
                qry="(SELECT Q1.qualifyingExam,NoOfQ,COALESCE(NoOfNQ,0) AS NoOfNQ FROM ((SELECT qualifyingExam,COUNT(status) AS NoOfQ FROM competative_exam_details WHERE status=\"qualified\" AND departmentId=\""+field['dep']+"\" GROUP BY qualifyingExam) AS Q1) LEFT JOIN ((SELECT qualifyingExam,COUNT(status) AS NoOfNQ FROM competative_exam_details WHERE status=\"not qualified\" AND departmentId=\""+field['dep']+"\"GROUP BY qualifyingExam) AS Q2) ON Q1.qualifyingExam=Q2.qualifyingExam) UNION (SELECT Q2.qualifyingExam,COALESCE(NoOfQ,0) AS NoOfQ,NoOfNQ FROM ((SELECT qualifyingExam,COUNT(status) AS NoOfQ FROM competative_exam_details WHERE status=\"qualified\" AND departmentId=\""+field['dep']+"\" GROUP BY qualifyingExam) AS Q1) RIGHT JOIN ((SELECT qualifyingExam,COUNT(status) AS NoOfNQ FROM competative_exam_details WHERE status=\"not qualified\" AND departmentId=\""+field['dep']+"\" GROUP BY qualifyingExam) AS Q2) ON Q2.qualifyingExam=Q1.qualifyingExam)"
            elif field['dep']=='all': 
                qry="(SELECT Q1.qualifyingExam,NoOfQ,COALESCE(NoOfNQ,0) AS NoOfNQ FROM ((SELECT qualifyingExam,COUNT(status) AS NoOfQ FROM competative_exam_details WHERE status=\"qualified\" AND yearOfPassing="+field['year']+" GROUP BY qualifyingExam) AS Q1) LEFT JOIN ((SELECT qualifyingExam,COUNT(status) AS NoOfNQ FROM competative_exam_details WHERE status=\"not qualified\"AND yearOfPassing="+field['year']+" GROUP BY qualifyingExam) AS Q2) ON Q1.qualifyingExam=Q2.qualifyingExam) UNION (SELECT Q2.qualifyingExam,COALESCE(NoOfQ,0) AS NoOfQ,NoOfNQ FROM ((SELECT qualifyingExam,COUNT(status) AS NoOfQ FROM competative_exam_details WHERE status=\"qualified\" AND yearOfPassing="+field['year']+" GROUP BY qualifyingExam) AS Q1) RIGHT JOIN ((SELECT qualifyingExam,COUNT(status) AS NoOfNQ FROM competative_exam_details WHERE status=\"not qualified\" AND yearOfPassing="+field['year']+" GROUP BY qualifyingExam) AS Q2) ON Q2.qualifyingExam=Q1.qualifyingExam)"
            else:
                qry="(SELECT Q1.qualifyingExam,NoOfQ,COALESCE(NoOfNQ,0) AS NoOfNQ FROM ((SELECT qualifyingExam,COUNT(status) AS NoOfQ FROM competative_exam_details WHERE status=\"qualified\" AND yearOfPassing="+field['year']+" AND departmentId=\""+field['dep']+"\" GROUP BY qualifyingExam) AS Q1) LEFT JOIN ((SELECT qualifyingExam,COUNT(status) AS NoOfNQ FROM competative_exam_details WHERE status=\"not qualified\"AND yearOfPassing="+field['year']+" AND departmentId=\""+field['dep']+"\" GROUP BY qualifyingExam) AS Q2) ON Q1.qualifyingExam=Q2.qualifyingExam) UNION (SELECT Q2.qualifyingExam,COALESCE(NoOfQ,0) AS NoOfQ,NoOfNQ FROM ((SELECT qualifyingExam,COUNT(status) AS NoOfQ FROM competative_exam_details WHERE status=\"qualified\" AND yearOfPassing="+field['year']+" AND departmentId=\""+field['dep']+"\" GROUP BY qualifyingExam) AS Q1) RIGHT JOIN ((SELECT qualifyingExam,COUNT(status) AS NoOfNQ FROM competative_exam_details WHERE status=\"not qualified\" AND yearOfPassing="+field['year']+" AND departmentId=\""+field['dep']+"\" GROUP BY qualifyingExam) AS Q2) ON Q2.qualifyingExam=Q1.qualifyingExam)"
                
    cur.execute(qry)

    f, ax = plt.subplots(figsize=(10,5))
    if req=="graph":
        if field['y']=='examScore':
            y_label='Max Score'
        else:
            y_label='NoOfStu'
        data=cur.fetchall()
        if field['y']=='status':
            df=pd.DataFrame(data,columns=['Exam','NoOfQ','NoOfNQ'])
            df.plot(x="Exam", y=["NoOfQ", "NoOfNQ"], kind="bar")
        else:
            df=pd.DataFrame(data,columns=[field['x'],y_label])
            plt.bar(df[field['x']],df[y_label])
        plt.xticks(fontsize=8, rotation=90)
        plt.xlabel(field['x'])
        plt.ylabel(y_label)
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0) 
        return bytes_image
    else:
        if field['y']=='examScore':
            y_label='Max Score'
        else:
            y_label='NoOfStu'
        if field['y']=='status':
            rv=cur.fetchall()
            payload = []           
            content = {}
            for result in rv:
                content = {field['x']: result[0], 'NoOfQ': result[1], 'NoOfNQ': result[2]}
                payload.append(content)
        else:    
            rv=cur.fetchall()
            payload = []           
            content = {}
            for result in rv:
                content = {field['x']: result[0], y_label: result[1]}
                payload.append(content)
        return payload

def internship(req,cur,field):
    pass

#Routes for testing (Ignore this front end guys)
@app.route("/")
def root():
    return "Hello, this is a Flask server listening at port 5000!"

@app.route('/testg',methods=['GET'])
def testg():
    try:
        cur=mysql.connection.cursor()
        try:
            qry="(SELECT Q1.qualifyingExam,NoOfQ,COALESCE(NoOfNQ,0) AS NoOfNQ FROM ((SELECT qualifyingExam,COUNT(status) AS NoOfQ FROM competative_exam_details WHERE status=\"qualified\" GROUP BY qualifyingExam) AS Q1) LEFT JOIN ((SELECT qualifyingExam,COUNT(status) AS NoOfNQ FROM competative_exam_details WHERE status=\"not qualified\" GROUP BY qualifyingExam) AS Q2) ON Q1.qualifyingExam=Q2.qualifyingExam) UNION (SELECT Q2.qualifyingExam,COALESCE(NoOfQ,0) AS NoOfQ,NoOfNQ FROM ((SELECT qualifyingExam,COUNT(status) AS NoOfQ FROM competative_exam_details WHERE status=\"qualified\" GROUP BY qualifyingExam) AS Q1) RIGHT JOIN ((SELECT qualifyingExam,COUNT(status) AS NoOfNQ FROM competative_exam_details WHERE status=\"not qualified\" GROUP BY qualifyingExam) AS Q2) ON Q2.qualifyingExam=Q1.qualifyingExam)"
            cur.execute(qry)
            data=cur.fetchall()
            df=pd.DataFrame(data,columns=['Exam','NoOfQ','NoOfNQ'])
            df.plot(x="Exam", y=["NoOfQ", "NoOfNQ"], kind="bar")
            plt.xticks(fontsize=8, rotation=0)
            plt.xlabel('Exam')
            plt.ylabel('NoOfStu')
            bytes_image = io.BytesIO()
            plt.savefig(bytes_image, format='png')
            bytes_image.seek(0)  
            return send_file(bytes_image,attachment_filename='HS1.png',mimetype='image/png')
        except:
            mysql.connection.commit()
            cur.close()
            return "Fetch error"
    except:   
        return "Cannot connect to database!"

@app.route('/testd',methods=['POST'])
def testd():
    try:
        cur=mysql.connection.cursor()
        try:
            qry="(SELECT Q1.qualifyingExam,NoOfQ,COALESCE(NoOfNQ,0) AS NoOfNQ FROM ((SELECT qualifyingExam,COUNT(status) AS NoOfQ FROM competative_exam_details WHERE status=\"qualified\" GROUP BY qualifyingExam) AS Q1) LEFT JOIN ((SELECT qualifyingExam,COUNT(status) AS NoOfNQ FROM competative_exam_details WHERE status=\"not qualified\" GROUP BY qualifyingExam) AS Q2) ON Q1.qualifyingExam=Q2.qualifyingExam) UNION (SELECT Q2.qualifyingExam,COALESCE(NoOfQ,0) AS NoOfQ,NoOfNQ FROM ((SELECT qualifyingExam,COUNT(status) AS NoOfQ FROM competative_exam_details WHERE status=\"qualified\" GROUP BY qualifyingExam) AS Q1) RIGHT JOIN ((SELECT qualifyingExam,COUNT(status) AS NoOfNQ FROM competative_exam_details WHERE status=\"not qualified\" GROUP BY qualifyingExam) AS Q2) ON Q2.qualifyingExam=Q1.qualifyingExam)"
            cur.execute(qry) 
            rv=cur.fetchall()
            payload = []           
            content = {}
            for result in rv:
                content = {'Exam': result[0], 'NoOfQ': result[1],'NoOfNQ': result[2]}
                payload.append(content)
                content = {}   
            return jsonify(payload)
        except:
            mysql.connection.commit()
            cur.close()
            return "Fetch error"
    except:   
        return "Cannot connect to database!"
#Main routes
@app.route('/graph',methods=['GET'])
def graph():
    field=request.args
    try:
        cur=mysql.connection.cursor()
        try:
            print(field['x'],field['tab'])
            if field['tab']=='higher_studies':
                bytes_image=higher_studies('graph',cur,field)
                return send_file(bytes_image,attachment_filename='HS.png',mimetype='image/png')
            elif field['tab']=='competative_exam_details':
                bytes_image=competative_exam_details('graph',cur,field)
                return send_file(bytes_image,attachment_filename='CE.png',mimetype='image/png')
        except:
            mysql.connection.commit()
            cur.close()
            return "Fetch error"
    except:   
        return "Cannot connect to database!"

@app.route('/data',methods=['POST'])
def data():
    field=request.get_json()
    try:
        cur=mysql.connection.cursor()
        try:
            if field['tab']=='higher_studies':
                payload=higher_studies("data",cur,field)
                print(payload)
            elif field['tab']=='competative_exam_details':
                payload=competative_exam_details('data',cur,field) 
                print(payload)
            return jsonify(payload)
        except:
            mysql.connection.commit()
            cur.close()
            return "Fetch error"
    except:   
        return "Cannot connect to database!"