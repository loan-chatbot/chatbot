## intent:affirm
- yes
- yup
- indeed
- of course
- that sounds good
- correct
- yes sure
- absolutely
- for sure
- yes yes yes
- definitely
- yes, it did
- yes
- yes

## intent:bye
- Bye
- Goodbye
- See you later
- Bye bot
- Goodbye friend
- bye
- bye for now
- catch you later
- gotta go
- See you
- goodnight
- have a nice day
- i'm off
- see you later alligator
- we'll speak soon
- end
- finish

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really
- nope
- Nah
- nay
- no
- no

## intent:greet
- Hi
- Hey
- heyy
- Hi bot
- Hey bot
- Hello
- Good morning
- hi again
- hi folks
- hi Mister
- hi pal!
- hi there
- greetings
- hello everybody
- hello is anybody there
- hello robot
- who are you?
- what are you?
- what's up
- how do you do?
- hi
- hey

## intent:helpNPA
- get me [total npa](type:count) as of [today](time:2019-07-24T00:00:00.000+05:30)
- get me [total npa](type:count) as of [yesterday](time:2019-07-24T00:00:00.000+05:30)
- get me [total npa](type:count) as of [last month](time:2019-07-24T00:00:00.000+05:30)
- get me [total amount of npa](type:amount) as of [last week](time:2019-07-24T00:00:00.000+05:30)
- get me [total amount of npa](type:amount) as of [today](time:2019-07-24T00:00:00.000+05:30)

## intent:helpNPAForeclosed
- How [many NPAs](type:count) have be [foreclosed](closure) in the [last year](time:2019-07-24T00:00:00.000+05:30)
- How [many NPAs](type:count) have be [foreclosed](closure) in the [last financial year](time:2019-07-24T00:00:00.000+05:30)
- How [many npas](type:count) have been [foreclosed](closure) [today](time:2019-07-24T00:00:00.000+05:30)
- How [much NPAs](type:amount) have be [foreclosed](closure) in the [last month](time:2019-07-24T00:00:00.000+05:30)
- How [much npas](type:amount) have been [foreclosed](closure) [yesterday](time:2019-07-24T00:00:00.000+05:30)

## intent:helpTimeBasedLoanDisbursed
- get me [total loans](type:count) [disbursed](flag) in [last month](time:2019-07-24T00:00:00.000+05:30)
- get me [total loans](type:count) [disbursed](flag) in the [last month of last year](time:2019-07-24T00:00:00.000+05:30)
- get me [total amount of loans](type:amount) [disbursed](flag) in the [same month last year](time:2019-07-24T00:00:00.000+05:30)
- get me [total loans](type:count) [disbursed](flag) in the month of [january 2018](time:2019-07-24T00:00:00.000+05:30)
- get me [total amount of loans](type:amount) [disbursed](flag) in [last quarter](time:2019-07-24T00:00:00.000+05:30)

## intent:helpRegionInfo
- compare the [loans](type:count) performance between [different regions](region:all) in [last 6 months](time:2019-07-24T00:00:00.000+05:30)
- get the [amount of loans](type:amount) performance in [Karnataka](region:Karnataka) in [last month](time:2019-07-24T00:00:00.000+05:30)
- get the [loans](type:count) performance in [Maharashtra](region:Maharashtra) as of [today](time:2019-07-24T00:00:00.000+05:30)
- get the [amount of loans](type:amount) performance in [Madhya Pradesh](region:Madhya_Pradesh) in [last year](time:2019-07-24T00:00:00.000+05:30)
- get the [amount of loans](type:amount) performance in [MP](region:MP) in [previous week](time:2019-07-24T00:00:00.000+05:30)
- get me [loans](type:count) performance in [goa](region:goa) in [previous year](time:2019-07-24T00:00:00.000+05:30)

## intent:helpSalesPerformance
- Which is the [top](order:ascending) performing [sales](flag) officer for [last 6 months](time:2019-07-24T00:00:00.000+05:30) based on [amount](type:amount)?
- Which is the [worst](order:descending) performing [sales](flag) officer for [last 1 year](time:2019-07-24T00:00:00.000+05:30) based on [count](type)?
- Who is the [top](order:ascending) performing [sales](flag) officer for [Karnataka](region)?

## intent:helpMonthlySalesPerformance
- Get me [monthly](time) sales performance of sales officer [Krishnamurthy](PERSON)
- Get me [yearly](time) sales performance of the sales officer [Pranav](PERSON)
- Get me [quarterly](time) sales performance of sales officer [Adithya](PERSON)
- show me [weekly](time) sales performance of sales officer [Balu](PERSON)

## intent:helpLiveLoans
- Get me the total [live](ref_time:current) [loans](type:count) as of [last Tuesday](time)
- Get me the total [live](ref_time:current) [loans](type:count) as of [last year](time)
- How many [loans](type:count) created in the [last year](time) are still [active](ref_time:current)?
- What is the [count](type:count) of [live](ref_time:current) loans as of [April 2019](time)?

## synonym:2019-07-24T00:00:00.000+05:30
- today
- last week
- last year
- last financial year
- last month
- last quarter
- yesterday
- january 2018

## synonym:amount
- total amount of npa
- total amount of loans
- total amount of loan
- much NPAs
- much npas
- much npa

## synonym:count
- total npa
- total loans
- total loan
- many NPAs
- many npas
- many npa
- loan
- loans
