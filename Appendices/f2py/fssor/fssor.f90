! This will be a subroutine since it does not
! return any values.
subroutine fssor(U, m, n, omega, tol, maxiters, info)
    
!   Here we declare the types for the inputs.
!   This is where we use the c_double and c_int types.
!   The 'dimension' statement tells the compiler that
!   the argument is an array of the given shape.
    integer, intent(in) :: m, n, maxiters
    double precision, intent(out) :: info
    double precision, dimension(m,n), intent(inout) :: U
    double precision, intent(in) :: omega, tol
    
!   Temporary variables:
!   'maxerr' is a temporary value.
!   It is used to determine when to stop iteration.
!   'i', 'j', and 'k' are indices for the loops.
!   lcf and rcf will be precomputed values
!   used on the inside of the loops.
    double precision :: maxerr, temp, lcf, rcf
    integer i, j, k
    
    lcf = 1.0D0 - omega
    rcf = 0.25D0 * omega
    do k = 1, maxiters
        maxerr = 0.0D0
        do j = 2, n-1
            do i = 2, m-1
                temp = U(i,j)
                U(i,j) = lcf * U(i,j) + rcf * (U(i,j-1) + U(i,j+1) + U(i-1,j) + U(i+1,j))
                maxerr = max(abs(U(i,j) - temp), maxerr)
            enddo
        enddo
!       Break the outer loop if within
!       the desired tolerance.
        if (maxerr < tol) exit
    enddo
!   Here we have it set status to 0 if
!   the desired tolerance was attained
!   within the the given maximum
!   number of iterations.
    if (maxerr < tol) then
        info = 0
    else
        info = 1
    end if
end subroutine fssor
