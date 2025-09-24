from flask import Flask,jsonify,render_template_string,request,Response,render_template,url_for,redirect
from werkzeug.utils import secure_filename
from werkzeug.datastructures import Headers
import os
import threading
import time
import requests
import db

app = Flask(__name__)

app.config['UPLOAD_FOLDER']="upload"

dd = 0

@app.route("/" , methods=['GET', 'POST'])

@app.route("/home" , methods=['GET', 'POST'])

def home():
    global dd
    dd += 1
    if request.method == "POST":
       search =request.form.get("search")
       search1=search.replace(" ","")
       return redirect(url_for(f"{search1}")) 
       if response.status_code == 304:
          return "not fand"
    
    return render_template('home.html')
def keep_alive():
    while True:
        try:
            requests.get("https://flask-i3r0.onrender.com")  # غيّر هذا إلى رابط موقعك
            
        except Exception as e:
        time.sleep(200)  # كل 5 دقائق = 300 ثانية

# شغل المهمة في الخلفية
threading.Thread(target=keep_alive, daemon=True).start()
@app.route("/johnwick1")

def johnwick1():
    
    return render_template('johnwick1.html')

@app.route("/johnwick2")

def johnwick2():
    
    return render_template('johnwick2.html')

@app.route("/johnwick3")

def johnwick3():
   
    return render_template('johnwick3.html')


@app.route("/adminlogin" , methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
       username=request.form.get('username')
       password1=request.form.get('password_one')
       password2=request.form.get('password_two')
       password3=request.form.get('password_three')
       user=db.user
       pas1=db.pas1
       pas2=db.pas2
       pas3=db.pas3
       if username == user:
          if password1 == pas1:
             if password2 == pas2:
                if password3 == pas3:               
                   return render_template('admin.html', count=dd)              
       else:
           return"<center> <h1> <font face='arial'> <font color='red'>enter the corect password<br></font> </font> </h1> </center>" 
    return render_template('main.html')         
@app.route("/surs=7854hggfcw482481r9rg2f0tg4998tg989__password__changer" , methods=['GET', 'POST'])
def password_ch():
    if request.method == 'POST':
       my_password_1=request.form.get('my_password_1')
       my_password_2=request.form.get('my_password_2')
       my_password_3=request.form.get('my_password_3')
       new_password_1=request.form.get('new_password_1')
       new_password_2=request.form.get('new_password_2')
       new_password_3=request.form.get('new_password_3')
       if my_password_1 == db.pas1 and my_password_2 == db.pas2 and my_password_3 == db.pas3:
          os.system(f'rm db.py')
          with open("db.py", "w") as f:
              f.write(f'user="yaccyber"' + "\n")
              f.write(f'pas1="{new_password_1}"' + "\n")
              f.write(f'pas2="{new_password_2}"'+ "\n")
              f.write(f'pas3="{new_password_3}"' + "\n") 
              return"<center> <font face='arial> <font color='red'> <h1>password changer<br></h1> </font> </font> </center>"        
           
       else:
           return '<h1>password  incoract</h1>' 
    return render_template('changer.html')   
    return render_template('main.html')

@app.route('/surs=byd57648hb84bbc834ndsg__add__film', methods = ['GET','POST'])
def uploadfile():
   import os
   if request.method == 'POST':
      if "file3" and "file2" and "file" and "link1" and "link2" and "link3" and "filme1" and "filme2" and "filme3" and "name1" and "name2" and "name3":
         user=request.form.get("username")
         pas1=request.form.get("password1")
         pas2=request.form.get("password2")
         pas3=request.form.get("password3")
         if user == db.user and pas1 == db.pas1 and pas2 == db.pas2 and pas3 == db.pas3:
            f = request.files['file']
            f1 = request.files['file1']
            f2 = request.files['file2']
            filename=secure_filename(f1.filename)
            f1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filename=secure_filename(f2.filename)
            f2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filename=secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
       
            filme1=request.form.get('filme1')
            filme2=request.form.get('filme2')
            filme3=request.form.get('filme3')
      
            name1=request.form.get('name1')
            name2=request.form.get('name2')
            name3=request.form.get('name3')
       
      
            link1=request.form.get('link1')
            link2=request.form.get('link2')
            link3=request.form.get('link3')
            
            vlink1=request.form.get('vlink1')
            vlink2=request.form.get('vlink2')
            vlink3=request.form.get('vlink3')
            
            cat1=request.form.get('cat1')
            cat2=request.form.get('cat2')
            cat3=request.form.get('cat3')
            
            ane1=request.form.get('ane1')
            ane2=request.form.get('ane2')
            ane3=request.form.get('ane3')
            
            n1=request.form.get('n1')
            n2=request.form.get('n2')
            n3=request.form.get('n3')
            
            
            os.system(f"cp upload/{name1}  static/img/")
            os.system(f"cp upload/{name2}  static/img/")
            os.system(f"cp upload/{name3}  static/img/")
         
            url1=f"{{url_for('static' , filename='img/{name1}')}}"
            url2=f"{{url_for('static' , filename='img/{name2}')}}"
            url3=f"{{url_for('static' , filename='img/{name3}')}}"
            a="{"
            b="}"
            t="{url_for('static' , filename='img/t.jpeg')}"
            v="{url_for('static' , filename='img/v.jpeg')}"

            with open(f"templates/{filme1}.html", "w") as f:
                f.write(f""" 
<html>
<head>
<title> {filme1}</title>
</head>
<body bgcolor="black" text="white">
<center>
<font face="andalus"> <font color="red"><font color="blue"> <font size="5"> <h1> filme: {filme1}<br> </h1> </font> </font> </font></font>
</center>
<br>
<br><center>
<img src="{a}{url1}{b}" width="300" height="350"><p align="center">categorie : {cat1} <br> annee  : {ane1} <br></p><center></center>
<center>
<a href="{link1}">
  <img src="{a}{t}{b}" width="200" height="100" align="center">
</a>
<a href="{vlink1}">
  <img src="{a}{v}{b}" width="200" height="100" align="center">
</a></center>
</body>
</html>
                              
                              """+ "\n")
            with open(f"templates/{filme2}.html", "w") as f:
                f.write(f""" 
<html>
<head>
<title> {filme2}</title>
</head>
<body bgcolor="black" text="white">
<center>
<font face="andalus"> <font color="red"><font color="blue"> <font size="5"> <h1> filme: {filme2}<br> </h1> </font> </font> </font>
</center>
<br>
<br><center>
<img src="{a}{url2}{b}" width="300" height="350"><p align="center">categorie : {cat2} <br> annee  : {ane2} <br></p><center></center>
<center>
<a href="{link2}">
  <img src="{a}{t}{b}" width="200" height="100" align="center">
</a>
<a href="{vlink2}">
  <img src="{a}{v}{b}" width="200" height="100" height="100" align="center">
</a></center>
</body>
</html>
                              
                              """+ "\n")
            with open(f"templates/{filme3}.html", "w") as f:
                f.write(f""" 
<html>
<head>
<title> {filme3}</title>
</head>
<body bgcolor="black" text="white">
<center>
<font face="andalus"> <font color="red"> <font size="5"><font color="blue"> <h1> filme: {filme3}<br> </h1> </font> </font> </font></font>
</center>
<br>
<br><center>
<img src="{a}{url3}{b}" width="300" height="350"><p align="center">categorie : {cat3} <br> annee  : {ane3} <br></p><center></center>
<center>
<a href="{link3}">
  <img src="{a}{t}{b}" width="200" height="100" align="center">
</a>
<a href="{vlink3}">
  <img src="{a}{v}{b}" width="200" height="100" align="center">
</a></center>
</body>
</html>
                              
                              """+ "\n")
      
            f3="  "
            f4="    "
            with open("templates/home.html" ,"r") as f:
                lines = f.readlines()
                lines=lines + ["<br> <br>\n"]+[f"""<div style="display: flex; justify-content: center ; gap : 20px;">\n"""]+[f"   <a href='/{filme1}'>\n"]+[f"""     <img src="{a}{url1}{b}"width='300' height='300' align='left'>\n"""]+["   </a>\n"]+[f"   <a href='{filme2}'>\n"]+[f"""     <img src="{a}{url2}{b}"width="300" height="300" align="center">\n"""]+["   </a>\n"]+[f"   <a href='/{filme3}'>\n"]+[f"""     <img src="{a}{url3}{b}"width='300' height='300' align='right'>\n"""]+["   </a>\n"]+["</div>\n"]+["<center>\n"]+[f"""{n1}  &nbsp &nbsp &nbsp&nbsp&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp
{n2}&nbsp &nbsp &nbsp&nbsp&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp{n3} <br>\n"""]

            with open(f"templates/home.html" ,"w") as f:
                f.writelines(lines)
                 
           
            dz="    "                     
            with open(f"app.py", "r") as f:
                lines = f.readlines()
             
            if len (lines) >= 2:
               lines = lines [:-2] + [f"@app.route('/{filme1}') \n"]+[f"def {filme1}():\n"]+[f"{dz}return render_template('{filme1}.html')"]+[f"{dz}\n"]+lines[-2:]
            with open (f"app.py", "w") as f:
                f.writelines(lines)
         
            with open(f"app.py", "r") as f:
                lines = f.readlines()
             
            if len (lines) >= 2:
               lines = lines [:-2] + [f"@app.route('/{filme2}') \n"]+[f"def {filme2}():\n"]+[f"{dz}return render_template('{filme2}.html')"]+[f"{dz}\n"]+lines[-2:]
            with open (f"app.py", "w") as f:
                f.writelines(lines)  
         
            with open(f"app.py", "r") as f:
                lines = f.readlines()
             
            if len (lines) >= 2:
               lines = lines [:-2] + [f"@app.route('/{filme3}') \n"]+[f"def {filme3}():\n"]+[f"{dz}return render_template('{filme3}.html')"]+[f"{dz}\n"]+lines[-2:]
            with open (f"app.py", "w") as f:
                f.writelines(lines)                  
                             
      
      return '''<center> File uploaded successfully</center>
                 <a href="/home">
                    <center><input type="submit" value="log out"></center>
                 </a>
      
      
      
      
      '''
   else:
      return '''
<html>
   <body bgcolor="yellow" text="blue">
      <form  method = "POST"  enctype = "multipart/form-data">
      <font face="arial">
      <br>
      <hr color="green">
      <center> 
      <font color="red"> <font size="5"><h1> add filme page <br></h1></font></font>
      </center>
      <br>
      <hr color="green">
      <br>
      <br>
      <center>
      filme 1 : &nbsp &nbsp &nbsp&nbsp&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp  filme 2 : &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp  &nbsp&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp filme 3 :<br>
         </center>
         <center>
         <input type="text" name="filme1">&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp 
         <input type="text" name="filme2">&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp 
         <input type="text" name="filme3">
         </center>
         <br>
         <br> 
         <center>
         name fime 1  &nbsp &nbsp &nbsp&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp name filme 2  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp name filme 3<br>
         <input type="text" name="n1">&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp
         <input type="text" name="n2">&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp
         <input type="text" name="n3">
         </center>
         <br>
         <center>
         name image 1  &nbsp &nbsp &nbsp&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp name image 2   &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp name image 3<br>
         </center>
         <center>
         <input type="text" name="name1">&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp
         <input type="text" name="name2">&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp
         <input type="text" name="name3">
         </center>
         <br>
         <br>
         <center>
         image 1 : &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp&nbsp &nbsp &nbsp &nbsp &nbsp  image 2 : &nbsp &nbsp &nbsp &nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp&nbsp &nbsp &nbsp &nbsp &nbsp image 3 : <br>
         <input type = "file" name = "file" />
         <input type = "file" name = "file1" />
         <input type = "file" name = "file2" />
         </center>
         <br>
         <br>
         <center>
         link 1 : &nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp link 2 :  &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp link 3 : <br>
         </center>
         <center>
         <input type="text" name="link1">&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp
         <input type="text" name="link2">&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp
         <input type="text" name="link3">
         </center>
         <br>
         <br>
         <center>
         v link 1 : &nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp v link 2 :  &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp v link 3 : <br>
         <input type="text" name="vlink1">&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp
         <input type="text" name="vlink1">&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp
         <input type="text" name="vlink1">
         </center>
         <br>
         <br>
         <center>
         catigori 1 : &nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp catigori 2 :  &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp catigori 3 : <br>
         <input type="text" name="cat1">&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp
         <input type="text" name="cat2">&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp
         <input type="text" name="cat3">
         </center>
         <br>
         <br>
         <center>
         annee 1 : &nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp annee 2 :  &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp annee 3 : <br>
         <input type="text" name="ane1">&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp
         <input type="text" name="ane2">&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp
         <input type="text" name="ane3">
         
         <br>
         <br>
         <center>
         username:&nbsp&nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp password 1:&nbsp &nbsp&nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsppassword 2 :&nbsp&nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp password 3 : <br>
         </center>
         <center>
         <input type="text" name="username">
         <input type="password" name="password1">
         <input type="password" name="password2">
         <input type="password" name="password3"> 
         </center>
         <br>
         <br>
         <center><input type = "submit" value="add"></center>
         </font>
      </form>   
   </body>
</html>


      '''


@app.errorhandler(404)
def page404(e):
    return render_template('404.html'), 404   
  
 

   

  
 

@app.route('/kandahar') 
def kandahar():
    return render_template('kandahar.html')    
@app.route('/beekeeper') 
def beekeeper():
    return render_template('beekeeper.html')    
@app.route('/thefallgue') 
def thefallgue():
    return render_template('thefallgue.html')    
@app.route('/thecovenant') 
def thecovenant():
    return render_template('thecovenant.html')    
@app.route('/homestead') 
def homestead():
    return render_template('homestead.html')    
@app.route('/johnwick4') 
def johnwick4():
    return render_template('johnwick4.html')    
@app.route('/extraction') 
def extraction():
    return render_template('extraction.html')    
@app.route('/landofbad') 
def landofbad():
    return render_template('landofbad.html')    
@app.route('/The_MinistryofUngentlemanlyWarfare') 
def The_MinistryofUngentlemanlyWarfare():
    return render_template('The_MinistryofUngentlemanlyWarfare.html')    
 
 
if __name__ == '__main__': 
   app.run(host="0.0.0.0",port=80 ,debug=True)
