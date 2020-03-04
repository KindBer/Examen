from flask import Flask, render_template, request, jsonify, flash, json
from urllib.request import urlopen

import os, platform, logging

app = Flask(__name__)

#se hace el archivo log
if platform.platform().startswith('Windows'):
    fichero_log = os.path.join(os.getenv('HOMEDRIVE'), 
                               os.getenv("HOMEPATH"),
                               'test.json')
else:
    fichero_log = os.path.join(os.getenv('HOME'), 'test.json')
# se imprime la ruta
print('Archivo Log en ', fichero_log)
# se le da formato
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    filename = fichero_log,
                    filemode = 'w',)

#Settings
app.secret_key = 'mysecretkey'

@app.route('/')
def asegurado():
    return render_template('Asegurado.html')

@app.route('/empleado')
def empleado():
    return render_template('Empleado.html')

# @app.route('/add_empleado', methods=['POST'])
# def add_empleado():
#     if request.method == 'POST':
#         nombre = request.form['Nombre']
#         apellidos = request.form['Apellidos']
#         cedula = request.form['Cedula']
#         print(nombre)
#         print(apellidos)
#         print(cedula)
#         return 'received'


@app.route('/add_estudiante', methods=['POST'])
def add_estudiante():
    if request.method == 'POST':
        nombre = request.form['Nombre']
        apellidos = request.form['Apellidos']
        direccion = request.form['Direccion']
        carrera = request.form['Carrera']

        new_estudiante = {}
        new_estudiante['estudiante'] = []
        new_estudiante['estudiante'].append({"nombre": nombre, "apellidos": apellidos, "direccion": direccion, "carrera": carrera})
        
        logging.info('log_action:' + 'Post method/agregarEstudiante,' + 'parameters:' + str(new_estudiante) + ',' + 'Form: Estudiante.html' ) 
        
        #lee el json
        with open('estudiante.json') as f:
            data = json.load(f)

        # new_estudiante_str = str(new_estudiante)
        # data_str = str(data)
        # #mezclar los dos str
        # new_estudiante_str = new_estudiante_str + data_str
        # #convierte variables
        # estudiantes_str = json.dumps(new_estudiante_str)
        #escribe en el json

        estudiantes = str(new_estudiante) + str(data)

        with open('estudiante.json','w') as f:
            json.dump(estudiantes, f, indent=2) 
        flash('Contact Added Succesfully')
        return jsonify({"message": "Student Added Succesfully", "Estudiantes": new_estudiante})
        
@app.route('/add_empleado', methods=['POST'])
def add_empleado():
    if request.method == 'POST':
        nombre = request.form['Nombre']
        apellidos = request.form['Apellidos']
        cedula = request.form['Cedula']

        new_empleado = {}
        new_empleado['empleados'] = []
        new_empleado['empleados'].append({"nombre": nombre, "apellidos": apellidos, "cedula": cedula})

        logging.info('log_action:' + 'Post method/agregarEmpleado,' + 'parameters:' + str(new_empleado) + ',' + 'Form: Empleado.html' )

        #lee el json
        with open('empleado.json') as f:
            data = json.load(f)

        # new_empleado_str = str(new_empleado)
        # data_str = str(data)
        # #mezclar los dos str
        # new_empleado_str = new_empleado_str + data_str
        # #convierte variables
        # empleado_str = json.dumps(new_empleado_str)
        # #escribe en el json

        empleados = str(new_empleado) + str(data)   

        with open('empleado.json','w') as f:
            json.dump(empleados, f, indent=2) 
        flash('Contact Added Succesfully')
        return jsonify({"message": "Employee Added Succesfully", "Empleados": new_empleado})

@app.route('/add_asegurado', methods=['POST'])
def add_asegurado():
    if request.method == 'POST':
        nombre = request.form['Nombre']
        apellidos = request.form['Apellidos']
        cedula = request.form['Cedula']
        estado_civil = request.form['Estado']

        new_asegurado = {}
        new_asegurado ['asegurado'] = []

        new_asegurado['asegurado'].append({"nombre": nombre, "apellidos": apellidos, "cedula": cedula, "estado civil": estado_civil})
        #lee el json
        with open('asegurado.json') as f:
            data = json.load(f)

        # new_asegurado_str = str(new_asegurado)
        # data_str = str(data)
        # #mezclar los dos str
        # new_asegurado_str = new_asegurado_str + data_str
        # #convierte variables
        # asegurado_str = json.dumps(new_asegurado_str)
        # #escribe en el json

        asegurados = str(new_asegurado) + str(data)

        with open('asegurado.json','w') as f:
            json.dump(asegurados, f, indent=2) 
        flash('Contact Added Succesfully')
        return jsonify({"message": "Employee Added Succesfully", "Asegurados": new_asegurado})

@app.route('/add_empleado', methods=['GET'])
def get_empleado():
    #print (type(new_empleado))
    with open('empleado.json') as f:
        data = json.load(f)
    print(json.dumps(data, indent=2))
    return data

@app.route('/add_estudiante', methods=['GET'])
def get_estudiante():
    #print (type(new_empleado))
    with open('estudiante.json') as f:
        data = json.load(f)
    print(json.dumps(data, indent=2))
    return data

@app.route('/add_asegurado', methods=['GET'])
def get_asegurado():
    #print (type(new_empleado))
    with open('asegurado.json') as f:
        data = json.load(f)
    print(json.dumps(data, indent=2))
    return data

@app.route('/estudiante')
def estudiante():
    return render_template('Estudiante.html')

if __name__ == '__main__':
    app.run(debug=True)