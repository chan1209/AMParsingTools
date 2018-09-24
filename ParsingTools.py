# code : utf8
import os
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

tPath = os.getcwd()

source_filePath = tPath + r'\xmlTest\xml\AndroidManifest.xml'
to_doc_file_path = tPath + r'\xmlTest\xml\a.xml'
output_file_path = tPath + r'\xmlTest\outputFile\output.txt'


def getElementTree(filePath):
    with open(filePath, encoding='utf8') as f:
        doc = ET.parse(f)
    return doc


def getSourceActList(doc):
    nodelist = doc.findall('application/activity')
    act_list = []
    for node in nodelist:
        act_list.append(node.get('{http://schemas.android.com/apk/res/android}name'))
    return act_list


def getSourceReceiverList(doc):
    nodelist = doc.findall('application/receiver')
    receiverList = []
    for node in nodelist:
        receiverList.append(node.get('{http://schemas.android.com/apk/res/android}name'))
    return receiverList


def getSourceServiceList(doc):
    nodelist = doc.findall('application/service')
    serviceList = []
    for node in nodelist:
        serviceList.append(node.get('{http://schemas.android.com/apk/res/android}name'))
    return serviceList


def getSourceProviderList(doc):
    nodelist = doc.findall('application/provider')
    providerList = []
    for node in nodelist:
        providerList.append(node.get('{http://schemas.android.com/apk/res/android}name'))
    return providerList


if __name__ == "__main__":
    source_doc = getElementTree(source_filePath)
    source_lists = []
    source_lists.extend(getSourceActList(source_doc))
    source_lists.extend(getSourceReceiverList(source_doc))
    source_lists.extend(getSourceProviderList(source_doc))
    source_lists.extend(getSourceServiceList(source_doc))
    to_lists = []
    # with open(to_doc_file_path, encoding='utf8') as to_file:
    #     for line in to_file:
    #         if 'android:name' in line and 'uses-permission' not in line:
    #             to_lists.append(line)
    # to_lists_real = []
    # for ls in to_lists:
    #     a = ls[ls.index('"')]
    #     to_lists_real.append(ls[ls.index('"') + 1:ls.rfind('"'):])
    # with open(output_file_path, 'tw', encoding='utf8') as output_file:
    #     for source_line in source_lists:
    #         if source_line not in to_lists_real:
    #             output_file.write(source_line + "\n")
