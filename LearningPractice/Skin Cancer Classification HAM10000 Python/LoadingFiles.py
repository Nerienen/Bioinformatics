import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import os
from glob import glob
from PIL import Image
import torchvision
from torchvision import transforms
from torch.utils.data import DataLoader

print("Script started")
skin_df = pd.read_csv('N:\AI Data\dataverse_files\HAM10000_metadata.csv')

print ("Hello")

# print("CSV loaded successfully!")
# print(skin_df.head())

folder_path = r'N:\AI Data\dataverse_files\HAM10000_images'
image_path = {os.path.splitext(os.path.basename(x))[0]: x 
              for x in glob(os.path.join(folder_path, '*.jpg'))}

#Define the path and add as a new column
skin_df['path'] = skin_df['image_id'].map(image_path.get)
#Use the path to read images.
skin_df['image'] = skin_df['path'].map(lambda x: np.asarray(Image.open(x).resize((32,32))))

print(skin_df['dx'].value_counts())

n_samples = 5  # number of samples for plotting
# Plotting
fig, m_axs = plt.subplots(7, n_samples, figsize = (4*n_samples, 3*7))
for n_axs, (type_name, type_rows) in zip(m_axs, 
                                         skin_df.sort_values(['dx']).groupby('dx')):
    n_axs[0].set_title(type_name)
    for c_ax, (_, c_row) in zip(n_axs, type_rows.sample(n_samples, random_state=1234).iterrows()):
        c_ax.imshow(c_row['image'])
        c_ax.axis('off')

#Actinic keratoses and intraepithelial carcinoma / Bowen's disease (AKIEC),
#basal cell carcinoma (BCC),
#benign keratosis-like lesions (solar lentigines / seborrheic keratoses and lichen-planus like keratoses, BKL),
#dermatofibroma (DF),
#melanoma (MEL),
#melanocytic nevi (NV)
#vascular lesions (angiomas, angiokeratomas, pyogenic granulomas and hemorrhage, VASC).