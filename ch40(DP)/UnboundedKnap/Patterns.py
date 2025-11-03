"""
0/1 -> Here once we make a choice the element/index is processed and we never visit it again and increment i
Unbounded -> If we do not pick then it is processed and i+=1
          -> But if we do pick, we can keep picking and we just increment the weight not the i

Think of it this way, if YES then keep going till your heart is content. 
But once you say NO then its processed.

INTUITION: So have as much Snacks as you want before you say i am done and moving to Dessert. You cannot come back once you go.

Std Unbounded knapsack
Patterns:
	- Rod Cutting
	- Coin Exachange
	- Coin Exachange 2
    - Max Ribbon cut
"""
