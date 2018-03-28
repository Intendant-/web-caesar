from flask import Flask, request
from caesar import rotate_string

app =  Flask(__name__)
app.config['DEBUG'] = True
form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method="POST" >
            <label for="rot" >Rotate by</label>
            <input name="rot" value=0 >
            <textarea name="text" id="" cols="30" rows="10">{0}</textarea>
            <input type="submit" value="Submit" >
        </form>
    </body>
</html>"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rotate = int(request.form['rot'])
    cypher = request.form['text']

    ##return "<h1>"rotate_string(cypher, rotate)"</h1>"
    return form.format(rotate_string(cypher, rotate))



app.run()