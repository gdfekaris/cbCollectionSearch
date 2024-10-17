import json

# open raw json list of comic issues
with open('raw_list.json') as data:
  collection = json.load(data)

# returns an alphabetized list of all series titles in the comic list

def get_series_titles(comics):
   comics = sorted(comics, key=lambda x: (x["alphabetized_title"]), reverse=False)
   series_title_list = []
   for issue in comics:
     if series_title_list.count(issue["title"]) < 1:
        series_title_list.append(issue["title"])
   return(series_title_list)

# puts each issue under its correct series title.
# takes as variables output from get_series_titles and loaded raw json list
def sort_issue_by_series(series_list, comics):
   array = []
   for series in series_list:
      obj = {series:[]}
      for issue in comics:
         if issue["title"] == series:
            obj[series].append(issue)
      array.append(obj)
   return(array)

# returns issues in numeric order, organized under the correct series title
def order_issues_in_series(comics):
  array = []
  for series in comics:
    for key, value in series.items():
      final_array = (sorted(value, key=lambda x: (x["issue"], x["collectible_criteria"]["variant"]), reverse=False))
      array.append({key: final_array})
  return(array)

# returns json formatted, ordered list of comics
# this function's output must be used in the list_traverse.py functions
def create_ordered_json(comics, output_file_name):

   series_titles = get_series_titles(comics)
   organized_issues = sort_issue_by_series(series_titles, comics)
   ordered_collection = order_issues_in_series(organized_issues)

   json_object = json.dumps(ordered_collection, indent=2)

   with open(output_file_name, "w") as outfile:
    outfile.write(json_object)

   print("Output file is: " + output_file_name)

create_ordered_json(collection, "ordered_list.json")


# To do:

# need function that returns full JSON object of a specified issue
# need function that allows edits for any specified quality on any specified issue
# DONE -- need alphabetical list (sort) to NOT use 'The' as part of the alphebetizing process


