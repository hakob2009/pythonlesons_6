import matplotlib.pyplot as plt

n = 10
index_list = []
fact_list = []
fact = 1
for f in range(1,n+1):
    fact = fact * f
    index_list.append(f)
    fact_list.append(fact)

# plt.plot(index_list,fact_list)
plt.bar(index_list,fact_list)
plt.show()