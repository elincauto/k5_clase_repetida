from flask import Flask

app = Flask(__name__)

#Vamos a definir un endpoint siempre a continuación de la función que tiene que actuar

@app.route('/')
def hello():
    return '''
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Mi primera página</title>
    </head>
    <body>
    <h1> Título de mi página </h1>
    <p> Hola mundo </p>
    </body>
    </html>

'''

@app.route('/adios')
def bye():
     return 'Adiós, mundo cruel'   