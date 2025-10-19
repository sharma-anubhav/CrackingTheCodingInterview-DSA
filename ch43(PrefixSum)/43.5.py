"""
YouTube Video Unusual Days
A YouTuber has fetched the number of likes and dislikes of a video each day since its publication, 
with the goal of finding days with unusually high or low like-to-dislike ratios.

We are given two arrays,likes and dislikes, of length n, representing the likes and dislikes on each day.

The reception score of a day is the number of likes minus the number of dislikes. 
The deviation between two days is the absolute value of the difference in their reception scores. 
The total deviation of a given day is the sum of the deviations between it and every other day.

Find the highest total deviation of any day and return it.
"""

likes    = [3, 6, 1]
dislikes = [0, 1, 9]
Output = 24

"""
The reception scores are [3, 5, -8]. The total deviation of each day is:
day 0: |3 - 5| + |3 - (-8)| = 2 + 11 = 13
day 1: |5 - 3| + |5 - (-8)| = 2 + 13 = 15
day 2: |-8 - 3| + |-8 - 5| = 11 + 13 = 24
"""
### TOO DIFFICULT TO THINK OF IN A INTERVIEW!!! SKIPPING
explanation = """
If you have negatives, say:
scores = [-8, 3, 5]
then after sorting, you still have:
sorted_scores = [-8, 3, 5]
prefix = [-8, -5, 0]

Now take i = 1 (s_1 = 3):

Left contribution:
left_contrib = i * s_i - prefix[i-1] = 1 * 3 - (-8) = 11

Right contribution:
right_contrib = (prefix[2] - prefix[1]) - (2 - 1) * s_i
                = (0 - (-5)) - (1 * 3)
                = 5 - 3 = 2

Total deviation:
total_deviation = left_contrib + right_contrib = 11 + 2 = 13

Which matches exactly what you’d get from direct computation:
|3 - (-8)| + |3 - 5| = 11 + 2 = 13
"""


