import random

"""
Delegated Proof of Stake (DPoS) Simulation

Description:
Token holders vote for delegates.
Top N delegates are selected.
"""

token_holders = {
    "User1": 100,
    "User2": 50,
    "User3": 200
}

delegates = ["A","B","C","D"]

def elect_delegates():
    votes = {d:0 for d in delegates}

    for holder, tokens in token_holders.items():
        choice = random.choice(delegates)
        votes[choice] += tokens

    sorted_delegates = sorted(votes.items(), key=lambda x: x[1], reverse=True)
    return sorted_delegates[:2]

print("Elected Delegates:", elect_delegates())