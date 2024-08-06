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

# 2c) We can also use the seq() function to create more complex vectors, create a vector from 1 to 100 going in steps of 5. (so: 1, 6, 11, …)

    vector2c <- seq(from = 1, to = 100, by = 5)
    print(paste("2c =", vector2c))

# 2d) Use the LETTERS constant and the seq() function to create a vector that stores all the ‘even’ letters (gerade Buchstaben: B, D, F, etc)

    vector2d <- LETTERS[seq(from = 2, to = 26 , by = 2)]
    print(paste("2d =", vector2d))

# 2e) what is the type of vector2a, either use the class() function or ask explicitly using the is.numeric() , is.character() or the is.logical() functions

    vectorA_Class <- class(vector2a)
    print(paste("2e =", vectorA_Class))

# 2f) combine vector2a and vector2d, what is the type of the resulting vector ?

    vectorAplusDclass <- class(c(vector2a, vector2d))
    print(paste( "2f =", vectorAplusDclass))


# 2g) Use the sqrt() function to compute the square root of vector2a

    vector2aSqrt <- sqrt(vector2a)
    print(paste( "2g =", vector2aSqrt))

# 2h) Extra, square root the sum of vector 2a

    sumVector2a <- sum(vector2a)
    sqrtSumVector2a <- sqrt(sumVector2a)
    print(paste( "2h =", sqrtSumVector2a))