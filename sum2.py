# function which accepts the given list and list size
# as parameters and calculates the sum of the given list using recursion


def sumListRecursion(given_list, sizeOflist):
  # Return 0 if the list's length is zero.(base condition)
    if (sizeOflist == 0):
        return 0
    else:
      # Otherwise, along with the recursive function call,
      # return the sum of the last entry of the list (with the size reduced by 1).

        return given_list[sizeOflist-1] + sumListRecursion(given_list, sizeOflist-1)


# Give the input of the list as static input and store it in a variable.
given_list = [9, 1, 27, 48, 91, 93, 99, 27, 29,
              33, 39, 19, 11, 27, 29, 35, 39, 12, 65, 69, 67]
# Calculate the size of the list using len() function and store it in a variable.
sizeOflist = len(given_list)
# passing the given list and sizeOflist as arguments to the recursive function sumListRecursion.
print('The sum of the given list\n', given_list, '\nwith size ',
      sizeOflist, ' =', sumListRecursion(given_list, sizeOflist))