from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import glob

# silence tensorflow
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # or any {'0', '1', '2'}
# download nltk_data to /tmp
os.environ["NLTK_DATA"] = "/tmp"

from madochan.generator import Madochan
import tensorflow as tf

BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
MODEL_DIR = f"{BASE_DIR}/madochan/models"

app = FastAPI()


def allow_cors(app):
    # https://fastapi.tiangolo.com/tutorial/cors/
    origins = [
        "*",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


allow_cors(app)

base_route = ""
api_base = base_route + "/api/v1"


def models():
    return [os.path.basename(f) for f in glob.glob(f"{MODEL_DIR}/*.h5")]


def load_model(modelfile):
    return tf.keras.models.load_model(f"{MODEL_DIR}/{modelfile}", compile=False)


@app.get(api_base + "/settings")
async def get_settings():
    return {
        "model": models(),
        "weirdness": [1, 2, 3],
    }



@app.post(api_base + "/_create_word")
async def list_tags_prefixes(data: dict):
    model = data.get('model', None)
    definition = data.get('definition', None)
    if not definition:
        return {"word": ""}

    gen = Madochan()
    gen.weirdness = data.get('weirdness', 1) or 1
    if model:
        gen.change_model(load_model(model))
    new_word = gen.create_word(definition)
    return {"word": new_word}
