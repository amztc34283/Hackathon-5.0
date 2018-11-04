## This script finds the conversation json with a particular person, given the absolute path of the facebook messenger msgs inbox folder 
# 
# e.g. "Jonah Moon" /home/bhsieh/calhacks/messages/inbox

import sys
import os

def longest_conv(file_path):
    return os.path.getsize(file_path)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Correct usage is python locate_conv.py <Person_Name> <facebook inbox file")
    else:
        name = sys.argv[1]
        inbox_path = sys.argv[2]
        results = []

        for root, dirs, files in os.walk(inbox_path):
            conv_name = root.rsplit('/', 1)[-1]
            conv_name = conv_name.split('_', 1)[0]
            conv_name = conv_name.lower()
            given_name = name.replace(" ", "").lower()

            if (given_name == conv_name and 'message.json' in files):
                results.append(root + "/message.json")

        largest_file_path = max(results, key=longest_conv)
        print(largest_file_path)
                