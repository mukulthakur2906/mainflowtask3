#----------------------------------------
# Matrix Addition
#-----------------------------------------
# Function to input a matrix
def input_matrix(rows, cols, name="Matrix"):
    print(f"\nEnter elements for {name}:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1} (space-separated): ").split()))
        if len(row) != cols:
            print("Invalid input. Please enter exactly", cols, "values.")
            return None
        matrix.append(row)
    return matrix

# Input number of rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input both matrices
A = input_matrix(rows, cols, "Matrix A")
B = input_matrix(rows, cols, "Matrix B")

# Check if both matrices were input correctly
if A is None or B is None:
    print("Matrix input error.")
else:
    # Perform matrix addition
    result = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]

    # Output the result
    print("\nResultant Matrix after Addition:")
    for row in result:
        print(" ".join(map(str, row)))

