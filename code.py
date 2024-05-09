def read_from_file(message_file):
  input = []
  with open(message_file, 'r') as file:
    for line in file:
      words = line.split()
      if len(words) != 2:
        raise ValueError("Invalid input file format")
      if not words[0].isdigit():
        raise ValueError("1st word in the file is not a digit")
      input.append((int(words[0]), words[1]))
  return input

def pyramid_can_be_formed(input):
  n = len(input)
  expected_sum = (n * (n + 1)) // 2
  return expected_sum == sum(num for num, word in input)

def consecutive_numbers(input):
  for i in range(1, len(input)):
    if input[i][0] - input[i-1][0] != 1:
      return False
  return True

def print_msg(input):
  i = 1
  while True:
    n = i * (i + 1) // 2 - 1
    if n > len(input):
      break
    num, word = input[n]
    print(f"{num}: {word}")
    i += 1

def decode(message_file):
    input = read_from_file(message_file)
    if not pyramid_can_be_formed(input):
      raise ValueError("Pyramid cannot be formed") 
    input.sort(key=lambda x: x[0])
    if not consecutive_numbers(input):
      raise ValueError("Numbers are not consecutive")
    print_msg(input)


