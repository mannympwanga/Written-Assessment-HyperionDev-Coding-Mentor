def resist(net):
    # Helper functions for series and parallel resistor calculations
    def ser(*args):
        return sum(args)

    def par(*args):
        return 1 / sum(1 / arg for arg in args)

    # Convert string representation of network to Python expression and evaluate
    tot = eval(net.replace('(', 'ser(').replace('[', 'par(').replace(']', ')'))

    # Return result rounded to nearest tenth of an ohm
    return round(tot, 1)


# Test the function with example cases
print(resist("[20, 30]"))  # should print 22.0
print(resist("[10, (20, 30)]"))  # should print 8.3
print(resist("([10, 20], (30, 40))"))  # should print 76.7
print(resist("(1, [12, 4, (1, [10, (2, 8)])])"))  # should print 3.0
# should print 10.0
print(resist("(6, [8, (4, [8, (4, [6, (8, [6, (10, 2)])])])])"))
