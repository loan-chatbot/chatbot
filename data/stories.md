## getNPA path
* greet
    - utter_greet
    - utter_ask_help
* helpNPA{"type": "count", "time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"type": "count"}
    - action_get_getNPA
    - utter_did_that_help
> check_asked_help



## getNPAForeclosed path
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



## getTimeBasedLoanDisbursed path
* greet
    - utter_greet
    - utter_ask_help
* helpTimeBasedLoanDisbursed{"type": "count", "flag": "disbursed", "time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"type": "count"}
    - slot{"flag": "disbursed"}
    - slot{"time": "2019-07-24T00:00:00.000+05:30"}
    - action_get_getTimeBasedLoanDisbursed
    - utter_did_that_help
> check_asked_help



## getRegionInfo path
* greet
    - utter_greet
    - utter_ask_help
* helpRegionInfo{"type": "count", "region": "Karnataka", "time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"type": "count"}
    - slot{"region": "Karnataka"}
    - slot{"time": "2019-07-24T00:00:00.000+05:30"}
    - action_get_getRegionInfo
    - utter_did_that_help
> check_asked_help



## getSalesPerformance path
* greet
    - utter_greet
    - utter_ask_help
* helpSalesPerformance{"type": "count", "region": "Karnataka", "time": "2019-07-24T00:00:00.000+05:30","flag": "sales","order":"ascending"}
    - slot{"type": "count"}
    - slot{"region": "Karnataka"}
    - slot{"time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"flag": "sales"}
    - slot{"order":"ascending"}
    - action_get_getSalesPerformance
    - utter_did_that_help
> check_asked_help



## getMonthlySalesPerformance path
* greet
    - utter_greet
    - utter_ask_help
* helpMonthlySalesPerformance{"type": "count",  "PERSON": "Krishnamurthy", "time": "monthly"}
    - slot{"type": "count"}
    - slot{ "PERSON": "Krishnamurthy"}
    - slot{"time": "monthly"}
    - action_get_getMonthlySalesPerformance
    - utter_did_that_help
> check_asked_help

## getLiveLoans path
* greet
    - utter_greet
    - utter_ask_help
* helpLiveLoans{"type": "count",  "ref_time": "live", "time": "monthly"}
    - slot{"type": "count"}
    - slot{ "ref_time": "live"}
    - slot{"time": "monthly"}
    - action_get_getLiveLoans
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
