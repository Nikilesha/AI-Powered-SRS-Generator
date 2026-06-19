import json
from datetime import datetime


def save_json(data):
    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = (
        f"data/generated_srs/"
        f"srs_{timestamp}.json"
    )

    with open(filename,"w",encoding="utf-8") as file:
        json.dump(data,file,indent=4)
    return filename