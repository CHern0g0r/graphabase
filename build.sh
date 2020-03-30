#!/bin/bash
if pip3 install pytest && pip3 install rdflib && pip3 install pyformlang && pip3 install grammpy
then
echo -e "Complete"
else
echo -e "Error"
fi