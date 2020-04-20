import json
import os.path

dict_Type = {"כדורסל":("כדורסל","מגרש משולב","מגרש ספורט משולב"),"כדורגל":("כדורגל","מגרש משולב","מגרש ספורט משולב"),"קט-רגל":("קט רגל","קטרגל"),"מגרש-מיני":("מגרש מיני"),"מגרש טניס":("מגרש טניס"),"בריכת-שחיה":("בריכת שחיה"),"מגרש-חול":("מגרש חול"),"אתלטיקה-קלה":("אתלטיקה קלה"),"פארק-כושר":("פארק כושר","כושר גופני"),"אולם-ספורט":("אולם ספורט","מתקן ספורט כללי"),"כל-המתקנים":None}
dict_neighborho = {"א":("שכונה א'", "א'", "א"), "ב":("ב'"), "ג":("ג'", "ג", "שכונה ג'"), "ד":("ד'", "שכ' ד'"), "ה":("ה' הישנה", "ה'"), "ו":("ו' החדשה", "ו' הישנה", "שכ' ו' הישנה"), "ט":("ט'", "שכ' ט'", "שכונה ט'"), "יא":("יא", "י\"א", "יי\"א", "יא'"), "עיר-עתיקה":("עיר עתיקה"), "נווה-זאב":("נווה זאב"), "נאות-לון":("נאות לון"), "נווה-נוי":("נווה נוי"), "רמות":("רמות"), "נחל-עשן":("נחל עשן"), "רמב\"ם":("רמב\"ם"), "נחל-בקע":("נחל בקע"), "פלח-7":("פלח 7")}
class Sports_facilities():

    def __init__(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "sport.json")
        with open(path,encoding="utf8") as f:
            self.distros_dict = json.load(f)

    def get_by_type_neighborho(self, neighborho, facility_type):
        lst_result = []
        lst_tmp = []
        lst_neig = dict_neighborho[neighborho]
        lst_f_type = dict_Type[facility_type]
        for distro in self.distros_dict:
            if (distro['neighborho'] in lst_neig):
                if(lst_f_type != None):
                    for ty in lst_f_type:
                        if(ty in distro['Type']):
                            lst_result.append(distro)
                else:
                    lst_result.append(distro)

        return lst_result


    def get_distros_dict(self):
        return self.distros_dict


