## happy path
* greet
- utter_greet
* name
- utter_ask_help
* help
- action_get_help
- utter_did_that_help
* affirm
- utter_anything_else
* deny
- utter_happy
- utter_bye

## happy path 2
* greet
- utter_greet
* name
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
- utter_bye

## sad path
* greet
- utter_greet
* name
- utter_ask_help
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

## help path
* help
- action_get_help
- utter_did_that_help

## anything path
* affirm
- utter_anything_else



## bye path
* deny
- utter_happy
- utter_bye