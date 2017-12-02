#
# Initialize Arrays A1...At to be sorted  
A0 <- [[4,7,3,9,1,4,3,2,6,8,4,3,6,9,3],[0,4,2,6,7,4,3,8],[7,4,2,1,0,4,3,5,6]]
# Provide maximum element value from all observed Arrays
k <- 9
# Provide length of concatenated Array
m <- 0
for d in range(0, len(A0)):
    for e in range(0, len(A0[d])):
        m += 1
ENDFOR
    ENDFOR
OUTPUT (m)
# Modify A1...At: To each element g from A0[f] we add f*k so that Array
     ENDIF
# boundaries persist after CountingSort
# Concatenate A1...At in one Array
A <- m*[0]
aind <- 0
for f in range (0, len(A0)):
    for g in range (0, len(A0[f])):
        A[aind] <- f*k + A0[f][g]
        aind += 1
ENDFOR
    ENDFOR
OUTPUT (A)
FUNCTION counting_sort(array, maxval):
    """in-place counting sort"""
    n <- len(array)
    m <- maxval + 1
    count <- [0] * m               # init with zeros
    for a in array:
        count[a] += 1             # count occurences
    ENDFOR
    i <- 0
    for a in range(m):            # emit
        for c in range(count[a]): # - emit 'count[a]' copies of 'a'
            array[i] <- a
            i += 1
    ENDFOR
        ENDFOR
    RETURN array
ENDFUNCTION

OUTPUT counting_sort(A,m)
# Re-calculate arrays from A
    # Create result array X with same subarray structure as A0 
X <- len(A0)*[[]]
for r in range(0, len(A0)):
    X[r] <- len(A0[r])*[0]
    # Fill X with values from A, re-calculated to subtract previously added multiples of k
ENDFOR
OUTPUT (X)
xind <- 0    
for p in range(0, len(A0)):
    for q in range(0, len(A0[p])):
        X[p][q] <- int(A[xind] - p*k)
        xind += 1
ENDFOR
    ENDFOR
OUTPUT (X)
