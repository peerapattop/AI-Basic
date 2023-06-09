#การเรียกใช้ชุดข้อมูล MNIST DataSet ชุดข้อมูลลายมือตัวเลขอารบิก


from sklearn import datasets

digits_dataset = datasets.load_digits() #ตัวเลข

print(digits_dataset.images[0]) 

#ใช้ keys() เพื่อเช็ค

# print(digits_dataset.keys()) 

#dict_keys(['data', 'target', 'frame', 
# 'feature_names', 'target_names', 'images', 'DESCR'])

