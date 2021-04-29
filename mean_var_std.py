import numpy as np

def calculate(list):
  arr=np.array(list,dtype='float')
  if(len(list)<9):
    raise ValueError("List must contain nine numbers.")
  arr=arr.reshape(3,3)
  
 
  m=[np.mean(arr,axis=0).tolist(),np.mean(arr,axis=1).tolist(),np.mean(arr.flatten()).tolist()]
  v=[np.var(arr,axis=0).tolist(),np.var(arr,axis=1).tolist(),np.var(arr.flatten()).tolist()]
  sd=[np.std(arr,axis=0).tolist(),np.std(arr,axis=1).tolist(),np.std(arr.flatten()).tolist()]
  mx=[np.max(arr,axis=0).tolist(),np.max(arr,axis=1).tolist(),np.max(arr.flatten()).tolist()]
  mi=[np.min(arr,axis=0).tolist(),np.min(arr,axis=1).tolist(),np.min(arr.flatten()).tolist()]
  sm=[np.sum(arr,axis=0).tolist(),np.sum(arr,axis=1).tolist(),np.sum(arr.flatten()).tolist()]
  calculations={
    'mean':m,
    'variance':v,
    'standard deviation':sd,
    'max':mx,
    'min':mi,
    'sum':sm
  }

  return calculations
