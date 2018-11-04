#!/bin/bash
# Script for getting facebook messenger inbox file paths
# Argument 1: Name of person's conversation to locate
# Argument 2: Absolute path of inbox folder for facebook messenger chat
# example usage:
#  ./find_conv.sh "Jonah Moon" /home/bhsieh/calhacks/messages/inbox

msg_json_fp=`python locate_conv.py "$1" "$2"`
echo $msg_json_fp
## TODO: Add a condition if locate_conv fails

python parse_msg.py "$msg_json_fp" "$1"
echo
echo "message.json parsed, placed in directory: watson_in/ "
## TODO: Add a condition if parse_msg fails

python get_watson_pred.py watson_in/"$1" "$1"

echo
echo "prediction json, placed in directory: watson_out/"
## TODO: Add a condition if prediction fails
