import numpy as np

# Array = np.array([1,2,3,4,5,6,7,8,9,10])
# print(Array)
# Min = np.min(Array)
# print(Min)
# Max = np.max(Array)
# print(Max)
# Shape = np.shape(Array)
# print(Shape)



arr1 = np.array([1,2,3,4,5])
arr2 = np.array([9,8,7,6,5])

print("Two array multiplication : ",arr1*arr2)
print("Two array Addition : ",arr1+arr2)
print("Two array Division : ",arr1/arr2)
print("Two array Power : ",arr1**arr2)

# print()
# print()
# print()
# print()


# Basic operation
print("Max of Array :",np.max(arr1))
print("Min of Array :",np.min(arr1))
print("Mean of Array :",np.mean(arr1))
print("STD of Array :",np.std(arr1))
print("Variance of Array :",np.std(arr1))


#Array Creation Operation
 
print("Zero's arr of 2*3 matrix:\n",np.zeros((2,3)))# Create 2 row and 3 col matrix of 1's
print("One's arr of 2*3 matrix:\n",np.ones((5,3))) # Create 5 row and 2 col matrix of 1's
print("LineSpace:\n",np.linspace(10,100,15)) #Divide 10 to 100 into 15 parts
print("Arange ",np.arange(2,27,3)) #start , stop , step 
print("Generate random",np.random.rand(2,3)) #Generate 2 by 3 matrix with random int from 0 to less then 1 
print(" Generate random int array\n",np.random.randint(1,100,size=(2,3))) #Create array of random integer in range 1 to 100 of size 2 by 3






# Simple array function

arr5 = np.array([1,2,3,4,5])

print("Shape : ",arr5.shape) #Gives no. of (row ,col)
print("Size",arr5.size) #Size of array
print("Data type of array : ",arr5.dtype)
print("Concatenated array",np.concatenate((arr1,arr2)))
