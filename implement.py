from flask import Flask,render_template,request
import numpy as np
from urllib.parse import * 
import tldextract
import re
import joblib

app=Flask(__name__)
@app.route("/")
def temp():
    return render_template("index.html")

@app.route("/pred",methods=["POST"])
def pred():
    if request.method=="POST":
        x=request.form["url"]
        cur=[]
        cur.append(x.count('.'))
        cur.append(x.count('-'))
        cur.append(x.count('_'))
        cur.append(x.count('/'))
        cur.append(x.count('?'))
        cur.append(x.count('='))
        cur.append(x.count('@'))
        cur.append(x.count('&'))
        cur.append(x.count('!'))
        cur.append(x.count(' '))
        cur.append(x.count('~'))
        cur.append(x.count(','))
        cur.append(x.count('+'))
        cur.append(x.count('*'))
        cur.append(x.count('#'))
        cur.append(x.count('$'))
        cur.append(x.count('%'))
        cur.append(len(x))
        l=tldextract.extract(x)
        cur.append(len(l[2]))
        if (urlparse(x).scheme).lower()=='http':
            cur.append(1)
        else:
            cur.append(0)
        if (urlparse(x).scheme).lower()=='https':
            cur.append(1)
        else:
            cur.append(0)
        if urlparse(x).port:
            cur.append(1)
        else:
            cur.append(0)
        if urlparse(x).query:
            cur.append(1)
        else:
            cur.append(0)
        dom=urlparse(x).netloc
        cur.append(dom.count('.'))
        cur.append(dom.count('-'))
        cur.append(dom.count('_'))
        cur.append(dom.count('/'))
        cur.append(dom.count('?'))
        cur.append(dom.count('='))
        cur.append(dom.count('@'))
        cur.append(dom.count('&'))
        cur.append(dom.count('!'))
        cur.append(dom.count(' '))
        cur.append(dom.count('~'))
        cur.append(dom.count(','))
        cur.append(dom.count('+'))
        cur.append(dom.count('*'))
        cur.append(dom.count('#'))
        cur.append(dom.count('$'))
        cur.append(dom.count('%'))
        cur.append(len(dom))
        pattern=re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
        res=pattern.match(dom)
        if res:
            cur.append(1)
        else:
            cur.append(0)
        p=urlparse(x).path
        cur.append(p.count('.'))
        cur.append(p.count('-'))
        cur.append(p.count('_'))
        cur.append(p.count('/'))
        cur.append(p.count('?'))
        cur.append(p.count('='))
        cur.append(p.count('@'))
        cur.append(p.count('&'))
        cur.append(p.count('!'))
        cur.append(p.count(' '))
        cur.append(p.count('~'))
        cur.append(p.count(','))
        cur.append(p.count('+'))
        cur.append(p.count('*'))
        cur.append(p.count('#'))
        cur.append(p.count('$'))
        cur.append(p.count('%'))
        cur.append(len(p))
        par=urlparse(x).params
        cur.append(par.count('.'))
        cur.append(par.count('-'))
        cur.append(par.count('_'))
        cur.append(par.count('/'))
        cur.append(par.count('?'))
        cur.append(par.count('='))
        cur.append(par.count('@'))
        cur.append(par.count('&'))
        cur.append(par.count('!'))
        cur.append(par.count(' '))
        cur.append(par.count('~'))
        cur.append(par.count(','))
        cur.append(par.count('+'))
        cur.append(par.count('*'))
        cur.append(par.count('#'))
        cur.append(par.count('$'))
        cur.append(par.count('%'))
        cur.append(len(par))
        df=[]
        df.append(cur)
        dtc=joblib.load('dtc.pkl')
        res=dtc.predict(df)
        if res==1:
            a="Phishing URL"
        else:
            a="Legitimate URL"
        return render_template("index.html",data=a)

     
if __name__=="__main__":
    app.run(port=3000,debug=True)