"""
https://codesensei.nl/courses/shared/exercises/exceptions.html

Consider the following code:

addresses = {
    "Pluralsight": "182 N. Union Ave, Farmington, UT 84025",
    "Apple": "One Infinite Loop. Cupertino, CA 95014",
    "Microsoft": "One Microsoft Way, Redmond, WA 98052-6399"
}

contact = input("Contact name? ")
print(contact, ":\n------------")
print(addresses[contact])

Please add exception handling to detect unknown contacts.
"""

addresses = {
    "Pluralsight": "182 N. Union Ave, Farmington, UT 84025",
    "Apple": "One Infinite Loop. Cupertino, CA 95014",
    "Microsoft": "One Microsoft Way, Redmond, WA 98052-6399",
}

# try:
contact = input("Contact name? ")
print(contact, ":\n------------")
print(addresses[contact])
# except Exception as e:
#     print(f'Error: {e}')
