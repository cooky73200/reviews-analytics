data = []
count = 0
i = 0
g = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		count = count + 1				
		data.append(line)
		if count % 100000 ==0:
			print(len(data))
			count = 0
print('檔案讀取完 總共有', len(data), '筆資料')
while i < len(data):
	g = len(data[i]) + g
	i = i + 1	
print('平均資料長度為', g / len(data), '個字')	
	

	