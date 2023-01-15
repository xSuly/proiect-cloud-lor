from flask import Flask, jsonify, render_template, request, redirect
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import subprocess
from PIL import Image

connection_string = "DefaultEndpointsProtocol=https;AccountName=storagelorctivideo;AccountKey=pdRnraSCZZ99egTVjciVus8RIUUwVxbTxFcYTEE7O0GIDExU+sHS+S7OW1u5gpcJppXR2m7AXGja+AStgX4I5A==;EndpointSuffix=core.windows.net"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)


app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey123"

@app.route("/")  # this sets the route to this page
def home():
        return render_template('index.html')

@app.route("/", methods=['POST'])
def upload():
        file = request.files['file']
        email = request.form['email']
        with open("/var/www/uploads/emailurile_kober.txt", "w") as kober:
                kober.write(str(email))
        file.save ("/var/www/uploads/data/inputs/cocos_spatiu.mp4")
        #file.save ("/var/www/uploads/data/file.mp4")
        container_name = "videoclipzlorcti"

        container_client = blob_service_client.get_container_client(container_name)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file.filename)
        with open("/var/www/uploads/data/inputs/cocos_spatiu.mp4", "rb") as data:
                blob_client.upload_blob(data)



#       container_client = blob_service_client.get_container_client(container_name)
#       blob_client = container_client.get_blob_client(file.filename)



        #with open('/var/www/uploads/nume_fisier.txt', 'w') as f:
                #f.write(str(file.filename))


#       blob_client.upload_blob(file.filename)
        rulare_script = subprocess.check_output(["python3", "/var/www/uploads/1_thumbs.py"])
        rulare_email = subprocess.check_output(["python3", "/var/www/uploads/email_server.py"])
        rulare_queue = subprocess.check_output(["python3", "/var/www/uploads/queue_service.py"])
        rulare_bazadate = subprocess.check_output(["python3", "/var/www/uploads/baza_date.py"])
        
        
        #test.open("/var/www/uploads/data/outputs/thumbnails/5.jpg")
        #im = Image.open("/var/www/uploads/data/outputs/thumbnails/5.jpg")
        #cale = '/var/www/uploads/data/outputs/thumbnails/5.jpg'
        #nume_container = 'thumbnail1.jpg'
        ###blob_service = BlockBlobService(connection_string='DefaultEndpointsProtocol=https;AccountName=storagelorctivideo;AccountKey=pdRnraSCZZ99egTVjciVus8RIUUwVxbTxFcYTEE7O0GIDExU+sHS+S7OW1u5gpcJppXR2m7AXGja+AStgX4I5A==;EndpointSuff>        ###blob_service.create_blob_from_path(container_name, nume_container, cale)
        #with open(file.filename, "rb") as data:
                #blob_client.upload_blob(data)
        with open('/var/www/uploads/fisier_nume.txt', 'r') as f:
                numar_container = int(f.readline())

        numar_container = numar_container - 1
        with open("/var/www/uploads/data/outputs/thumbnails/" + str(numar_container) + ".jpg", "rb") as coco:
                container_client.upload_blob("thumbnailul" + str(numar_container) + ".jpg", coco)

        urlhtml= ("https://storagelorctivideo.blob.core.windows.net/videoclipzlorcti/thumbnailul" + str(numar_container)  + ".jpg")
        return render_template('succesul.html', string_to_show = urlhtml)

if __name__ == "__main__":
    app.run()
