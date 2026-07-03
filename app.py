import json
import os
import sys

data = {
    "bootcamp": {
        "title": "karvand python",
        "year": 2026
    },
    "karvands": []
}


def add_def():
    person = {}
    try:
        person["id"] = input("please enter id\n")
        person["fullname"] = input("enter fullname:\n")
        person["email"] = input("enter email :\n")
        person["city"] = input("enter city :\n")
        person["education"] = {
            "degree" : input("enter Degree:\n"),
            "field" : input("enter field\n")
        }
    except ValueError:
        print("There is been a problem, Try again\n")
    while True:
        try:
            skill_num =int(input("enter number of skills\n"))
            break
        except ValueError:
            print("you didn't enter a number. Try Again!\n")
    person["skills"] = []  
    for i in range(skill_num):  
        skill = {
                "name": input("skill name\n"),
                "level": input("skill level:\n")
            }
        while True:
            try:
                xx = int(input("score\n"))
                if xx<=100 and xx>=0:
                    skill["score"] = xx
                    break
                else:
                    print("score must be between 0-100\n")
            except ValueError:
                print("score must be a number❌\n Try again\n")
        person["skills"].append(skill)
    data["karvands"].append(person)
    try:
        with open("G:\AI_Course\week2\HW\karvand_manager\data\data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("saved successfully✅\n")
    except PermissionError:
        print("not allowed to save the data here!\n")
    except OSError:
        print("There was an error saving the file!\n")
    except Exception as e:
        print("unexpected error!\n", e)

def show_def():
    try:
        with open("G:\AI_Course\week2\HW\karvand_manager\data\data.json.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        print(data)
        if data is None:
            print("empty list!\n")
        else:
            for karvand in data["karvands"]:
                print(f"""
                name : {karvand["fullname"]}
                email: {karvand["email"]}
                city : {karvand["city"]}
                education field : {karvand["education"]["field"]}
                education degree : {karvand["education"]["degree"]}
                skills :
                """)
                for skill in karvand["skills"]:
                    print(f"""
                        skill name : {skill['name']}
                        skill level : {skill['level']}
                        skill score : {skill['score']}
                    """)
    except FileNotFoundError:
        print("file not found!\n")
    except json.JSONDecodeError:
        print("file content was not standard!")

def search_def():
    try:
        
        with open("G:\AI_Course\week2\HW\karvand_manager\data\data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        if data is None:
                print("empty list!\n")
        else:
            search_id = input("enter the id of karvand you are looking for:\n")
            for karvand in data["karvands"]:
                if karvand["id"]==search_id:
                    print(f"""
                    name : {karvand["fullname"]}
                    email: {karvand["email"]}
                    city : {karvand["city"]}
                    education field : {karvand["education"]["field"]}
                    education degree : {karvand["education"]["degree"]}
                    skills :
                    """)
                    for skill in karvand["skills"]:
                        print(f"""
                            skill name : {skill['name']}
                            skill level : {skill['level']}
                            skill score : {skill['score']}
                        """)
                    break
                else:
                    print("karvand not found!\n")
    except FileNotFoundError:
        print("file not found!\n")
    except json.JSONDecodeError:
        print("file content was not standard!")

def edit_def():
    try:
        with open("G:\AI_Course\week2\HW\karvand_manager\data\data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        if data is None:
            print("empty list!\n")
        else:
            search_id = input("enter id to edit:\n")
            found = False
            for karvand in data["karvands"]:
                if karvand["id"] == search_id:
                    try:
                        edit_input = input("""witch of this attributes you want to change
                            1 . email
                            2 . city
                            3 . degree
                            4 . field
                            """)
                        if edit_input == 1 or edit_input == "email":
                            karvand["email"] = input("enter new email\n")
                        elif edit_input == 2 or edit_input == "city":
                            karvand["city"] = input("new city:\n")
                        elif edit_input == 3 or edit_input == "degree":
                            karvand["education"]["degree"]=input("new degree:\n")
                        elif edit_input == 4 or edit_input == "field":
                            karvand["education"]["field"]=input("new degree:\n")
                    except:
                        print("invalid input\n")
                    found = True
                    break
            if found:
                with open("data/data.json", "w", encoding="utf-8") as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)
                print("edited!\n")
            else:
                print("karvand not found!\n")
    except FileNotFoundError:
        print("file not found")
    except json.JSONDecodeError:
        print("not a standard json file!\n")

def delete_def():
    try:
        with open("G:\AI_Course\week2\HW\karvand_manager\data\data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        search_id = input("enter id to remove:\n")
        found = False
        for karvand in data["karvands"]:
            if karvand["id"] == search_id:
                data["karvands"].remove(karvand)
                found = True
                break

        if found:
            with open("G:\AI_Course\week2\HW\karvand_manager\data\data.json", "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            print("karvand was deleted!\n")
        else:
            print(f"no karvand found with id : {search_id}\n")

    except FileNotFoundError:
        print("file not found")
    except json.JSONDecodeError:
        print("not a standard json file!\n")

while True:
    try:
        user_input = input("""Menu:\nchoose one of the items below:\n
            1. add karvand
            2. show all karvands
            3. searching karvands by their IDs
            5. edit karvand information
            6. delete karvand
            7. exit
            """).lower()
        if user_input is None:
                print("please type one of the functions mentioned before!\n")
        elif user_input=="add karvand" or user_input=="1":
            data = add_def()      
        elif user_input =="show all karvands" or user_input =="2":
            show_def('data.txt')
        elif user_input=="earching karvands by their IDs" or user_input=="3":
            search_def()
        elif user_input=="edit karvand information" or user_input=="5":
            edit_def()
        elif user_input =="delete karvand" or user_input =="6":
            delete_def()
        elif user_input == "exit" or user_input == "7":
            print("GoodBye")
            break
        else:
            print("you did'nt choose correctly. try again!\n")

    except:
        print("you did'nt choose correctly. try again!\n")
