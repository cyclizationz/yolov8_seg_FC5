'''
Convert predicted yolo txt file to labelme json file
'''
import os
import json
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser(description='txt convert to json params')
parser.add_argument('--txt-dir', type=str, default='./labels', help='txt path dir')
parser.add_argument('--image-dir', type=str, default='./images', help='image path dir')
parser.add_argument('--save-dir', type=str, default='./jsons', help='json save dir')
parser.add_argument('--classes', type=list[str], default=['gun'], help='classes')
parser.add_argument('--width', type=int, default=1920, help='width')
parser.add_argument('--height', type=int, default=1080, help='height')
parser.add_argument('--seg2bbox', type=bool, default=False, help='convert polygon points outputs to bbox')

args = parser.parse_args()
WIDTH = args.width
HEIGHT = args.height
BBOX = args.seg2bbox

def convert_label_json(txt_dir, image_dir, save_dir, classes=args.classes):
    src = os.listdir(txt_dir)
    for txt_path in tqdm(src):
        image_path = os.path.join(image_dir, txt_path.replace('txt', 'png'))
        convert_txt_to_json(txt_path, image_path, save_dir, classes=classes)

def convert_txt_to_json(txt_path, image_path, save_dir, width=WIDTH, height=HEIGHT, classes=args.classes):
    shapes = []
    txt_file_path = os.path.join(txt_dir, txt_path)
    with open(txt_file_path, 'r') as txt_file:
        for line in txt_file.readlines():
            line = line.strip().split()
            label = classes[int(line[0])]
            points = []
            for i in range(1, len(line), 2):
                x = float(line[i]) * width
                y = float(line[i + 1]) * height
                points.append([x, y])
            
            shape = {
                "label": label,
                "points": points,
                "group_id": None,
                "description": "",
                "shape_type": "polygon",
                "flags": {}
            }
            if BBOX:
                shape["shape_type"] = "rectangle"
                shape["points"] = seg2bbox(points)
            shapes.append(shape)
    
    json_data = {
        "version": "5.2.1",
        "flags": {},
        "shapes": shapes,
        "imagePath": image_path
    }
    
    json_file_path = txt_path.replace(".txt", ".json")
    with open(os.path.join(save_dir ,json_file_path), 'w') as json_file:
        json.dump(json_data, json_file, indent=2)

def seg2bbox(points):
    x_list = []
    y_list = []
    for point in points:
        x_list.append(point[0])
        y_list.append(point[1])
    x_min = min(x_list)
    x_max = max(x_list)
    y_min = min(y_list)
    y_max = max(y_list)
    return [x_min, y_min, x_max, y_max]
    
if __name__ == '__main__':
    txt_dir = args.txt_dir
    image_dir = args.image_dir
    save_dir = args.save_dir
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    convert_label_json(txt_dir, image_dir, save_dir)