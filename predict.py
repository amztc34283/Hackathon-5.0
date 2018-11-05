import sys
import os
import json
import datetime
sys.path.append("..")
from watson_developer_cloud import PersonalityInsightsV3


""" Methods for finding the message json """
def longest_conv(file_path):
    return os.path.getsize(file_path)


def get_msg_file_path(inbox_path, name):
    results = []
    for root, dirs, files in os.walk(inbox_path):
        conv_name = root.rsplit('/', 1)[-1]
        conv_name = conv_name.split('_', 1)[0]
        conv_name = conv_name.lower()
        given_name = name.replace(" ", "").lower()
        print(root)

        if (given_name == conv_name and 'message.json' in files):
            results.append(root + "/message.json")

    largest_file_path = max(results, key=longest_conv)
    return largest_file_path




""" Methods for parsing the message json, preparing for watson input """
# Parses a message from a facebook messenger json file, extracts the content
# given by the person with name. Returns a string of the person's conversation.
def parse_msg(msg_dict, name):
    print
    msg_lst = msg_dict["messages"]
    content_lst = [msg["content"] for msg in msg_lst \
                        if msg['sender_name'] == name]
    content_str = " ".join(content_lst)
    return content_str


# Parses messages within a date interval
def parse_msg_time(msg_dict, name, start_date, end_date):
    # Todo
    pass

# Creates a input json for the watson personality analytics api call
# Places the json in the watson in folder
def make_json(content_str, name):
    data = {}
    data["contentItems"] = []
    data["contentItems"].append({
        "content":content_str,
        "contenttype": "text/plain"})
    with open("watson_in/" + name + ".json", "w+") as out_file:
        json.dump(data, out_file, indent=2)


# Takes in the file name of the message.json to parse into input for watson prediction input
def msg_to_input(file_name, name):
    with open(file_name) as data_file:
        msg_dict = json.load(data_file)

        content_str = parse_msg(msg_dict, name)
        make_json(content_str, name)
        
        participants_dct = msg_dict["participants"]
        self_name = participants_dct[1]["name"]
        if (self_name == name):
            self_name = participants_dct[0]["name"]

        path = os.getcwd()
        self_dir = path + "/watson_in/self"
        if (not os.path.isdir(self_dir)):
            os.mkdir(self_dir)

        content_str_self = parse_msg(msg_dict, self_name)
        make_json(content_str_self, "self_" + name)



""" Get the prediction from watson api call, stores it at location watson_out """
def get_watson_pred(file_name, name):
    service = PersonalityInsightsV3(version='2017-10-13',
    url='https://gateway-wdc.watsonplatform.net/personality-insights/api',
    iam_apikey='W7wjiNAzqzpVxaXhYMFMQ138rNY6g7GrwXVYj5nHzU7l')

    with open(file_name + ".json") as \
            profile_json:
        profile = service.profile(
            profile_json.read(),
            content_type='application/json', 
            raw_scores=True,
            consumption_preferences=True).get_result()

    with open("watson_out/"+ name +".json", "w+") as out_file:
        json.dump(profile, out_file, indent=2)


def name_to_pred(name):
    wd = os.getcwd()
    msg_fp = get_msg_file_path(wd + "/inbox", name)
    msg_to_input(msg_fp, name)
    get_watson_pred(wd + "/watson_in/" + name, name)
    get_watson_pred(wd + "/watson_in/self_" + name, "self_" + name)



def get_personality_self(name):
    file_name = "watson_out/self_" + name + ".json"
    if (not os.path.isfile(file_name)):
        name_to_pred(name)

    with open("watson_out/self_" + name + ".json") as data_file:
        profile_dict = json.load(data_file)
        big5_dict = { profile_dict["personality"][i]["name"].encode("ascii") : \
                 profile_dict["personality"][i]["percentile"] for i in range(5)}
        return big5_dict
    