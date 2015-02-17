def compareDiff(num1,num2):
	list_num1 = map(int,str(num1))
	list_num2 = map(int,str(num2))
	len_num1 = len(list_num1)
	len_num2 = len(list_num2)

	
	if (len_num1==len_num2):
		return (True if num1>num2 else False)
	else:
		G = {len_num1:list_num1,len_num2:list_num2}
		less = min(len_num1,len_num2)
		greater = max(len_num1,len_num2)

		diff = greater - less
		first = G[less][0]

		for i in range(0,diff):
			G[less].append(first)

		piv = (less if less==len_num2 else greater)
		other = (less if less!=len_num2 else greater)


		int_piv=int(''.join(map(str,G[piv])))
		int_other=int(''.join(map(str,G[other])))


		if int_other>int_piv: 
			return True
		else:
			return False



def partition(arr,l,r):
	#set pivot equal to the first element of the array
	pivot = arr[l]
	i = l+1
	j = l+1

	#iterate all the element after array
	for j in range(j,r):
		#if jth element less than pivot, swap it with ith element
		if compareDiff(arr[j],pivot):
			arr[j],arr[i] = arr[i],arr[j]
			i += 1

	#swap the pivot to the middle	
	arr[i-1],arr[l] = arr[l],arr[i-1]

	return i-1,[arr[i-1]]

def QuickSort(array):
	#base case for recursive call
	if len(array) <= 1:
		return array

	else:
		index,p = partition(array,0,len(array))

		#return all the elements on the left side of the pivot
		left = QuickSort(array[:index])

		#return all the elements on the right side of the pivot
		right = QuickSort(array[index+1:])
		
		return left + p + right

def main():
	# a testing method
	data=[3,3612,34,5,9]

	return QuickSort(data)

print main()