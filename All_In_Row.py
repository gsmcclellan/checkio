""" All in a Row
	Greg McClellan

	Program takes a list nested any number of times, and
	returns a flattened list.
"""

def checkio(data):
	"""Takes nested list and returns flattened version"""
    one_dim_list = []
    for item in data:

        if isinstance(item, list):
            for item2 in checkio(item):
            	one_dim_list.append(item2)

        else:
            one_dim_list.append(item)
            
    return one_dim_list


def main():
	print(checkio([1,[2,2,2],4]))


if __name__ == '__main__':
	main()