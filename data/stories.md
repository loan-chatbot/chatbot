## happy path
* greet
- utter_greet
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
* help
- action_get_help
- utter_did_that_help
* affirm
- utter_anything_else
* affirm
- action_restart
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
* help
- action_get_help
- utter_did_that_help
* deny
- action_restart
- utter_default
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
* deny
- action_restart
* help
- action_get_help
- utter_did_that_help
* affirm
- utter_anything_else
* deny
- utter_happy
- utter_bye


## askhelptrue path
- action_get_help
- utter_did_that_help
* affirm
- utter_anything_else

## askhelpfalse path
- action_get_help
- utter_did_that_help
* deny
- action_restart
 
