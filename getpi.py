#coding:utf-8
import io

txt=""

with io.open("pi.txt","r",encoding="utf-8") as file: # Use file to refer to the file object
    data = file.read()
    i=data.find("Pi = 3.")
    if i>=0 :
        datas=data[i:].split("\n")
        for l in datas:
            ll=l.split(":")[0].strip()
            txt+=ll.replace(" ","")

f=io.open("npi.txt","w",encoding="utf-8")
f.write(txt)
f.close()

ttxt="""
<html>
    <head>
        <meta charset='utf-8'>
        <title>Le nombre Pi</title>
        <style>

body{
    text-align:center;
    font-size:20px;
    overflow-wrap: break-word;
}

        </style>
    <head>
    <body>
        <h1>Les """+str(len(txt)-5)+""" premieres décimales de pi : </h1>
        <div>
            <p>"""+txt+"""</p>
        </div>
    </body>
</html>

"""

f=io.open("npi.html","w",encoding="utf-8")
f.write(ttxt)
f.close()

