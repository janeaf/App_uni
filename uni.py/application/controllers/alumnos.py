import web  # pip install web.py
import appi  # CSV parser
import json  # json parser

'''
    Controller Alumnos que es invocado cuando el usuario ingrese a la 
    URL: http://localhost:8080/alumnos?action=get&token=1234
'''


class Alumnos:

    app_version = "0.01p"  # version de la webapp
    file = 'static/csv/alumnos.csv'  # define el archivo donde se almacenan los datos

    def __init__(self):  # Método inicial o constructor de la clase
        pass  # Simplemente continua con la ejecución

    def GET(self):
        try:
            data = web.input()  # recibe los datos por la url
            if data['token'] == "1234":  # valida el token que se recibe por url
                if data['action'] == 'get':  # evalua la acción a realizar
                    result = self.actionGet(self.app_version, self.file)  # llama al metodo actionGet(), y almacena el resultado
                    return json.dumps(result)  # Parsea el diccionario result a formato json
                else:
                    result = {}  # crear diccionario vacio
                    result['app_version'] = self.app_version  # version de la webapp
                    result['status'] = "Command not found"
                    return json.dumps(result)  # Parsea el diccionario result a formato json
            else:
                result = {}  # crear diccionario vacio
                result['app_version'] = self.app_version  # version de la webapp
                result['status'] = "Invalid Token"
                return json.dumps(result)  # Parsea el diccionario result a formato json
        except Exception as e:
            print("Error")
            result = {}  # crear diccionario vacio
            result['app_version'] = self.app_version  # version de la webapp
            result['status'] = "Values missing, sintaxis: alumnos?action=get&token=XXXX"
            return json.dumps(result)  # Parsea el diccionario result a formato json

    @staticmethod
    def actionGet(app_version, file):
        try:
            result = {}  # crear diccionario vacio
            result['app_version'] = app_version  # version de la webapp
            result['status'] = "200 ok"  # mensaje de status
            
            with open(file, 'r') as csvfile:  # abre el archivo en modo lectura
                reader = csv.DictReader(csvfile)  # toma la 1er fila para los nombres
                alumnos = []  # array para almacenar todos los alumnos
                for row in reader:  # recorre el archivo CSV fila por fila
                    fila = {}  # Genera un diccionario por cada registro en el csv
                    fila['matricula'] = row['matricula']  # obtiene la matricula y la agrega al diccionario
                    fila['nombre'] = row['nombre']  # optione el nombre y lo agrega al diccionario
                    fila['primer_apellido'] = row['primer_apellido']  # optiene el primer_apellido
                    fila['segundo_apellido'] = row['segundo_apellido']  # optiene el segundo apellido
                    fila['carrera'] = row['carrera']  # obtiene la carrera
                    alumnos.append(fila)  # agrega el diccionario generado al array alumnos
                result['alumnos'] = alumnos  # agrega el array alumnos al diccionario result
            return result  # Regresa el diccionario generado
        except Exception as e:
            result = {}  # crear diccionario vacio
            print("Error {}".format(e.args()))
            result['app_version'] = app_version  # version de la webapp
            result['status'] = "Error "  # mensaje de status
            return result  # Regresa el diccionario generado
