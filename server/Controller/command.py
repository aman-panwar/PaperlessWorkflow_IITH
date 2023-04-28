import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/..')
from  Model.form import Form
from Model.util import show_form
from Model.formMetaData import FormMetaData
from Model.level import Level
from Model.fields import Field
from Model.data import Data
import time
import datetime

from io import StringIO
import textwrap
class Command:
    def execute(self):
        pass

class Accept:
    """This function is used when the officer has filled the fields and approved the form to the next level
    """
    def __init__(self,_form_id,_user_id,_field_vals) -> None:
        """This initalilizes the paramters of the function

        Args:
            _form_id (_type_): ID of the form
            _user_id (_type_): User ID making changes
            _field_vals (_type_): List of field values from front end ,in index order where you want to make changes
        """
        self.form_id=_form_id
        self.user_id=_user_id
        self.field_vals=_field_vals
    
    def officer_approve(self,remarks:str) -> bool:
        """_summary_

        Returns:
            bool: Tells if the execution of the Accept request was successfull,can fault due to invalid parameters

        """
        #This function internally faults if invalid form_id requested
        F_instance =Form(ID=self.form_id)
        if self.user_id in F_instance.cur_level.approvers_id and F_instance.status=="PENDING":
            for x in range(len(self.field_vals)):
                F_instance.update_field(x,self.user_id,self.field_vals[x])
            F_instance.data.append_approval(time.time(),self.user_id,F_instance.cur_level_no,"APPROVED",remarks)
            F_instance.cur_level_no+=1
            # n levels total ,last level is n-1 ,equality implies  all levels exhausted,ie accpeted
            if F_instance.cur_level_no>=F_instance.form_meta.n_levels:
                F_instance.status="ACCEPTED"
                # F_instance.cur_level=None
            else:
                users_info,field_info=F_instance.form_meta.get_level(F_instance.cur_level_no)
                F_instance.cur_level=Level(users_info,field_info,users_info,F_instance.cur_level_no)
            #POST BACK TO DB
            if F_instance.save_to_db():
                return True
            else :
                print("Error,DB not updated")
                return False
        else:
            print("Invalid call,User not valid/ Invalid Form")
            return False
    
    def user_submit(self,form_name:str):
        F_instance =Form()
        F_new=Form()
        F_new.form_meta=FormMetaData(form_type=form_name)
        # Initilizing current level in special manner,
        # Modify Current level to have applicant id in level 0 of form metadata copy of form
        # This way even in reviews when formis sent back to applicant ,applicant can see the form

        F_new.form_meta.users[0].append(self.user_id)
        F_new.applicant_id=self.user_id
        F_new.cur_level_no=0

        
        field_lvl0_info=F_new.form_meta.get_level(0)[1]
        F_new.cur_level=Level([F_new.applicant_id],field_lvl0_info,[F_new.applicant_id],0)
        F_new.status="PENDING"
        F_new.data=Data()

        #Add the vals the user gave to the form
        for i in range(len(self.field_vals)):
            F_new.update_field(i,self.user_id,self.field_vals[i])

        F_new.cur_level_no+=1
        user_info,field_info=F_new.form_meta.get_level(1)
        F_new.cur_level=Level(user_info,field_info,user_info,1)
        F_new.data.append_approval(time.time(),self.user_id,0,"SUBMITTED","NA")

        #POST BACK TO DB
        if(F_new.save_to_db()):
            print(F_new.ID)
            return True
        else: 
            print("Created form not posted to DB")
            return False
        
    def notify():
        pass

class Reject:
    def __init__(self,_form_id,_user_id,_rejection_remarks) -> None:
        self.form_id=_form_id
        self.user_id=_user_id
        self.reject_reason=_rejection_remarks

    def execute(self):
        #This function internally faults if invalid form_id requested
        F_instance =Form(ID=self.form_id)
        if self.user_id in F_instance.cur_level.approvers_id and F_instance.status=="PENDING":
            F_instance.status="REJECTED"
            F_instance.data.append_approval(time.time(),self.user_id,F_instance.cur_level_no,"REJECTED",self.reject_reason)
            #POST BACK TO DB
            if(F_instance.save_to_db()):
                print(F_instance.ID)
                return True
            else: 
                print("Error,DB not updated")
                return False
        else: 
            print("Invalid call,User not valid/ Invalid Form")
            return False
    def notify():
        pass

class Review:
    def __init__(self,_form_id:str,_user_id:str,_review_remark:str) -> None:
        self.form_id=_form_id
        self.user_id=_user_id
        self.review_reason=_review_remark
    def execute(self):
        F_instance =Form(ID=self.form_id)
        if self.user_id in F_instance.cur_level.approvers_id and F_instance.status=="PENDING":
            #Applicant layer(0) cant send for review
            if F_instance.cur_level_no==0:
                print("Invalid request applicant (layer 0) cannot send form for review")
                return False
            F_instance.data.append_approval(time.time(),self.user_id,F_instance.cur_level_no,"REVIEW",self.review_reason)
            F_instance.cur_level_no-=1
            
            users_info,field_info=F_instance.form_meta.get_level(F_instance.cur_level_no)
            F_instance.cur_level=Level(users_info,field_info,users_info,F_instance.cur_level_no)
            
            #POST BACK TO DB
            if F_instance.save_to_db():
                print(F_instance.ID)
                return True
            else :
                print("Error,DB not updated")
                return False
        else: 
            print("Invalid call,User not valid/ Invalid Form")
            return False   
        pass
    def notify():
        pass

def print_form_info(F_ID: str):
    print("\033[1;30;44m")
    F_inst=Form(ID=F_ID)
    latest_form_info=F_inst.data.get_form_state()
    print("Most recent form fields")
    for i,x in enumerate(latest_form_info):
        print("field ",i)
        for y in x.keys():
            str_tmp=str(y)+"::"+str(x[y])
            indented_str = textwrap.indent(str_tmp, ' '*4)
            print(indented_str)
    form_pipeline_info=F_inst.data.get_approval_log()
    print("Form approval log")
    for i,x in enumerate(form_pipeline_info):
        print("Action ",i)
        for y in x.keys():
            str_tmp=str(y)+"::"+str(x[y])
            indented_str = textwrap.indent(str_tmp, ' '*4)
            print(indented_str)
    print("Form status",F_inst.status)
    print("Form current level",F_inst.cur_level_no)
    print("\033[0;0m\n")

def test_submit_approve_accept(print_info=False):
    # Test 0 ,simple submission
    buffer = StringIO()
    sys.stdout = buffer
    Submission=Accept(None,"es20btech11035@iith.ac.in",["Pranav K Nayak","today",0])
    action_status=Submission.user_submit("leave")

    print_output = buffer.getvalue()
    print(print_output)
    sys.stdout = sys.__stdout__

    if(action_status):
        print("Form Submitted")
    else:
        print("Form submission Failed")
        raise Exception("Form submission Failed")
    print("Form id created",print_output.rstrip())
    F_ID=print_output.rstrip()

    try:
        # Test 1 ,simple approval
        Approval_lvl1=Accept(F_ID,"cs20btech11060@iith.ac.in",["this is remark for field entry"])
        if Approval_lvl1.officer_approve("These are the log remarks"):
            print("\033[1;32mPASSED::Form Approved by officer\033[0;0m \n")
        else:
            print("\033[1;31mFAILED::Form Approval Failed\033[0;0m \n")

        # Test 2 ,simple Acceptance
        Acceptance_lvl2=Accept(F_ID,"es20btech11026@iith.ac.in",["signature.png","Form Accepted by final officer"])
        if Acceptance_lvl2.officer_approve("These are the log remarks"):
            print("\033[1;32mPASSED::Form Accepted by final officer\033[0;0m \n")
        else:
            print("\033[1;31mFAILED::Form Acceptance Failed\033[0;0m \n")

        # Test 3 ,Invalid accept request on approved form
        Acceptance_invalid=Accept(F_ID,"es20btech11060@iith.ac.in",["signature.png","double acceptance"])
        if Acceptance_invalid.officer_approve("These are the log remarks"):
            print("\033[1;31mFAILED :: FINALIZED FORM MODIFIED BY ACCEPT\033[0;0m \n")
        else:
            print("\033[1;32mPASSED:: FINALIZED FORM NOT MODIFIED BY ACCEPT\033[0;0m \n")
        

        if(print_info):
            print_form_info(F_ID)
    except Exception as e:
        print(e)
        print("\033[1;31mFAILED CATASTROPHIC FAILURE<TEST CASES STOPPED>\033[0;0m \n")
    #Delete this test form
    F_inst=Form(ID=F_ID)
    if(F_inst.delete_from_db()):
        print("Form deleted")
    else:
        print("Form deletion Failed")
        raise Exception("Form deletion Failed")
    print("\033[1;32;47mPIPELINE TESTING FOR SIMPLE APPROVALS PASSED \033[0;0m \n")
  
def test_submit_reject(print_info=False):
    #Create the form for testing
    buffer = StringIO()
    sys.stdout = buffer
    Submission=Accept(None,"es20btech11035@iith.ac.in",["Pranav K Nayak","no date",0])
    action_status=Submission.user_submit("leave")

    print_output = buffer.getvalue()
    print(print_output)
    sys.stdout = sys.__stdout__

    if(action_status):
        print("Form Submitted")
    else:
        print("Form submission Failed")
        raise Exception("Form submission Failed")
    print("Form id created",print_output.rstrip())
    F_ID=print_output.rstrip()

    try:
        #Test 0 : simple Rejection
        Rejection_lvl1=Reject(F_ID,"cs20btech11060@iith.ac.in","Form lacks a date")
        if Rejection_lvl1.execute():
            print("\033[1;32mPASSED::Form Rejected by officer\033[0;0m \n")
        else:
            print("\033[1;31mFAILED::Form Rejection Failed\033[0;0m \n")

        #Test 1 : Invalid acceptance of rejected form
        Invalid_accept_lvl1=Accept(F_ID,"cs20btech11060@iith.ac.in",["Shouldnt be accepted"])
        if Invalid_accept_lvl1.officer_approve("ERROR :: SHOULDNT BE IN LOG"):
            print("\033[1;31mFAILED :: REJECTED FORM MODIFIED BY ACCEPT\033[0;0m \n")
        else:
            print("\033[1;32mPASSED:: REJECTED FORM NOT MODIFIED BY ACCEPT\033[0;0m \n")

        #Test 2 : Invalid review of rejected form
        invalid_review_lvl1=Review(F_ID,"cs20btech11060@iith.ac.in",["Shouldnt be reviewed"])
        if invalid_review_lvl1.execute():
            print("\033[1;31mFAILED :: REJECTED FORM MODIFIED BY REVIEW\033[0;0m \n")
        else:
            print("\033[1;32mPASSED:: REJECTED FORM NOT MODIFIED BY REVIEW\033[0;0m \n")
    except Exception as e:
        print(e)
        print("\033[1;31mFAILED CATASTROPHIC FAILURE<TEST CASES STOPPED>\033[0;0m \n")

    if print_info:
        print_form_info(F_ID)

    #Delete this test form
    F_inst=Form(ID=F_ID)
    if(F_inst.delete_from_db()):
        print("Form deleted")
    else:
        print("Form deletion Failed")
        raise Exception("Form deletion Failed")
    print("\033[1;32;47mPIPELINE TESTING FOR REJECTION CASE PASSED \033[0;0m \n")

def test_submit_review_then_accept(print_info=False):
    #Create the form for testing
    buffer = StringIO()
    sys.stdout = buffer
    Submission=Accept(None,"es20btech11035@iith.ac.in",["Pranav K Nayak","today",1])
    action_status=Submission.user_submit("leave")

    print_output = buffer.getvalue()
    print(print_output)
    sys.stdout = sys.__stdout__

    if(action_status):
        print("Form Submitted")
    else:
        print("Form submission Failed")
        raise Exception("Form submission Failed")
    print("Form id created",print_output.rstrip())
    F_ID=print_output.rstrip()
    try:
        #Test 0 : simple review
        review_lvl1=Review(F_ID,"cs20btech11060@iith.ac.in","Incorrect gender selected as per record ,kindly correct")
        if review_lvl1.execute():
            print("\033[1;32mPASSED::Form Reviewed by officer\033[0;0m \n")
        else:
            print("\033[1;31mFAILED::Form Review Failed\033[0;0m \n")
        #Test 1 : Invalid review at lvl 0(user)
        invalid_review_lvl0=Review(F_ID,"es20btech11035@iith.ac.in",["Shouldnt be reviewed by user"])
        if invalid_review_lvl0.execute():
            print("\033[1;31mFAILED :: REVIEW BY USER\033[0;0m \n")
        else:
            print("\033[1;32mPASSED:: USER DENIED REVIEW OPTION\033[0;0m \n")
        #Test 2 : Resubmission of existing form by user using officer approve
        user_resbmit=Accept(F_ID,"es20btech11035@iith.ac.in",["Pranav KN","tomorrow",0])
        if user_resbmit.officer_approve("resubmission due to wrong gender"):
            print("\033[1;32mPASSED::Form Resubmitted by user successfully\033[0;0m \n")
        else:
            print("\033[1;31mFAILED::Form Resubmission Failed\033[0;0m \n")
        #Test 3 : approval and acceptance of form
        Acceptance_lvl1=Accept(F_ID,"cs20btech11004@iith.ac.in",["I think this works now"])
        if Acceptance_lvl1.officer_approve("level1 approves corrected form"):
            print("\033[1;32mPASSED::Form Accepted by officer after changes\033[0;0m \n")
        else:
            print("\033[1;31mFAILED::Form Acceptance Failed\033[0;0m \n")

        Acceptance_lvl2=Accept(F_ID,"es20btech11026@iith.ac.in",["signature.png","Seen,Approved"])
        if Acceptance_lvl2.officer_approve("Quokka approves"):
            print("\033[1;32mPASSED::Form Accepted by final officer\033[0;0m \n")
        else:
            print("\033[1;31mFAILED::Form Acceptance Failed\033[0;0m \n")
    except Exception as e:
        print(e)
        print("\033[1;31mFAILED CATASTROPHIC FAILURE<TEST CASES STOPPED>\033[0;0m \n")

    if print_info:
        print_form_info(F_ID)

    #Delete this test form
    F_inst=Form(ID=F_ID)
    if(F_inst.delete_from_db()):
        print("Form deleted")
    else:
        print("Form deletion Failed")
        raise Exception("Form deletion Failed")
    print("\033[1;32;47mPIPELINE TESTING FOR REVIEW CASE PASSED \033[0;0m \n")

def main():
    #Default is false ,set to true to view form details aftter all tests are done
    test_submit_approve_accept(print_info=False)
    test_submit_reject()
    test_submit_review_then_accept()
    

    #Stray cleanup code
    # F_ID="644c3418d532a20021cf267b"
    # F_inst=Form(ID=F_ID)
    # F_inst.delete_from_db()
    # print("Form deleted")
if __name__=="__main__":
    
    main()