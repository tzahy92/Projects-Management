import json
import os.path

from dns._compat import xrange

dict_Type = {"כדורסל":("כדורסל","מגרש משולב","מגרש ספורט משולב"),"כדורגל":("כדורגל","מגרש משולב","מגרש ספורט משולב"),"קט-רגל":("קט רגל","קטרגל"),"מגרש-מיני":("מגרש מיני"),"מגרש-טניס":("מגרש טניס"),"בריכת-שחיה":("בריכת שחיה"),"מגרש-חול":("מגרש חול"),"אתלטיקה-קלה":("אתלטיקה קלה"),"פארק-כושר":("פארק כושר","כושר גופני"),"אולם-ספורט":("אולם ספורט","מתקן ספורט כללי"),"כל-המתקנים":None}
dict_neighborho = {"א":("שכונה א'", "א'", "א"), "ב":("ב'"), "ג":("ג'", "ג", "שכונה ג'"), "ד":("ד'", "שכ' ד'"), "ה":("ה' הישנה", "ה'"), "ו":("ו' החדשה", "ו' הישנה", "שכ' ו' הישנה"), "ט":("ט'", "שכ' ט'", "שכונה ט'"), "יא":("יא", "י\"א", "יי\"א", "יא'"), "עיר-עתיקה":("עיר עתיקה"), "נווה-זאב":("נווה זאב"), "נאות-לון":("נאות לון"), "נווה-נוי":("נווה נוי"), "רמות":("רמות"), "נחל-עשן":("נחל עשן"), "רמב\"ם":("רמב\"ם"), "נחל-בקע":("נחל בקע"), "פלח-7":("פלח 7")}
dict_light = {"לא":("לא","אין","אין תאורה",""),"כן":("כן","קיימת תאורה")}
class Sports_facilities():

    def __init__(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "Sport.json")
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
                    if(type(lst_f_type) is tuple):
                        for ty in lst_f_type:
                            if(ty in distro['Type']):
                                lst_result.append(distro)
                    else:
                        if (lst_f_type in distro['Type']):
                            lst_result.append(distro)
                else:
                    lst_result.append(distro)

        return lst_result


    def get_distros_dict(self):
        return self.distros_dict

    def delete_facility(self,facility):
        for obj in self.distros_dict:
            if(obj['Type']== facility['Type'] and obj['Name']== facility['Name'] and
                    obj['neighborho']== facility['neighborho'] and obj['Operator']== facility['Operator'] and obj['Owner']== facility['Owner']):
                self.distros_dict.remove(obj)
                break
        # print(self.distros_dict)
        ##x= self.distros_dict
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "temp.json")
        ##with open(path, 'w') as fp:
         ##   json.dump(x, fp, indent=4)
        jsonFile = open(path, "w+",encoding='utf-8')
        x= json.dumps(self.distros_dict,indent=4)
        jsonFile.write(x)
        jsonFile.close()

    def updateFacility(self, originalFacility, newFacility):
        for obj in self.distros_dict:
            if (obj['Type'] == originalFacility['Type'] and obj['Name'] == originalFacility['Name'] and
                    obj['neighborho'] == originalFacility['neighborho'] and obj['Operator'] == originalFacility[
                        'Operator'] and obj[
                        'Owner'] == originalFacility['Owner']):

                obj.update(newFacility)
                break
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "temp.json")
        ##with open(path, 'w') as fp:
        ##   json.dump(x, fp, indent=4)
        jsonFile = open(path, "w+", encoding='utf-8')
        x = json.dumps(self.distros_dict, indent=4)
        jsonFile.write(x)
        jsonFile.close()


def modular_filtering(lst_of_dict_facility,type_,name_of_filter):
    tmp = []
    filtered_facilities = []
    if(type_ == "lighting"):
        tmp = dict_light[name_of_filter]
    for facility in lst_of_dict_facility:
        if(facility[type_] in tmp):
            filtered_facilities.append(facility)
    return filtered_facilities




def Add_New_Facility(new_Facilities):
    print(new_Facilities)
    with open('PM/Sport.json', encoding="utf-8") as Sport_Json:
        data = json.load(Sport_Json)

    temp = data['Sports']
    temp.append(new_Facilities)

    with open('PM/Sport.json', 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    """for sport in data['Sports']:
        print(sport)"""
    Sport_Json.close()
    file.close()



"""""
####try to add
with open('Sport.json', encoding='utf-8') as Sport_Json:
    data = json.load(Sport_Json)

temp = data['Sports']
y = {
    'Type': 'New_Facilities',
    'Name': 'ניס',
    'street': '',
    'HouseNumbe': '0.0',
    'neighborho': "None",
    'Operator': 'כיוונים',
    'Seats': '0.0',
    'Activity': 'כן',
    'fencing': 'כן',
    'lighting': 'כן',
    'handicappe': 'כן',
    'condition': '7777',
    'Owner': 'כיוונים',
    'ForSchool': '777',
    'associatio': '77',
    'SportType': '777',
    'lat': '7777',
    'lon': '7777'
}

temp.append(y)

with open('Sport.json', 'w') as f:
    json.dump(data, f, indent=4)

for sport in data['Sports']:
    print(sport)
"""""


