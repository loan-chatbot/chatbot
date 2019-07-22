from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa.core.events import AllSlotsReset
from rasa.core.events import Restarted
import re

class ActionGetHelp(Action):

    def name(self):
        return "action_get_help"

    
    def run(self, dispatcher, tracker, domain): 
        size = tracker.get_slot('size') 
        field = tracker.get_slot('field')
        order = tracker.get_slot('order') 
        typo = tracker.get_slot('type') 
        time = tracker.get_slot('time') 
        time1 = tracker.get_slot('time1') 
        time2 = tracker.get_slot('time2') 
        refrence_time = tracker.get_slot('refrence_time') 
        allreg = tracker.get_slot('allreg') 
        reg1 = tracker.get_slot('reg1') 
        reg2 = tracker.get_slot('reg2') 
        closure=tracker.get_slot('closure')
        person=tracker.get_slot('PERSON')
        payout=tracker.get_slot('payout')


        message = "\nSize: " + size + "\nField: " + field + "\nOrder: " + order + "\ntypo:  " + typo + "\nTime: " + time + "\nTime1: " + time1 + "\nTime2: " + time2 +"\nPayout: " + payout+"\nRefrence time: " + refrence_time +"\nAll Reg: " + allreg + "\nReg1: " + reg1 + "\nReg2: " + reg2 +"\nClosure: " + closure +"\nPerson:" + person  
        dispatcher.utter_message(message)

        pattern= re.compile(r'\s+')
        typo=re.sub(pattern,'',typo)
        time=re.sub(pattern,'',time)
        time1=re.sub(pattern,'',time1)
        time2=re.sub(pattern,'',time2)
        field=re.sub(pattern,'',field)

        if((size.isalpha()) == True):
            size=size.lower()
        if((field.isalpha()) == True):
            field=field.lower()
        if((order.isalpha()) == True):
           order=order.lower()
        if((typo.isalpha()) == True):
            typo= typo.lower()
        if((time.isalpha()) == True):
           time= time.lower()
        if((time1.isalpha()) == True):
           time1= time1.lower()
        if((time2.isalpha()) == True):
          time2= time2.lower()
        if((refrence_time.isalpha()) == True):
          refrence_time= refrence_time.lower()
        if((allreg.isalpha()) == True):
           allreg= allreg.lower()
        if((reg1.isalpha()) == True):
          reg1=reg1.lower()
        if((reg2.isalpha()) == True):
            reg2=reg2.lower()
        if((closure.isalpha()) == True):
           closure= closure.lower()
        if((person.isalpha()) == True):
           person= person.lower()
        
        
                

        if(typo!="" and time!=""):
            if(closure=="foreclosed"):
                dispatcher.utter_message("call getNPAForeclosed(type:"+typo+","+time+")")
            elif(("disbursed" in payout) and time!="" and refrence_time=="" and time1=="" and time2=="" and field==""):
                dispatcher.utter_message("call getTimeBasedLoanDisbursed(type:"+typo+","+time+")")


        if(refrence_time!=""):
            if(typo!=""):
                dispatcher.utter_message("call getLiveLoans(type:"+typo+",refrence_time:"+refrence_time+","+time+")")
        

        if(time1!="" or time2!=""):
            if(typo!=""):
                dispatcher.utter_message("call timeBasedCompareLoans(type:"+typo+",refrence_time:"+refrence_time+","+time+")")
    
            
        if(field!=""):
            if(allreg!=""):
                dispatcher.utter_message("call getSalesPerformance(order:"+order+",region:"+allreg+","+time+")")
            elif(reg1!="" or reg2!=""):
                dispatcher.utter_message("call getSalesPerformance(order:"+order+",region 1:"+reg1+",region 2:"+reg2+","+time+")")

        else:
            if(reg1!="" or reg2!=""):
                dispatcher.utter_message("call getRegionInfo(order:"+order+",region 1:"+reg1+",region 2:"+reg2+","+time+")")
            elif(allreg!=""):
                dispatcher.utter_message("call getRegionInfo(order:"+order+",region:"+allreg+","+time+")")

              
        return []
        
class ActionRestarted(Action): 	
    def name(self): 		
        return 'action_restarted' 	
    def run(self, dispatcher, tracker, domain): 
        return[Restarted()] 
class ActionSlotReset(Action): 	
    def name(self): 		
        return 'action_slot_reset' 	
    def run(self, dispatcher, tracker, domain): 		
        return[AllSlotsReset()]
        