"""
searching in const time
- here we are using a hashing function to decide where the input will be stored
- collision
    |__closed address (usi jagah store karna)
        |__chaining [ _ | ([-]) | _ | _ | _ | _ ]
                            |__ [-]->[-]->[-]
            h(i) = element % size
    |__open address
        |__linear probing
    (jidhar bharna hai, agar udhar jagah naa ho to aage wale se
    pucho, agar udhar jagah naao to uske aage wale se aaisa)
    g(i) = [h(i)+k(i')] % size
    k(i') = i ;i will increment after every collision

        |__quadratic probing
    g(i) = [h(i)+k(i')] % size
    k(i') = i^2
"""
