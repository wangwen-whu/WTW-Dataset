import xml.etree.ElementTree as ET
import os
import json

coco = dict()
coco['images'] = []
coco['type'] = 'instances'
coco['annotations'] = []
coco['categories'] = []

category_set = dict()
image_set = set()

category_item_id = 0
image_id = 20140000000
annotation_id = 0

def addCatItem(name):
    global category_item_id
    category_item = dict()
    category_item['supercategory'] = 'none'
    category_item_id += 1
    category_item['id'] = category_item_id
    category_item['name'] = name
    coco['categories'].append(category_item)
    category_set[name] = category_item_id
    return category_item_id

def addImgItem(file_name, size):
    global image_id
    if file_name is None:
        raise Exception('Could not find filename tag in xml file.')
    if size['width'] is None:
        raise Exception('Could not find width tag in xml file.')
    if size['height'] is None:
        raise Exception('Could not find height tag in xml file.')
    image_id += 1
    image_item = dict()
    image_item['id'] = image_id
    image_item['file_name'] = file_name
    image_item['width'] = size['width']
    image_item['height'] = size['height']
    coco['images'].append(image_item)
    image_set.add(file_name)
    return image_id

def addAnnoItem(object_name, image_id, category_id, bbox, seg):
    global annotation_id
    annotation_item = dict()
    annotation_item['segmentation'] = []

    annotation_item['segmentation'].append(seg)

    annotation_item['area'] = bbox[2] * bbox[3]
    annotation_item['iscrowd'] = 0
    annotation_item['ignore'] = 0
    annotation_item['image_id'] = image_id
    annotation_item['bbox'] = bbox
    annotation_item['category_id'] = category_id
    annotation_id += 1
    annotation_item['id'] = annotation_id
    coco['annotations'].append(annotation_item)

def parseXmlFiles(XML_path): 
    for xml_path in XML_path:
        for f in os.listdir(xml_path):
            if not f.endswith('.xml'):
                continue
            
            bndbox = dict()
            size = dict()
            current_image_id = None
            current_category_id = None
            file_name = None
            size['width'] = None
            size['height'] = None
            size['depth'] = None

            xml_file = os.path.join(xml_path, f)
            print(xml_file)

            tree = ET.parse(xml_file)
            root = tree.getroot()
            if root.tag != 'annotation':
                raise Exception('pascal voc xml root element should be annotation, rather than {}'.format(root.tag))

            #elem is <folder>, <filename>, <size>, <object>
            for elem in root:
                current_parent = elem.tag
                current_sub = None
                object_name = None
                
                if elem.tag == 'folder':
                    continue
                
                if elem.tag == 'filename':
                    file_name = elem.text
                    if file_name in category_set:
                        raise Exception('file_name duplicated')
                    
                #add img item only after parse <size> tag
                elif current_image_id is None and file_name is not None and size['width'] is not None:
                    if file_name not in image_set:
                        current_image_id = addImgItem(file_name, size)
                    else:
                        raise Exception('duplicated image: {}'.format(file_name)) 
                #subelem is <width>, <height>, <depth>, <name>, <bndbox>
                for subelem in elem:
                    bndbox ['xmin'] = None
                    bndbox ['xmax'] = None
                    bndbox ['ymin'] = None
                    bndbox ['ymax'] = None
                    
                    current_sub = subelem.tag
                    if current_parent == 'object' and subelem.tag == 'name':
                        object_name = subelem.text
                        if object_name not in category_set:
                            current_category_id = addCatItem(object_name)
                        else:
                            current_category_id = category_set[object_name]

                    elif current_parent == 'size':
                        if size[subelem.tag] is not None:
                            raise Exception('xml structure broken at size tag.')
                        size[subelem.tag] = int(subelem.text)

                    #option is <xmin>, <ymin>, <xmax>, <ymax>, when subelem is <bndbox>
                    filter = {'x1':0,'x2':0,'x3':0,'x4':0,'y1':0,'y2':0,'y3':0,'y4':0}#,'x5':0,'y5':0,'x6':0,'y6':0}
                    seg = []
                    for option in subelem:
                        if current_sub == 'bndbox':
                            if option.tag in filter.keys():
                                filter[option.tag]=float(option.text)
                            #elif bndbox[option.tag] is not None:
                            #    raise Exception('xml structure corrupted at bndbox tag.')
                            bndbox[option.tag] = float(option.text)
                    seg=[filter['x1'],filter['y1'],filter['x2'],filter['y2'],filter['x3'],filter['y3'],
                         filter['x4'],filter['y4']]#,filter['x5'],filter['y5'],filter['x6'],filter['y6']]

                    #only after parse the <object> tag
                    if bndbox['xmin'] is not None:
                        if object_name is None:
                            raise Exception('xml structure broken at bndbox tag')
                        if current_image_id is None:
                            raise Exception('xml structure broken at bndbox tag')
                        if current_category_id is None:
                            raise Exception('xml structure broken at bndbox tag')
                        bbox = []
                        #x
                        bbox.append(bndbox['xmin'])
                        #y
                        bbox.append(bndbox['ymin'])
                        #w
                        bbox.append(bndbox['xmax'] - bndbox['xmin'])
                        #h
                        bbox.append(bndbox['ymax'] - bndbox['ymin'])
                        addAnnoItem(object_name, current_image_id, current_category_id, bbox, seg )

if __name__ == '__main__':
    #xml_path = ['./xml/test/']
    #xml_path = ['./Customs_export_declaration_0920/train_resize/xml/', \
    #            './ICBU_3311/train_resize/xml/', \
    #            './dingding_sp/train_resize/xml/', \
    #            '/home/rujiao.lrj/DATA/masked_images/train/xml/', \
    #            '/home/rujiao.lrj/DATA/icbu_pdf2jpg_scan/train/xml/', \
    #            '/home/rujiao.lrj/DATA/table_lst_yhd_excel_all/train/xml/', \
    #            '/home/rujiao.lrj/DATA/spider/xml/', \
    #            './xml/train/', \
    #            '/home/rujiao.lrj/DATA/kuake_table/xml/']
    xml_path = ['./test/xml/']
    json_file = './test/test.json'
    parseXmlFiles(xml_path)
    json.dump(coco, open(json_file, 'w'))

