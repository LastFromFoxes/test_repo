import time
import random
import subprocess

for i in range(1, 101):
    time.sleep(2)
    rand_num = random.randint(1, 1000000)
    with open('test1.py', 'a', encoding='utf-8') as f:
        f.write(f'# Рандомное число: {rand_num}\n')
    subprocess.run(['git', 'add', 'test1.py'])
    subprocess.run(['git', 'commit', '-m', f'Добавлено рандомное число {rand_num} на шаге {i}'])
    subprocess.run(['git', 'push'])