import os, io
from google.cloud import vision
from google.cloud.vision import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'./keys/gvison-keys.json'

def starter(path):

    client = vision.ImageAnnotatorClient()
 
    if path.startswith('http') or path.startswith('gs:'):
        image = types.Image()
        image.source.image_uri = path
    else:
        with io.open(path, 'rb') as image_file:
            content = image_file.read()
        image = types.Image(content=content)
 
    result = client.face_detection(image=image).face_annotations
 
    return result

face_file = '/home/hg/Desktop/MyCode/gvison/faces/url-shortenerheyeEconomie__Immigration.png'



faceesdetailes = starter(face_file)
print(faceesdetailes)

likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')

i=1
for f in faceesdetailes:
    print('Face nomber {}'.format(i))
    print('Joy : {}'.format(likelihood_name[f.joy_likelihood]))
    print('Sorrow : {}'.format(likelihood_name[f.sorrow_likelihood]))
    print('Anger : {}'.format(likelihood_name[f.anger_likelihood]))
    print('Surprise : {}'.format(likelihood_name[f.surprise_likelihood]))
    i=i+1
    

iter(faceesdetailes)
print((iter(faceesdetailes)).next())
