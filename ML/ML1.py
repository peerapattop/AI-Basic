#การเรียกใช้ชุดข้อมูล Iris Data Set

from sklearn import datasets

iris_dataset = datasets.load_iris()

print(iris_dataset['data'][0:10]) # 10 แถวแรก

#ใช้ keys() เพื่อเช็ค
#dict_keys(['data', 'target', 'frame', 'target_names', 
# 'DESCR', 'feature_names', 'filename', 'data_module'])

