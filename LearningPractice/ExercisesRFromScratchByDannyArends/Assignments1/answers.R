# Analysis of Hardy-Weinberg equilibrium
#
# copyright (c) 2024 - Yevgeniy Gugala Fomin
# written by: Yevgeniy Gugala Fomin
# last modified 1 Aug, 2024
# first written 1 Aug, 2024

# Instruct R to go to the working directory
setwd("C:\\Users\\user\\Documents\\GitHub\\Bioinformatics\\LearningPractice\\ExercisesRFromScratchByDannyArends\\Assignments1")

# R as a calculator

# Use R to calculate the following:
# 1a) 1234 + 4567

    print(paste("1a =", 1234 + 4567))

# 1b) 100456 - 3350 + 23

    print(paste("1b =", 1234 + 4567))

# 1c) natural logarithm of 15

    print(paste("1c =", log(15)))

# 1d) 4596 / 12

    print(paste("1d =", 4596 / 12))

# 1e) 8998 * 76

    print(paste("1e =", 8998 * 76))

# 1f) Euclidean division remainder of 10 and 6 (When you divide 10 / 6 , what number remains?)

    print(paste("1f", 10 %% 6))

# 1g) the square root of -8 (Square root = what number multiplied by itself will give you said number)

    print(paste("1g =", sqrt_neg8 <- sqrt(-8 + 0i)))
    


# Vectors
# If you even need help about a function you can do ?functionname to get an overview of the function
# parameters, scroll down the end of the help page to have an example of how to use the function

# For these exercises store the result each time in a variable: vector2a, vector2b, etc unless specified
# differently in the assignment. 

# 2a) Use the c() function to create a vector from 1 to 10

    vector2a <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(paste("2a =", vector2a))

# 2b) Use the : operator to create a vector from 11 to 20

    vector2b <- c(11:20)
    print(paste("2b =", vector2b))

# 2c) We can also use the seq() function to create more complex vectors, 
# create a vector from 1 to 100 going in steps of 5. (so: 1, 6, 11, …)

    vector2c <- seq(from = 1, to = 100, by = 5)
    print(paste("2c =", vector2c))

# 2d) Use the LETTERS constant and the seq() function to create a vector 
# that stores all the ‘even’ letters (gerade Buchstaben: B, D, F, etc)

    vector2d <- LETTERS[seq(from = 2, to = 26 , by = 2)]
    print(paste("2d =", vector2d))

# 2e) what is the type of vector2a, either use the class() function or ask 
# explicitly using the is.numeric() , is.character() or the is.logical() functions

    vectorA_Class <- class(vector2a)
    print(paste("2e =", vectorA_Class))

# 2f) combine vector2a and vector2d, what is the type of the resulting vector ?

    vectorAplusDclass <- class(c(vector2a, vector2d))
    print(paste( "2f =", vectorAplusDclass))


# 2g) Use the sqrt() function to compute the square root of vector2a

    vector2aSqrt <- sqrt(vector2a)
    print(paste( "2g =", vector2aSqrt))

# 2h) Extra, square root the sum of vector 2a

    sum_vector2a <- sum(vector2a)
    sqrt_sum_vector2a <- sqrt(sum_vector2a)
    print(paste( "2h =", sqrt_sum_vector2a))




#     Matrices


# Store the result each time in a variable: matrix3a, matrix3b, etc


# 3a) We can use the matrix() function to create a matrix, create a 10x10 matrix that holds the numbers 1 to 100.

    
    matrix_10x10 <- matrix(1:100, nrow = 10, ncol = 10)
    matrix3a <- matrix_10x10

    print(paste("3a ="))
    print(matrix_10x10)
    
    
# 3b) If you look at the help file of the matrix() function, you see it has a parameter byrow do the same
# thing as in exercise 3a, but now set the byrow parameter to TRUE, how is this matrix different from
# the one in exercise 3a ?

    matrix_10x10byRow <- matrix(1:100, nrow = 10, ncol = 10, byrow = TRUE)
    matrix3b <- matrix_10x10byRow

    print(paste("3b ="))
    print(matrix_10x10byRow)

# 3c) Select the 5th column from matrix3a, and select the 5th row from matrix3b

    matrix3a_5th_column <- matrix3a[ ,5]
    matrix3b_5th_row <- matrix3b[5,]
    print(paste("3c ="))

    print(paste(matrix3a_5th_column))
    print(paste(matrix3b_5th_row))

# 3d) How can we translate matrix3a into matrix3b ?

    print(paste("3d ="))
    transposed3a_matrix <- t(matrix3a)
    transposed3a_matrix == matrix3b
    print(paste(transposed3a_matrix == matrix3b))

# 3e) Add column names to matrix3a, using the LETTERS constant

    print(paste("3e ="))
    colnames(matrix3a) <- paste0("Column", LETTERS[1:ncol(matrix3a)])
    print(matrix3a)
  

# 3f) Look up help for paste() and add your own rownames to matrix3a, in the structure: “measurement N”, where N is the row number

    print(paste("3f ="))
    rownames(matrix3a) <- paste("Measurement", (1:10))
    print(matrix3a)