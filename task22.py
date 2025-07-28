#---------------------------------------------------
#Matrix Multiplication
#---------------------------------------------------
# Matrix Multiplication with User Input

def input_matrix(rows, cols, name="Matrix"):
    print(f"\nEnter values for {name}:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            raise ValueError(f"Each row must have exactly {cols} integers.")
        matrix.append(row)
    return matrix

def multiply_matrices(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Input matrix sizes
r1 = int(input("Enter number of rows for Matrix A: "))
c1 = int(input("Enter number of columns for Matrix A: "))
r2 = int(input("Enter number of rows for Matrix B: "))
c2 = int(input("Enter number of columns for Matrix B: "))

# Check matrix multiplication condition
if c1 != r2:
    print("Matrix multiplication not possible. Columns of A must equal rows of B.")
else:
    A = input_matrix(r1, c1, "Matrix A")
    B = input_matrix(r2, c2, "Matrix B")

    print("\nMatrix A:")
    for row in A:
        print(row)

    print("\nMatrix B:")
    for row in B:
        print(row)

    result = multiply_matrices(A, B)

    print("\nResultant Matrix after Multiplication:")
    for row in result:
        print(row)
