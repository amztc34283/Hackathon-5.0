import json
import sys
import time
import os


# Parses a message from a facebook messenger json file, extracts the content
# given by the person with name. Returns a string of the person's conversation.
def parse_msg(msg_dict, name):
    msg_lst = msg_dict["messages"]
    content_lst = [msg["content"] for msg in msg_lst \
                        if msg['sender_name'] == name]
    content_str = " ".join(content_lst)
    return content_str


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


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Correct usage is python clean_msg.py <message.json> <Person_Name>")
    else:
        file_name = sys.argv[1]
        name = sys.argv[2]
        with open(file_name) as data_file:
            msg_dict = json.load(data_file)


            content_str = parse_msg(msg_dict, name)
            make_json(content_str, name)
            
            participants_dct = msg_dict["participants"]
            self_name = participants_dct[1]["name"]
            if (self_name == name):
                self_name = participants_dct[0]["name"]

            path = os.getcwd()
            self_dir = path + "/watson_in/" + self_name
            if (not os.path.isdir(self_dir)):
                os.mkdir(self_dir)

            content_str_self = parse_msg(msg_dict, name)
            make_json(content_str_self, self_name + "/" + name)