import statistics as st
from fractions import Fraction as fr
from decimal import Decimal as dec
from decimal import *
import random as ran
def test_fr_dec():
  a=[12,15,10,3,5]
  print (st.mean(a)) #mean tính giá trị trung bình

  print (fr(1.13))

  getcontext().prec = 6 #using decimal *
  print (dec(1)/dec(7))

  a=[fr(12, 35),fr(1.54),fr(2,17),fr()]
  print (st.mean(a))

def create_rand_mean():
  data_points = [ ran.randint(1, 100) for x in range(1,1001) ]
  print (st.mean(data_points))
 
  data_points = [ ran.triangular(1, 100, 80) for x in range(1,1001) ]
  print (st.mean(data_points))
  
  print(st.mode(["cat", "dog", "dog", "cat", "monkey", "monkey", "dog"]))
  #mode đếm tần suất xuất hiện của các phần tử

create_rand_mean()
