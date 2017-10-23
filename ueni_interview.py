subtotals = {
    "count": 15,
    "amount": 425,
    "num_items": 12,
    "gender": {
        "F": {
            "count": 5,
            "amount": 225,
            "num_items": 7
        },
        "M": {
            "count": 10,
            "amount": 200,
            "num_items": 5
        }
    },
    "currency": {
        "EUR": {
            "count": 13,
            "amount": 175,
            "num_items": 6
        },
        "USD": {
            "count": 2,
            "amount": 250,
            "num_items": 6
        }
    }
}

new_entry = {
    "gender": "M",
    "amount": 17.0,
    "num_items": 2,
    "currency": "EUR"
}

additionable_keys = ["count", "amount", "num_items"]


# Exercise 1
def increment_count_in_dict(dictionary, key, value):
    if key in dictionary:
        dictionary[key] += value
    else:
        dictionary[key] = value


def add_new_entry_in_subtotals(additionable_keys, subtotals, new_entry):
    str_values = []
    additionable_values = []

    if not "count" in new_entry:
        new_entry["count"] = 1
    print new_entry
    for key, value in new_entry.iteritems():
        if key in additionable_keys:
            increment_count_in_dict(subtotals, key, value)
            additionable_values.append((key, value))
        elif type(value) == str:
            str_values.append((key, value))

    for skey, svalue in str_values:
        if not skey in subtotals:
            subtotals[skey] = {}
        if not svalue in subtotals[skey]:
            subtotals[skey][svalue] = {}
        for nkey, nvalue in additionable_values:
            increment_count_in_dict(subtotals[skey][svalue], nkey, nvalue)
    return subtotals


add_new_entry_in_subtotals(additionable_keys, subtotals, new_entry)


def merge_two_dico(dico1, dico2, additionable_keys):
    for key, value in dico2.iteritems():
        if key in additionable_keys:
            dico1[key] += dico2[key]
        elif type(value) == str:
            if dico1[key] != dico2[key]:
                print "Attention: the key {} has different string values in the two dict.".format(key)
        elif type(value) == dict:
            dico1[key] = merge_two_dico(dico1[key], dico2[key], additionable_keys)
        else:
            print "Attention: value type not handled for key {}.".format(key)
    return dico1


merge_two_dico(subtotals, subtotals, additionable_keys)


# Exercise 2

# If one number between 1 and N included is missing in the array, we can find it easily by summing the array.
# As the sum should be of value N*(N-1)/2, we can find the missing element by : missing_element = supposed_sum - actual_sum
# time is linear, space is O(1)

# If we are now looking to find two numbers missing in the array we need another equation to solve the problem (two eq 2 unknowns)
# There are a few possibilities : such as summing the squares (this should be equal to n(n+1)(2n+1)/6).
# We could also multiply all the numbers, which should equal to n! but it might be computationnaly demanding.
# With our 1st choice, time is still linear and space is O(1)

# Even with infinite memory, I wont be able to go above linear time as I have to go though the array at least once.
# With unlimited time, if I can modify my input array, I won't need any more memory than that so minimum space complexity is n
# (in this case I'll sort the array & search overe the sorted list)


# Exercise 3

def memoize(func):
    cache = {}

    def func_wrapper(arg):
        key = str(arg)
        # print cache
        if key not in cache:
            cache[key] = func(arg)
        return cache[key]

    return func_wrapper


@memoize
def foo(a):
    return a * a + 1


foo(2), foo(3), foo(2)

from collections import OrderedDict


class LimitedSizeDict(OrderedDict):
    def __init__(self, size_limit):
        self.size_limit = size_limit
        OrderedDict.__init__(self)

    def __setitem__(self, key, value):
        OrderedDict.__setitem__(self, key, value)
        self._check_size_limit()

    def _check_size_limit(self):
        if len(self) > self.size_limit:
            self.popitem(last=False)


def memoize_limited_size(n):
    def memoize(func):
        cache = LimitedSizeDict(n)

        def func_wrapper(arg):
            key = str(arg)
            # print cache
            if key not in cache:
                cache[key] = func(arg)
            return cache[key]

        return func_wrapper

    return memoize


@memoize_limited_size(2)
def bar(a):
    return a * a + 1


bar(1), bar(2), bar(3), bar(4)


def memoize_limited_size_with_args(n):
    def memoize_with_args(func):
        cache = LimitedSizeDict(n)

        def func_wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)
            print cache, key
            if key not in cache:
                cache[key] = func(*args, **kwargs)
            return cache[key]

        return func_wrapper

    return memoize_with_args


@memoize_limited_size_with_args(2)
def foobar(a, b, c, d):
    return a * b + c / d


foobar(1, 2, 3, 4)
foobar(1, 2, 3, 5)
foobar(1, 2, 3, 6)
foobar(1, 2, 3, 4)