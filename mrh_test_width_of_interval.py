from kmer_mutation_formulas_thm5 import confidence_interval_r1_from_n_mutated
import math
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python mrh_test_width_of_interval.py <L> <k>")
        sys.exit(1)
    try:
        L = int(sys.argv[1])
        k = int(sys.argv[2])
    except:
        print("L and k must be integers.")
        sys.exit(1)    
        
    alpha = 0.05

    for x in range(101):
        r1 = x/100.0
        c0, c1 = confidence_interval_r1_from_n_mutated(L,k,r1,alpha)
        if math.isnan(c0):
            c0 = 0.0
        if math.isnan(c1):
            c1 = 1.0
            
        print(f"{r1:.2f} {c1-c0:.4f}")