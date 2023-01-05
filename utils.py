from validators import validator_by_field_type, ValidationError


def find_form_by_request_fields(db, request_json: dict):
    # Simple loop to find our form (didn't care about performance)
    found_form = None

    for db_form in db:
        found_form = db_form

        for form_field, field_value in found_form.items():
            if form_field == "name":
                continue

            if request_json.get(form_field) is None:
                found_form = None
                break

        if found_form is None:
            continue

        for key, value in request_json.items():
            field_type = db_form.get(key)

            if field_type is None:
                continue

            try:
                validator_by_field_type[field_type](value)
            except ValidationError:
                found_form = None
                break

        if found_form is not None:
            break

    return found_form


def match_types_to_request_fields(request_json):
    fields_with_types = {}

    for field, value in request_json.items():
        guessed_types = ["phone", "date", "email", "text"]

        for guessed_type in guessed_types:
            try:
                validator_by_field_type[guessed_type](value)
            except ValidationError:
                continue
            else:
                fields_with_types[field] = guessed_type
                break

    return fields_with_types
