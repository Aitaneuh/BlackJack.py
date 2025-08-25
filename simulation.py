import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from game import Game
from player import Player
from dealer import Dealer

simulation_count = 100000
results = []

for i in range(simulation_count):
    player = Player("Math master")
    dealer = Dealer("Las Vegas King")
    game = Game(player, dealer)
    results.append(game.play_one_game())
    print(f"{i+1}/{simulation_count}")

df = pd.DataFrame(results)

print(df.head())

print("\nOutcome counts:")
print(df["outcome"].value_counts())


print("\nMoyenne des scores joueur/dealer:")
print(df[["player_score", "dealer_score"]].mean())

print("\nTaux de victoire joueur:")
print((df["score"] > 0).mean())

counts = df["outcome"].value_counts()
percentages = counts / counts.sum() * 100

fig, ax = plt.subplots()

bars = ax.bar(np.array(counts.index, dtype=str), np.array(counts.values, dtype=float))

ax.bar_label(bars, labels=[f"{p:.1f}%" for p in percentages], padding=3)

ax.set_ylabel("Count")
ax.set_title("Blackjack Outcomes")
plt.show()