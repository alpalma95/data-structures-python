
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class Member:
    def __init__(self, first_name, id, age, lucky_numbers):
        self.first_name = first_name
        self.id = id
        self.age = age
        self.lucky_numbers = lucky_numbers

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        new_member = vars(member)
        self._members.append(new_member)
        return self._members

    def delete_member(self, id):
        # fill this method and update the return
        if len(self._members) != 0:
            print(f'Before: {self._members}')
            for i in range(len(self._members)):
                if self._members[i]['id'] == id:
                    del(self._members[i])
            print(f'After: {self._members}')
        else:
            print('Not as expected! Delete method doesnt work properly')

    def get_member(self, id):
        # fill this method and update the return
        # REMEMBER TO RETURN SOMETHING READABLE FOR THE API
        if len(self._members) != 0:
            for i in range(len(self._members)):
                if self._members[i]['id'] == id:
                    print(self._members[i])
                    return self._members[i]
        else:
            print('Not as expected! Find method doesnt work properly')
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

# testing

adams_family = FamilyStructure('Adams')
gomez = Member('Gomez', adams_family._generateId(), 40, [5, 2])
morticia = Member("Morticia", adams_family._generateId(), 35, [3, 7])
thing = Member("Thing", adams_family._generateId(), 3, [8, 9])
test = Member("Test", adams_family._generateId(), 3, [8, 9])

adams_family.add_member(gomez)
adams_family.add_member(morticia)
adams_family.add_member(thing)
adams_family.add_member(test)
