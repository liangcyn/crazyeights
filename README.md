# crazyeights
Crazy eights puzzle game.

## Rules (copied and edited from [kidspot] (https://www.kidspot.com.au/things-to-do/activity-articles/how-to-play-crazy-eights/news-story/4b1a3fdda104f68e45bd92a41fcc6297?)):

1. Each player is dealt seven cards. The remaining cards are placed face down in the center of the table, forming a draw pile. The top card of the draw pile is turned face up to start the discard pile next to it.

2. First player adds to the discard pile by playing one card that matches the top card on the discard pile either by suit or by rank (i.e. 6, jack, ace, etc.). A player who cannot match the top card on the discard pile by suit or rank must draw cards until he can play one.

3. When the draw pile is empty, a player who cannot add to the discard pile passes his turn.

4. All eights are wild and can be played on any card during a player's turn.

5. When a player discards an eight, he chooses which suit is now in play.

6. The next player must play either a card of that suit or another eight.

7. The first player to discard all of his cards wins.

## Structure
- card objects with the following attributes:
  - suit (clubs, diamonds, hearts, spades)
  - value (ace, two, three, ..., queen, king)
  
- deck, a stack (for easy access to last element)
