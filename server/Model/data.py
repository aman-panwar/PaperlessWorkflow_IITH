class Data:
    """Holds the log value as json

    NOTE: we need to come up with exactly what field out log is supposed to hold
    """
    def __init__(data: str = "") -> None:
        """takes the string saved in db and converts it into log info

        Args:
            data (str, optional): string to make json file from. Defaults to "".
        """
        pass
    def append(data: dict):
        """adds the data to the log
           
        Args:
            data (dict): info as a dictionary
        """
    def get_form_state(self)->dict:
        """return the cur state of form instance

        Returns:
            dict: form as json
        """
    def get_log(self)->str:
        """return log of the form instance

        Returns:
            str: _description_
        """