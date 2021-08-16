import xml.etree.ElementTree as ET
import os
import json
import numpy as np
from glob import glob

def parseXmlFiles(xml_path):
  for f in os.listdir(xml_path):
    xml_file = os.path.join(xml_path, f)
    #print(f)
    r = open(xml_file)
    lines = r.readlines()
    fw = open('C:/Users/qidian/Desktop/test/teststd_tab/'+f[:f.rfind('.')]+'.label','w')
    if len(lines)==0:
      print(f)
      continue
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for info in root:
      for table in info:
        for cell in table:
          if cell.tag!='tablecell':
            continue
          x0,y0,x1,y1 = -1,-1,-1,-1
          start_col,end_col = -1,-1
          start_row,end_row = -1,-1
          for vh in cell:
            if vh.tag=='x0':
              x0 = vh.text
            if vh.tag=='x1':
              x1 = vh.text
            if vh.tag=='y0':
              y0 = vh.text
            if vh.tag=='y1':
              y1 = vh.text
            if vh.tag=='start_col':
              start_col = vh.text
            if vh.tag=='end_col':
              end_col = vh.text
            if vh.tag=='start_row':
              start_row = vh.text
            if vh.tag=='end_row':
              end_row = vh.text
          fw.write(x0+','+y0+';'+x1+','+y0+';'+x1+','+y1+';'+x0+','+y1+';'+start_col+','+end_col+';'+start_row+','+end_row+';0\n')
    fw.close()
    #break

if __name__ == '__main__':
  xml_path = 'C:/Users/qidian/Desktop/test/xml_tab/'
  parseXmlFiles(xml_path)
