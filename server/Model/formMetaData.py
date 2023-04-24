import json
import os

filepath = os.path.dirname(os.path.abspath(__file__))+"/forminfo.json"
class FormMetaData:
    """
    Contains metadata for every form instance.

    Attributes:
        form_uid (str): unique id of the form
        display_name (str): display name of the form
        n_levels (int): number of levels in the chain of approval (including applicant level)
        users (list): contains the list of users at each level
        req_fields (list): contains the list of required fields at each level
    """
    def __init__(self, form_uid, json_str:str = None):

        if json_str ==None:
            with open(filepath) as f:
                forminfo = json.load(f)
            if form_uid not in forminfo:
                raise ValueError(f"Form with unique id '{form_uid}' does not exist!")
            
            forminfo = forminfo[form_uid]

            self.form_uid = form_uid
            self.display_name = forminfo["name"]
            self.n_levels = forminfo["n_levels"]
            self.users = [[]]*self.n_levels
            self.req_fields = [[]]*self.n_levels


            for i, level in enumerate(forminfo["level_data"]):
                self.users[i] = level["users"]
                self.req_fields[i] = level["req_fields"]
        else:
            json_dict = json.loads(json_str)
            self.form_uid = json_dict["form_uid"]
            self.display_name = json_dict["display_name"] 
            self.n_levels = json_dict["n_levels"]
            self.users = json_dict["users"]
            self.req_fields = json_dict["req_fields"]
      
    def get_level(self,index):
        return self.users[index],self.req_fields[index]
    
    def get_field_cnt_at_level(self,index):
        return len(self.req_fields[index])
    def to_json(self)->str:
        json_dict = {}
        json_dict["form_uid"]=self.form_uid
        json_dict["display_name"] = self.display_name
        json_dict["n_levels"] = self.n_levels
        json_dict["users"] = self.users
        json_dict["req_fields"] = self.req_fields
        return json.dumps(json_dict)
# Testing code
# f = FormMetaData("leave")
# print(f.form_uid)
# print(f.display_name)
# print(f.n_levels)
# print(f.users[2])
# print(f.req_fields[2])
