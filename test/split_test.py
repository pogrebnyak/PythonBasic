def get_tasks(x):
    return x, int(x+7) % 15

print(get_tasks(15))