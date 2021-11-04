import time
import random
import string


# define the function and pass the length as argument
def rand_upper_lower_string(length):
    # Print the string in Lowercase
    result = ''.join((random.choice(string.ascii_lowercase)
                     for x in range(length)))  # run loop until the define length
    # print(" Random string generated in Lowercase: ", result)

#     # Print the string in Uppercase
#     result1 = ''.join((random.choice(string.ascii_uppercase) for x in range(length))) # run the loop until the define length
#     print(" Random string generated in Uppercase: ", result1)
    return result


'''
Return FALSE or TRUE
'''


def rand_sql_bool():
    val = 'TRUE' if random.getrandbits(1) == 1 else 'FALSE'
    # print(val)
    return val


def timeitutil(f):

    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print('func:%r args:[%r, %r] took: %2.4f sec' %
              (f.__name__, args, kw, te-ts))
        return result

    return timed
