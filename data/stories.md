## 1 happy path
* greet
    - utter_greet
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

## 2 happy path
* greet
    - utter_greet
    - utter_ask_help
* help
    - action_get_help
    - utter_did_that_help
* affirm
    - utter_anything_else
* affirm
    - action_slot_reset
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
    - utter_ask_help
* help
    - action_get_help
    - utter_did_that_help
* deny
    - action_slot_reset
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
    - utter_ask_help
* help
    - action_get_help
    - utter_did_that_help
* deny
    - action_slot_reset
    - utter_ask_help
* help
    - action_get_help
    - utter_did_that_help
* affirm
    - utter_anything_else
* affirm
    - action_slot_reset
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
    - action_slot_reset
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

## total npa happy path
* greet
    - utter_greet
    - utter_ask_help
* help{"type": "total npa", "time": "2019-07-22T00:00:00.000+05:30"}
    - slot{"type": "total npa"}
    - slot{"time": "2019-07-22T00:00:00.000+05:30"}
    - action_get_help
    - utter_did_that_help
* affirm
    - utter_anything_else
* deny
    - utter_happy
    - utter_bye

## total npa sad path
* greet
    - utter_greet
    - utter_ask_help
* help{"type": "total npa", "time": "2019-07-22T00:00:00.000+05:30"}
    - slot{"type": "total npa"}
    - slot{"time": "2019-07-22T00:00:00.000+05:30"}
    - action_get_help
    - utter_did_that_help
* deny
    - action_slot_reset
    - utter_ask_help
* help{"type": "total npa", "time": "2019-07-22T00:00:00.000+05:30"}
    - slot{"type": "total npa"}
    - slot{"time": "2019-07-22T00:00:00.000+05:30"}
    - action_get_help
    - utter_did_that_help
* affirm
    - utter_anything_else
* deny
    - utter_happy
    - utter_bye

## total npa foreclosed happy path
* greet
    - utter_greet
    - utter_ask_help
* help{"type": "many NPAs", "closure": "foreclosed", "time": "2018-07-23T00:00:00.000+05:30"}
    - slot{"type": "many NPAs"}
    - slot{"closure": "foreclosed"}
    - slot{"time": "2019-07-23T00:00:00.000+05:30"}
    - action_get_help
    - utter_did_that_help
* affirm
    - utter_anything_else
* deny
    - utter_happy
    - utter_bye

## total npa foreclosed sad path
* greet
    - utter_greet
    - utter_ask_help
* help{"type": "many NPAs", "closure": "foreclosed", "time": "2018-07-23T00:00:00.000+05:30"}
    - slot{"type": "many NPAs"}
    - slot{"closure": "foreclosed"}
    - slot{"time": "2019-07-23T00:00:00.000+05:30"}
    - action_get_help
    - utter_did_that_help
* deny
    - action_slot_reset
    - utter_ask_help
* help{"type": "many NPAs", "closure": "foreclosed", "time": "2019-07-23T00:00:00.000+05:30"}
    - slot{"type": "many NPAs"}
    - slot{"closure": "foreclosed"}
    - slot{"time": "2019-07-23T00:00:00.000+05:30"}
    - action_get_help
    - utter_did_that_help
* affirm
    - utter_anything_else
* deny
    - utter_happy
    - utter_bye

## timeBasedLoanDisbursed happy path
* greet
    - utter_greet
    - utter_ask_help
* help{"type": "total loans", "time": "2018-06-22T00:00:00.000+05:30"}
    - slot{"type": "total loans"}
    - slot{"time": "2019-06-22T00:00:00.000+05:30"}
    - action_get_help
    - utter_did_that_help
* affirm
    - utter_anything_else
* deny
    - utter_happy
    - utter_bye

## timeBasedLoanDisbursed sad path
* greet
    - utter_greet
    - utter_ask_help
* help{"type": "total loans", "time": "2018-06-22T00:00:00.000+05:30"}
    - slot{"type": "total loans"}
    - slot{"time": "2019-07-23T00:00:00.000+05:30"}
    - action_get_help
    - utter_did_that_help
* deny
    - action_slot_reset
    - utter_ask_help
* help{"type": "total loans", "time": "2018-06-22T00:00:00.000+05:30"}
    - slot{"type": "total loans"}
    - slot{"time": "2019-07-23T00:00:00.000+05:30"}
    - action_get_help
    - utter_did_that_help
* affirm
    - utter_anything_else
* deny
    - utter_happy
    - utter_bye

## timeBasedcompareloan happy path
* greet
    - utter_greet
    - utter_ask_help
* help{"type": "total loans","payout": "disbursed","time1": "2018-06-22T00:00:00.000+05:30","time2": "2018-06-22T00:00:00.000+05:30"}
    - slot{"type": "total loans"}
    - slot{"time1": "2019-06-22T00:00:00.000+05:30"}
    - slot{"time2": "2019-06-22T00:00:00.000+05:30"}
    - slot{"payout": "disbursed"}
    - action_get_help
    - utter_did_that_help
* affirm
    - utter_anything_else
* deny
    - utter_happy
    - utter_bye

## timeBasedcompareloan sad path
* greet
    - utter_greet
    - utter_ask_help
* help{"type": "total loans","payout": "disbursed","time1": "2018-06-22T00:00:00.000+05:30","time2": "2018-06-22T00:00:00.000+05:30"}
    - slot{"type": "total loans"}
    - slot{"time1": "2019-06-22T00:00:00.000+05:30"}
    - slot{"time2": "2019-06-22T00:00:00.000+05:30"}
    - slot{"payout": "disbursed"}
    - action_get_help
    - utter_did_that_help
* deny
    - action_slot_reset
    - utter_ask_help
* help{"type": "total loans","payout": "disbursed","time1": "2018-06-22T00:00:00.000+05:30","time2": "2018-06-22T00:00:00.000+05:30"}
    - slot{"type": "total loans"}
    - slot{"time1": "2019-06-22T00:00:00.000+05:30"}
    - slot{"time2": "2019-06-22T00:00:00.000+05:30"}
    - slot{"payout": "disbursed"}
    - action_get_help
    - utter_did_that_help
* affirm
    - utter_anything_else
* deny
    - utter_happy
    - utter_bye

## getliveloans happy path
* greet
    - utter_greet
    - utter_ask_help
* help{"type": "loans","active": "refrence_time" ,"time1": "2018-06-22T00:00:00.000+05:30","time2": "2018-06-22T00:00:00.000+05:30","time": "2018-07-23T00:00:00.000+05:30"}
    - slot{"type": "total loans"}
    - slot{"time1": "2019-06-22T00:00:00.000+05:30"}
    - slot{"time2": "2019-06-22T00:00:00.000+05:30"}
    - slot{"active": "refrence_time"}
    - slot{"time": "2018-07-23T00:00:00.000+05:30"}
    - action_get_help
    - utter_did_that_help
* affirm
    - utter_anything_else
* deny
    - utter_happy
    - utter_bye

## getliveloans sad path
* greet
    - utter_greet
    - utter_ask_help
* help{"type": "loans","active": "refrence_time" ,"time1": "2018-06-22T00:00:00.000+05:30","time2": "2018-06-22T00:00:00.000+05:30","time": "2018-07-23T00:00:00.000+05:30"}
    - slot{"type": "total loans"}
    - slot{"time1": "2019-06-22T00:00:00.000+05:30"}
    - slot{"time2": "2019-06-22T00:00:00.000+05:30"}
    - slot{"active": "refrence_time"}
    - slot{"time": "2018-07-23T00:00:00.000+05:30"}
    - action_get_help
    - utter_did_that_help
* deny
    - action_slot_reset
    - utter_ask_help
* help{"type": "loans","active": "refrence_time" ,"time1": "2018-06-22T00:00:00.000+05:30","time2": "2018-06-22T00:00:00.000+05:30","time": "2018-07-23T00:00:00.000+05:30"}
    - slot{"type": "total loans"}
    - slot{"time1": "2019-06-22T00:00:00.000+05:30"}
    - slot{"time2": "2019-06-22T00:00:00.000+05:30"}
    - slot{"active": "refrence_time"}
    - slot{"time": "2018-07-23T00:00:00.000+05:30"}
    - action_get_help
    - utter_did_that_help
* affirm
    - utter_anything_else
* deny
    - utter_happy
    - utter_bye

