dict = {
    "hello": 1,
    "hi": 2
}

strs = ["hiii", "b", "hiiiiiii"]
strs.sort(key=lambda a: len(a))
print(strs)