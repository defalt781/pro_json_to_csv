# json to csv converter - converter structured json data to csv. is assigned to3 Hussien Al-wjeeh
import json
import csv
import pyfiglet
import traceback

# هذه الداله تقوم بطباعه 
def PrintFun():
    text = "                      JSON to CSV"
    text2= "                    Dr.Sundus                   Eng.HUSSIEN"
    ascii_art = pyfiglet.figlet_format(text)
    ascii_art2 = pyfiglet.figlet_format(text2)
    print(ascii_art)
    print(ascii_art2)
    print("---------------------------------<[🌷 Hello My D.Sundus 🌷 ]>---------------------------------------")
    print("Select the transfer number : ")
    print("-----------------")
    print("[01] Json to Csv |")
    print("-----------------")
    print("-----------------")
    print("[02] CSV to Json |")
    print("-----------------")
    print("----------")
    print("[03] Exit |")
    print("----------")

# كلاس الاداة كامل 
class JsonTocsvConverter:
# هذه الداله عرفنا فيها المتغيرات 

    def __init__(self,file_path):
        self.file_path = file_path
        self.data = None
        # هذه الداله تتحقق من محتوى ملف ال csv وتخزين البيانات الى متغير 
    def read_csv(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                self.data = [row for row in csv_reader]
                
            if not self.data:
                print("Error: The CSV file is empty or contains no data.")
                return False

            print("The CSV file has been uploaded successfully ^_^")
            return True

        except FileNotFoundError:
            print(f"Error: CSV file not found ==> {self.file_path}")
            return False

        except Exception as e:
            print(f"An unexpected Error occurred while reading the CSV file: {e}")
            traceback.print_exc()
            return False

    # هذه الداله تقوم بقرائة محتوى ملف  json وتخزينه في متغير وتحليل الاخطاء 
    def read_json(self):
        try :
            with open(self.file_path,'r',encoding='utf-8') as file :
                loaded_date = json.load(file)

            if isinstance(loaded_date,list):
                self.data = loaded_date

            elif isinstance(loaded_date,dict):
                list_found = False
                for value in loaded_date.values():
                    if isinstance(value,list) and value:
                        self.data = value
                        list_found = True
                        break

                if not list_found:
                    print("Error : The json file does not contain a list of data to convert.")
                    return False

            else:
                print("Error : The json file format is not a list or dictionary of data .")
                return False

            print("The file has been uploaded successfully ^_^ ")
            return True

        except FileNotFoundError:
            print(f"Error : File not found ==> {self.file_path}")
            return False
        except json.JSONDecodeError:
            print(f"Error : In File formatting ==> {self.file_path}")
            return False
        except Exception as e:
            print("An unexpected Error occurred ==> {e}")
            traceback.print_exc()
            return False

# هذه تقوم بانشاء ملف csv وتحويل النص من json الى csv وتخزينه في الملف الذي انشاناه            
    def convert_to_csv(self,csv_file_path):

        if not self.data:
            print("Error : Empty json file or no data to convert ")
            return False

        try:
            headers = set()
            for row in self.data:
                if isinstance(row, dict):
                    headers.update(row.keys())
                else:
                    print(f"Skipping non-dictionary data: {row}")    

            headers = list(headers)

            with open(csv_file_path,'w',newline='',encoding='utf-8') as file:
                csv_writer = csv.DictWriter(file,fieldnames=headers,restval='')
                csv_writer.writeheader()
                for row in self.data:
                    csv_writer.writerow(row)

            print(f"The file has been successfully converted and saved in :{csv_file_path}")
            return True
        except Exception as e:
            print(f"An Error occurred while writing the csv file {e}")
            traceback.print_exc()
            return False

    def convert_to_json(self,csv_file_path,json_file_path):
        data = []
        try:
            with open(csv_file_path,'r',encoding='utf-8')as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    data.append(row)

            if not data:
                print("Error: The CSV file is empty or contains no data.")
                return False
        

            with open(json_file_path,'w',encoding='utf-8')as file:
                json.dump(data,file,indent=4)

            print(f"The file has been successfully converted and saved in :{json_file_path}")
            return True
            
        except FileNotFoundError:
            print(f"Error : csv file not found ==> {csv_file_path}")
            return False
            
        except csv.Error as e:
            print(f"Error: An error occurred while reading the CSV file: {e}")
            return False
    
        except Exception as e:
            print(f"An unexpected Error occurred : {e}")
            traceback.print_exc()
            return False


            

if __name__=="__main__":
    PrintFun()
    while True:
        number_transfer = input("Choose a number 🔢 : ")

        if number_transfer == '1' :

            file_path = input("Enter the name of the file you want to convert with an extension 📁 :")
            converter = JsonTocsvConverter(file_path)

            if converter.read_json():
                csv_file_path = input("Enter the name of the new csv file (with .csv extension ) 📁 :")
                #التحقق من امتداد الملف 
                if not csv_file_path.endswith('.csv'):
                    csv_file_path += '.csv'

                converter.convert_to_csv(csv_file_path)
            break

        elif number_transfer == '2' :

            csv_file_path = input("Enter the name of the csv file to convert(with  extension ) 📁 :")
           # file_path = input("Enter the name of the new json file (with .json extension ) 📁 :")
            converter = JsonTocsvConverter(csv_file_path)
            if converter.read_csv():
                json_file_path = input("Enter the name of the new JSON file (without extension) 📁 :")
                #التحقق من امتداد الملف 
                if not json_file_path.endswith('.json'):
                    json_file_path += '.json'

                  # استخدام نفس الاوبجكت لتحويل البيانات 
                converter.convert_to_json(csv_file_path,json_file_path)
            break

        elif number_transfer == '3' :
            print("Exit 💬.............")
            break
        else :
            print(f"[{number_transfer}]:💢 invalid number.. ♻ ")
