import os

# define the paths to the images directory
# IMAGES_PATH = "../datasets/kaggle_dogs_vs_cats/train"
BASE_PATH = r"C:\github\\create_hdf5\deeplearning\datasets\kaggle_dogs_vs_cats"
IMAGES_PATH = os.path.join(BASE_PATH, "train")

# since we do not have validation data or access to the testing
# labels we need to take a number of images from the training
# data and use them instead
NUM_CLASSES = 2
NUM_VAL_IMAGES = 1250 * NUM_CLASSES
NUM_TEST_IMAGES = 1250 * NUM_CLASSES

# define the path to the output training, validation, and testing HDF5 files
HDF5_PATH = r"C:\github\\create_hdf5\deeplearning\datasets\kaggle_dogs_vs_cats\hdf5"
TRAIN_HDF5 = os.path.join(HDF5_PATH, "train.hdf5")
VAL_HDF5 = os.path.join(HDF5_PATH, "val.hdf5")
TEST_HDF5 = os.path.join(HDF5_PATH, "test.hdf5")

# define the path to the output directory used for storing plots,
# classification reports, etc.
OUTPUT_PATH = r"C:\github\create_hdf5\output"

# path to the output model file
MODEL_PATH = os.path.join(HDF5_PATH, "alexnet_dogs_vs_cats.model")

# define the path to the dataset mean
DATASET_MEAN = os.path.join(HDF5_PATH, "dogs_vs_cats_mean.json")
