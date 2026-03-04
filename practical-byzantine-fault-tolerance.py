import random

"""
PBFT (Practical Byzantine Fault Tolerance) Simulation

Description:
Simulates 3-phase PBFT protocol:
1. Pre-Prepare
2. Prepare
3. Commit

Safety Condition:
n >= 3f + 1
"""
class PBFT:
    """Simple PBFT simulation."""
    def __init__(self, n, f):
        assert n >= 3*f + 1, "Safety violated (n >= 3f+1)"
        self.n = n
        self.f = f
        self.nodes = ["Node"+str(i) for i in range(n)]

    def run(self, value):
        print("Phase 1: Pre-Prepare")
        print("Primary proposes:", value)

        print("Phase 2: Prepare")
        prepare_votes = random.randint(self.n-self.f, self.n)
        print("Prepare Votes:", prepare_votes)

        if prepare_votes >= 2*self.f + 1:
            print("Prepared State Achieved")

            print("Phase 3: Commit")
            commit_votes = random.randint(self.n-self.f, self.n)
            print("Commit Votes:", commit_votes)

            if commit_votes >= 2*self.f + 1:
                print("Final Consensus:", value)
            else:
                print("Commit Failed")
        else:
            print("Prepare Failed")

pbft = PBFT(n=4, f=1)
pbft.run("Block 1")