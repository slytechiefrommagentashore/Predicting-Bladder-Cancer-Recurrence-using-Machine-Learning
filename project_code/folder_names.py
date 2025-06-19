import os
import pandas as pd

# 👇 CHANGE this to your actual folder path
root_folder = r'D:\gall bladderr research dataset\manifest-1567090213715\TCGA-BLCA'

# Get only folder names (not files)
folder_names = [f.name for f in os.scandir(root_folder) if f.is_dir()]

# Convert to Excel
df = pd.DataFrame(folder_names, columns=["Folder Name"])
df.to_excel("folder_names.xlsx", index=False)

print("✅ Done! Saved as 'folder_names.xlsx'")
print("📂 Folders found:")