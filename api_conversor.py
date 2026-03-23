from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convertir-temperatura', methods=['POST'])
def convertir():
    datos = request.get_json()
    
    # Validamos que nos envíen lo necesario
    if not datos or 'valor' not in datos or 'escala' not in datos:
        return jsonify({"error": "Faltan datos (valor numérico o escala 'C' / 'F')"}), 400
        
    valor = float(datos['valor']) # Aseguramos que sea un número
    escala = datos['escala'].upper() # Convertimos a mayúscula por si envían "c" o "f"
    
    if escala == 'C':
        # Convertir de Celsius a Fahrenheit
        resultado_fahrenheit = (valor * 9/5) + 32
        respuesta = {
            "valor_original": valor,
            "escala_original": "Celsius",
            "resultado": resultado_fahrenheit,
            "escala_resultado": "Fahrenheit"
        }
    elif escala == 'F':
        # Convertir de Fahrenheit a Celsius
        resultado_celsius = (valor - 32) * 5/9
        # Redondeamos a 2 decimales para que se vea mejor
        resultado_celsius = round(resultado_celsius, 2) 
        respuesta = {
            "valor_original": valor,
            "escala_original": "Fahrenheit",
            "resultado": resultado_celsius,
            "escala_resultado": "Celsius"
        }
    else:
        return jsonify({"error": "Escala no válida. Usa 'C' o 'F'"}), 400
        
    return jsonify(respuesta), 200

if __name__ == '__main__':
    # Usamos el puerto 5001 para que no choque si el otro servidor sigue corriendo
    app.run(debug=True, port=5001)