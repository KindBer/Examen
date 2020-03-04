from flask import Flask, render_template, request, jsonify, flash, json
from urllib.request import urlopen

app = Flask(__name__)

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



@app.route('/add_empleado', methods=['POST'])
def add_empleado():
    if request.method == 'POST':
        nombre = request.form['Nombre']
        apellidos = request.form['Apellidos']
        cedula = request.form['Cedula']
        new_empleado = [{"nombre": nombre, "apellidos": apellidos, "cedula": cedula}]
        #lee el json
        with open('empleado.json') as f:
            data = json.load(f)

        #convertir los objetos en str
        new_empleado_str = str(new_empleado)
        data_str = str(data)

        #mezclar los dos str
        new_empleado_str = new_empleado_str + data_str

        #agregar al json
        empleado_str = json.dumps(new_empleado_str)
        print(json.dumps(empleado_str, indent=2))
        with open('empleado.json','w') as f:
            json.dump(empleado_str, f, indent=2) 
        flash('Contact Added Succesfully')
        return jsonify({"message": "Employee Added Succesfully", "Empleados": new_empleado})


@app.route('/add_empleado', methods=['GET'])
def get_empleado():
    #print (type(new_empleado))
    with open('empleado.json') as f:
        data = json.load(f)
    print(json.dumps(data, indent=2))
    return data

@app.route('/estudiante')
def estudiante():
    return render_template('Estudiante.html')

if __name__ == '__main__':
    app.run(debug=True)