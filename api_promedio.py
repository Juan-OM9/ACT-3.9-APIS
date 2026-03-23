from flask import Flask, request, jsonify # [cite: 38]

app = Flask(__name__) # [cite: 44]

@app.route('/promedio', methods=['POST']) # [cite: 48, 51, 82]
def calcular_promedio(): # [cite: 49]
    datos = request.get_json() # [cite: 56, 83]
    
    # Validaciones extra
    if not datos or 'nombre' not in datos or 'calificaciones' not in datos:
        return jsonify({"error": "Faltan datos (nombre o calificaciones)"}), 400
        
    nombre = datos['nombre'] # [cite: 59, 84]
    calificaciones = datos['calificaciones'] # [cite: 60, 84]
    
    # Verificamos que la lista no esté vacía para no dividir entre 0
    if len(calificaciones) == 0:
        return jsonify({"error": "La lista de calificaciones está vacía"}), 400

    promedio = sum(calificaciones) / len(calificaciones) # [cite: 66, 85]
    
    respuesta = { # [cite: 72, 86]
        "nombre": nombre, # [cite: 73, 87]
        "promedio": promedio # [cite: 74, 88]
    } # [cite: 75, 89]
    
    return jsonify(respuesta), 200 # [cite: 77, 90]

if __name__ == '__main__': # [cite: 91, 92, 93]
    app.run(debug=True) # [cite: 94]