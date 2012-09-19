

language = ['A list is a one-dimensional vector of data. A am  table is a list, but with multiple although columns?a two- got dimensional data structure. A tree  simply a table, but  yet another dimension because   data might be hidden inside other data                    ']
   


noise = ["a","about","above","all","along","also","although","am","an","any","are","aren't",
    "as","at","be","because","been","but","by","can","cannot","could","couldn't",
    "did","didn't","do","does","doesn't","e.g.","either","etc","etc.","even","ever",
    "for","from","further","get","gets","got","had","hardly","has","hasn't","having","he",
    "hence","her","here","hereby","herein","hereof","hereon","hereto","herewith","him",
    "his","how","however","I","i.e.","if","into","it","it's","its","me","more","most",
    "mr","my","near","nor","now","of","on","onto","other","our","out","over","really",
    "said","same","she","should","shouldn't","since","so","some","such","than","that",
    "the","their","them","then","there","thereby","therefore","therefrom","therein",
    "thereof","thereon","thereto","therewith","these","they","this","those","through",
    "thus","to","too","under","until","unto","upon","us","very","viz","was","wasn't",
    "we","were","what","when","where","whereby","wherein","whether","which","while",
    "who","whom","whose","why","with","without","would","you","your"] #noise words
print_sent = [' '.join(x for x in place.split() if x.lower() not in noise)
         for place in language
         ]
print print_sent


