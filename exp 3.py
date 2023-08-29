import numpy as np
num_bedrooms=np.array([3,4,5,6,3,5,4,6,5,7])
sale_prices=np.array([200000,250000,300000,350000,180000,320000,260000,380000,290000,410000])
houses_with_more_than_4_bedrooms=num_bedrooms>4

filtered_sale_prices=sale_prices[houses_with_more_than_4_bedrooms]

avg_sale_price=np.mean(filtered_sale_prices)
print(f"the average sale price of houses with more than four bedrooms is ${avg_sale_price:.2f}.")
