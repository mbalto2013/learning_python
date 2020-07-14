def my_function(x,y):
    print('my_function in')
    result = x / y
    print('My function out')
    return result

print('Starting')

try:
    print('Before my_function')
    my_function(6,0)
    print('After my_function')
except ZeroDivisionError as exp:
    print('Oops! No debes usar un denominador en 0')
    print('lo arreglaremos')
    raise
else:
    print(' Accion inicial completada de manera satisfactoria')

print('Done')