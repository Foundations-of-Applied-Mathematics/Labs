subroutine flaplace(u, t, n, m, it)
!   Solve Laplace's equation on a rectangular domain
!   with values at an equispaced grid of points.
!   Use the boundaries of the array u as the boundary conditions
!   Perform 'it' number of iterations on the values in u.
!   In each iteration set each value to the
!   average of its four neighbors
    implicit none
    integer, intent(in) :: n, m, it
!   Columns are listed first in in array shapes in Fortran.
    double precision, dimension(n, m), intent(inout) :: u
!   t is a preallocated temporary array.
    double precision, dimension(n-2, m-2), intent(inout) :: t
    integer i
    do i = 1, it
!       & is the line continuation character in Fortran.
!       Fortran supports array slice notation.
!       Indices for arrays start at 1.
!       The ranges indicated in the slices include the end points
!       of the range.
!       Column indices come before row indices.
        t = .25 * (u(1:n-2,2:m-1) +&
            u(3:n,2:m-1) + u(2:n-1,1:m-2) + u(2:n-1,3:m))
        u(2:n-1,2:m-1) = t
    enddo
end subroutine flaplace
