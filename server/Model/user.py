class User:
    def __init__(self,email) -> None:
        self.user_key=email
        self.pending_approvals=[]
        self.submitted_forms=[]
        self.notifications=True
        self.not_freq="Daily"

    def change_not_freq(self,new_freq):
        valid_list=["Daily","Weekly","Per_Form"]
        if new_freq in valid_list:
            self.not_freq=new_freq
        else:
            raise Exception("Invalid frequency selected")
    
    def enable_not(self,notif_state):
        if notif_state:
            self.notifications=True
        else:
            self.notifications=False
            
    def get_user_info() -> dict:
        '''Return the user info as a json dictionary.'''
        pass
    def update(changes: dict) -> bool:
        """ Updates the field to the fields provides as json.
        
        Args:
            changes (dict): json with field from User.get_user_info()

        Returns:
            bool: true iff the save into database was successful. 
        """