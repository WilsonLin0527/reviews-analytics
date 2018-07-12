data = [];
count = 0;
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line);
		count += 1;
		
print('檔案讀取完了,總共有', len(data), '資料');
len_1 = 0;
#for i in range(0, len(data) - 1, 1):
for d in data:
	len_1 += len(d);
print('average len is', len_1 / len(data));
