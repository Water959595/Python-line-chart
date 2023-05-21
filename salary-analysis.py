import matplotlib.pyplot as plt
import random   #引入random

x = []
y = []
z = []
r = []

for i in range(1,7): # 做 6次
    x.append(i)
    y.append(i**2)
    z.append(i**3)
    a = random.randint(1,200)  #產生隨機整數
    r.append(a)                #綠線會不斷變化
    
print(x)
print(y)
print(z)
print(r)
print(len(x),len(y),len(z),len(r))

plt.plot(x,y,label = "Jonah")  # 3組數據 (x,y)(x,z)(x,r)
plt.plot(x,z,label = "Ryan")
plt.plot(x,r,label = "Louie")

plt.grid()                #顯示格線
plt.title("Square")
plt.xlabel("Month")
plt.ylabel("Salary")
plt.legend(loc = "best")  #顯示圖例(location = 最佳位置) (4 右下)(2 左上) (plot要加 label)
plt.show()                #隱藏位址id
