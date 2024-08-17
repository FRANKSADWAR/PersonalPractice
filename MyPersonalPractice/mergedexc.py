"""
The merged try -> except -> else -> finally block
"""

sep = '-' * 32 + '\n'
print(sep + 'EXCEPTION RAUSED AND CAUGHT')

try:
    x = 'spam'[99]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run resume here')

print(sep + 'NO EXCEPTION RAISED')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')


print(sep + 'NO EXCEPTION RAISED, WITH ELSE')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
else:
    print('else is now run') ## The else is only run when no exceptions have been raised
finally:
    print('finally run')
print('after run')


print(sep + 'EXCEPION RAISED BUT NOT CAUGHT')
try:
    x = 1/0
except IndexError:
    print('except run')
except ZeroDivisionError:
    print("Division by zero not allowed")
finally:
    print('finally run here')
print('after run')


