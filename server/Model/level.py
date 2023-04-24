import json
class Level:
    def __init__(self,_users_id=None,_fields=None,_approvers_id=None,_lvl_no=None, json_str = None) -> None:
        if json_str==None:
            self.fields=_fields
            self.total_fields=len(_fields)
            self.u_id=_users_id
            self.a_id=_approvers_id
            self.lvl=_lvl_no
        else:
            json_dict = json.loads(json_str)
            self.fields=json_dict['fields']
            self.total_fields=json_dict['total_fields']
            self.u_id=json_dict['u_id']
            self.a_id=json_dict['a_id']
            self.lvl=json_dict['lvl']
    
    def get_field_at(self,index):
        if(index> len(self.fields)):
            raise Exception("Invalid index requested")
        return self.fields[index]
    
    def get_level_no(self):
        return self.lvl
    
    def get_tot_fields(self):
        return self.total_fields
    
    def to_json(self):
        json_dic = {}
        json_dic["fields"]=self.fields
        json_dic["total_fields"]=self.total_fields
        json_dic["u_id"]=self.u_id
        json_dic["a_id"]=self.a_id
        json_dic["lvl"]=self.lvl
        return json.dumps(json_dic)