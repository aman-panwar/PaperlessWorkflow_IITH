class User:
    def __init__(self) -> None:
        pass
    def get_user_info() -> dict:
        '''Return the user info as a json dictionary.'''
        pass
    def update(self, changes: dict) -> bool:
        """ Updates the field to the fields provides as json.
        
        Args:
            changes (dict): json with field from User.get_user_info()

        Returns:
            bool: true iff the save into database was successful. 
        """
        
        # The following is temporary code to test out request handling, feel free to delete it. Note that this will break the 'Controller/routes.py' file
        
    def addInfo(self, data):
        self.name = data['name']
        self.email = data['email']
        self.dob = data['dob']
