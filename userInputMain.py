def fibonacci(num):
    if num < 0:
        raise Exception('Num need\'s to be a positive integer')
    # Initial fibonacci sequence
    curr, prev = 0, 1

    # Logic: the result of the sum is our current num + previor num,
    # so the prev num becomes the current num
    # and the curr num receive the result of the sum

    for count in range(num):
        result_sum = curr + prev
        prev = curr
        curr = result_sum
        print(f'{curr}... ', end='')


number = int(input('How many numbers in the fibonacci sequence do you want to see: '))
fibonacci(number)
