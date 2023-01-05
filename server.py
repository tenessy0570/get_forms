from fastapi import FastAPI, Request

from db import db
from utils import find_form_by_request_fields, match_types_to_request_fields

app = FastAPI()


@app.post("/get_form")
async def get_form(request: Request):
    request_json: dict = await request.json()

    matched_form: dict = find_form_by_request_fields(db, request_json)

    if matched_form is not None:
        return {"name": matched_form["name"]}

    fields_with_types: dict = match_types_to_request_fields(request_json)
    return fields_with_types
