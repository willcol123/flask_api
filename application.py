from flask import Flask, request, render_template, redirect, json
from keras.saving.save import load_model
import numpy as np

def Modelo(A,V,T,P):
        #Normalizacao dos inputs
        An=(A-800)/(3000-800)
        Vn=(V-0.1)/(0.9-0.1)
        Tn=(T-297)/(345-297)
        Pn=(P)/(40)
        print(modelo.predict(np.array([[An,Vn,Tn,Pn]]))[0][0])
        
        return modelo.predict(np.array([[An,Vn,Tn,Pn]]))[0][0]



P=[]
for i in range(1,21,1):
        P.append(i)

def Modelo_list(A,V,T):
        saida=[]
        for p in P:
                saida.append(Modelo(A,V,T,p))
        return saida




modelo=load_model(r"Model\Exemplo.h5")


application = Flask(__name__)

@application.route('/index')
def index():
	return "Teste Python"


@application.route('/form')
def form():
    return render_template('base.html',var1=[0,1,23,4])

@application.route('/', methods=('GET', 'POST'))
def api():

        if request.method=='POST':
                area = float(request.form['area'])
                temperatura = float(request.form['temperatura'])
                volume = float(request.form['volume'])
                #x=np.array([['area','vol','T','Pressão']]])
                #out=modelo.predict(x)
                
                return render_template('grafico.html',var1=json.dumps(P),var2=str(Modelo_list(area,volume,temperatura)))
        return render_template('api.html')





if __name__=="__main__":
	application.run(host='0.0.0.0')

