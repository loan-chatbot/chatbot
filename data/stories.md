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

## 1 help path
* help
    - action_get_help
    - utter_did_that_help
* affirm
    - utter_anything_else
* deny
    - utter_happy
* bye
    - utter_bye

## 1 affirm path
* affirm
    - utter_anything_else
* deny
    - utter_happy
* bye
    - utter_bye

## 1 deny path
* deny
    - utter_happy
* bye
    - utter_bye

## 1 bye path
* bye
    - utter_bye















 


