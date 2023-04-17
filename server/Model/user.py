class User:
    def __init__(self) -> None:
        pass
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