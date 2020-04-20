import json
import os.path


lst_Type = ("כדורסל","מגרש משולב","פארק כושר","קטרגל","כושר גופני","מתקן ספורט כללי","אתלטיקה קלה","מגרש חול","בריכת שחיה","מגרש מיני","מגרש טניס","קט רגל","אולם ספורט","כדורגל","מגרש ספורט משולב",)
class Sports_facilities():

    def __init__(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "sport.json")
        with open(path,encoding="utf8") as f:
            self.distros_dict = json.load(f)

    def get_by_type_neighborho(self,facility_type,neighborho):
        lst_result = []
        lst_tmp = []
        for distro in self.distros_dict:
            if(facility_type in distro['Type'] and neighborho in distro['neighborho']):
                lst_tmp.append(distro)
        if (lst_tmp != []):
            have_type = False
            for distro in lst_tmp:
                for type_facility in lst_Type:
                    if (type_facility in distro['Type']):
                        have_type = True
                        break
                if (have_type):
                    lst_result.append(distro)
                have_type = False
        return lst_result

    def get_by_neighborho(self,neighborho):
        lst_result = []
        lst_tmp = []
        for distro in self.distros_dict:
            if(neighborho in distro['neighborho']):
                lst_tmp.append(distro)
        if (lst_tmp != []):
            have_type = False
            for distro in lst_tmp:
                for type_facility in lst_Type:
                    if (type_facility in distro['Type']):
                        have_type = True
                        break
                if (have_type):
                    lst_result.append(distro)
                have_type = False
        return lst_result

    def get_distros_dict(self):
        return self.distros_dict


