from names import cap, starts_with

# assert esprssion, statement
# assert names.cap('comfort') == 'Comfort', 'Function is failing.'
# print(names.title('ComFort'))
# print(names.getFullName('comfort', 'Ekpe'))

# if names.cap('Comfort') == 'COMFORT':
# 	print("test passed")

def test_cap():
	# test if names.cap('Comfort') will return 'COMFORT'
	assert cap('Comfort') == 'COMFORT', 'there is error with the function'
	
def test_cap_with_numbers():
	assert cap('com4ort') == 'COM4ORT',  'cap function expects a string value'


def test_name_starts_with_K():
	assert 	starts_with('komfort', 'A') == False
	assert 	starts_with('komfort', 'B') == False
	assert 	starts_with('komfort', 'V') == False
	assert 	starts_with('komfort', 'J') == False
	assert 	starts_with('komfort', 'K') == True