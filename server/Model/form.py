import time
from formMetaData import FormMetaData
from level import Level
# import sys
# sys.path.insert(1, '/home/ojjas/PaperlessWorkflow_IITH/server/Controller')
# print(sys.path)
# from Controller import fields 
import fields
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
        field_meta=self.cur_level.get_field_at(field_index)
        #Later replace by meta classes ,for now dum dum if else
        
        field_entry=fields.FieldFactory(field_meta,val)
        self.log.append((time.time(),u_id, self.cur_level.get_level_no() ,field_index ,field_entry))
        # Should be something like Field(type,val)

    def get_form_info(self,till_layer:int) ->dict:
        ret={}
        for x in range(till_layer):
            for y in range(self.form_type.get_field_cnt_at_level(x)):
                ret[(x,y)]=(0,0)
        for ele in self.log:
            kee=(ele[2],ele[3])
            if  kee in ret :
                if(ret[kee][0]< ele[0]):
                    ret[kee]=(ele[0],ele[4])
            else:
                ret[kee]=(ele[0],ele[4])
        print(ret)#IDK why this guy doesnt use the TExtbox print method,probably some inheritance bs
        return ret

    def save_to_db() -> bool:
        pass
def main():
    print("hey there")
    f = FormMetaData("leave")
    
    print(f.form_uid)
    F_instance=Form(0,f)
    F_instance.update(0,"Pojeshawar","Pojus")
    F_instance.get_form_info(2)
    print(F_instance.log[0][-1])
  
if __name__=="__main__":
    main()

