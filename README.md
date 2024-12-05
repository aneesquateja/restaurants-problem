# restaurants-problem
Problem to be completed during Industry Prep - Interview Prep

## Problem Statement

Your goal is to write a function that determines who has visited the most restaurants. You will be given a dictionary that records restaurant visits, such as the example below:

```
visits = {
    "Spicy City" : ["Auberon", "Elora"],
    "La Especial Norte": ["Elora", "Auberon", "Rowan"],
    "Sushi Kashiba": ["Xinting", "Aisha", "Xinting"],
    "Lyon's Grocery": ["Auberon", "Xinting", "Sam", "Xinting"],
    "Applebee's": ["Sam", "Eliza"],
}
```

Each key holds the name of a restaurant, and the value is a list of restaurants visits. Each visit is represented as a string holding the name of the person who visited. Note that a person may visit the same restaurant multiple times.

In this example, Auberon has visited three different restaurants: Spicy City, La Especial Norte, and Lyon's Grocery. This is more different restaurants than anyone else in the dictionary so the function should return "Auberon".

Write a function that accepts a dictionary of restaurant visits and returns the name of the person who visited the most different restaurants. See assertions in `restaurants.py` for more test cases.




Problem Statement: racers.py

Your goal is to write a function to identify which drivers in a dataset have NOT won any race.

The dataset will be a dictionary. The keys will be the names of races and the values will be, the top three drivers to finish at that race. The first driver in the tuple will be the one who won the race. An example dataset is shown below:

races = {
    "Suzuka": ("Tsunoda", "Latifi", "Stroll"),
    "Mexico City": ("Pérez", "Hamilton", "Tsunoda"),
    "Silverstone": ("Hamilton", "Latifi", "Tsunoda")
}

In this example, Tsunoda won at Suzuka, Pérez won at Mexico City, and Hamilton won at Silverstone. Latifi and Stroll are present in the dictionary, but they did not win any of the races.

Write a function that accepts a races dicitonary and returns a set of all drivers that are present in that dictionary but did NOT win any race. For example, for the above dictionary, your function should return:

{"Latifi", "Stroll"}

See assertions in racers.py for more test cases.