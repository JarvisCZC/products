# 使用while loop, 用於不知道會輸入多少項目時
products = []
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q': #逃出迴圈
		break
	price = input('請輸入商品價格： ')
	#p = []
	#p.append(name)
	#p.append(price)
	#products.append(p) #清單中還有清單
	products.append([name, price]) #最佳寫法，不用再定義小清單

print(products)

# products[0][0] #第1個大清單內的第1個小清單