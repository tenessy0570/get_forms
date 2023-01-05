import re


class ValidationError(Exception):
    pass


def validate_phone_number(value: str):
    pattern = r"\+7 \d{3} \d{3} \d{2} \d{2}"

    if not re.match(pattern, value):
        raise ValidationError("Invalid phone number format, allowed format: \"+7 xxx xxx xx xx\"")


def validate_date(value: str):
    pattern = r"(\d{2}\.\d{2}\.\d{4}|\d{4}-\d{2}-\d{2})"

    if not re.match(pattern, value):
        raise ValidationError("Invalid date format, allowed formats: \"DD.MM.YYYY or YYYY-MM-DD\"")


def validate_email(value: str):
    # Took from Google

    pattern = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[
    \x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[
    a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(
    5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[
    \x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

    if not re.match(pattern, value):
        raise ValidationError("Invalid email format")


def validate_text(value: str):
    pass


validator_by_field_type = {
    "email": validate_email,
    "phone": validate_phone_number,
    "date": validate_date,
    "text": validate_text
}
