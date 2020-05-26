#!/bin/bash
if pip3 install -r requirements.txt && sudo apt install antlr4 && cd src/antlr_parser && antlr4 -Dlanguage=Python3 Gram.g4 && cd ../antlr_regex && antlr4 -Dlanguage=Python3 Rule.g4
then
echo -e "Complete"
else
echo -e "Error"
fi