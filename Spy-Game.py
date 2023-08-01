def spy_game(numbers):

  # Check if the list is long enough to contain 007. If it is, then the list cannot contain 007 in order, so the function returns False.
  if len(numbers) < 3:
       return False

  # Initialize a variable to keep track of the number of zeros that have been seen.
  zeros = 0

  # Iterate through the list.
  for i in range(len(numbers)):

    # If the current number is 0, increment the number of zeros by 1.
    if numbers[i] == 0:
      zeros += 1
      
    # If the current number is 7 and the number of zeros is 2, then the list contains 007 in order, return True.
    elif numbers[i] == 7 and zeros == 2:
      return True
      
    # Otherwise, reset the number of zeros to 0.
    else:
      zeros = 0

  # Return False if the end of the list is reached without finding 007.
  return False
