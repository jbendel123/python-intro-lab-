import math 
swallow_weight = 60/3
swallows_per_coconut = 1450 /swallow_weight 
answer = 1450/swallow_weight
print (answer) 

carrying_weight_percentage = 1/3
coconut_weight = 1450
macaw_weight = 900
macaw_limit = macaw_weight * carrying_weight_percentage
number_macaws = coconut_weight/macaw_limit
print(math.ceil(number_macaws))