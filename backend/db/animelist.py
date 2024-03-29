import os
import json
from db.db import SessionLocal
import db.models
import re


local_session=SessionLocal()

dirname = os.path.dirname(__file__)
file = os.path.join(dirname, "scraper/animelist.json")
def animeFile():
    list = open(file,"r")
    anime = json.load(list)
    return anime

for anime in animeFile():
    dub = re.search("(Dub)", anime["title"])
    new_anime = db.models.Anime_List(
        title=anime["title"],
        code=anime["code"],
        edition=anime["edition"],
        isDubbed=True if dub else False
        )
    local_session.add(new_anime)
    local_session.commit()

    animeFile()