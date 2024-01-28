hi = {
    "hi" : 10,
    "bye" : 30,
    "op": 20,
    "aw": 25
}

# print(dict)
print(hi.items())
print(dict(sorted(hi.items(), key=lambda a : a[0])))
print(dict(sorted(hi.items(), key=lambda item: item[1])))

bu = [2,5,6,2,1]
bu.sort(reverse=True)
print(bu)