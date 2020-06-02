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

#Harsha tables 
def stud_ach(req,cur,field,tab):
    #cur=mysql.connection.cursor()
    if req=="graph":
        qry=""
        if field['x']=="year":
            x_lab="year"
            k="year(date)"
            #field['x']+="(date)"
        else:
            x_lab=field['x']
            k=field['x']

        qry+="SELECT "+k+",COUNT(slNo) AS NoOfStu FROM "+tab+" "
        if k!="year(date)" and field['year']!="all" and field['dep']=="all":
            qry+="where "+"year(date)="+field['year']+" "
        if k!="departmentId" and field['dep']!="all" and field['year']=="all" :
            qry+="where departmentId="+"\""+field['dep']+"\""+" "
        if k!="departmentId" and  k!="year(date)" and field['dep']!="all" and field['year']!="all" :
            qry+="where "+"year(date)="+field['year']+" and "+"departmentId="+"\""+field['dep']+"\""+" "
        qry+="group by "+k
        cur.execute(qry)
        data=cur.fetchall()
        df=pd.DataFrame(data,columns=[field['x'],'NoOfStu'])
        a= list(set(df[field['x']].values))
        l=(len(a))
        f, ax = plt.subplots(figsize=(10,5))
        plt.bar(df[field['x']],df['NoOfStu'],align='center')
        plt.xticks(fontsize=8, rotation=30)
        ax.set_xlabel(x_lab)
        plt.ylabel('NoOfStu')
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
        return send_file(bytes_image,attachment_filename='st_act.png',mimetype='image/png')
    qry=""
    if field['x']=="year":
        x_lab="year"
        k="year(date)"
            #field['x']+="(date)"
    else:
        x_lab=field['x']
        k=field['x']

    qry+="SELECT "+k+",COUNT(slNo) AS NoOfStu FROM "+tab+" "
    if k!="year(date)" and field['year']!="all" and field['dep']=="all":
        qry+="where "+"year(date)="+field['year']+" "
    if k!="departmentId" and field['dep']!="all" and field['year']=="all" :
        qry+="where departmentId="+"\""+field['dep']+"\""+" "
    if k!="departmentId" and  k!="year(date)" and field['dep']!="all" and field['year']!="all" :
        qry+="where "+"year(date)="+field['year']+" and "+"departmentId="+"\""+field['dep']+"\""+" "
    qry+="group by "+k
    cur.execute(qry)
    rv=cur.fetchall()
    payload = []           
    content = {}
    for result in rv:
        content = {field['x']: result[0], field['y']: result[1]}
        payload.append(content)
        content = {}
    return jsonify(payload)


def stud_act(req,cur,field,tab):
    cur=mysql.connection.cursor()
    if req=="graph":
        qry=""
        if field['x']=="year":
            x_lab="year"
            k="year(date)"
        else:
            x_lab=field['x']
            k=field['x']
        qry+="SELECT "+k+",COUNT(slNo) AS NoOfStu FROM "+tab+" "
        if k!="year(date)" and field['year']!="all" and field['dep']=="all":
            qry+="where "+"year(date)="+field['year']+" "
        if k!="departmentId" and field['dep']!="all" and field['year']=="all" :
            qry+="where departmentId="+"\""+field['dep']+"\""+" "
        if k!="departmentId" and  k!="year(date)" and field['dep']!="all" and field['year']!="all" :
            qry+="where "+"year(date)="+field['year']+" and "+"departmentId="+"\""+field['dep']+"\""+" "
        qry+="group by "+k
        cur.execute(qry)
        data=cur.fetchall()
        df=pd.DataFrame(data,columns=[field['x'],'NoOfStu'])
        a= list(set(df[field['x']].values))
        l=(len(a))
        f, ax = plt.subplots(figsize=(10,5))
        plt.bar(df[field['x']],df['NoOfStu'],align='center')
        plt.xticks(fontsize=8, rotation=30)
        ax.set_xlabel(x_lab+" dep="+field['dep']+" year= "+field['year'] )
        plt.ylabel('NoOfStu')
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
        return send_file(bytes_image,attachment_filename='st_ach.png',mimetype='image/png')
  

    qry=""
    if field['x']=="year":
        x_lab="year"
        k="year(date)"
    else:
        x_lab=field['x']
        k=field['x']
    qry+="SELECT "+k+",COUNT(slNo) AS NoOfStu FROM "+tab+" "
    if k!="year(date)" and field['year']!="all" and field['dep']=="all":
        qry+="where "+"year(date)="+field['year']+" "
    if k!="departmentId" and field['dep']!="all" and field['year']=="all" :
        qry+="where departmentId="+"\""+field['dep']+"\""+" "
    if k!="departmentId" and  k!="year(date)" and field['dep']!="all" and field['year']!="all" :
        qry+="where "+"year(date)="+field['year']+" and "+"departmentId="+"\""+field['dep']+"\""+" "
    qry+="group by "+k
    cur.execute(qry)
    rv=cur.fetchall()
    payload = []           
    content = {}
    for result in rv:
        content = {field['x']: result[0], field['y']: result[1]}
        payload.append(content)
        content = {}
    return jsonify(payload)




def stud_conf(req,cur,field,tab):
    cur=mysql.connection.cursor()
    if req=="graph":
        qry=""
        x_lab=field['x']
        qry+="SELECT "+field['x']+",COUNT(slNo) AS NoOfStu FROM "+tab+" "
        if field['x']!="year" and field['year']!="all" and field['dep']=="all":
            qry+="where "+"year="+field['year']+" "
        if field['x']!="departmentId" and field['dep']!="all" and field['year']=="all" :
            qry+="where departmentId="+"\""+field['dep']+"\""+" "
        if field['x']!="departmentId" and  field['x']!="year" and field['dep']!="all" and field['year']!="all" :
            qry+="where "+"year="+field['year']+" and "+"departmentId="+"\""+field['dep']+"\""+" "
        qry+="group by "+field['x']
        cur.execute(qry)
        data=cur.fetchall()
        df=pd.DataFrame(data,columns=[field['x'],'NoOfStu'])
        a= list(set(df[field['x']].values))
        l=(len(a))
        f, ax = plt.subplots(figsize=(10,5))
        plt.bar(df[field['x']],df['NoOfStu'],align='center')
        plt.xticks(fontsize=8, rotation=30)
        ax.set_xlabel(x_lab)
        plt.ylabel('NoOfStu')
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
        return send_file(bytes_image,attachment_filename='st_act.png',mimetype='image/png')


    qry=""
    x_lab=field['x']
    qry+="SELECT "+field['x']+",COUNT(slNo) AS NoOfStu FROM "+tab+" "
    if field['x']!="year" and field['year']!="all" and field['dep']=="all":
        qry+="where "+"year="+field['year']+" "
    if field['x']!="departmentId" and field['dep']!="all" and field['year']=="all" :
        qry+="where departmentId="+"\""+field['dep']+"\""+" "
    if field['x']!="departmentId" and  field['x']!="year" and field['dep']!="all" and field['year']!="all" :
        qry+="where "+"year="+field['year']+" and "+"departmentId="+"\""+field['dep']+"\""+" "
    qry+="group by "+field['x']
    cur.execute(qry)
    rv=cur.fetchall()
    payload = []           
    content = {}
    for result in rv:
        content = {field['x']: result[0], field['y']: result[1]}
        payload.append(content)
        content = {}
    return jsonify(payload)

def stud_journ(req,cur,field,tab):
    cur=mysql.connection.cursor()
    if req=="graph":
        qry=""
        x_lab=field['x']
        print("hi")
        qry+="SELECT "+field['x']+","+"COUNT(slNo) AS NoOfStu FROM "+tab+" "
        if field['x']!="year" and field['year']!="all" and field['dep']=="all":
            qry+="where "+"year="+field['year']+" "
        if field['x']!="departmentId" and field['dep']!="all" and field['year']=="all" :
            qry+="where departmentId="+"\""+field['dep']+"\""+" "
        if field['x']!="departmentId" and  field['x']!="year" and field['dep']!="all" and field['year']!="all" :
            qry+="where "+"year="+field['year']+" and "+"departmentId="+"\""+field['dep']+"\""+" "
        qry+="group by "+field['x']
        cur.execute(qry)
        data=cur.fetchall()
        df=pd.DataFrame(data,columns=[field['x'],'NoOfStu'])
        a= list(set(df[field['x']].values))
        l=(len(a))
        f, ax = plt.subplots(figsize=(10,5))
        plt.bar(df[field['x']],df['NoOfStu'],align='center')
        plt.xticks(fontsize=8, rotation=30)
        ax.set_xlabel(x_lab)
        plt.ylabel('NoOfStu')
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
        return send_file(bytes_image,attachment_filename='st_act.png',mimetype='image/png')
    cur=mysql.connection.cursor()
    qry=""
    x_lab=field['x']
    print("hi")
    qry+="SELECT "+field['x']+","+"COUNT(slNo) AS NoOfStu FROM "+tab+" "
    if field['x']!="year" and field['year']!="all" and field['dep']=="all":
        qry+="where "+"year="+field['year']+" "
    if field['x']!="departmentId" and field['dep']!="all" and field['year']=="all" :
        qry+="where departmentId="+"\""+field['dep']+"\""+" "
    if field['x']!="departmentId" and  field['x']!="year" and field['dep']!="all" and field['year']!="all" :
        qry+="where "+"year="+field['year']+" and "+"departmentId="+"\""+field['dep']+"\""+" "
    qry+="group by "+field['x']
    cur.execute(qry)
    rv=cur.fetchall()
    payload = []           
    content = {}
    for result in conrv:
        content = {field['x']: result[0], field['y']: result[1]}
        payload.append(content)
        content = {}
    return jsonify(payload)


  

def stud_funded(req,cur,field):
    cur=mysql.connection.cursor()
    if req=="graph":
        qry=""
        y_lab=field['y']
        if y_lab=="nof":
            qry="SELECT "+field['x']+", count(slNo) from student_funded_projects_dept group by "+ field['x']
        elif y_lab=="funding":
            qry="SELECT "+field['x']+", sum(amount) from student_funded_projects_dept group by "+field['x']
        cur.execute(qry)
        data=cur.fetchall()
        print(data)
        li=[]
        for i in data:
            li.append([i[0],int(i[1])])
        print(li)
        df=pd.DataFrame(li,columns=[field['x'],'No'])
        print(df.head())
        a= list(set(df[field['x']].values))
        l=(len(a))
        f, ax = plt.subplots(figsize=(10,5))
        plt.bar(df[field['x']],df['No'],align='center')
        plt.xticks(fontsize=8, rotation=30)
        ax.set_xlabel(field['x'])
        plt.ylabel('No')
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
        return send_file(bytes_image,attachment_filename='st_act.png',mimetype='image/png')

    qry=""
    y_lab=field['y']
    if y_lab=="nof":
        qry="SELECT "+field['x']+", count(slNo) from student_funded_projects_dept group by "+ field['x']
    elif y_lab=="funding":
        qry="SELECT "+field['x']+", sum(amount) from student_funded_projects_dept group by "+field['x']
    cur.execute(qry)
    rv=cur.fetchall()
    payload = []           
    content = {}
    for result in rv:

        content = {field['x']: result[0], field['y']: int(result[1])}
        payload.append(content)
        content = {}
    return jsonify(payload)

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
            if(y_label == 'Max Score'):
                    y_label = 'examScore'
            for result in rv:
                content = {field['x']: result[0], y_label: result[1]}
                payload.append(content)
        return payload

def internship(req,cur,field):
    qry="SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM internship_"+field['op']+" "
    if field['x']=='departmentId': 
        if field['year']=='all':
            qry+="GROUP BY "+field['x']
        else:
            y=int(str(datetime.now())[:4])
            d=int(field['year'])
            qry+="WHERE (YEAR(startDate)="+str(y-d-1)+" OR YEAR(startDate)="+str(y-d)+") AND YEAR(endDate)="+str(y-d)+" GROUP BY "+field['x'] 
    elif field['x']=='year':
        if field['dep']=='all':
            qry="(SELECT YEAR,COUNT(USN) AS NoOfStu FROM ((SELECT YEAR(startDate) AS YEAR,USN FROM internship_"+field['op']+") UNION ALL (SELECT YEAR(endDate) AS YEAR,USN FROM internship_"+field['op']+"))AS T GROUP BY YEAR)"
        else:
            qry="(SELECT YEAR,COUNT(USN) AS NoOfStu FROM ((SELECT YEAR(startDate) AS YEAR,USN FROM internship_"+field['op']+" WHERE departmentId=\""+field['dep']+"\") UNION ALL (SELECT YEAR(endDate) AS YEAR,USN FROM internship_"+field['op']+" WHERE departmentId=\""+field['dep']+"\"))AS T GROUP BY YEAR)"    
    else: 
        if field['dep']=='all' and field['year']=='all': 
            qry+="GROUP BY "+field['x']
        elif field['year']=='all':
            qry+="WHERE departmentId=\""+field['dep']+"\" GROUP BY "+field['x']
        elif field['dep']=='all': 
            y=int(str(datetime.now())[:4])
            d=int(field['year']) 
            qry+="WHERE (YEAR(startDate)="+str(y-d-1)+" OR YEAR(startDate)="+str(y-d)+") AND YEAR(endDate)="+str(y-d)+" GROUP BY "+field['x']
        else:
            y=int(str(datetime.now())[:4])
            d=int(field['year'])  
            qry+="WHERE (YEAR(startDate)="+str(y-d-1)+" OR YEAR(startDate)="+str(y-d)+") AND YEAR(endDate)="+str(y-d)+" AND departmentId=\""+field['dep']+"\" GROUP BY "+field['x'] 
 
    cur.execute(qry)

    if req=="graph":
        data=cur.fetchall()
        df=pd.DataFrame(data,columns=[field['x'],'NoOfStu'])
        r=df.shape[0]
        if r<=50:    
            fig,ax = plt.subplots(figsize=(10,5))
            plt.bar(df[field['x']],df['NoOfStu'])
            plt.xticks(fontsize=8, rotation=90)
            plt.xlabel(field['x'])
            plt.ylabel('NoOfStu')
            bytes_image = io.BytesIO()
            plt.savefig(bytes_image, format='png',bbox_inches = "tight")    
            bytes_image.seek(0)  
            return bytes_image 
        else:
            k=50
            n=r//k
            if r%k!=0:
                n+=1
            #n is the number of subplots needed    
            nrow=n
            fig,ax = plt.subplots(nrows=nrow,figsize=(10,5*n))
            fig.tight_layout(h_pad=30)
            i=0
            bytes_image = io.BytesIO() 
            for row in range(nrow):
                if i+k<=r:
                    ax[row].bar(df[field['x']][i:i+k],df['NoOfStu'][i:i+k])
                else:
                    ax[row].bar(df[field['x']][i:],df['NoOfStu'][i:])
                ax[row].set(xlabel=field['x'],ylabel='NoOfStu')
                ax[row].tick_params(axis="x", labelsize=8,labelrotation=90)
                fig.savefig(bytes_image, format='png',bbox_inches = "tight")   
                bytes_image.seek(0)    
                if i+k>=r:
                    break
                i=i+k      
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

def placement(req,cur,field):
    if field['y']=='Count Of Students':
        y_label="NoOfStu"
    elif field['y']=='Students with multiple offers':
        y_label="NoOfStu with Multiple Offers"
    else:
        y_label=field['y']
        
    if field['op']=='ug':
        if field['x']=='departmentId': 
            if field['y']=='Count Of Students':
                qry="SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM placement_details_"+field['op']+" "
                if field['year']=='all':
                    qry+="GROUP BY "+field['x']
                else:
                    qry+="WHERE yearOfPassing="+field['year']+" GROUP BY "+field['x']
            elif field['y']=='Students with multiple offers':
                if field['year']=='all':
                    qry=" SELECT departmentId,COUNT(departmentId) AS NoOfStu FROM (SELECT departmentId,usn,COUNT(usn) FROM placement_details_ug GROUP BY usn HAVING COUNT(usn)>1) AS T GROUP BY departmentId"
                else:
                    qry=" SELECT departmentId,COUNT(departmentId) AS NoOfStu FROM (SELECT departmentId,usn,COUNT(usn) FROM placement_details_ug WHERE yearOfPassing="+field['year']+" GROUP BY usn HAVING COUNT(usn)>1) AS T GROUP BY departmentId"
            else:
                qry="SELECT "+field['x']+","
                if field['y']=='Average Package':
                    qry+="AVG(package) "
                elif field['y']=='Maximum Package':
                    qry+="MAX(package) "
                elif field['y']=='Minimum Package':
                    qry+="MIN(package) "
                if field['year']=='all':
                    qry+="FROM placement_details_ug GROUP BY "+field['x']
                else:
                    qry+="FROM placement_details_ug WHERE yearOfPassing=\""+field['year']+"\" GROUP BY "+field['x']        
        elif field['x']=='yearOfPassing':
            if field['y']=='Count Of Students':
                qry="SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM placement_details_"+field['op']+" "
                if field['dep']=='all':
                    qry+="GROUP BY "+field['x']
                else:
                    qry+="WHERE departmentId=\""+field['dep']+"\" GROUP BY "+field['x']
            elif field['y']=='Students with multiple offers':
                if field['dep']=='all':
                    qry="SELECT yearOfPassing,COUNT(yearOfPassing) AS NoOfStu FROM (SELECT yearOfPassing,usn,COUNT(usn) FROM placement_details_ug GROUP BY usn HAVING COUNT(usn)>1) AS T GROUP BY yearOfPassing"
                else:
                    qry=" SELECT yearOfPassing,COUNT(yearOfPassing) AS NoOfStu FROM (SELECT yearOfPassing,usn,COUNT(usn) FROM placement_details_ug WHERE departmentId=\""+field['dep']+"\" GROUP BY usn HAVING COUNT(usn)>1) AS T GROUP BY yearOfPassing"    
            else:
                qry="SELECT "+field['x']+","
                if field['y']=='Average Package':
                    qry+="AVG(package) "
                elif field['y']=='Maximum Package':
                    qry+="MAX(package) "
                elif field['y']=='Minimum Package':
                    qry+="MIN(package) "
                if field['dep']=='all':
                    qry+="FROM placement_details_ug GROUP BY "+field['x']
                else:
                    qry+="FROM placement_details_ug WHERE departmentId=\""+field['dep']+"\" GROUP BY "+field['x']
        elif field['x']=='companyName': 
            qry="SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM placement_details_"+field['op']+" " 
            if field['dep']=='all' and field['year']=='all': 
                qry+="GROUP BY "+field['x']
            elif field['year']=='all':
                qry+="WHERE departmentId=\""+field['dep']+"\" GROUP BY "+field['x']
            elif field['dep']=='all':
                qry+="WHERE yearOfPassing="+field['year']+" GROUP BY "+field['x']  
            else:
                qry+="WHERE yearOfPassing="+field['year']+" AND departmentId=\""+field['dep']+"\" GROUP BY "+field['x']
    else:
        if field['x']=='departmentId':
            if field['y']=='Count Of Students':
                if field['year']=='all': 
                    qry="(SELECT Q1.departmentId,OnCampus,COALESCE(OffCampus,0) AS OffCampus FROM ((SELECT departmentId,COUNT(usn) AS OnCampus FROM placement_details_pg WHERE on_off_Campus=\"On Campus\" GROUP BY departmentId) AS Q1 LEFT JOIN (SELECT departmentId,COUNT(usn) AS OffCampus FROM placement_details_pg WHERE on_off_Campus=\"Off Campus\" GROUP BY departmentId) AS Q2 ON Q1.departmentId=Q2.departmentId)) UNION (SELECT Q2.departmentId,COALESCE(OnCampus,0) AS OnCampus,OffCampus FROM ((SELECT departmentId,COUNT(usn) AS OnCampus FROM placement_details_pg WHERE on_off_Campus=\"On Campus\" GROUP BY departmentId) AS Q1 RIGHT JOIN (SELECT departmentId,COUNT(usn) AS OffCampus FROM placement_details_pg WHERE on_off_Campus=\"Off Campus\" GROUP BY departmentId) AS Q2 ON Q1.departmentId=Q2.departmentId))"
                else:
                    qry="(SELECT Q1.departmentId,OnCampus,COALESCE(OffCampus,0) AS OffCampus FROM ((SELECT departmentId,COUNT(usn) AS OnCampus FROM placement_details_pg WHERE on_off_Campus=\"On Campus\" AND yearOfPassing="+field['year']+" GROUP BY departmentId) AS Q1 LEFT JOIN (SELECT departmentId,COUNT(usn) AS OffCampus FROM placement_details_pg WHERE on_off_Campus=\"Off Campus\" AND yearOfPassing="+field['year']+" GROUP BY departmentId) AS Q2 ON Q1.departmentId=Q2.departmentId)) UNION (SELECT Q2.departmentId,COALESCE(OnCampus,0) AS OnCampus,OffCampus FROM ((SELECT departmentId,COUNT(usn) AS OnCampus FROM placement_details_pg WHERE on_off_Campus=\"On Campus\" AND yearOfPassing="+field['year']+" GROUP BY departmentId) AS Q1 RIGHT JOIN (SELECT departmentId,COUNT(usn) AS OffCampus FROM placement_details_pg WHERE on_off_Campus=\"Off Campus\" AND yearOfPassing="+field['year']+" GROUP BY departmentId) AS Q2 ON Q1.departmentId=Q2.departmentId))"
            elif field['y']=='Students with multiple offers': 
                if field['year']=='all':
                    qry=" SELECT departmentId,COUNT(departmentId) AS NoOfStu FROM (SELECT departmentId,usn,COUNT(usn) FROM placement_details_pg GROUP BY usn HAVING COUNT(usn)>1) AS T GROUP BY departmentId"
                else:
                    qry=" SELECT departmentId,COUNT(departmentId) AS NoOfStu FROM (SELECT departmentId,usn,COUNT(usn) FROM placement_details_pg WHERE yearOfPassing="+field['year']+" GROUP BY usn HAVING COUNT(usn)>1) AS T GROUP BY departmentId"
        elif field['x']=="yearOfPassing":
            if field['y']=='Count Of Students':
                if field['dep']=="all":
                    qry="(SELECT Q1.yearOfPassing,OnCampus,COALESCE(OffCampus,0) AS OffCampus FROM ((SELECT yearOfPassing,COUNT(usn) AS OnCampus FROM placement_details_pg WHERE on_off_Campus=\"On Campus\" GROUP BY yearOfPassing) AS Q1 LEFT JOIN (SELECT yearOfPassing,COUNT(usn) AS OffCampus FROM placement_details_pg WHERE on_off_Campus=\"Off Campus\" GROUP BY departmentId) AS Q2 ON Q1.yearOfPassing=Q2.yearOfPassing)) UNION (SELECT Q2.yearOfPassing,COALESCE(OnCampus,0) AS OnCampus,OffCampus FROM ((SELECT yearOfPassing,COUNT(usn) AS OnCampus FROM placement_details_pg WHERE on_off_Campus=\"On Campus\" GROUP BY yearOfPassing) AS Q1 RIGHT JOIN (SELECT yearOfPassing,COUNT(usn) AS OffCampus FROM placement_details_pg WHERE on_off_Campus=\"Off Campus\" GROUP BY yearOfPassing) AS Q2 ON Q1.yearOfPassing=Q2.yearOfPassing))"
                else:
                    qry="(SELECT Q1.yearOfPassing,OnCampus,COALESCE(OffCampus,0) AS OffCampus FROM ((SELECT yearOfPassing,COUNT(usn) AS OnCampus FROM placement_details_pg WHERE on_off_Campus=\"On Campus\" AND departmentId=\""+field['dep']+"\" GROUP BY yearOfPassing) AS Q1 LEFT JOIN (SELECT yearOfPassing,COUNT(usn) AS OffCampus FROM placement_details_pg WHERE on_off_Campus=\"Off Campus\" AND departmentId=\""+field['dep']+"\" GROUP BY departmentId) AS Q2 ON Q1.yearOfPassing=Q2.yearOfPassing)) UNION (SELECT Q2.yearOfPassing,COALESCE(OnCampus,0) AS OnCampus,OffCampus FROM ((SELECT yearOfPassing,COUNT(usn) AS OnCampus FROM placement_details_pg WHERE on_off_Campus=\"On Campus\" AND departmentId=\""+field['dep']+"\" GROUP BY yearOfPassing) AS Q1 RIGHT JOIN (SELECT yearOfPassing,COUNT(usn) AS OffCampus FROM placement_details_pg WHERE on_off_Campus=\"Off Campus\" AND departmentId=\""+field['dep']+"\" GROUP BY yearOfPassing) AS Q2 ON Q1.yearOfPassing=Q2.yearOfPassing))"
            elif field['y']=='Students with multiple offers':
                if field['dep']=='all':
                    qry="SELECT yearOfPassing,COUNT(yearOfPassing) AS NoOfStu FROM (SELECT yearOfPassing,usn,COUNT(usn) FROM placement_details_pg GROUP BY usn HAVING COUNT(usn)>1) AS T GROUP BY yearOfPassing"
                else:
                    qry=" SELECT yearOfPassing,COUNT(yearOfPassing) AS NoOfStu FROM (SELECT yearOfPassing,usn,COUNT(usn) FROM placement_details_pg WHERE departmentId=\""+field['dep']+"\" GROUP BY usn HAVING COUNT(usn)>1) AS T GROUP BY yearOfPassing"     
        elif field['x']=='companyName': 
            qry="SELECT "+field['x']+",COUNT(usn) AS NoOfStu FROM placement_details_"+field['op']+" "
            if field['dep']=='all' and field['year']=='all': 
                qry+="GROUP BY "+field['x']
            elif field['year']=='all':
                qry+="WHERE departmentId=\""+field['dep']+"\" GROUP BY "+field['x']
            elif field['dep']=='all':
                qry+="WHERE yearOfPassing="+field['year']+" GROUP BY "+field['x']  
            else:
                qry+="WHERE yearOfPassing="+field['year']+" AND departmentId=\""+field['dep']+"\" GROUP BY "+field['x']

    cur.execute(qry)

    if req=="graph":
        data=cur.fetchall()
        if field['op']=='pg' and (field['x']=='departmentId' or field['x']=='yearOfPassing') and field['y']=='Count Of Students':
            df=pd.DataFrame(data,columns=[field['x'],'OnCampus','OffCampus'])     
        elif field['y']=='Count of Students':
            df=pd.DataFrame(data,columns=[field['x'],'NoOfStu'])
        elif field['y']=='Students with multiple offers':
            df=pd.DataFrame(data,columns=[field['x'],'NoOfStu with Multiple Offers'])
        else: 
            df=pd.DataFrame(data,columns=[field['x'],field['y']])
            y_label=field['y']
 
        r=df.shape[0]
        if r<=50:    
            if field['op']=='pg' and (field['x']=='departmentId' or field['x']=='yearOfPassing') and field['y']=='Count Of Students':
                df.plot(x=field['x'],y=['OnCampus','OffCampus'],kind="bar")
            else:
                fig,ax = plt.subplots(figsize=(10,5))
                plt.bar(df[field['x']],df[y_label])
            plt.xticks(fontsize=8, rotation=90)
            plt.xlabel(field['x'])
            plt.ylabel(y_label)
            bytes_image = io.BytesIO()
            plt.savefig(bytes_image, format='png',bbox_inches = "tight")    
            bytes_image.seek(0)  
            return bytes_image 
        else:                                          #if number of rows is more than 50 in the data, one graph is split into many subplots
            k=50
            n=r//k                                     #n is the number of subplots needed   
            if r%k!=0:
                n+=1                               
            fig,ax = plt.subplots(nrows=n,figsize=(10,5*n))
            fig.tight_layout(h_pad=30)
            i=0
            bytes_image = io.BytesIO() 
            for row in range(n):
                if i+k<=r:
                    ax[row].bar(df[field['x']][i:i+k],df[y_label][i:i+k])
                else:
                    ax[row].bar(df[field['x']][i:],df[y_label][i:])
                ax[row].set(xlabel=field['x'],ylabel=y_label)
                ax[row].tick_params(axis="x", labelsize=8,labelrotation=90)
                fig.savefig(bytes_image, format='png',bbox_inches = "tight")   
                bytes_image.seek(0)    
                if i+k>=r:
                    break
                i=i+k      
            return bytes_image
    else:
        rv=cur.fetchall()
        payload = []           
        content = {}
        if field['op']=='pg' and (field['x']=='departmentId' or field['x']=='yearOfPassing') and field['y']=='Count Of Students':
            for result in rv:
                content = {"departmentId": result[0], "OnCampus": result[1],"OffCampus": result[2]}
                payload.append(content)
        else: 
            print(y_label)
            for result in rv:
                content = {field['x']: result[0], y_label: result[1]}
                payload.append(content)
        return payload

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
            if field['tab']=='higher_studies':
                bytes_image=higher_studies('graph',cur,field)
                return send_file(bytes_image,attachment_filename='HS.png',mimetype='image/png')
            elif field['tab']=='competative_exam_details':
                bytes_image=competative_exam_details('graph',cur,field)
                return send_file(bytes_image,attachment_filename='CE.png',mimetype='image/png')
            elif field['tab']=='placement':
                bytes_image=placement('graph',cur,field)
                return send_file(bytes_image,attachment_filename='PL.png',mimetype='image/png')
            elif field['tab']=='internship':
                bytes_image=internship('graph',cur,field)
                return send_file(bytes_image,attachment_filename='IN.png',mimetype='image/png')
            elif field['tab']== "student_achievement":
                if field['op']=="pg":
                    tab="student_achievement_pg"
                else:
                    tab="student_achievement"
                return stud_ach("graph",cur,field,tab)
            elif field['tab']== "student_activities":
                if field['op']=="pg":
                    tab="student_activities_pg"
                else:
                    tab="student_activities"
                return stud_act("graph",cur,field,tab)
            elif field['tab']=="student_conference_publications":
                if field['op']=="pg":
                    tab="student_conference_publications_pg"
                else:
                    tab="student_conference_publications"
                return stud_conf("graph",cur,field,tab)
            elif field['tab']=="student_journal_publications":
                if field['op']=="pg":
                    tab="student_journal_publications_pg"
                else:
                    tab="student_journal_publications"
                return stud_journ("graph",cur,field,tab)
            
            elif field['tab']=="student_funded_projects_dept":
                return stud_funded("graph",cur,field)
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
                return jsonify(payload)
            elif field['tab']=='competative_exam_details':
                payload=competative_exam_details('data',cur,field) 
                print(payload)
                return jsonify(payload)
            elif field['tab']=='placement':
                print(field)
                payload=placement('data',cur,field) 
                print(payload)
                return jsonify(payload)
            elif field['tab']=='internship':
                payload=internship('data',cur,field)
                print(payload)
                return jsonify(payload)
            elif field['tab']== "student_achievement":
                if field['op']=="pg":
                    tab="student_achievement_pg"
                else:
                    tab="student_achievement"
                return stud_ach("data",cur,field,tab)
            elif field['tab']== "student_activities":
                if field['op']=="pg":
                    tab="student_activities_pg"
                else:
                    tab="student_activities"
                return stud_act("data",cur,field,tab)
            elif field['tab']=="student_conference_publications":
                if field['op']=="pg":
                    tab="student_conference_publications_pg"
                else:
                    tab="student_conference_publications"
                return stud_conf("data",cur,field,tab)
            elif field['tab']=="student_journal_publications":
                if field['op']=="pg":
                    tab="student_journal_publications_pg"
                else:
                    tab="student_journal_publications"
                return stud_journ("data",cur,field,tab)
            elif field['tab']=="student_funded_projects_dept":
                return stud_funded("data",cur,field)

        except:
            mysql.connection.commit()
            cur.close()
            return "Fetch error"
    except:   
        return "Cannot connect to database!"