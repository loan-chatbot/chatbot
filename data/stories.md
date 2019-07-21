## 1 happy path
* greet
    - utter_greet
* help
    - action_get_help
    - utter_did_that_help
* affirm
    - utter_anything_else
* deny
    - utter_happy
* bye
    - utter_bye

## 2 happy path
* greet
    - utter_greet
* help
    - action_get_help
    - utter_did_that_help
* affirm
    - utter_anything_else
* affirm
    - utter_ask_help
* help
    - action_get_help
    - utter_did_that_help
* affirm
    - utter_anything_else
* deny
    - utter_happy
    - utter_bye

## 1 sad path
* greet
    - utter_greet
* help
    - action_get_help
    - utter_did_that_help
* deny
    - utter_default
    - utter_ask_help
* help
    - action_get_help
    - utter_did_that_help
* affirm
    - utter_anything_else
* deny
    - utter_happy
* bye
    - utter_bye

## 2 sad path
* greet
    - utter_greet
* help
    - action_get_help
    - utter_did_that_help
* deny
    - utter_default
    - utter_ask_help
* help
    - action_get_help
    - utter_did_that_help
* affirm
    - utter_anything_else
* affirm
    - utter_ask_help
* help
    - action_get_help
    - utter_did_that_help
* affirm
    - utter_anything_else
* deny
    - utter_happy
* bye
    - utter_bye

## happy help path
* help
    - action_get_help
    - utter_did_that_help
* affirm
    - utter_anything_else
* deny
    - utter_happy
* bye
    - utter_bye

## sad help path
* help
    - action_get_help
    - utter_did_that_help
* deny
    - utter_default
    - utter_ask_help
* help
    - action_get_help
    - utter_did_that_help
* affirm
    - utter_anything_else
* deny
    - utter_happy
* bye
    - utter_bye

## bye path
* bye
    - utter_bye

## Generated Story -6553352608088712229
* greet
    - utter_greet
* help{"amount": "total npa", "time": "2019-07-21T00:00:00.000+05:30"}
    - slot{"amount": "total npa"}
    - slot{"time": "2019-07-21T00:00:00.000+05:30"}
    - action_get_help
    - utter_did_that_help
* affirm
    - utter_anything_else
* deny
    - utter_happy
    - utter_bye
