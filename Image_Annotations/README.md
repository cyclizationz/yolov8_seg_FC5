# Dataset Converter Scripts

This repository contains scripts to convert YOLO format annotations (.txt) to LableMe JSON format annotations (.json) and vice versa. It also includes a script to split the dataset into train and validation sets.

## Prerequisites

- Python 3.x
- tqdm

## Directory Structure

The dataset directory should have the following structure:

```
dataset/
│
├── train/
│   ├── images/
│   └── labels/
│       ├── <yolo_txt_files>
│
├── val/
│   ├── images/
│   └── labels/
│       ├── <yolo_txt_files>
│
└── test/
    ├── images/
    └── labels/
        ├── <yolo_txt_files>
```

The `train`, `val`, and `test` directories should contain the corresponding images and labels directories.

## Usage

### Converting YOLO TXT to JSON

To convert YOLO format annotations (.txt) to JSON format annotations:

```bash
python txt2JSON.py --txt-dir=./train/labels --image-dir=./train/images --save-dir=./train/bbox_jsons --seg2bbox True
```

- `--txt-dir`: Path to the directory containing YOLO format TXT files.
- `--image-dir`: Path to the directory containing the corresponding images.
- `--save-dir`: Path to the directory where the JSON format annotations will be saved.
- `--seg2bbox`: Optional flag to indicate whether to convert segmentation polygons to bounding boxes (default: `False`).

### Converting JSON to YOLO TXT

To convert JSON format annotations to YOLO format annotations:

```bash
python JSON2txt.py --json-dir=./jsons --save-dir=./labels --classes gun
```

- `--json-dir`: Path to the directory containing JSON format files.
- `--save-dir`: Path to the directory where the YOLO format annotations will be saved.
- `--classes`: Optional argument to specify the classes to be converted, separated with "," (default: gun).

### Splitting Train and Validation Sets

To split the dataset into train and validation sets:

```bash
python split.py
```

This script randomly splits the dataset into train and validation sets and moves the corresponding images and labels to the appropriate directories.

## License

This project is licensed under the [MIT License](LICENSE).
