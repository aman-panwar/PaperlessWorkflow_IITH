import time
from formMetaData import FormMetaData
class Form:

    def __init__(self,_ID,_form_type : FormMetaData) -> None:
        self.ID=_ID
        self.form_type=_form_type
        self.cur_level=self.form_type.get_level(0)#Get 0th layer from metadata
        self.log=[]

        pass

    def update(self,field_index,u_id,val) -> None:
        # if field_id not in valid_fields:
        #     return
        # self.log.append((time.time(),field_id,u_id,val))
        # Should be something like Field(type,val)
        pass
    
    def get_form_info(self) ->dict:
        #returns a json 
        pass