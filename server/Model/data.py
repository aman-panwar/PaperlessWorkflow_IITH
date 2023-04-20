import time
from fields import Field
class Data:
    """Holds the log value as json

    """
    def __init__(self,data: str = "") -> None:
        """initializes the data object

        Args:
            data (str, optional): _description_. Defaults to "".
        """
        self.log=[]

    def append(self,u_id : str,level_no :int ,field_index:int ,field_entry: Field):
        """_summary_

        Args:
            u_id (str): user_id who made this update
            level_no (int): The level at which this update is being made
            field_index (int): the index of the field where update is being made
            field_entry (Field): The actual field value getting stored
        """
        self.log.append((time.time(),u_id, level_no ,field_index ,field_entry))

    def get_form_state(self)->dict:
        """return the cur state of form instance

        Returns:
            dict: form as json
        """
        ret={}
        for ele in self.log:
            kee=(ele[2],ele[3])
            if  kee in ret :
                if(ret[kee][0]< ele[0]):
                    ret[kee]=(ele[0],ele[4])
            else:
                ret[kee]=(ele[0],ele[4])
        print(ret)
        return ret
    
    def get_log(self)->list:
        """returns log made so far

        Returns:
            list: the object log
        """
        return self.log
    
    def get_update_cnt(self)->int:
        return len(self.log)
    
    def get_field_cnt(self)->int:
        ret=set()
        for ele in self.log:
            key=(ele[2],ele[3])
            ret.add(key)
        return len(ret)
