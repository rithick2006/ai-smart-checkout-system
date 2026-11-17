# AI Smart Checkout System

A computer-vision learning project that recognizes products and supports an automated billing workflow.

## Project structure

- `train_classifier.py` trains a MobileNetV2 classifier from `dataset/train` and `dataset/val`.
- `create_db.py` creates a SQLite product database after `class_names.json` exists.
- `setup_db.py` initializes the application database when the `app` package is present.

## Requirements

Install the dependencies first:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
```

## Training

Arrange labelled images in this structure:

```text
dataset/
  train/<class-name>/...
  val/<class-name>/...
```

Then train the classifier:

```bash
python train_classifier.py --data_dir dataset
```

The script writes `class_names.json` and `model.h5`.

## Database setup

After training creates `class_names.json`, create the product database:

```bash
python create_db.py
```

## Status

Portfolio prototype. The repository currently contains the training and database utilities; a complete production checkout interface, tests, and deployment configuration still need to be added.

## License

No license has been declared yet. Add one before accepting contributions or granting reuse rights.
