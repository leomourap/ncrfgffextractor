# **ncrfgffextractor**

The script is intended to extract portions of a  GFF annotation file based on the summary output from Noise Cancelling Repeat Finder (https://github.com/makovalab-psu/NoiseCancellingRepeatFinder).

Usage: ncrfgffextractor1-1.py NCRFsummaryfile GFFfile output.csv

BEFORE THE START, YOU MUST REMOVE THE GFF STANDARD HEADER AND INPUT A NEW ONE (tab delimited!!!):

Cromossomo    Genbank    regiao    pbinicio    pbfim    .    +    .    annotation

Example:

![image](https://user-images.githubusercontent.com/105673165/168724377-984f871c-e6d1-4870-8515-8f525d054689.png)

*just like that!

(you can adapt it if you want. If so, remember to change the columns names in the loop lines of the code).
