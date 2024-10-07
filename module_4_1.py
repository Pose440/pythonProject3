from fake_math import divide as error
from true_math import divide as inf

result1 = error(12,4)
result2 = error(43,0)
result3 = inf(55,5)
result4 = inf(88,0)
print(result1)
print(result2)
print(result3)
print(result4)