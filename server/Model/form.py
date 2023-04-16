import time
from formMetaData import FormMetaData
from level import Level
from server.Controller import fields 
class Form:

    def __init__(self,_ID,_form_type : FormMetaData) -> None:
        self.ID=_ID
        self.form_type=_form_type
        self.cur_level=Level(*self.form_type.get_level(0),[],0)#Get 0th layer from metadata
        self.log=[]

        pass

    def update(self,field_index,u_id,val) -> None:
        # if field_id not in valid_fields:
        #     return
        field_meta=self.cur_level(field_index)
        #Later replace by meta classes ,for now dum dum if else
        
        if field_meta[1]=="textbox":
            field_entry=fields.Textbox(field_meta[0],val)
        elif field_meta[1]=="date":
            field_entry=fields.Date(field_meta[0],val)
        elif field_meta[1]=="dropdown":
            field_entry=fields.Dropdown(field_meta[0],field_meta[2],val)
        elif field_meta[1]=="file":
            field_entry=fields.File(field_meta[0],val)
        else :
            raise Exception("INVALID FIELD VALUE")
        self.log.append((time.time(),u_id,self.cur_level.get_level_no(),field_index,field_entry))
        # Should be something like Field(type,val)

    def get_form_info(self) ->dict:
        #returns a json 
        pass