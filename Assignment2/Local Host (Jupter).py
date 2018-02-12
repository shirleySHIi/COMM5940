
# coding: utf-8

# In[ ]:


import os
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.wrappers import Request, Response
from flask import Flask, render_template

app = Flask(__name__)
root_path = os.path.sep.join(app.instance_path.split(os.path.sep)[:-1])
@app.route("/")

def result():
    ta_name = ["Mary","Jack","Tom","Jerry","Lily"]
    ta_rate = [30,40,40,50,60]
    ta_hours = [10,11,12,13,14]
  
    index = 0
    output = []
  
    for x in ta_name:
        name = ta_name[index]
        hours = ta_hours[index]
        rate = ta_rate[index]
        
        index = index + 1
        ta_fees = name + ' has received $' + str(hours * rate) + '.'
        
        output.append(ta_fees)
    
    that = dict(zip(ta_name,output))
    return render_template('result.html', result = that)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
        '/static': root_path+'/static',
        '/templates': root_path+'/templates'
     })
    run_simple('localhost', 9000, app)

