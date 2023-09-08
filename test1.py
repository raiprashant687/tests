# l = [1,2,3,4,5,6,1]
# new = {}
# for num in l:
#     if num not in new:
#         new[num] = 0
#         new[num] = new[num] +1
#     else:
#         new[num] = new[num] + 1
#
# for key,value in new.items():
#     if new[key] > 1:
#         print(key)

# from collections import Counter
#
# print(Counter([1,2,3,1,1,1,1,1,4,4,4,4,4,2,3,3]))
class Vehicle:
    def maruti(self):
        print("i am the real one")

def ford(self):
    print("i am just for time pass")
Vehicle.maruti = ford

x = Vehicle()
x.maruti()