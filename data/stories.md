## getNPA count path
* greet
    - utter_greet
    - utter_ask_help
* helpNPA{"type": "count", "time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"type": "count"}
    - action_get_getNPA
    - utter_did_that_help
> check_asked_help

## getNPA amount path
* greet
    - utter_greet
    - utter_ask_help
* helpNPA{"type": "amount", "time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"type": "amount"}
    - action_get_getNPA
    - utter_did_that_help
> check_asked_help

## getNPAForeclosed count path
* greet
    - utter_greet
    - utter_ask_help
* helpNPAForeclosed{"type": "count", "closure": "foreclosed", "time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"type": "count"}
    - slot{"closure": "foreclosed"}
    - slot{"time": "2019-07-24T00:00:00.000+05:30"}
    - action_get_getNPAForeclosed
    - utter_did_that_help
> check_asked_help

## getNPAForeclosed amount sad path
* greet
    - utter_greet
    - utter_ask_help
* helpNPAForeclosed{"type": "amount", "closure": "foreclosed", "time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"type": "amount"}
    - slot{"closure": "foreclosed"}
    - slot{"time": "2019-07-24T00:00:00.000+05:30"}
    - action_get_getNPAForeclosed
    - utter_did_that_help
> check_asked_help

## checkpoint affirm path
> check_asked_help
* affirm
    - utter_anything_else
* deny
    - utter_happy
    - utter_bye

## checkpoint 1 deny path
> check_asked_help
* deny
    - action_slot_reset
    - utter_ask_help

## checkpoint 2 deny path
> check_asked_help
* affirm
    - utter_anything_else
* affirm
    - action_slot_reset
    - utter_ask_help

## bye path
* bye
    - utter_bye
