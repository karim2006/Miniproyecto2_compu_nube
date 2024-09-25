from gluoncv.model_zoo import get_model
import matplotlib.pyplot as plt
from mxnet import gluon, nd, image
from mxnet.gluon.data.vision import transforms
from gluoncv import utils
from PIL import Image
import io
import flask

app = flask.Flask(_name_)

@app.route("/predict", methods=["POST"])
def predict():
    if flask.request.method == "POST":
        if flask.request.files.get("img"):
            try:
                # Leer la imagen desde el archivo cargado
                img = Image.open(io.BytesIO(flask.request.files["img"].read()))

                # Preprocesar la imagen
                transform_fn = transforms.Compose([
                    transforms.Resize(32),
                    transforms.CenterCrop(32),
                    transforms.ToTensor(),
                    transforms.Normalize([0.4914, 0.4822, 0.4465], [0.2023, 0.1994, 0.2010])
                ])
                img = transform_fn(nd.array(img))

                # Cargar el modelo preentrenado
                net = get_model('cifar_resnet20_v1', classes=10, pretrained=True)

                # Realizar predicción
                pred = net(img.expand_dims(axis=0))
                class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
                               'dog', 'frog', 'horse', 'ship', 'truck']
                ind = nd.argmax(pred, axis=1).astype('int')
                prediction = ('The input picture is classified as [%s], with probability %.3f.' %
                             (class_names[ind.asscalar()], nd.softmax(pred)[0][ind].asscalar()))

                return prediction

            except Exception as e:
                return f"Error processing image: {str(e)}", 400

    return "No image uploaded", 400

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
