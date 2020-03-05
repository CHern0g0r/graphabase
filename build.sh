#!/bin/bash
if pip3 install pytest && pip3 install rdflib && pip3 install pyformlang
then
echo -e "Complete"
else
echo -e "Error"
fi