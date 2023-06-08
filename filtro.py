import cv2
import os

base_dir = os.getcwd()
path = base_dir+'/COVID-19_Radiography_Dataset/Viral Pneumonia/images'
url = os.listdir(path)
print(len(url))
for i in range(len(url)):
    nameread = "Viral Pneumonia-" + str(i+1) + ".png"
    img_path = path + "/" + nameread
    # print (nameread)
    img = cv2.imread(img_path)
    bilateral = cv2.bilateralFilter(img, 9, 75, 75)
    name = "Viral Pneumonia-" + str(i+1) + "-filtrado.png"
    save_img_path = os.path.join(base_dir, "Viral-Bilateral-Filter", name)
    cv2.imwrite(save_img_path, bilateral)
    
'''# Read the image.
img = cv2.imread('COVID-1.png')
  
# Apply bilateral filter with d = 15, 
# sigmaColor = sigmaSpace = 75.
bilateral = cv2.bilateralFilter(img, 9, 75, 75)
  
# Save the output.
cv2.imwrite('COVID-1_bilateral.png', bilateral)'''
