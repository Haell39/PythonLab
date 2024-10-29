brand = 'Apple'
exchangeRate = 1.235235245

message = 'The price of this %s laptop is %d USD and the exchange rate is %4.2f USD to 1 EUR' %(brand, 1299, exchangeRate)

print(message)

'''
%s ---- string
%d ---- interguer
%f ---- float

'''

# ^^ Using the format() method

message2 = 'The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.2f} USD to 1 EUR'.format('Apple', 1299, 1.235235245)

print(message2)

'''
Inside the curly bracket, we first write the position of the parameter to
use, followed by a colon. After the colon, we write the formatter. There
should not be any spaces within the curly brackets.
'''

'''
The parameter ‘Apple’ has a position of 0,
1299 has a position of 1 and
1.235235245 has a position of 2.
'''

#Note: If you do not want to format the string, you can simply write:

message3 = 'The price of this {} laptop is {} USD and the exchange rate is {} USD to 1 EUR'.format('Apple', 1299, 1.235235245)

print(message3)

text = '{0} is easier than {1}'.format('Python', 'Java')
text2 = '{1} is easier than {0}'.format('Python', 'Java')
text3 = '{:10.2f} and {:d}'.format(1.234234245, 12)
text4 = '{}'.format(1.235234245)

print('\n' + text, text2, text3, text4, sep='\n')
























