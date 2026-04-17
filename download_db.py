import gdown

folder_id = "128VOydnhhONOJY_S-yh-i2xWB9VDus18"

gdown.download_folder(
    id=folder_id,
    output="data",
    quiet=False
)