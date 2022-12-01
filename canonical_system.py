
def greedy_approoach(change, system):
    sorted_sys = sorted(system, reverse=True)
   

    representation = [0 for _ in sorted_sys]  # Create an empty solution list
    for i, sorted_sy in enumerate(sorted_sys):
        # If the coin can be subtracted from the change
        if sorted_sy <= change:
            multplier = change // sorted_sy # How many times can we subtract?
            representation[i] = multplier # Add to the solution
            change -= multplier * sorted_sy # Subtract the coin(s)
    
    return representation




def is_canonical(system, return_counterexample):
    '''
    The greedy algorithm repeatedly uses the biggest coin whose value is no 
    larger than the remaining amount. 
    '''
    sorted_sys = sorted(system, reverse=True)

    # Loop over every possible combination of indices
    for i in range(1, len(sorted_sys)):
        for j in range(i, len(sorted_sys)):

            # Compute the representation of greedy representation
            check_greedy = greedy_approoach(change=sorted_sys[i - 1] - 1, system=sorted_sys)
            # From the representation greedy, Theorem 1 in the paper
            # gives us a way to compute M(w), where w is the minimal candidate
            M_w = check_greedy.copy() # M(w) is equal for indices 1 trough j - 1
            M_w[j] = M_w[j] + 1 # M(w) is one greater in entry j
            M_w[j + 1:] = [0] * (len(M_w) - (j + 1)) # Remaining indices = 0

            # From M(w) we can compute the candidate minimal counterexample w
            w = sum(c_i * r_i for (c_i, r_i) in zip(sorted_sys, M_w))
            # The greedy representation of w
            G_w = greedy_approoach(change=w, system=sorted_sys)
            if sum(M_w) < sum(G_w):
                return (False, G_w, M_w) if return_counterexample else False

    return (True, None, None) if return_counterexample else True


         
    




print(is_canonical(system=[1, 2, 5, 10, 20, 50], return_counterexample=False))


test = [[1, 2, 5, 11, 23, 97],
[1,2,3,4,11,31,79],
[1,4,24,57,88,93],
[1,35,36,56,72,84,100],
[1,8,35,36,43,74],
[1,2,4,8,18,53],
[1,2,34,40,45,57,73],
[1,2,3,6,12,18,64]]

for i in range(len(test)):
    print(i, is_canonical(system=test[i], return_counterexample=True))




