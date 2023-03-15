from flask import Flask, render_template, request #pip install flask
from forms import DefectForm
import pandas as pd


app = Flask(__name__,template_folder='templates')
app.config['SECRET_KEY'] = 'randomNumber'



@app.route('/', methods=['GET', 'POST'])
def defect():
    form = DefectForm()
    if form.is_submitted():
        dfCsv = pd.read_csv('C:/Users/Pierluigi/Documents/Python Scripts/flaskWebApp/dfCsv.csv') #link has to be adjusted
        dfCsv = pd.DataFrame(dfCsv)
        result = request.form
        df = pd.DataFrame(list(result.items(1)),columns = 
        ['title','content'])
        dfT = df.transpose()
        dfT.columns = dfT.iloc[0]
        dfT = dfT.reset_index().drop(index=0)
        dfT = dfT.reset_index()
        dfT.drop(axis = 1, columns=['level_0','index', 'submit'], inplace=True)
        #print(dfT)
        #if dfCsv.empty():
        #dfCsv = dfCsv.append(dfT)
        dfCsv = pd.concat([dfCsv, dfT], axis = 0, ignore_index=True)
        ##dfCsv = dfT #to create table
        dfCsv = dfCsv.reset_index()
        dfCsv.drop(axis = 1, columns=['index'], inplace=True)
        try:
            dfCsv.drop(axis = 1, columns=['Unnamed: 0'], inplace=True)
        except:
            print('ok')
        dfCsv.to_csv('C:/Users/Pierluigi/Documents/Python Scripts/flaskWebApp/dfCsv.csv') #link has to be adjusted

    return render_template('form.html', form = form)

if __name__ =='__main__':
    app.run()