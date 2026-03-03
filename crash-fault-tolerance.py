import random

class CFTCluster:
    def __init__(self, n, f):
        assert n >= 2*f + 1, "Safety condition violated (n >= 2f+1)"
        self.n = n
        self.f = f
        self.nodes = ["Node"+str(i) for i in range(n)]

    def propose(self, value):
        alive_nodes = random.sample(self.nodes, self.n - self.f)
        votes = len(alive_nodes)
        quorum = (self.n // 2) + 1

        print("Alive Nodes:", alive_nodes)
        print("Votes:", votes)

        if votes >= quorum:
            print("Consensus Reached:", value)
        else:
            print("Consensus Failed")

cluster = CFTCluster(n=5, f=2)
cluster.propose("Transaction A")