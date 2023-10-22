#CSCI 71 Programming Project
#194892 - Kyle Tandoc

#Generating possibilities. Write programs that facilitate the generation of possible answers, given n (n is presumably the size of the input). Specifically:

#a. Write a program that generates all subsets of the set {1, 2, ... , n}.
def generateSubsets(n):
    #create subsets variable that already has empty set to accept n = 0
    subsets = [[]]
    for x in range(1, n+1):
        #list comprehension that performs recursions on previous iterations to determine new subsets (e.x. n = 2: once subsets = [], [1] -> this determines that once [2] has been added to the end of the list that it will create a new subset of [1, 2] then adds it to the subsets variable making subsets = [], [1], [2], [1, 2])
        newSubsets = [subset + [x] for subset in subsets]
        subsets.extend(newSubsets)
    return subsets

#b. Write a program that generates all permutations over the elements {1, 2, ... , n}.
def generatePermutations(n):
    if n == 0:
        return [[]]

    permutations = []
    #performs recursion again to calculate permutations so it calls itself until it reaches a base case
    for x in generatePermutations(n-1):
        for i in range(n):
            #navigates list since base case of 1 returns a list of [1]. #inserts integer n into the list at position i, then appends the resulting list to the list of permutations
            permutations.append(x[:i] + [n] + x[i:])
    return permutations

# functionality for .exe file
print("Choose a function to test. Input one of the following options:")
print("1 - Generate Subsets")
print("2 - Generate Permutations")

while(True):
    choice = input()
    if choice == "1":
        n = int(input("Enter a value for n: "))
        subsets = generateSubsets(n)
        print("The subsets for %d are: %s" % (n, subsets))
        print("Press 0 to exit, 1 to continue, 2 to Generate Permutations")
    elif choice == "2":
        n = int(input("Enter a value for n: "))
        permutations = generatePermutations(n)
        print("The permutations for %d are: %s" % (n, permutations))
        print("Press 0 to exit, 2 to continue, 1 to Generate Subsets")
    else:
        exit()
    
    