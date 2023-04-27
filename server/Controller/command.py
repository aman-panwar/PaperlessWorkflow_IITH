import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/..')
from  Model.form import Form
from Model.temp import show
from Model.formMetaData import FormMetaData
from Model.level import Level
from Model.fields import Field
from Model.data import Data
import time
import datetime

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
                F_instance.status=="ACCEPTED"
                F_instance.cur_level=None
            else:
                users_info,field_info=F_instance.form_meta.get_level(F_instance.cur_level_no)[1]
                F_instance.cur_level=Level(users_info,field_info,users_info,F_instance.cur_level_no)
            #POST BACK TO DB
            print("in command", self.form_id, " # ", F_instance.ID)
            if F_instance.save_to_db():
                print(F_instance.ID)
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
            return False
        
    def notify():
        pass

class Reject:
    def __init__(self) -> None:
        pass
    def execute(self):
        pass
    def notify():
        pass

class Review:
    def __init__(self) -> None:
        pass
    def execute(self):
        pass
    def notify():
        pass

def main():
    # Submission=Accept(None,"cs20btech11060@iith.ac.in",["Ojjas Tyagi","today",0])
    # if(Submission.user_submit("leave")):
    #     print("Form Submitted")
    # else:
    #     print("Form submission Failed")

    # #Set this to whatever you get from above code
    # F_ID="644a05946158406dd18d5c28"

    # F_existing= Form(ID=F_ID)
    # d=F_existing.to_dict()
    # #show(d)

    # #returns invalid call,due to inappropriate email
    # Approval=Accept(F_ID,"tyagi@gmail",["this is remark for field entry"])
    # Approval.officer_approve("These are the log remarks")

    #Bug over here approval returns true first time for the form but when form is viewed no
    #changes are made and on trying for approval/save_to_db() again it returns false
    
    #show(Form(ID='6449ad0e6158406dd146efa9').to_dict())
    
    
    F_ID="6449ad0e6158406dd146efa9"
    Approval=Accept(F_ID,"cs20btech11060@iith.ac.in",["this is remark for field entry"])
    if Approval.officer_approve("These are the log remarks"):
        print("Form Approved by officer")
    else:
        print("Form Approval Failed")
    show(Form(ID = F_ID ).to_dict())
    # F_existing= Form(ID=F_ID)
    
    # d=F_existing.to_dict()
    # #show(d)

    # print(F_existing.save_to_db())
    

    pass

if __name__=="__main__":
    
    main()