import numpy as np
import matplotlib.pyplot as plt
salestr=str(input("Enter the data:"))
saleslist=list(map(int,salestr.split()))
sales=np.array(saleslist)
print(sales)
print(f"The total sales:{np.sum(sales)}")
print(f"The average sales are:{np.mean(sales)}")
print(f"The month with the highest sales was:{np.argmax(sales)+1}/25")
indices=np.array(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
plt.plot(indices,sales)
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Sales Graph")
plt.show()

