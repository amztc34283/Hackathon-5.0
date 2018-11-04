import json
import sys
import time



# Parses a message from a facebook messenger json file, extracts the content
# given by the person with name. Returns a string of the person's conversation.
def parse_msg(file_name, name):
    with open(file_name) as data_file:
        msg_dict = json.load(data_file)
        msg_lst = msg_dict["messages"]
        content_lst = [msg["content"].encode('ascii', 'ignore') for msg in msg_lst if                      msg['sender_name'] == name]
        content_str = " ".join(content_lst)
        return content_str


def make_json(content_str, name):
    data = {}
    data["content_items"] = []
    data["content_items"].append({
        "content":content_str,
        "content_type": "text/plain",
        "created" :str(time.time()) })
    with open("watson_in/" + name + ".json", "w+") as out_file:
        json.dump(data, out_file)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Correct usage is python clean_msg.py <message.json> <Person_Name>")
    else:
        file_name = sys.argv[1]
        name = sys.argv[2]
        content_str = parse_msg(file_name, name)
        make_json(content_str, name)