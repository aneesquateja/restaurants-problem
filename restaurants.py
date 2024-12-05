def most_varied_visitor(visits):
    # Write your solution here!
    # assign a new varaible which is empty
    # itterate through dictionary and if the value is repeated , append the value to a new valiable and return the value of that variable 
    # then use max builtin method on new varaible to return the person's name who visited more.


   # frequency dictionary:
    #   key will be person, value will be how many 
    #   restaurants they visited
    unique_visit_count = {}
    
    for visitors in visits.values():
        # remove duplicates
        # we only want to count a person once per restaurant
        unique_visitors = set(visitors)
        
        for visitor in unique_visitors:
            if visitor not in unique_visit_count:
                unique_visit_count[visitor] = 1
            else:
                unique_visit_count[visitor] += 1

    best_visitor = None
    most_visits = None
    for visitor, count in unique_visit_count.items():
        # update the most varied visitor if we find one with more visits
        if most_visits is None or count > most_visits:
            most_visits = count
            best_visitor = visitor

    return best_visitor



#  most_varied_visitor(visits)


visits_1 = {
    "Spicy City" : ["Eliza"],
    "La Especial Norte" : ["Eliza"],
    "Sushi Kashiba": ["Xinting"],
}
assert most_varied_visitor(visits_1) == "Eliza"

visits_2 = {
    "Spicy City" : ["Auberon", "Elora"],
    "La Especial Norte": ["Elora", "Auberon", "Rowan"],
    "Sushi Kashiba": ["Xinting", "Aisha", "Xinting"],
    "Lyon's Grocery": ["Auberon", "Xinting", "Sam", "Xinting"],
    "Applebee's": ["Sam", "Eliza"],
}
assert most_varied_visitor(visits_2) == "Auberon"

visits_3 = {
    "Spicy City" : ["Elora", "Elora", "Elora"],
}
assert most_varied_visitor(visits_3) == "Elora"
print("All tests passed! If time remains, discuss time/space complexity")