#	List Comprehensions
#
#	https://www.udacity.com/course/progress#!/c-cs212

udacity_list = ['peter', 'andy', 'sarah',
				'gundega', 'job', 'sean']

""" This is a non-elegant way to write a function that will
	uppercase a whole list"""
bad_uppercase_tas=[]
	for i in range(len(udacity_list)):
		bad_uppercase_tas.append(udacity_list[i].upper())
print bad_uppercase_tas

""" Iterates through udacity_list, call each entry 'name
	and then use upper() to uppercase all of the entries.
	The brackets in the variable is us telling python
	that we want the result in a list."""
uppercase_tas = [name.upper() for name in udacity_list]

""" This will print every uppercase_tas 
	entries in their own line"""
for name in uppercase_tas:
	print name

""" Lets test tuples. We know that a list is a tuple when
	the data is inside paranthesis, inside the list. 
	Tuples are non-immutable lists that can't be changed."""
ta_data = [['Peter', 'USA', 'CS262'],
           ['Andy', 'USA', 'CS212'],
           ['Sarah', 'England', 'CS101'],
           ['Gundega', 'Latvia', 'CS373'],
           ['Job', 'USA', 'CS387'],
           ['Sean', 'USA', 'CS253']]

""" We want to print out all this information togheter
	with strings. Since our tuples contain 3 elements, we need 
	to reference each of the 3 elements for python to understand."""
#	use this:
[name + ' lives in ' + country for name, country, course in ta_data]
#	or this:
[x + ' lives in ' + y for x, y, z in ta_data]
#	it does not matter, but the second variation is more readable!


""" We can also filter out tuples to only get certain values."""
filter_facts = [name + ' lives in ' + country + ' and is the TA for ' +
			course for name, country, course in ta_data if country != 'USA']

"""and then even print them!"""
for filtered in filter_facts:
	print filtered

""" Creates a list that will print everyone with the string "CS3" inside
	their tuple. This is done by reversing the find() function with 
	'if not' sentence, and also calling it upon course. """
ta_300 = [name + ' is the TA for ' + course 
          for name, country, course in ta_data if not course.find("CS3")]

""" And here we print it out."""
for x in ta_300:
    print x

