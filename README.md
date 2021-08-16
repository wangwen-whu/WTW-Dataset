# WTW-Dataset
WTW-Dataset is the first wild table dataset for table detection and table structure recongnition tasks, which is constructed from photoing, scanning and web pages, 
covers 7 challenging cases like: (1)Inclined tables, (2) Curved tables, (3) Occluded tables or blurredtables (4) Extreme aspect ratio tables
(5) Overlaid tables, (6) Multi-color tables and (7) Irregular tables in table structure recognition.
## jiagetu
WTW dataset with the following ground-truths:

```
- data
 - train
  - images
  - xml (including image name, table id, table cell bbox(four vertices), start col/row, end col/row)
 - test
  - images
  - xml
  - class (7 .txt files include image names for 7 different challenging cases)
```

Download link is [here](https://tianchi.aliyun.com/dataset/dataDetail?dataId=108587)

## Data to other forms:
If you want to change to other common forms, you can do followings :
- run the ```xmltococo.py``` to change the xml to json form.
- run the ```xmltohtml.py``` to change the xml to html form.

## Citation:
If you use the dataset, please consider citing our work-
```
@InProceedings{Long_2021_ICCV,
	author = {Rujiao, Long and Wen, Wang and Nan, Xue and Feiyu, Gao and Zhibo, Yang and Yongpan, Wang and Gui-Song, Xia},
	title = {Parsing Table Structures in the Wild},
	booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
	month = {October},
	year = {2021}
}

```
