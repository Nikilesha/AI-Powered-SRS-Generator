import json


def parse_llm_json(response):
    try:
        return json.loads(response)
    except Exception:
        return {
            "error": "Invalid JSON",
            "raw_response":response
        }