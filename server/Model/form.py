from data import Data
from formMetaData import FormMetaData
from level import Level
from datetime import date
# import sys
# sys.path.insert(1, '/home/ojjas/PaperlessWorkflow_IITH/server/Controller')
# print(sys.path)
# from Controller import fields 
import fields

from enum import Enum

class FORM_STATUS(Enum):
    IN_PROCESS=0
    REJECTED=1
    ACCEPTED=2

class Form:

    def __init__(self,_ID,_form_type : FormMetaData,submitter_id :str) -> None:
        self.ID=_ID
        self.form_type=_form_type
        self.cur_level_no=0
        self.cur_level=Level(*self.form_type.get_level(0),[],0)#Get 0th layer from metadata
        self.data=Data()
        self.applicant_id=submitter_id
        self.status= FORM_STATUS.IN_PROCESS

    def fill_field(self,field_index,u_id,val) -> None:
        # if field_id not in valid_fields:
        #     return
        field_meta=self.cur_level.get_field_at(field_index)
        
        field_entry=fields.FieldFactory(field_meta,val)
        self.data.append_field(u_id, self.cur_level.get_level_no() ,field_index ,field_entry)

    # def approve_to_next_lvl(self,approver_id,remarks):
    #     self.cur_level_no+=1
    #     if self.form_type.n_levels>=self.cur_level_no:
    #         self.status=FORM_STATUS.ACCEPTED
    #         self.data.append_approval(approver_id,self.cur_level_no-1,"ACCEPTED",remarks)
    #     else:
    #         users,fields=self.form_type.get_level(self.cur_level_no)
    #         self.cur_level=Level(users,fields,users,self.cur_level_no)
    #         self.data.append_approval(approver_id,self.cur_level_no-1,"APPROVED",remarks)

    # def flag_to_previous(self,approver_id,remarks):
    #     self.cur_level_no-=1
    #     if self.cur_level_no==0:
            

    # def reject_form(self,approver_id,remarks):
    #     self.status=FORM_STATUS.REJECTED
    #     self.data.append_approval(approver_id,self.cur_level_no,"REJECTED",remarks)

    def get_form_info(self) ->dict:
        self.data.get_form_state()

    def save_to_db() -> bool:
        pass
def main():
    print("hey there")
    f = FormMetaData("leave")
    
    print(f.form_uid)
    F_instance=Form(0,f)
    F_instance.fill_field(0,"cs20btech11060@iith.ac.in","Ojjas Tyagi")
    F_instance.fill_field(1,"cs20btech11060@iith.ac.in",date(2023,1,1))
    F_instance.fill_field(2,"cs20btech11060@iith.ac.in",0)
    F_instance.get_form_info()

    F_log=F_instance.data.get_log()
    print(F_log[0][-1])
    print(F_log[1][-1])
    print(F_log[2][-1])

if __name__=="__main__":
    main()

