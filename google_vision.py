import re
import pprint
import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

path = 'data/'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.jpg' in file:
            files.append(os.path.join(r, file))
path = []
file_names= []
for f in files:
    path.append(f.split('/')[0]+ '/' + f.split('/')[1] + '/')
    file_names.append(f.split('/')[2].split('.')[0])

    
for counter, f in enumerate(files):
    
    # Loads the image into memory
    with io.open(f, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    doc_txt = open(path[counter] + "text.txt","w")
    doc_txt.write(texts[0].description)
    doc_txt.close()
    
    doc_desc = open(path[counter] + "desc.txt","w")

    for text in texts[1:]:
        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])
        doc_desc.write('\n"{}"'.format(text.description))
        doc_desc.write('bounds: {}'.format(','.join(vertices)))
    doc_desc.close()
    
    response = client.label_detection(image=image)
    labels = response.label_annotations
    doc_label = open(path[counter] + "label.txt","w")
    for label in labels:
        doc_label.write(label.description + ': '+ "{:.2f}".format(label.score) + '\n')
    doc_label.close()