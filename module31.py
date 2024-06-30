calls = 0

def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    count_calls()
    if string in list_to_search:
        return True
    else:
        return False


print(string_info('Capibara'))
print(string_info('Armageddon'))
print(is_contains('Urban'.lower(), ['ban', 'BaNaN', 'urBAN'.lower()]))  #Urban~urBan
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
