#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Haihua on 11/18/2018

import os
import xml.dom.minidom


def fileindex(datapath):
    # Swahili punction
    punction = ["'",",","«","»",".","","{","}","‒","–","—","―","-","?","[","]","…","·",";",":","!","‽","/","⁄","(",")"]
    f_stopwords = open("D:\\Pyproject\\openCLIR.unt.edu\\src\\resources\\stopwords-sw")
    stopwords = f_stopwords.readlines()
    stop_sign = []
    for stopword in stopwords:
        stopword = stopword.strip("\n")
        stop_sign.append(stopword)

    # 解析txt文件
    files = os.listdir(datapath)
    for file in files:
        doc_id = file.strip(".txt")
        filepath = os.path.join(datapath,file)
        with open(filepath,encoding='utf-8') as f:
            contents = f.readlines()
            for line in contents:
                line_id = contents.index(line)+1
                document_id = doc_id+"_"+str(line_id)
                line_content = line.strip("\n")
                impl = xml.dom.minidom.getDOMImplementation()
                dom = impl.createDocument(None,'Document',None)
                root = dom.documentElement

                Doc_id = dom.createElement("Doc_id")
                Doc_text = dom.createTextNode(document_id)
                Doc_id.appendChild(Doc_text)
                root.appendChild(Doc_id)

                Doc_content = dom.createElement("Doc_content")
                Content_text = dom.createTextNode(line_content)
                Doc_content.appendChild(Content_text)
                root.appendChild(Doc_content)

                f = open("D:\\Academic_Study\\UNT_PHD\\projects\\OpenCLIR\\data_clean\\"+document_id+".xml","w",encoding='utf-8')
                dom.writexml(f,addindent='',newl='\n',encoding='utf-8')
                f.close()

if __name__ == '__main__':
    fileindex ("D:\\Pyproject\\openCLIR.unt.edu\\src\\data_collection\\Swahili")