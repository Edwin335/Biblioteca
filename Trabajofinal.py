from flask import Flask, request, redirect, url_for

import pymongo
from pymongo import MongoClient

app = Flask(__name__)

html ='''<html>
                  <head>
                      <meta charset="UTF-8">
                      <title>Login</title>
                      <link href="https://fonts.googleapis.com/css?family=Roboto&display=swap" rel="stylesheet">

                      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
                    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.bundle.min.js"></script>
                    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js">
                    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.0.3/css/font-awesome.css">
                      <link rel="stylesheet" type="text/css" href="static/css.css">
                      <style>
                            body {
                                  color: #000;
                                  overflow-x: hidden;
                                  height: 100%;
                                  background-image: url("https://images.pexels.com/photos/4862876/pexels-photo-4862876.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
                                  background-position: center;
                                  background-size: cover;
                                  background-repeat: no-repeat;
                                  
                                }

                            .card {
                                  padding: 30px 40px;
                                  margin-top: 60px;
                                  margin-bottom: 60px;
                                  border-radius: 20px 20px 20px 20px;
                                  box-shadow: 0 6px 12px 0 rgba(0, 0, 0, 0.2);
                                  background-color: rgba(255, 255, 255, 0.5);

                                }

                            .blue-text {
                                  color: #00BCD4;
                                }

                            .form-control-label {
                                  margin-bottom: 0;
                                }
                                

                            input,
                            textarea {
                                    padding: 8px 15px;
                                    border-radius: 5px !important;
                                    margin: 5px 0px;
                                    box-sizing: border-box;
                                    border: 1px solid #ccc;
                                    font-size: 18px !important;
                                    font-weight: 300;
                                    background-color: rgba(255, 255, 255, 0.3);

                                }

                            input:focus,
                            textarea:focus {
                                    -moz-box-shadow: none !important;
                                    -webkit-box-shadow: none !important;
                                    box-shadow: none !important;
                                    border: 1px solid #00BCD4;
                                    outline-width: 0;
                                    font-weight: 400;
                                }

                            .btn-block {
                                    text-transform: uppercase;
                                    font-size: 15px !important;
                                    font-weight: 400;
                                    height: 43px;
                                    cursor: pointer;

                                    padding: 8px 15px;
                                    border-radius: 5px !important;
                                    margin: 5px 0px;
                                    box-sizing: border-box;
                                    border: 1px solid #01bcb5;
                                    font-size: 18px !important;
                                    font-weight: 300;
                                    background-color: #01bcb5;
                                }

                            .btn-block:hover {
                                    color: #fff !important;
                                    background-color: #63c8c4 !important;
                                     border: 1px solid #63c8c4 !important;
                                }

                            button:focus {
                                    -moz-box-shadow: none !important;
                                    -webkit-box-shadow: none !important;
                                    box-shadow: none !important;
                                    outline-width: 0;
                                }
                            .inicio{
                                  border-radius: 20px 20px 20px 20px;
                                    font-size: 20px;
                                    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                                    color: white;
                                    background-image: url("https://images.pexels.com/photos/268832/pexels-photo-268832.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
                                    width: 100%;
                                    margin: 0;
                                    padding: 12.5%;
                                    height: 200px;
                                    justify-content: center; /* Centra horizontalmente */
                                    align-items: center; /* Centra verticalmente */
                                    margin-bottom: 25px;
                            }

                      </style>

                  </head>   
                  
                  <body>
                      <form method="post" action=".">
                          <div class="container-fluid px-1 py-5 mx-auto">
    <div class="row d-flex justify-content-center">
        <div class="col-xl-7 col-lg-8 col-md-9 col-11 text-center">
            
            <div class="card">
                <div class="inicio">
                <h3>Formulario</h3>
                <!-- <p class="white-text">Este es un formulario conectado a MondoDB Atlas.</p> -->
                </div>

                <form class="form-card" onsubmit="event.preventDefault()">
                    <div class="row justify-content-between text-left">
                        <div class="form-group col-sm-6 flex-column d-flex"> <label style="font-family: 'Roboto', sans-serif; font-size: 18px; font-weight: 400;" class="form-control-label px-3">Id del Libro<span class="text-danger"> *</span></label> <input style="border-bottom: 1px solid #ccc; border-top: none; border-left: none; border-right: none;" type="text" id="id" name="id" placeholder="Ingresa el id" onblur="validate(1)"> </div>
                        <div class="form-group col-sm-6 flex-column d-flex"> <label style="font-family: 'Roboto', sans-serif; font-size: 18px; font-weight: 400;" class="form-control-label px-3">Titulo del Libro<span class="text-danger"> *</span></label> <input style="border-bottom: 1px solid #ccc; border-top: none; border-left: none; border-right: none;" type="text" id="titulo" name="titulo" placeholder="Ingresa el titulo del libro" onblur="validate(2)"> </div>
                    </div>

                    <div class="row justify-content-center text-left">
                        <div class="form-group col-sm-6 flex-column d-flex"> <label style="font-family: 'Roboto', sans-serif; font-size: 18px; font-weight: 400;" class="form-control-label px-3">Autor del Libro<span class="text-danger"> *</span></label> <input style="border-bottom: 1px solid #ccc; border-top: none; border-left: none; border-right: none;" type="text" id="autor" name="autor" placeholder="ingresa el autor" onblur="validate(3)"> </div>
                        <div class="form-group col-sm-6 flex-column d-flex"> <label style="font-family: 'Roboto', sans-serif; font-size: 18px; font-weight: 400;" class="form-control-label px-3">Precio del Libro<span class="text-danger"> *</span></label> <input style="border-bottom: 1px solid #ccc; border-top: none; border-left: none; border-right: none;" type="text" id="precio" name="precio" placeholder="ingresa el precio" onblur="validate(4)"> </div>
                        <div class="form-group col-sm-6 flex-column d-flex"> <label style="font-family: 'Roboto', sans-serif; font-size: 18px; font-weight: 400;" class="form-control-label px-3">Cantidad<span class="text-danger"> *</span></label> <input style="border-bottom: 1px solid #ccc; border-top: none; border-left: none; border-right: none;" type="text" id="cantidad" name="cantidad" placeholder="ingresa la cantidad" onblur="validate(5)"> </div>
                    </div>
 
                    <div class="row justify-content-center">
                        <div class="form-group col-sm-6"> <button type="submit" class="btn-block btn-primary">AGREGAR LIBRO</button> </div>
                    </div>
                    
                </form>
                    
                <form class="form-card" method="get" action="/busca">
                    <div class="row justify-content-center">
                        <div class="form-group col-sm-6"> <button type="submit" class="btn-block btn-primary">BUSCAR LIBRO</button> </div>
                    </div>
                </form>

            </div>
        </div>
                      </form>


                  </body>
              </html>'''

client = pymongo.MongoClient("mongodb+srv://edwin:12345@example.hpmkvfw.mongodb.net/")
#client = pymongo.MongoClient("mongodb+srv://edwinjavierpabonrodriguez:edwin1234@cluster0.9plgztn.mongodb.net/")

db = client.libros
libros = db.libros

print(client.list_database_names())

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        id = request.form['id']
        titulo = request.form['titulo']
        autor = request.form['autor']
        precio = request.form['precio']
        cantidad = request.form['cantidad']


        libros.insert_one({
            '_id': id,
            'titulo': titulo,
            'autor': autor,
            'precio': precio,
            'cantidad': cantidad
        })
        return 'Se registro correctamente el libro'
    return html


@app.route('/busca')
def index():
    return '''
              <html>
                  <head>
                      <meta charset="UTF-8">
                      <title>Login</title>
                      <link href="https://fonts.googleapis.com/css?family=Roboto&display=swap" rel="stylesheet">

                      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
                    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.bundle.min.js"></script>
                    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js">
                    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.0.3/css/font-awesome.css">
                      <link rel="stylesheet" type="text/css" href="static/css.css">
                      <style>
                            body {
                                  color: #000;
                                  overflow-x: hidden;
                                  height: 100%;
                                  background-image: url("https://images.pexels.com/photos/4862876/pexels-photo-4862876.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
                                  background-position: center;
                                  background-size: cover;
                                  background-repeat: no-repeat;
                                  
                                }

                            .card {
                                  padding: 30px 40px;
                                  margin-top: 60px;
                                  margin-bottom: 60px;
                                  border-radius: 20px 20px 20px 20px;
                                  box-shadow: 0 6px 12px 0 rgba(0, 0, 0, 0.2);
                                  background-color: rgba(255, 255, 255, 0.5);

                                }

                            .blue-text {
                                  color: #00BCD4;
                                }

                            .form-control-label {
                                  margin-bottom: 0;
                                }
                                

                            input,
                            textarea {
                                    padding: 8px 15px;
                                    border-radius: 5px !important;
                                    margin: 5px 0px;
                                    box-sizing: border-box;
                                    border: 1px solid #ccc;
                                    font-size: 18px !important;
                                    font-weight: 300;
                                    background-color: rgba(255, 255, 255, 0.3);

                                }

                            input:focus,
                            textarea:focus {
                                    -moz-box-shadow: none !important;
                                    -webkit-box-shadow: none !important;
                                    box-shadow: none !important;
                                    border: 1px solid #00BCD4;
                                    outline-width: 0;
                                    font-weight: 400;
                                }

                            .btn-block {
                                    text-transform: uppercase;
                                    font-size: 15px !important;
                                    font-weight: 400;
                                    height: 43px;
                                    cursor: pointer;

                                    padding: 8px 15px;
                                    border-radius: 5px !important;
                                    margin: 5px 0px;
                                    box-sizing: border-box;
                                    border: 1px solid #01bcb5;
                                    font-size: 18px !important;
                                    font-weight: 300;
                                    background-color: #01bcb5;
                                }

                            .btn-block:hover {
                                    color: #fff !important;
                                    background-color: #63c8c4 !important;
                                     border: 1px solid #63c8c4 !important;
                                }

                            button:focus {
                                    -moz-box-shadow: none !important;
                                    -webkit-box-shadow: none !important;
                                    box-shadow: none !important;
                                    outline-width: 0;
                                }
                            .inicio{
                                  border-radius: 20px 20px 20px 20px;
                                    font-size: 20px;
                                    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                                    color: white;
                                    background-image: url("https://images.pexels.com/photos/268832/pexels-photo-268832.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
                                    width: 100%;
                                    margin: 0;
                                    padding: 12.5%;
                                    height: 200px;
                                    justify-content: center; /* Centra horizontalmente */
                                    align-items: center; /* Centra verticalmente */
                                    margin-bottom: 25px;
                            }

                      </style>

                  </head>   
                  
                  <body>
    <form class="form-card" method="get" action="/result">
        <div class="container-fluid px-1 py-5 mx-auto">
            <div class="row d-flex justify-content-center">
                <div class="col-xl-7 col-lg-8 col-md-9 col-11 text-center">
                    <div class="card">
                    <center>
                        <div class="inicio">
                            <h3>Buscar</h3>
                        </div>

                        <div class="row justify-content-between text-left">
                            <div class="form-group col-sm-6 flex-column d-flex ">
                            <center>
                                <label style="font-family: 'Roboto', sans-serif; font-size: 18px; font-weight: 400; display: flex; justify-content: center;" class="form-control-label px-3">Ingrese el ID del libro:<span class="text-danger"> *</span></label>
                                <input style="border-bottom: 1px solid #ccc; border-top: none; border-left: none; border-right: none; display: block; margin: 0 auto;" type="text" name="id" placeholder="Ingresa el id" onblur="validate(1)">
                            </center>
                            </div>
                        </div>

                        <div class="row justify-content-center">
                            <div class="form-group col-sm-6">
                                <button type="submit" value="Buscar" class="btn-block btn-primary">Buscar</button>            
                            </div>
                        </div>
                    </center>    
                    </div>
                </div>
            </div>
        </div>
    </form>


</body>
              </html>
           '''

@app.route('/result')
def result():
    id = request.args.get('id')
    result = libros.find_one({'_id': id})
    if result:
        return f'''
                      <html>
                  <head>
                      <meta charset="UTF-8">
                      <title>Login</title>
                      <link href="https://fonts.googleapis.com/css?family=Roboto&display=swap" rel="stylesheet">

                      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
                      <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.bundle.min.js"></script>
                      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js">
                      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.0.3/css/font-awesome.css">
                      <link rel="stylesheet" type="text/css" href="static/css.css">
                  </head>   
                  
                  <body style="color: #000;
                                  overflow-x: hidden;
                                  height: 100%;
                                  background-image: url('https://images.pexels.com/photos/4862876/pexels-photo-4862876.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1');                       
                                  background-position: center;
                                  background-size: cover;
                                  background-repeat: no-repeat;">

                  <div class="card" style="padding: 30px 40px;
                                 font-size: 25px !important;
                                  margin-top: 60px;
                                  margin-bottom: 60px;
                                  margin-left: 200px;
                                  margin-right: 200px;
                                  border-radius: 20px 20px 20px 20px;
                                  box-shadow: 0 6px 12px 0 rgba(0, 0, 0, 0.2);
                                  background-color: rgba(255, 255, 255, 0.5);">

                    <form class="form-card" method="get" action="/elimina">    

                        <div class="inicio" style="border-radius: 20px 20px 20px 20px;
                            font-size: 20px;
                            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                            color: white;
                            background-image: url('https://images.pexels.com/photos/268832/pexels-photo-268832.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1');
                            width: 100%;
                            margin: 0;
                            padding: 12.5%;
                            height: 200px;
                            justify-content: center; /* Centra horizontalmente */
                            align-items: center; /* Centra verticalmente */
                            margin-bottom: 25px;">
                            <center>
                            <h1>Resultado de la Busqueda</h1>
                            </center>
                        </div>

                     <center>   
                    <div style="padding: 30px 40px;
                    margin-top: 60px;
                    margin-bottom: 60px;
                    margin-left: 120px;
                    margin-right: 120px;
                    border-radius: 20px;
                    
                    background-color: rgba(255, 255, 255, 0.5);">
                    <table>
                    <center>
                        <thead>
                            <tr>
                            <th>ID</th>
                            <th>TITULO</th>
                            <th>AUTOR</th>
                            <th>PRECIO</th>
                            <th>CANTIDAD</th>
                            </tr>
                        </thead>

                        <tr>
                            <td><input style="background-color: transparent; width: 100px; display: inline-block; margin-right: 10px; border-bottom: none; border-top: none; border-left: none; border-right: none;" type="text" name="id" placeholder="{result['_id']}" onblur="validate(1)" value="{ result['_id'] }" readonly></td>
                            <td><input style="background-color: transparent; width: 100px; display: inline-block; margin-right: 10px; border-bottom: none; border-top: none; border-left: none; border-right: none;" type="text" name="id" placeholder="{result['titulo']}" onblur="validate(2)" value="{ result['titulo'] }" readonly></td>
                            <td><input style="background-color: transparent; width: 100px; display: inline-block; margin-right: 10px; border-bottom: none; border-top: none; border-left: none; border-right: none;" type="text" name="id" placeholder="{result['autor']}" onblur="validate(3)" value="{ result['autor'] }" readonly></td>
                            <td><input style="background-color: transparent; width: 100px; display: inline-block; margin-right: 10px; border-bottom: none; border-top: none; border-left: none; border-right: none;" type="text" name="id" placeholder="{result['precio']}" onblur="validate(4)" value="{ result['precio'] }" readonly></td>
                            <td><input style="background-color: transparent; width: 100px; display: inline-block; border-bottom: 1px none; border-top: none; border-left: none; border-right: none;" type="text" name="id" placeholder="{result['cantidad']}" onblur="validate(5)" value="{ result['cantidad'] }" readonly></td>
                        </tr>
                    </table>
                    <button type="submit" value="Eliminar" style="width: 150px; margin-top: 60px; background: red; color: white; border: none;">Eliminar</button>
                    

                    </div>
                    </center>   

                    </form>


                  </div>

                  </body>
              </html>

               
               '''
    else:
        return "No se encontró ningún libro con ese ID."
    

@app.route('/elimina')
def elimina():
    id = request.args.get('id')
    elimina = libros.delete_one({'_id': id})
    if elimina:
        return redirect(url_for('login'))
    else:
        return "No se encontró ningún libro con ese ID."

if __name__ == '__main__':
    app.run(port=19000)
