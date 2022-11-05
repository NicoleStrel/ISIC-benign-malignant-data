import pandas as pd
import os

def remove(remove):
    for i in remove:
        img = "images/"+i+".JPG"
        if os.path.exists(img):
            os.remove(img)

metadata = pd.read_csv('images/metadata.csv', low_memory=False)

#remove mislabelled
remove_df = metadata.loc[~metadata['benign_malignant'].isin(['benign', 'malignant'])]
all_remove = list(remove_df['isic_id'])
remove(all_remove)

#shorten dataset
rest_df = metadata.loc[metadata['benign_malignant'].isin(['benign', 'malignant'])]
rest_remove = list(rest_df['isic_id'])[9300:]
remove(rest_remove)
