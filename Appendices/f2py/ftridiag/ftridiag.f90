! This will be a subroutine since it does not
! return any values.
subroutine ftridiag(a, b, c, x, n)
    
!   Use the implicit none statement to say that
!   every variable must be explicitly declared
!   with a type.
!   Fortran allows a programmer to use undeclared
!   variables and has methods for inferring types
!   of undeclared variables. Using implicit type
!   declarations tends to cause errors and is now
!   widely considered poor style.
    implicit none

!   Here we declare the types for the inputs.
!   The 'dimension' statement tells the compiler that
!   the argument is an array of the given shape.
    integer, intent(in) :: n
    double precision,dimension(n),intent(in) :: b
    double precision,dimension(n),intent(inout) :: x
    double precision,dimension(n-1),intent(in) :: a
    double precision,dimension(n-1),intent(inout) :: c
    
!   Two temporary variables.
!   'm' is a temporary value.
!   'i' is the index for the loops.
    double precision m
    integer i
    
!   Here is the actual computation:
    c(1) = c(1) / b(1)
    x(1) = x(1) / b(1)
!   This is the syntax for a 'for' loop in Fortran.
!   Indexing for arrays in fortran starts at 1
!   instead of starting at 0 like it does in Python.
!   Arrays are accessed using parentheses
!   instead of brackets.
    do i = 1,n-2
        m = 1.0D0 / (b(i+1) - a(i) * c(i))
        c(i+1) = c(i+1) * m
        x(i+1) = x(i+1) - a(i) * x(i)
        x(i+1) = x(i+1) * m
!   Note that you have to explicitly end the loop.
    enddo
    x(n) = (x(n) - a(n-1) * x(n-1)) / (b(n) - a(n-1) * c(n-1))
    do i = n-1,1,-1
        x(i) = x(i) - c(i) * x(i+1)
    enddo
!   You must also explicitly end the function or subroutine.
end subroutine ftridiag
