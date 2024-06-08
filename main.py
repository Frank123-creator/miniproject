from flask import Flask, render_template, request, redirect, url_for
from seleniumrun import search
from emptyfield import Validate_form
app = Flask(__name__,template_folder='template')

@app.route('/', methods=['GET', 'POST'])
def index():
    error1=""
    error2=""
    if request.method == 'POST':
         error1,error2=Validate_form(request.form)
         if not error1 and not error2:
            search_query1 = request.form.get('search_query1')
            result1 = search(search_query1)
            search_query2 = request.form.get('search_query2')
            result2 = search(search_query2)
            return render_template('project.html', result1=result1,result2=result2)
    return render_template('project.html',error1=error1,error2=error2)

if __name__ == '__main__':
    app.run(debug=True)
