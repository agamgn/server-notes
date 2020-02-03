def outer():
    count=10
    def inner():
        nonlocal count
        count=20
        print(count)
    inner()
    print(count)
outer()