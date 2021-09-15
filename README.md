# WTW-Dataset
This is an official implementation for the WTW Dataset in "Parsing Table Structures in the Wild " on ICCV 2021. Here, you can download the [paper](https://arxiv.org/abs/2109.02199), and [Supplementary materials](https://github.com/wangwen-whu/WTW-Dataset/blob/main/Supplementary.pdf).

WTW-Dataset is the first wild table dataset for table detection and table structure recongnition tasks, which is constructed from photoing, scanning and web pages, 
covers 7 challenging cases like: (1)Inclined tables, (2) Curved tables, (3) Occluded tables or blurredtables (4) Extreme aspect ratio tables
(5) Overlaid tables, (6) Multi-color tables and (7) Irregular tables in table structure recognition.

![image](https://github.com/wangwen-whu/WTW-Dataset/blob/main/demo/20210816_210413.gif)

It contains 14581 images with the following ground-truths:
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

Download link is [here](https://tianchi.aliyun.com/dataset/dataDetail?dataId=108587).
(we revised the Ground Truth for testset, you can download the test-xml-revise.zip).

## Recent Updates
- **[Sep, 2021]** Revised the Ground Truth for test set. (test-xml-revise.zip in download link)
- **[Sep, 2021]** Revised the Cycle-Centernet evaluation results for the WTW testset. (in /demo/newresult.txt)

## To be updated
Our results on WTW-dataset

Evaluation code

## Data to other forms:
If you want to change to other common forms, you can do followings :
- run the ```xmltococo.py``` to change the xml to json form.(To be updated)
- run the ```xmltohtml.py``` to change the xml to html form.(To be updated)

## Model link
Our model Cycle-Centernet has been used as Alibaba's online business software, so we can't open the model code. If you need to test, you can use the following online [test link](https://duguang.aliyun.com/experience?type=universal&subtype=table#intro) to try the different table images.

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
