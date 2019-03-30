import sys
import itertools

# fareCost: int - total cost of fare for transportation
# gaavoPieces: int[] - list of integer denominations of gaavo pieces
def findMinSubset(fareCost, gaavoPieces):
	"""
	Finds and returns the minimum number such that the first num elements of the gaavoPieces 
	list contains a subset which sums to fareCost, 0 otherwise
	"""

	""" 
	Create truth matrix (2d list) where the (i,j)th index represents if 
	there exists a subset of the first i_th elements of gaavoPieces that sums to j.
	Note: the dimensions are (number of pieces + 1) x (fare amount + 1)
	"""
	sumLookup = [[0 for i in range(fareCost+1)] for j in range(len(gaavoPieces) + 1)]
	for i in range(1, len(gaavoPieces) + 1):
		for j in range(1, fareCost + 1):
			if j - gaavoPieces[i-1] >= 0:
				if gaavoPieces[i-1] == j or sumLookup[i-1][j] == True or sumLookup[i-1][j - gaavoPieces[i-1]] == True:
					if(j == fareCost):
						return i
					sumLookup[i][j] = 1
			elif gaavoPieces[i-1] == j or sumLookup[i-1][j] == True:
				if(j == fareCost):
					return i
				sumLookup[i][j] = 1
	return 0 

# fareCost: int - number to which subset needs to add to 
# denominations: int[] - list of gaavo pieces
def findPieces(fareCost, denominations):

	for i in range(1, len(denominations) + 1):
		subsets = itertools.combinations(denominations, i)
		for subset in subsets:
			gaavoSum = 0 
			for gaavo in subset:
				gaavoSum += gaavo

			if gaavoSum == fareCost:
				neededGaavos = []
				for gaavo in subset:
					neededGaavos.append(gaavo)
				return neededGaavos	
	return []

def main():
	# Read in and check command line arguments
	if len(sys.argv) < 3:
		print("Please provide a total fare amount and denomination(s)")
		return 

	fareCost = int(sys.argv[1])
	gaavoPieces = []
	for gaavoPiece in sys.argv[2:]:
		gaavoPieces.append(int(gaavoPiece))

	minSize = findMinSubset(fareCost, gaavoPieces)
	if minSize == 0:
		print("You do not have a necessary combinations of Gaavos in order to complete the transaction.")
		return

	minPieces = gaavoPieces[:minSize]
	finalList = findPieces(fareCost, minPieces)
	print("The following gaavo(s) will be sufficient to pay with:")
	for gaavo in finalList:
		print(gaavo)


if __name__ == "__main__": 
    main()
