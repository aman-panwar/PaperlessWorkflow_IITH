from data import Data
from formMetaData import FormMetaData
from level import Level
from database_manager import DbManager
import json
from datetime import date
import fields
import json
from bson.objectid import ObjectId
import time

"""
Form can be init with json string but i dont see any use case where we could use this feature effectively
So For now it remains a in the code. We may remove it later. 
Json strings are useful for other Classes tho.
"""

"""All updates to db follow optimistic concurrency control"""

"""DONT FUCK AROUND WITH VERSION. I WILL MAKE IT PRIVATE IN LATER STAGES"""


class Form:

    def __init__(self, ID: str = None, inp_dict: dict = None) -> None:
        """initialises the Form first with json_str. If json_str is not provided
        (or is None) then inits with ID (retrieves info from db). If both json_str
        and ID are not provided or is None then init an empty form

        Args:
            ID (str, optional): ID corresponding to the db
            json_str (str, optional): json string from a 

        Raises:
            Exception: _description_
        """
        data_dict = {}  # will eventually populate form entries
        if inp_dict != None:
            # init form with json_str
            data_dict = inp_dict
        elif ID != None:
            # init form from db use _id= ID
            with DbManager().get_client() as c:
                forms = c['PaperlessWorkflow']['Forms']
                data_dict = forms.find_one({"_id": ObjectId(ID)})
                if data_dict == None:
                    raise Exception(f"Did not find object with id: {ID}")

        # populating form entries with json_dict
        self.ID = str(data_dict['_id']) if '_id' in data_dict.keys() else None
        self.form_meta = FormMetaData(
            input_dict=data_dict.setdefault('form_meta', None))
        self.cur_level_no = data_dict.setdefault('cur_level_no', None)
        self.cur_level = Level(
            inp_dict=data_dict.setdefault('cur_level', None))
        self.data = Data(inp_dict=data_dict.setdefault('data', None))
        self.applicant_id = data_dict.setdefault('applicant_id', None)
        self.status = data_dict.setdefault('status', None)
        self.version = data_dict.setdefault('version', 0)

    def save_to_db(self) -> bool:
        """saves the form to db

        Returns:
            bool: if a change was made to the db. returns False when update is not valid or if no change was made to the db entry 
        """
        with DbManager().get_client() as c:
            forms = c['PaperlessWorkflow']['Forms']

            search_field = {'version': self.version}
            if self.ID != None:
                search_field['_id'] = self.ID

            my_data = self.to_dict()
            my_data.pop('_id', None)
            my_data['version'] += 1

            try:
                replace_result = forms.replace_one(
                    search_field, my_data, upsert=True)
            except:
                return False
            self.ID = replace_result.upserted_id
            return replace_result.acknowledged

    def delete_from_db(self) -> bool:
        """deletes the entry from db

        Returns:
            bool: if entry was deleted successfully. will return False incase an update was made to a form or form doesnt exist in db
        """
        with DbManager().get_client() as c:
            forms = c['PaperlessWorkflow']['Forms']
            try:
                del_result = forms.delete_one(
                    {"_id": ObjectId(self.ID), 'version': self.version})
            except:
                return False
            return del_result.acknowledged

    def update(self, field_index, u_id, val) -> None:
        # idk what this does ???
        field_meta = self.cur_level.get_field_at(field_index)
        field_entry = fields.FieldFactory(field_meta, val)
        self.data.append_field(
            time.time(), u_id, self.cur_level.get_level_no(), field_index, field_entry)

    def set_form_type(self, form_type: str):
        """only to provide a more intutive to to do form.form_meta.set_type()"""
        self.form_meta = FormMetaData(form_type=form_type)

    def get_form_info(self) -> dict:
        self.data.get_form_state()

    def to_dict(self) -> dict:
        json_dict = {}
        json_dict["_id"] = self.ID
        json_dict["form_meta"] = self.form_meta.to_dict()
        json_dict["cur_level_no"] = self.cur_level_no
        json_dict["cur_level"] = self.cur_level.to_dict()
        json_dict["applicant_id"] = self.applicant_id
        json_dict["data"] = self.data.to_dict()
        json_dict["status"] = self.status
        json_dict['version'] = self.version
        return json_dict

# def main():
#     print("hey there")
#     F_instance = Form(ID='643ff5dd326f4d6638bea447')
#     j = F_instance.to_dict()
#     print(j)
#     print("="*50)
#     F2 = Form()
#     print(F2.ID)
#     print(type(F2.ID))
#     F2.status = "YEEWWWw"
#     print(F2.save_to_db())
#     print(F2.to_dict())
#     print("="*50)
#     print("="*40)
#     print(type(j))
#     print(j)

#     F3 = Form()
#     F3.applicant_id = "aman.panwar2002@gmail.com"
#     print(F3.save_to_db())

#     F4 = Form()
#     F4.applicant_id = "aman.panwar2002@gmail.com"
#     print(F3.save_to_db())


# F = Form()
# print(F.ID)
# F.cur_level_no =90
# F.cur_level.approvers_id = [
#     "aman.panwar2002@gmail.com", "jjk@manga.com", "SDFSDFSDF"]
# print(F.save_to_db())
# print(F.ID)
# if __name__ == "__main__":
#     main()
