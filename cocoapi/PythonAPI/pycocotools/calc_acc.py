# from cocoeval_custom import COCOeval
from pycocotools.cocoeval import COCOeval
from tqdm import tqdm
import pickle
import numpy as np
import pandas as pd

def get_entry_dict():
    return {
        "segmentation": None,
        "iscrowd": 0,
        "image_id": None,
        "category_id": 1,
        "id": None,
        "bbox": None,
        "area": None
    }

gt_json = []
annot = pd.read_csv('../../../groundtruth/annotations_test.csv')
imgIds = sorted(list(set(annot['image_name'].tolist())))

def get_gt_json():
	'''
	Function to convert the GT csv into json which COCO likes
	'''
	for annotid,row in tqdm(annot.iterrows()):
	    entry = get_entry_dict()
	    
	    entry['image_id'] = imgIds.index(row['image_name'])
	    entry['id'] = annotid
	    entry['bbox'] = [row['x1'], row['y1'], row['x2']-row['x1'], row['y2']-row['y1']]
	    entry['area'] = (row['x2']-row['x1']) * (row['y2']-row['y1'])
	    
	    gt_json.append(entry)

	return gt_json

def get_dt_json(pred_path = '../../../predictions/output_singlescale.csv'):
	'''
	Function to convert the predictions into json which COCO likes
	'''
	dt_json = []
	dets = pd.read_csv(pred_path)

	for detid,row in tqdm(dets.iterrows()):
	        
		entry = get_entry_dict()

		entry['image_id'] = imgIds.index(row['image_name'])
		entry['id'] = detid
		entry['bbox'] = [row['x1'], row['y1'], row['x2']-row['x1'], row['y2']-row['y1']]
		entry['area'] = (row['x2']-row['x1']) * (row['y2']-row['y1'])
		entry['score'] = row['score']

		dt_json.append(entry)

	return dt_json

if __name__ == "__main__":
	
	gt_json, dt_json = get_gt_json(), get_dt_json()

	from coco_custom import CustomCOCO
	gt_coco_format = CustomCOCO(gt_json)
	dt_coco_format = CustomCOCO(dt_json)

	# running evaluation
	cocoEval = COCOeval(gt_coco_format, dt_coco_format, iouType='bbox')
	
	# if you want to evaluate on a subset
	# cocoEval.params.imgIds  = range(0,100)
	
	cocoEval.evaluate()
	cocoEval.accumulate()
	cocoEval.summarize()
