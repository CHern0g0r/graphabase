#!/bin/bash
if pip3 install -r requirements.txt
then
echo -e "Complete"
else
echo -e "Error"
fi