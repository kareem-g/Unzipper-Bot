# Copyright (c) 2022 Itz-fork

import os

class Config(object):
    # Mandotory
    # APP_ID = int(os.environ.get("13217624"))
    APP_ID = int("13217624")
    # API_HASH = os.environ.get("85574fd1683b9e164fec4636b91c06ec")
    API_HASH = "85574fd1683b9e164fec4636b91c06ec"
    # BOT_TOKEN = os.environ.get("6323595055:AAEOct-YYQfky_PEo9HC59_bnmnnjMslmSM")
    BOT_TOKEN = "6323595055:AAEOct-YYQfky_PEo9HC59_bnmnnjMslmSM"
    # LOGS_CHANNEL = int(os.environ.get("-1001903078222"))
    LOGS_CHANNEL = int("-1001903078222")
    # BOT_OWNER = int(os.environ.get("890698327"))
    BOT_OWNER = int("890698327" )
    # MONGODB_URL = os.environ.get("mongodb+srv://kareem:Kareem<3hanona@cluster0.eouty5b.mongodb.net/?retryWrites=true&w=majority")
    MONGODB_URL = "mongodb+srv://kareem:Kareem<3hanona@cluster0.eouty5b.mongodb.net/?retryWrites=true&w=majority"
    # GOFILE_TOKEN = os.environ.get("ivlW1ZSGn2Y4AoADbCHUjllj2cO9m3WM")
    GOFILE_TOKEN = "ivlW1ZSGn2Y4AoADbCHUjllj2cO9m3WM"
    # Optional
    MAX_DOWNLOAD_SIZE = int(os.environ.get("MAX_DOWNLOAD_SIZE")) if os.environ.get("MAX_DOWNLOAD_SIZE") else 10737418240
    # Constents
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/"
    TG_MAX_SIZE = 2040108421
    CHUNK_SIZE = 1024 * 6