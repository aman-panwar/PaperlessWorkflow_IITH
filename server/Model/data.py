import time
import json
from fields import *


class Data:
    """Holds the log value as json

    """

    def __init__(self, data: str = "", inp_dict: dict = None) -> None:
        """initializes the data object

        Args:
            data (str, optional): _description_. Defaults to "".
        """
        json_dict = {}
        if inp_dict == None:
            json_dict['log'] = []
            json_dict['approval_log'] = []
        else:
            json_dict = inp_dict
            temp = []
            for l in json_dict['log']:
                fe= l['field_entry']
                arg_list = [fe['display_name'],fe['value']]
                if 'values_list' in fe.keys():
                    arg_list = arg_list[0:-1]+ [fe['values_list']]+ [arg_list[-1]]
                print(arg_list)
                l['field_entry'] = FieldFactory(field_type=fe['field_type'],arg_list=arg_list)
                temp.append(l)
            json_dict['log'] = temp

        self.log = json_dict['log']
        self.approval_log = json_dict['approval_log']

    def to_dict(self):
        json_dict = {}
        json_dict["log"] = self.log
        for l in json_dict['log']:
            #print(type(l['field_entry']), l['field_entry'])
            l['field_entry'] = l['field_entry'].to_dict()
        json_dict["approval_log"] = self.approval_log
        return json_dict

    def append_field(self, time: time.time, u_id: str, level_no: int, field_index: int, field_entry: Field):
        """_summary_

        Args:
            u_id (str): user_id who made this update
            level_no (int): The level at which this update is being made
            field_index (int): the index of the field where update is being made
            field_entry (Field): The actual field value getting stored
        """
        # it was storing actual time of save. i ask the caller for time now
        # also shouldn;t log save multiple fields in one entry. i'e all the field filled by the user
        # this works too but we are saving unnecessary data... :(
        self.log.append({'time': time,
                         'uid': u_id,
                         'level_no': level_no,
                         'field_index': field_index,
                         'field_entry': field_entry})

    def append_approval(self, time: time.time, u_id: str, level_no: int, action: str, remarks: str):
        self.approval_log.append({'time': time,
                                  'uid': u_id,
                                  'level_no': level_no,
                                  'action': action,
                                  'remark': remarks})

    def get_form_state(self) -> dict:
        """return the cur state of form instance

        Returns:
            dict: form as json
        """
        ret = {}
        for ele in self.log:
            kee = (ele[2], ele[3])
            if kee in ret:
                if(ret[kee][0] < ele[0]):
                    ret[kee] = (ele[0], ele[4])
            else:
                ret[kee] = (ele[0], ele[4])
        return ret

    def get_log(self) -> list:
        """returns log made so far

        Returns:
            list: the object log
        """
        return self.log

    def get_approval_log(self) -> list:
        return self.approval_log

    def get_update_cnt(self) -> int:
        return len(self.log)

    def get_field_cnt(self) -> int:
        ret = set()
        for ele in self.log:
            key = (ele[2], ele[3])
            ret.add(key)
        return len(ret)

# d = Data()
# # d.append_approval(time.time(), "sd", "sd", "ds", "SDf")
# # time.sleep(1)
# # d.append_approval(time.time(), "sd", "sd", "ds", "SDf")
# f = Dropdown("dfdf", ['sdfsd', 'kkkkk'],"SDFsd")
# d.append_field(time.time(), "sdf", 4, 34, f)
# dic = d.to_dict()
# print("="*40)


# nd = Data(inp_dict=dic)
# print(nd.to_dict())
