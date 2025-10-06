import json

# open & parse json data
with open('ordered_list.json') as data:
  collection = json.load(data)

# ---------------------------------SECTION 1---------------------------------------------
# Functions in this section traverse the whole collection.

# Prints the name of each series in the collection, alphabetically
def series_list():
   list_of_series_names = []
   for series in collection:
      for key, value in series.items():
         series_name = key
         list_of_series_names.append(series_name)
   #print(sorted(list_of_series_names, reverse=False))
   #print(list_of_series_names)
   for name in list_of_series_names:
      print(name)

# Prints all issues in collection (with details)
def get_all():
   for series in collection:
      for key, value in series.items():
            print("\n" + "---" + key + "---\n")
            for issue in value:
               title = issue["title"]
               issue_num = issue["issue"]
               year = issue["year_published"]
               variant = ", ".join(map(str, issue["collectible_criteria"]["variant"]))
               condition = issue["collectible_criteria"]["appraisal_status"] + " " + issue["collectible_criteria"]["condition"]

               printing = ""
               signed_by = ""
               first_appearances = ""
               other_notes = ""

               issue_details = ""

               if issue["print_run"] > 1:
                  printing = issue["print_run"]
                  lastDigit = int(repr(printing)[-1])
                  if lastDigit == 2:
                     printing = f"{printing}nd printing\n"
                  if lastDigit == 3:
                     printing = f"{printing}rd printing\n"
                  if lastDigit in (4, 5, 6, 7, 8, 9, 0):
                     printing = f"{printing}th printing\n"

               if issue["collectible_criteria"]["signature"]["signed"]:
                  signed_by = "signed by " + " and ".join(map(str, issue["collectible_criteria"]["signature"]["person"])) + " on " + " ".join(map(str, issue["collectible_criteria"]["signature"]["placement"])) + "\n"

               if issue["collectible_criteria"]["significant_first_appearances"]:
                first_appearances = "first appearances: " + ", ".join(map(str, issue["collectible_criteria"]["significant_first_appearances"])) + "\n"

               if issue["collectible_criteria"]["other_notable_criteria"]:
                other_notes = "other notes: " + ", ".join(map(str, issue["collectible_criteria"]["other_notable_criteria"])) + "\n"

               issue_details =(title  + " #" + issue_num + "\n" +
                "published in " + year + "\n" +
                printing +
                "variant: " + variant + "\n" +
                "condition: " + condition + "\n" +
                signed_by + first_appearances + other_notes
               )

               print(issue_details)

# Prints all issues in collection (with some details)
def get_all_min():
  for series in collection:
    for key, value in series.items():
       print("\n" + "---" + key + "---\n")
       for issue in value:
          variant = ", ".join(map(str, issue["collectible_criteria"]["variant"]))

          printing = ""
          signed_by = ""

          if issue["print_run"] > 1:
                  printing = issue["print_run"]
                  lastDigit = int(repr(printing)[-1])
                  if lastDigit == 2:
                     printing = f"{printing}nd printing\n"
                  if lastDigit == 3:
                     printing = f"{printing}rd printing\n"
                  if lastDigit in (4, 5, 6, 7, 8, 9, 0):
                     printing = f"{printing}th printing\n"

          if issue["collectible_criteria"]["signature"]["signed"]:
            signed_by = "signed by " + " and ".join(map(str, issue["collectible_criteria"]["signature"]["person"])) + " on " + " ".join(map(str, issue["collectible_criteria"]["signature"]["placement"])) + "\n"

          print(
            issue["title"] + " #" + issue["issue"] + "\n" +
            "published in " + issue["year_published"] + "\n" +
            printing +
            variant + "\n" +
            issue["collectible_criteria"]["appraisal_status"] + " " + issue["collectible_criteria"]["condition"] + "\n" +
            signed_by
          )

# Prints all issues in collection (without details)
def get_all_simplified():
  for series in collection:
    for key, value in series.items():
       print("\n" + key)
       for issue in value:
          print(" #" + issue["issue"]
            #issue["title"] + " #" + issue["issue"] + "\n" 
          )

# Prints all graded issues in collection (with details)
def get_all_graded():
   print("\nAll graded issues in collection:\n")
   for series in collection:
      for key, value in series.items():
            flag = True
            current_series = ""
            for issue in value:
               current_series = issue["title"]

               title = issue["title"]
               issue_num = issue["issue"]
               year = issue["year_published"]
               variant = ", ".join(map(str, issue["collectible_criteria"]["variant"]))
               condition = issue["collectible_criteria"]["appraisal_status"] + " " + issue["collectible_criteria"]["condition"]

               printing = ""
               signed_by = ""
               first_appearances = ""
               other_notes = ""

               issue_details = ""

               if issue["print_run"] > 1:
                  printing = issue["print_run"]
                  lastDigit = int(repr(printing)[-1])
                  if lastDigit == 2:
                     printing = f"{printing}nd printing\n"
                  if lastDigit == 3:
                     printing = f"{printing}rd printing\n"
                  if lastDigit in (4, 5, 6, 7, 8, 9, 0):
                     printing = f"{printing}th printing\n"

               if issue["collectible_criteria"]["signature"]["signed"]:
                  signed_by = "signed by " + " and ".join(map(str, issue["collectible_criteria"]["signature"]["person"])) + " on " + " ".join(map(str, issue["collectible_criteria"]["signature"]["placement"])) + "\n"

               if issue["collectible_criteria"]["significant_first_appearances"]:
                first_appearances = "first appearances: " + ", ".join(map(str, issue["collectible_criteria"]["significant_first_appearances"])) + "\n"

               if issue["collectible_criteria"]["other_notable_criteria"]:
                other_notes = "other notes: " + ", ".join(map(str, issue["collectible_criteria"]["other_notable_criteria"])) + "\n"

               issue_details =(title  + " #" + issue_num + "\n" +
                "published in " + year + "\n" +
                printing +
                "variant: " + variant + "\n" +
                "condition: " + condition + "\n" +
                signed_by + first_appearances + other_notes
               )

               if flag == True and issue["collectible_criteria"]["appraisal_status"] == "graded":
                  print("\n" + "---" + key + "---\n")
                  flag = False

               if current_series is not issue["title"]:
                  flag = True

               if issue["collectible_criteria"]["appraisal_status"] == "graded":
                  print(issue_details)

# Prints all graded issues in collection (without details)
def get_all_graded_simplified():
   print("\nAll graded issues in collection:\n")
   for series in collection:
      for key, value in series.items():
            flag = True
            current_series = ""
            for issue in value:
               current_series = issue["title"]

               title = issue["title"]
               issue_num = issue["issue"]

               #issue_details = ""

               issue_details = (title  + " #" + issue_num)

               if flag == True and issue["collectible_criteria"]["appraisal_status"] == "graded":
                  print("\n" + "---" + key + "---")
                  flag = False

               if current_series is not issue["title"]:
                  flag = True

               if issue["collectible_criteria"]["appraisal_status"] == "graded":
                  print(issue_details)

# ---------------------------------SECTION 2---------------------------------------------
# functions in this section traverse a specified series (e.g. "The Amazing Spider-Man").

# Prints all issues (with details) in a specified series
def get_issues(series_name):
   print("\nCollection of " + series_name + " issues:\n")
   for series in collection:
      for key, value in series.items():
         if key == series_name:
            for issue in value:
               title = issue["title"]
               issue_num = issue["issue"]
               year = issue["year_published"]
               variant = ", ".join(map(str, issue["collectible_criteria"]["variant"]))
               condition = issue["collectible_criteria"]["appraisal_status"] + " " + issue["collectible_criteria"]["condition"]

               printing = ""
               signed_by = ""
               first_appearances = ""
               other_notes = ""

               issue_details = ""

               if issue["print_run"] > 1:
                  printing = issue["print_run"]
                  lastDigit = int(repr(printing)[-1])
                  if lastDigit == 2:
                     printing = f"{printing}nd printing\n"
                  if lastDigit == 3:
                     printing = f"{printing}rd printing\n"
                  if lastDigit in (4, 5, 6, 7, 8, 9, 0):
                     printing = f"{printing}th printing\n"

               if issue["collectible_criteria"]["signature"]["signed"]:
                  signed_by = "signed by " + " and ".join(map(str, issue["collectible_criteria"]["signature"]["person"])) + " on " + " and ".join(map(str, issue["collectible_criteria"]["signature"]["placement"])) + "\n"

               if issue["collectible_criteria"]["significant_first_appearances"]:
                first_appearances = "first appearances: " + ", ".join(map(str, issue["collectible_criteria"]["significant_first_appearances"])) + "\n"

               if issue["collectible_criteria"]["other_notable_criteria"]:
                other_notes = "other notes: " + ", ".join(map(str, issue["collectible_criteria"]["other_notable_criteria"])) + "\n"

               issue_details =(title  + " #" + issue_num + "\n" +
                "published in " + year + "\n" +
                printing +
                "variant: " + variant + "\n" +
                "condition: " + condition + "\n" +
                signed_by + first_appearances + other_notes
               )

               print(issue_details)

# Prints all issues (without details) in a specified series
def get_issues_simplified(series_name):
   print("\nCollection of " + series_name + " issues:\n")
   for series in collection:
      for key, value in series.items():
         if key == series_name:
            for issue in value:
               title = issue["title"]
               issue_num = issue["issue"]
               
               issue_details =(title  + " #" + issue_num)

               print(issue_details)

# Prints all signed issues (with details) in a specified series
def get_signed_issues(series_name):
   print("\nCollection of " + series_name + " issues with signatures:\n")
   for series in collection:
      for key, value in series.items():
         if key == series_name:
            for issue in value:
               title = issue["title"]
               issue_num = issue["issue"]
               year = issue["year_published"]
               variant = ", ".join(map(str, issue["collectible_criteria"]["variant"]))
               condition = issue["collectible_criteria"]["appraisal_status"] + " " + issue["collectible_criteria"]["condition"]

               printing = ""
               signed_by = ""
               first_appearances = ""
               other_notes = ""

               issue_details = ""

               if issue["print_run"] > 1:
                  printing = issue["print_run"]
                  lastDigit = int(repr(printing)[-1])
                  if lastDigit == 2:
                     printing = f"{printing}nd printing\n"
                  if lastDigit == 3:
                     printing = f"{printing}rd printing\n"
                  if lastDigit in (4, 5, 6, 7, 8, 9, 0):
                     printing = f"{printing}th printing\n"

               if issue["collectible_criteria"]["signature"]["signed"]:
                  signed_by = "signed by " + " and ".join(map(str, issue["collectible_criteria"]["signature"]["person"])) + " on " + " and ".join(map(str, issue["collectible_criteria"]["signature"]["placement"])) + "\n"

               if issue["collectible_criteria"]["significant_first_appearances"]:
                first_appearances = "first appearances: " + ", ".join(map(str, issue["collectible_criteria"]["significant_first_appearances"])) + "\n"

               if issue["collectible_criteria"]["other_notable_criteria"]:
                other_notes = "other notes: " + ", ".join(map(str, issue["collectible_criteria"]["other_notable_criteria"])) + "\n"

               issue_details =(title  + " #" + issue_num + "\n" +
                "published in " + year + "\n" +
                printing +
                "variant: " + variant + "\n" +
                "condition: " + condition + "\n" +
                signed_by + first_appearances + other_notes
               )

               if issue["collectible_criteria"]["signature"]["signed"]:
                  print(issue_details)

# Prints all signed issues (without details) in a specified series
def get_signed_issues_simplified(series_name):
   print("\nCollection of " + series_name + " issues with signatures:\n")
   for series in collection:
      for key, value in series.items():
         if key == series_name:
            for issue in value:
               title = issue["title"]
               issue_num = issue["issue"]
               
               issue_details =(title  + " #" + issue_num)

               if issue["collectible_criteria"]["signature"]["signed"]:
                  print(issue_details)

# Prints all "first appearance" issues (with details) in a specified series
def get_fa_issues(series_name):
   print("\nCollection of " + series_name + " issues with significant first appearances:\n")
   for series in collection:
      for key, value in series.items():
         if key == series_name:
            for issue in value:
               title = issue["title"]
               issue_num = issue["issue"]
               year = issue["year_published"]
               variant = ", ".join(map(str, issue["collectible_criteria"]["variant"]))
               condition = issue["collectible_criteria"]["appraisal_status"] + " " + issue["collectible_criteria"]["condition"]

               printing = ""
               signed_by = ""
               first_appearances = ""
               other_notes = ""

               issue_details = ""

               if issue["print_run"] > 1:
                  printing = issue["print_run"]
                  lastDigit = int(repr(printing)[-1])
                  if lastDigit == 2:
                     printing = f"{printing}nd printing\n"
                  if lastDigit == 3:
                     printing = f"{printing}rd printing\n"
                  if lastDigit in (4, 5, 6, 7, 8, 9, 0):
                     printing = f"{printing}th printing\n"

               if issue["collectible_criteria"]["signature"]["signed"]:
                  signed_by = "signed by " + " and ".join(map(str, issue["collectible_criteria"]["signature"]["person"])) + " on " + " and ".join(map(str, issue["collectible_criteria"]["signature"]["placement"])) + "\n"

               if issue["collectible_criteria"]["significant_first_appearances"]:
                first_appearances = "first appearances: " + ", ".join(map(str, issue["collectible_criteria"]["significant_first_appearances"])) + "\n"

               if issue["collectible_criteria"]["other_notable_criteria"]:
                other_notes = "other notes: " + ", ".join(map(str, issue["collectible_criteria"]["other_notable_criteria"])) + "\n"

               issue_details =(title  + " #" + issue_num + "\n" +
                "published in " + year + "\n" +
                printing +
                "variant: " + variant + "\n" +
                "condition: " + condition + "\n" +
                signed_by + first_appearances + other_notes
               )

               if issue["collectible_criteria"]["significant_first_appearances"]:
                  print(issue_details)

# Prints all "first appearance" issues (without details) in a specified series
def get_fa_issues_simplified(series_name):
   print("\nCollection of " + series_name + " issues with significant first appearances:\n")
   for series in collection:
      for key, value in series.items():
         if key == series_name:
            for issue in value:
               title = issue["title"]
               issue_num = issue["issue"]
               
               issue_details = ""

               issue_details =(title  + " #" + issue_num)

               if issue["collectible_criteria"]["significant_first_appearances"]:
                  print(issue_details)

# Prints single issue (with details) in a specified series
# issue_num must be 3 digit string
# example: get_issue("The Amazing Spider-Man", "003")
def get_issue(series_name, issue_num):
   print("\n" + "Collected copies of " + series_name + " #" + issue_num +"\n")
   desired_issue = False
   for series in collection:
      for key, value in series.items():
         if key == series_name:
            for issue in value:

               if issue["issue"] == issue_num:

                  desired_issue = True

                  title = issue["title"]
                  issue_number = issue["issue"]
                  year = issue["year_published"]
                  variant = ", ".join(map(str, issue["collectible_criteria"]["variant"]))
                  condition = issue["collectible_criteria"]["appraisal_status"] + " " + issue["collectible_criteria"]["condition"]

                  printing = ""
                  signed_by = ""
                  first_appearances = ""
                  other_notes = ""

                  issue_details = ""

                  if issue["print_run"] > 1:
                     printing = issue["print_run"]
                     lastDigit = int(repr(printing)[-1])
                     if lastDigit == 2:
                        printing = f"{printing}nd printing\n"
                     if lastDigit == 3:
                        printing = f"{printing}rd printing\n"
                     if lastDigit in (4, 5, 6, 7, 8, 9, 0):
                        printing = f"{printing}th printing\n"

                  if issue["collectible_criteria"]["signature"]["signed"]:
                     signed_by = "signed by " + " and ".join(map(str, issue["collectible_criteria"]["signature"]["person"])) + " on " + " and ".join(map(str, issue["collectible_criteria"]["signature"]["placement"])) + "\n"

                  if issue["collectible_criteria"]["significant_first_appearances"]:
                     first_appearances = "first appearances: " + ", ".join(map(str, issue["collectible_criteria"]["significant_first_appearances"])) + "\n"

                  if issue["collectible_criteria"]["other_notable_criteria"]:
                     other_notes = "other notes: " + ", ".join(map(str, issue["collectible_criteria"]["other_notable_criteria"])) + "\n"

                  issue_details =(title  + " #" + issue_number + "\n" +
                  "published in " + year + "\n" +
                  printing +
                  "variant: " + variant + "\n" +
                  "condition: " + condition + "\n" +
                  signed_by + first_appearances + other_notes
                  )

                  print(issue_details)
   
   if desired_issue == False:
      print("__Collection does not contain that issue__" + "\n")


#Example function calls 
#series_list()
#get_all()
#get_all_min()
#get_all_simplified()
#get_all_graded()
#get_all_graded_simplified()
#get_issue("The Amazing Spider-Man", "300")
#get_issues("The Amazing Spider-Man")
#get_issues_simplified("The Amazing Spider-Man")
#get_signed_issues("The Amazing Spider-Man")
#get_signed_issues_simplified("The Amazing Spider-Man")
#get_fa_issues("The Amazing Spider-Man")
#get_fa_issues_simplified("The Amazing Spider-Man")

#You can can uncomment an example function call above and run this script directly.
#(e.g. run: python3 list_traverse.py)
#Or you can use the method below to call a specific function from the script.

#Example calls from command line:
#python3 -c "from list_traverse import get_issues; get_issues('The Amazing Spider-Man')"
#python3 -c "from list_traverse import get_issue; get_issue('The Amazing Spider-Man','300')"
#python3 -c "from list_traverse import series_list; series_list()"
#python3 -c "from list_traverse import get_all; get_all()"

# To Do:
# need function that returns any specified quality of a specified issue
# need function that returns all issues with a specified quality in a specified series

# example: how to iterate through a specified dictionary in the json list
'''
for i in collection:
   for key, value in i.items():
    if key == "The Amazing Spider-Man":
      for x in value:
         print(x["title"] + " #" + x["issue"])
'''

