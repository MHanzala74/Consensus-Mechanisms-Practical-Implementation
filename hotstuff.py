import random

class HotStuff:
    def __init__(self, n, f):
        assert n >= 3*f + 1
        self.n = n
        self.f = f

    def run(self, value):
        print("Leader Proposes:", value)

        votes = random.randint(self.n-self.f, self.n)

        print("Votes received:", votes)

        if votes >= 2*self.f + 1:
            print("Aggregated Signature Created")
            print("Block Committed:", value)
        else:
            print("Consensus Failed")

hotstuff = HotStuff(7,2)
hotstuff.run("Block X")