# Degrees
## My Implementation for CS50's [Six Degrees Of Kevin Bacon](https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon)

> Given distribution code is written by CS50's AI staff. I've only implemented `shortest_path` function 
---

### What does the function do?
- The shortest path function returns the shortest path from source to target. 
- Assuming there is a path from the source to the target, The fnction return a list, where each list item is the next (movie_id, person_id)
- If there are multiple paths of minimum length from the source to the target, The function returns any of them.
- If there is no possible path between two actors, The function returns None.
---

### Instruction to use
```
$ python degrees.py large
Loading data...
Data loaded.
Name: Emma Watson
Name: Jennifer Lawrence
3 degrees of separation.
1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
2: Brendan Gleeson and Michael Fassbender starred in Trespass Against Us
3: Michael Fassbender and Jennifer Lawrence starred in X-Men: First Class
```
