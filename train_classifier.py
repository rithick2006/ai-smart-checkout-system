import tensorflow as tf
import json
import argparse
import os

def train_model(data_dir, epochs=15, fine_tune_epochs=5, img_size=(224,224)):
    # Load dataset
    train_ds = tf.keras.utils.image_dataset_from_directory(
        os.path.join(data_dir, "train"),
        image_size=img_size,
        batch_size=32
    )
    val_ds = tf.keras.utils.image_dataset_from_directory(
        os.path.join(data_dir, "val"),
        image_size=img_size,
        batch_size=32
    )

    class_names = train_ds.class_names
    with open("class_names.json", "w") as f:
        json.dump(class_names, f)
    print("Classes:", class_names)

    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.prefetch(buffer_size=AUTOTUNE)

    # Model (Transfer Learning)
    base_model = tf.keras.applications.MobileNetV2(
        input_shape=img_size+(3,),
        include_top=False,
        weights="imagenet"
    )
    base_model.trainable = False

    model = tf.keras.Sequential([
        tf.keras.layers.Rescaling(1./255),
        base_model,
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(len(class_names), activation="softmax")
    ])

    model.compile(optimizer="adam",
                  loss="sparse_categorical_crossentropy",
                  metrics=["accuracy"])

    print("Training base model...")
    model.fit(train_ds, validation_data=val_ds, epochs=epochs)

    # Fine tune
    base_model.trainable = True
    model.compile(optimizer=tf.keras.optimizers.Adam(1e-5),
                  loss="sparse_categorical_crossentropy",
                  metrics=["accuracy"])

    print("Fine-tuning model...")
    model.fit(train_ds, validation_data=val_ds, epochs=fine_tune_epochs)

    # Save model
    model.save("model.h5")
    print("✅ Model trained and saved as model.h5")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", default="dataset")
    parser.add_argument("--epochs", type=int, default=15)
    parser.add_argument("--fine_tune_epochs", type=int, default=5)
    args = parser.parse_args()

    train_model(args.data_dir, args.epochs, args.fine_tune_epochs)
