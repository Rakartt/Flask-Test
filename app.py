from flask import Flask, jsonify
import boto3

app = Flask(__name__)

# Crear cliente S3 usando boto3
s3 = boto3.client('s3')

# Ruta para devolver la lista de buckets en viñetas HTML
@app.route('/')
def list_buckets_html():
    response = s3.list_buckets()
    buckets = response['Buckets']
    
    # Plantilla HTML para mostrar los buckets
    html = '''
    <html>
    <head>
        <title>Lista de Buckets</title>
    </head>
    <body>
        <h1>Lista de Buckets en S3</h1>
        <ul>
            {% for bucket in buckets %}
                <li>{{ bucket.Name }}</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    '''
    
    return render_template_string(html, buckets=buckets)

# Ruta para devolver la lista de buckets como JSON
@app.route('/json')
def list_buckets_json():
    response = s3.list_buckets()
    bucket_names = [bucket['Name'] for bucket in response['Buckets']]
    return jsonify(bucket_names)

if __name__ == '__main__':
    # Ejecutar la aplicación Flask en el puerto 5000
    app.run(host='0.0.0.0', port=5000, debug=True)