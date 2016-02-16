# -*- coding: utf-8 -*-
import os
import pyPdf


def pypdf2txt(filename):
    try:
        with open(filename, "rb") as pdffile:
            pdf = pyPdf.PdfFileReader(pdffile)
            for page in pdf.pages:
                return page.extractText()
    except Exception as err:
        print('open file error:' + str(err))


def judgement(path_name='~/'):
    for filename in os.listdir(path_name):
        # print filename
        if '.pdf' in filename:
            # print filename
            if len(pypdf2txt(path_name + filename)) > 500:
                print filename


judgement()
