from data import Data
from formMetaData import FormMetaData
from level import Level
from datetime import date
# import sys
# sys.path.insert(1, '/home/ojjas/PaperlessWorkflow_IITH/server/Controller')
# print(sys.path)
# from Controller import fields 
import fields
class Form:

    def __init__(self,_ID,_form_type : FormMetaData,submitter_id :str) -> None:
        self.ID=_ID
        self.form_type=_form_type
        self.cur_level=Level(*self.form_type.get_level(0),[],0)#Get 0th layer from metadata
        self.data=Data()
        self.applicant_id=submitter_id

    def fill_field(self,field_index,u_id,val) -> None:
        # if field_id not in valid_fields:
        #     return
        field_meta=self.cur_level.get_field_at(field_index)
        
        field_entry=fields.FieldFactory(field_meta,val)

        self.data.append(u_id, self.cur_level.get_level_no() ,field_index ,field_entry)
        # Should be something like Field(type,val)

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

