import requests
import pickle
import numpy as np

f=open("turnover.pkl","rb")
mp=pickle.load(f)
v=mp.predict(np.array([[0.9,0.3,2,20,1]]))

print(*v)