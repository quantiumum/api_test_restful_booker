from jsonschema import validate
import json


#sequens schema:

schema_get_all_id = {
  "type": "object",
  "properties": {
    "bookingid": {
      "type": "integer"
    }
  },
  "required": [
    "bookingid"
  ]
}

schema_booking = {
  "type": "object",
  "properties": {
    "bookingid": {
      "type": "integer"
    },
    "booking": {
      "type": "object",
      "properties": {
        "firstname": {
          "type": "string"
        },
        "lastname": {
          "type": "string"
        },
        "totalprice": {
          "type": "integer"
        },
        "depositpaid": {
          "type": "boolean"
        },
        "bookingdates": {
          "type": "object",
          "properties": {
            "checkin": {
              "type": "string"
            },
            "checkout": {
              "type": "string"
            }
          },
          "required": [
            "checkin",
            "checkout"
          ]
        },
        "additionalneeds": {
          "type": "string"
        }
      },
      "required": [
        "firstname",
        "lastname",
        "totalprice",
        "depositpaid",
        "bookingdates",
        "additionalneeds"
      ]
    }
  },
  "required": [
    "bookingid",
    "booking"
  ]
}

def valid_data(data: dict, json_schema: dict):
    try:
        validate(data, schema_get_all_id)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True



def to_dict(json_data: dict, param: str):
    if param == 'text':
        try:
              return json.loads(json_data.text)
        except:
              return False