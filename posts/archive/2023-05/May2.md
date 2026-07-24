---
layout: default
permalink: /blog/May23
---

[link back to all posts](https://alxwen711.github.io/blog)

## May 1st-15th

Here we have 3 more CodeForces contests I ran in these two weeks. Not noted here is that I’m also grinding through Codechef and Leetcode at the same time. I might give a further update on Codechef later, but for Leetcode I’ll only recap problems that I feel can generate significant discussion, and the fact that the winner of Leetcode contests nowadays solves the 4 problems routinely in under 10 minutes does not bode well.

### [Round 870](https://codeforces.com/contest/1826)

Problems Solved: A, B, C, D

New Rating: **1995** (+112)

Performance: **2283**

So it seems like that I’ve suddenly remembered how to commit SpeedForces now because I literally solved A through D in 31 minutes. I don’t even have to check past contests to know that is a record.

<details>
<summary>Quick rundown of problems C and D</summary>

[C](https://codeforces.com/contest/1826/problem/C)’s idea is that if you know the smallest prime factor of n (call this x), then as long as m is at least x then what could happen is the programmers split their votes evenly among x choices infinitely, else the voting process will end since the votes will be unevenly split each time. Thus the easiest way is to precompute the smallest prime factor up to 1000000 using a sieve.

[D](https://codeforces.com/contest/1826/problem/D) is best thought of in three parts. First is determining the optimal beauty value if you have to run through 1 sight that has to be A[i]. This is trivial. The second part is finding the optimal beauty where the last sight has to be A[i]. Logically thinking about this it isn’t too complex, you can track the highest 1st sight and decrease its value by 1 each time when comparing to new sights to represent the distance travelled. After solving the second part the third part with 3 beautiful sights functions similarly, and you can use the info gathered from the second part dynamically to solve here. Conveniently the code is quite short so I can place it here. `n` and `ar` is the number of sights and the array containing each sights’ beauty respectively. Notice how finding the highest beauty for 2 sights and 3 sights are quite similar; this idea could also be extended to an arbitrary number of sights.
```python
def solve(n,ar):
   # find best for top 2 (top 1 is trivial)
   two = [0]*n
   two[1] = ar[0]+ar[1]-1
   inc = ar[0]-1
   for j in range(2,n):
       inc = max(inc-1,ar[j-1]-1)
       two[j] = ar[j]+inc
   # find best for top 3 (given top 2 info)
   three = [0]*n
   three[2] = ar[0]+ar[1]+ar[2]-2
   inc = two[1]-1
   for k in range(3,n):
       inc = max(inc-1,two[k-1]-1)
       three[k] = ar[k]+inc
   return max(three)
```
</details>


I also had at least a decent attempt on [E](https://codeforces.com/contest/1826/problem/E), albeit there was something within my execution that was causing a TLE. The progress made on this problem is substantial, but solving it would’ve been nice since if we look at this contest, it happened to be a very strong one solely off of the greatest first 35 minutes of a contest followed by a respectable but somewhat mediocre last 85 minutes. Either way, I’m back to CM, which is pretty cool.

<details>
<summary>Rundown of E’s solution idea</summary>
If we invite model’s A and B, then it must hold that if A is placed in front of B, then `A[i] < B[i]` for all `1 <= i <= m`, where i is the ith city. This relationship can be constructed into a directed graph, for which the largest amount of money is the highest cost of any traversable path. To compute the maximum, we know that for a node n, it’s maximum cost path is equal to the cost of node n plus the maximum cost path starting from one of its children. This also means that the maximum cost path for children nodes is trivial. So we can work backwards by removing the children nodes and incrementing the values of their parents as needed based on their maximums until the maximum cost is found once all nodes are removed. This is possible since once all of a node’s children are removed, itself becomes a child node as well. In practice, an optimal implementation should only remove each possible edge and node once, with the maximum edge count being about 12.5 million.

It is here where I’ve noticed what could be the TLE problem with my code. In doing the comparisons I compared each pair of models with each other. In the extreme case where each model can be invited, this results in about 12.5 million pair comparisons, and with 500 cities, this means a total of 6.25 billion comparisons are made. Python can probably get around 50 million comparisons done a second, so there is a better way to create the graph. My initial thought here is to track each model hierarchy chain to only connect from children so that no additional edges are burned; ie. if there is a model hierarchy 1 -> 2 -> 3, model 1 should not connect directly to model 3. This is doable by only comparing with current children nodes in the graph setup, and if a supposed child does not work, adding their parents into the list of nodes to compare.

<details>
<summary> Update: </summary>
After some adjustments ([latest submission](https://codeforces.com/contest/1826/submission/205017423)) I have found that the main slow down is now occurring in the comparison of arrays to create new edges. I made several different ideas to fix this but the issue here is that with my current method each value in the arrays have to be checked so with a specific setup the 6.25 billion comparisons are still occurring. Now the idea is that there may be a way to precompute the possible edges while initialising the arrays in O(n^2) time, but this is where I’m stuck. At least I went from TLEing on test case 7 to test case 8?
</details>
</details>

### [Educational Round 148](https://codeforces.com/contest/1832)

Problems Solved: A, B, C, E

New Rating: **2016** (+20)

Performance: **2067**

The problems solved is a bit deceiving since [D1](https://codeforces.com/contest/1832/problem/D1) had around the same number of solves as [E](https://codeforces.com/contest/1832/problem/E). In this case, I’m more wondering how E was considered harder than D. D in particular, all I got to was that you could not just run O(n) tests to binary search the answer as the possibility of a minimum is not a simple boolean case of k >= x. Ie. a minimum of 4 and 2 may be possible, but 3 could be impossible. If this did work if I did this on each query then the final run time would be O(n^2 log n) which only solves D1 as D2 requires O(n log n) or better. E on the other hand is somewhat easier.


<details>
<summary>Thought Process on E</summary>
There is a solution that involves convolutions, but there is an idea that is significantly less convoluted then this. The k value makes things complicated, but let’s assume that k = 0 first. This makes C(x,0) = 1 for all positive values x, and would mean that the B array is simply `[a1,a2,a3…,an] mod 998244353`. Moving to k = 1, `B[0] = a1`. `B[1] = 2*a1+a2`. `B[2] = 3*a1+2*a2+a3`. At this point there is a pattern forming. If we take the running sum of the B array where k = 0, we get `[a1,a1+a2,a1+a2+a3…]`. Taking the running sum of this array results in the B array for k = 1. Manually determining the first few values for k = 2 results in this same double summation pattern from the k = 1 B array, albeit with the values shifted. This pattern can then be repeated until the needed k value.

As for implementation, it turns out Python is capable of handling a 10 million value array so no real adjustments need to be made. [My implementation](https://codeforces.com/contest/1832/submission/205598215) does take up around half of the 1 GB total memory though so there is some carefulness required.
</details>

I’m still a bit mixed on my performance on this contest, given that I was completely lost on D and I only really got E because it was maths heavy. That said, E was actually pretty difficult, and asides [one really dubious error on A](https://codeforces.com/contest/1832/submission/205549653) (this fails on `aaa`), the other problems were solved efficiently. If I can be more consistent on the problems like D/E in difficulty, I’ll be in good shape for future contests.

### [Round 873 (Div 1)](https://codeforces.com/contest/1827)

Problems Solved: A

New Rating: **1980** (-36)

Performance: **1866**

This is what I meant by lacking consistency on harder problems. In this case I was bailed out of losing more rating because I happened to get  [A](https://codeforces.com/contest/1827/problem/A) in 5 minutes. For a Div 2 C level problem this is probably a new record.

<details>
<summary>Speedrun of A</summary>
Array A can be reordered, so Array B’s ordering does not matter. Thus the simplest way is to initially sort both A and B. Starting from highest to lowest, track how many possible choices there are for the last element in A, ie. how many values in A exceed B[n-1]. Let this value be x. Set ans = x. For each of the remaining n-1 values, from largest to smallest, then decrease x by 1 and increase x by how many new elements in A exceed the specific value from B. After each element multiply ans by x, and after going through all elements, ans contains the total number of possible combinations. In short, you are counting the number of choices for each position in A starting from highest to lowest. -1 is needed to account for previous values already being inserted, and the easiest way to do this is with a pointer on A tracking the largest value just under B[i].
</details>

This contest really shows the skill gap between Div 1 and Div 2. In Div 2, the above was problem C, and the skill gap between it and [D1](https://codeforces.com/contest/1827/problem/B1) was a solve count from over 6000 to 279 out of 11567 coders. This case of SpeedForces is not prevalent in Div 1 as the solve rate between A and B1 only went from 746 to 518. Yes this was a hard problem; clist is rating B1 currently around 2066, ie. harder side of a CM level problem, but B1 I all but went into a foetal position for 115 minutes. There was some progress made. Through a lot of min/max tracking shenanigans and a dp method involving solving subarrays of length 1, then 2, then 3, etc., I managed to solve B1 IF only a single range was allowed to be used to fix a array. This meant if `[2,1,3,5,4]` was to be sorted, my algorithm calculated a beauty of 4 when it was only 2. On one hand, trying to solve an easier version of a complicated problem is a legit strategy, even if doing so took over an hour. That said, the only reason this occurred was because I misread and did not comprehend the very obvious *arbitrary number of range-sort operations* part of the statement. It’s a difficult question, but this is a mistake I should not be making regardless. I’ve already had enough experience with stupid misreads, and I really do not need another one.

## May 16th-31st

With 5 months of this year done, before I begin my usual recap, I’ll touch up on what’s been going on with my CodeChef profile. Since the start of this month I had begun an alternate account with the reason to fix my screwed up rating from last [February](https://alxwen711.github.io/blog/Feb23). For some reason it did not dawn on me to link my CodeChef profile back then, so here it is.

[alxwen711’s CodeChef profile](https://www.codechef.com/users/alxwen711) 

And here is how my current alternate account is going:

[my alternate account:](https://www.codechef.com/users/snowlucario)

I think it’s safe to say that my alternate account shows my skill level more accurately. This basically confirms my theory of CodeChef’s rating system working on some sort of confidence factor that heavily increases rating change in the first few contests, and is an inadvertent benefit to creating an alt account. Another note on this rating here is that while 2100 is pretty good, 2100 on CodeChef is not remotely close to 2100 on CodeForces. It feels more like 1900 on CodeForces. At least though CodeChef’s rating system, while very stubborn with a higher number of completed contests, isn’t as scuffed as Leetcode. That honestly feels like an entirely different discussion where I talk/rant about various rating systems on different competitive programming sites, where I go over how to approximately compare each one/explain the loopholes that are possible.

Anyways, I digress. On to the regularly scheduled programming.


### [Round 875](https://codeforces.com/contest/1830)

Problems Solved: A

New Rating: **1993** (-87)

Performance: **1727**

Remember the supposed luck I had in the previous contest? This is basically the opposite scenario. Again while this is a Division 1 contest, only getting one problem isn’t exactly good. With [A](https://codeforces.com/contest/1830/problem/A) the only real solace was that it was a tree problem that I actually executed properly, asides from the first submission having some of the worst implementation I’ve ever done causing a TLE. The difference between my two submissions for A was a 3 second TLE and a 654 ms Accepted verdict. It’s nice knowing that Python can be fast enough, but the fact the first TLE even happened was shameful.

This only acted as a prelude to [B](https://codeforces.com/contest/1830/problem/B). 




<details>
<summary>The Tribulations of B</summary>
Most of my methods ended up computing to $O(n^2)$ ideas involving finding all the possible pair values or iterating through 1 to n. In this the main observation was missed in that the sum of two values in the array can be at most 2n. This means for the multiplied values, call these a and b, `min(a,b)` has to be at most `sqrt(2n)`. 

From here, the solution is to first map all the pairs into a 2d dictionary setup, such that `d[a][b]` is the number of times the pair (a[i],b[i]) is in the array. Then you count how many pairs of $(a[i],b[i])$ and $(a[j],b[j])$ exist where $a[i] <= a[j], a[i] < sqrt(2n)$. This is done by iterating value a for d[a] up to sqrt(2n), and for each d[a], comparing it with every value in d[b] where b >= a, and if a pair exists, adding it to the answer. In my [example solution](https://codeforces.com/contest/1830/submission/207803351), one such pair possible could be $d[2][1] = 3$ and $d[3][5] = 2$ since 2x3 = 1+5, which would add 6 to the answer since (2,1) appears 3 times and (3,5) twice. There is also a bit of extra code to account for double counting in using the same a value or pair of values.

Since each value up to sqrt(2n) has to be iterated through and each iteration could search through the majority of the array, this ends up being a $O(n^{1.5})$ algorithm. Roughly speaking with this algorithm around 100 million operations are needed, and this is the point where the difference in C++ and Python somewhat matters. Both are capable of completing the problem in time, but the current fastest solution takes under 200ms while the fastest Python solution takes 1450ms. There is optimization I have to learn in Python as while I did end up solving this problem, my solution was extremely close to the 4 second time limit, and it passing through is borderline luck based.
</details>


As for [C](https://codeforces.com/contest/1830/problem/B)? I would like to say I made some sort of progress on this question but it turns out that Catalan numbers aren’t needed to solve the problem. I pretty much ran straight into a brick wall there which feels pretty symbolic of this contest.