# Towers of Hanoi
# source: https://www.geeksforgeeks.org/python-program-for-tower-of-hanoi/ 
# Recursive Python function to solve the tower of hanoi


def TowerOfHanoi(n, source, destination, auxiliary):
  # base case
  if n == 1:
    print("Move disk 1 from source", source, 
         "to destination", destination)
  # recursive step
  else: 
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print("Move disk", n, "from soure", source, 
          "to destination", destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
  
def main():
  n = 4
  TowerOfHanoi(n, 'A', 'B', 'C')
  #A, B, C names of rods 

if __name__ == "__main__":
  main()
