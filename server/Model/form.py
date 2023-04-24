from data import Data
from formMetaData import FormMetaData
from level import Level
import pymongo
from database_manager import DbManager
import json

from datetime import date
# import sys
# sys.path.insert(1, '/home/ojjas/PaperlessWorkflow_IITH/server/Controller')
# print(sys.path)
# from Controller import fields

import fields
import json
from enum import Enum

# class FORM_STATUS(Enum):
#     IN_PROCESS=0
#     REJECTED=1
#     ACCEPTED=2


class Form:

    def __init__(self, _ID=None, _form_type: FormMetaData = None, submitter_id: str = None, json_str: str = None) -> None:
        if json_str == None:
            self.ID = _ID
            self.form_type = _form_type
            self.cur_level_no = 0
            # Get 0th layer from metadata
            self.cur_level = Level(*self.form_type.get_level(0), [], 0)
            self.data = Data()
            self.applicant_id = submitter_id
            self.status = "IN_PROCESS"
        else:
            json_dict = json.loads(json_str)
            self.ID = json_dict['ID']
            self.form_type = json_dict['form_type']
            self.cur_level_no = json_dict['cur_level_no']
            self.cur_level = Level(json_str = json_dict['cur_level'])
            self.data = json_dict['data']
            self.applicant_id = json_dict['applicant_id']
            self.status = json_dict['status']
        
        # with DbManager().get_client() as c:
        #     forms = c['PaperlessWorkflow']['Forms']
        #     if c.PaperlessWorkflow.Forms.count_documents({"_id":id}, limit=1)>0:
        #         print('found')
        #     else:
        #         print('not found')

    def save_to_db(self):
        # print(json.dumps(self.__dict__))
        pass

    def update(self, field_index, u_id, val) -> None:
        # if field_id not in valid_fields:
        #     return
        field_meta = self.cur_level.get_field_at(field_index)

        field_entry = fields.FieldFactory(field_meta, val)
        self.data.append_field(
            u_id, self.cur_level.get_level_no(), field_index, field_entry)

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

    def get_form_info(self) -> dict:
        self.data.get_form_state()

    def save_to_db(self) -> bool:
        pass

    def to_json(self) -> dict:
        json_dict = {}
        json_dict["ID"] = self.ID
        json_dict["form_type"] = self.form_type.to_json()
        json_dict["cur_level_no"] = self.cur_level_no
        json_dict["cur_level"] = self.cur_level.to_json()
        json_dict["applicant_id"] = self.applicant_id
        json_dict["data"] = self.data.to_json()
        json_dict["status"] = self.status
        return json_dict


def main():
    print("hey there")
    f = FormMetaData("leave")

    print(f.form_uid)
    F_instance = Form(0, f, "ssjjjss.gmail.com")
    # F_instance.fill_field(0,"cs20btech11060@iith.ac.in","Ojjas Tyagi")
    # F_instance.fill_field(1,"cs20btech11060@iith.ac.in",date(2023,1,1))
    # F_instance.fill_field(2,"cs20btech11060@iith.ac.in",0)
    # F_instance.get_form_info()

    # F_log=F_instance.data.get_log()
    # print(F_log[0][-1])
    # print(F_log[1][-1])
    # print(F_log[2][-1])

    j = json.dumps(F_instance.to_json())
    print(j)
    print("="*50)
    F2 = Form(json_str=j)



if __name__ == "__main__":
    main()

# '_id': '643ff5dd326f4d6638bea447'

# a = Form('643ff5dd326f4d6638bea447')
