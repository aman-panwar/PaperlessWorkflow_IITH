class Level:
    def __init__(self,_users_id,_fields,_approvers_id,_lvl_no) -> None:
        self.fields=_fields
        self.total_fields=len(_fields)
        self.u_id=_users_id
        self.a_id=_approvers_id
        self.lvl=_lvl_no

    def get_field_at(self,index):
        if(index> len(self.fields)):
            raise Exception("Invalid index requested")
        return self.fields[index]
    
    def get_level_no(self):
        return self.lvl
    
    def get_tot_fields(self):
        return self.total_fields