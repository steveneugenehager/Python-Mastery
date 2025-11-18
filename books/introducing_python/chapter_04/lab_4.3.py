
salutation = 'Miss'
name = 'Jane Doe'
product = 'vacuum cleaner'
verbed = 'choked'
room = "den"
animals = 'dogs'
amount = 19.99
percent = 99.44
spokesman = 'Zig Ziglar'
job_title = 'CEO'

letter = f'''Dear {salutation} {name},
We are sorry that our {product}
{verbed} in your {room}.
It should never be used in a {room}, especially near any {animals}.

Send us the {amount}.
We will send you another {product} that
is {percent}% less likely to have {verbed}.

Sincerely,
{spokesman}
{job_title}'''

print(letter)