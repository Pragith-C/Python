"""Assignment 3: Club Recommendations - Starter code."""
from typing import List, Tuple, Dict, TextIO


# Sample Data (Used by Doctring examples)

P2F = {'Jesse Katsopolis': ['Danny R Tanner', 'Joey Gladstone',
                            'Rebecca Donaldson-Katsopolis'],
       'Rebecca Donaldson-Katsopolis': ['Kimmy Gibbler'],
       'Stephanie J Tanner': ['Michelle Tanner', 'Kimmy Gibbler'],
       'Danny R Tanner': ['Jesse Katsopolis', 'DJ Tanner-Fuller',
                          'Joey Gladstone']}

P2C = {'Michelle Tanner': ['Comet Club'],
       'Danny R Tanner': ['Parent Council'],
       'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
       'Jesse Katsopolis': ['Parent Council', 'Rock N Rollers'],
       'Joey Gladstone': ['Comics R Us', 'Parent Council']}


# Helper functions

def update_dict(key: str, value: str,
                key_to_values: Dict[str, List[str]]) -> None:
    """Update key_to_values with key/value. If key is in key_to_values,
    and value is not already in the list associated with key,
    append value to the list. Otherwise, add the pair key/[value] to
    key_to_values.

    >>> d = {'1': ['a', 'b']}
    >>> update_dict('2', 'c', d)
    >>> d == {'1': ['a', 'b'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    """

    if key not in key_to_values:
        key_to_values[key] = []

    if value not in key_to_values[key]:
        key_to_values[key].append(value)


def create_list(key_person: str, current_friend: List[str],
                current_club: List[str], person_friend: Dict[str, List[str]],
                person_club: Dict[str, List[str]]) -> None:
    """Modify person_friend and person_clubs dictionary by either removing
    key_person from either dictionary if they are empty or adding
    current_friend to it corresponsing person_key or assigns current_club
    to its corresponding person_club key.

    >>> key_person = 'Claire Dunphy'
    >>> friend = ['Jay Pritchett']
    >>> club = ['Parent Teacher Association']
    >>> person_friend = {'Claire Dunphy': []}
    >>> person_club = {'Claire Dunphy': []}
    >>> create_list(key_person, friend, club, person_friend, person_club)
    >>> person_friend == {'Claire Dunphy': ['Jay Pritchett']}
    True
    >>> person_club == {'Claire Dunphy': ['Parent Teacher Association']}
    True
    >>> friend = []
    >>> club = []
    >>> create_list(key_person, friend, club, person_friend, person_club)
    >>> person_friend == {}
    True
    >>> person_club == {}
    True

    >>> 

    """
    if current_friend == []:
        del person_friend[key_person]
    else:
        person_friend[key_person] = current_friend
    if current_club == []:
        del person_club[key_person]
    else:
        person_club[key_person] = current_club


def dictionary_to_list(dictionary: Dict[str, List[str]]) -> List[str]:
    """Return a list with all the keys and key values of the
    dictionary as elements of a list.

    >>> dictionary_to_list(P2C) == [
    ...    'Michelle Tanner', 'Comet Club', 'Danny R Tanner',
    ...    'Parent Council', 'Kimmy Gibbler', 'Rock N Rollers', 'Smash Club',
    ...    'Jesse Katsopolis', 'Joey Gladstone', 'Comics R Us']
    True

    >>> dictionary_to_list({'Claire D': ['Parent Teacher Association']})
    ['Claire D', 'Parent Teacher Association']

    """
    lst = []
    for key in dictionary:
        lst.append(key)
        for i in dictionary[key]:
            lst.append(i)
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst


def get_clubs_of_club_persons(person_to_clubs: Dict[str, List[str]],
                              person: str) -> List[str]:
    """Return a list of all the clubs the people in person's club(s)
    are apart of from person_to_clubs.

    >>> get_clubs_of_club_persons (P2C, 'Danny R Tanner')
    ['Rock N Rollers', 'Comics R Us']

    >>> get_clubs_of_club_persons (P2C, 'Rebecca Donaldson-Katsopolis')
    []

    """
    clubs_to_person = invert_and_sort(person_to_clubs)
    persons_in_clubs = []
    in_club_person_clubs = []
    if person in person_to_clubs:
        person_clubs = person_to_clubs[person]
    else:
        person_clubs = []
    for clubs in person_clubs:
        for each_person in clubs_to_person[clubs]:
            persons_in_clubs.append(each_person)
    for each_person in persons_in_clubs:
        if each_person in person_to_clubs:
            for each_club in person_to_clubs[each_person]:
                if each_club not in person_clubs:
                    in_club_person_clubs.append(each_club)
    return in_club_person_clubs


def sort_club_list(lst: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """Return a sorted list of lst. It is sorted from highest to
    score, the integer element of the tuple. If the score is the
    same then the function sorts it based on alphebetical order of
    the club name, the string of the tuple.

    >>> sort_club_list([('Zap Club', 3), ('Smash Club', 3), ('A Club', 1)])
    [('Smash Club', 3), ('Zap Club', 3), ('A Club', 1)]

    >>> sort_club_list([('Zap Club', 3), ('Smash Club', 3), ('A Club', 3)])
    [('A Club', 3), ('Smash Club', 3), ('Zap Club', 3)]

    """
    end = len(lst) - 1
    while end > 0:
        for item in range(end):
            if lst[item + 1][1] > lst[item][1]:
                lst[item], lst[item + 1] = lst[item + 1], lst[item]
            elif lst[item][1] == lst[item + 1][1]:
                real_order = [lst[item][0], lst[item + 1][0]]
                sort_order = [lst[item][0], lst[item + 1][0]]
                sort_order.sort()
                if real_order != sort_order:
                    lst[item], lst[item + 1] = lst[item + 1], lst[item]
        end = end - 1
    return lst


# Required functions

def load_profiles(profiles_file: TextIO) -> Tuple[Dict[str, List[str]],
                                                  Dict[str, List[str]]]:
    """Return a two-item tuple containing a "person to friends" dictionary
    and a "person_to_clubs" dictionary with the data from
    profiles_file.

    NOTE: Functions (including helper functions) that have a parameter
          of type TextIO do not need docstring examples.

    """
    content = profiles_file.readlines()
    content.append('\n')
    person_friend, person_club, current_friend, current_club = {}, {}, [], []
    profile = (person_friend, person_club)
    for i in range(len(content)):
        if i == 0 or content[i-1] == '\n':
            cur = content[i].rstrip('\n')
            cur = ((cur[cur.rfind(',') + 2:]) + " " + (cur[:cur.rfind(',')]))
            person_friend[cur], person_club[cur] = current_friend, current_club
        elif content[i] != '\n':
            if ',' in content[i]:
                n_cur = content[i].rstrip('\n')
                n_cur = (n_cur[n_cur.rfind(',') + 2:]
                         ) + " " + (n_cur[:n_cur.rfind(',')])
                current_friend.append(n_cur)
                current_friend.sort()
            else:
                current_club.append(content[i].rstrip('\n'))
                current_club.sort()
        else:
            create_list(cur, current_friend,
                        current_club, person_friend, person_club)
            current_friend, current_club = [], []
    return profile


def get_average_club_count(person_to_clubs: Dict[str, List[str]]) -> float:
    """Return the average number of clubs that a person in person_to_clubs
    belongs to.

    >>> get_average_club_count(P2C)
    1.6

    >>> get_average_club_count({'Claire D': ['Parent Association']})
    1.0

    """
    num_clubs = 0
    num_keys = 0
    for key in person_to_clubs:
        num_keys += 1
        i = 0
        while i < len(person_to_clubs[key]):
            num_clubs += 1
            i += 1

    if num_keys == 0 or num_clubs == 0:
        return 0
    else:
        return (num_clubs/num_keys)


def get_last_to_first(
        person_to_friends: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Return a "last name to first name(s)" dictionary with the people
    from the "person to friends" dictionary person_to_friends.

    >>> get_last_to_first(P2F) == {
    ...    'Katsopolis': ['Jesse'],
    ...    'Tanner': ['Danny R', 'Michelle', 'Stephanie J'],
    ...    'Gladstone': ['Joey'],
    ...    'Donaldson-Katsopolis': ['Rebecca'],
    ...    'Gibbler': ['Kimmy'],
    ...    'Tanner-Fuller': ['DJ']}
    True

    >>> get_last_to_first({'Clare Dunphy': ['Phil Dunphy']})
    {'Dunphy': ['Clare', 'Phil']}

    """
    the_lst = dictionary_to_list(person_to_friends)
    last_first = {}
    last_name = ''
    for i in the_lst:
        last_name = i[i.rfind(' ') + 1:]
        new_lst = []
        for j in the_lst:
            if last_name == j[j.rfind(' ') + 1:]:
                first_name = j[:j.rfind(' ')]
                new_lst.append(first_name)
            new_lst.sort()
        last_first[last_name] = new_lst
    return last_first


def invert_and_sort(key_to_value: Dict[object, object]) -> Dict[object, list]:
    """Return key_to_value inverted so that each key is a value (for
    non-list values) or an item from an iterable value, and each value
    is a list of the corresponding keys from key_to_value.  The value
    lists in the returned dict are sorted.

    >>> invert_and_sort(P2C) == {
    ...  'Comet Club': ['Michelle Tanner'],
    ...  'Parent Council': ['Danny R Tanner', 'Jesse Katsopolis',
    ...                     'Joey Gladstone'],
    ...  'Rock N Rollers': ['Jesse Katsopolis', 'Kimmy Gibbler'],
    ...  'Comics R Us': ['Joey Gladstone'],
    ...  'Smash Club': ['Kimmy Gibbler']}
    True

    >>> invert_and_sort({'Clare Dunphy': ['Phil Dunphy']}) == {
    ...  'Phil Dunphy': ['Clare Dunphy']}
    True

    """
    new_dic = {}
    for key in key_to_value:
        for element in key_to_value[key]:
            update_dict(element, key, new_dic)

    for key in new_dic:
        new_dic[key].sort()

    return new_dic


def get_clubs_of_friends(person_to_friends: Dict[str, List[str]],
                         person_to_clubs: Dict[str, List[str]],
                         person: str) -> List[str]:
    """Return a list, sorted in alphabetical order, of the clubs in
    person_to_clubs that person's friends from person_to_friends
    belong to, excluding the clubs that person belongs to.  Each club
    appears in the returned list once per each of the person's friends
    who belong to it.

    >>> get_clubs_of_friends(P2F, P2C, 'Danny R Tanner')
    ['Comics R Us', 'Rock N Rollers']

    >>> get_clubs_of_friends(P2F, P2C, 'Joey Gladstone')
    []

    """
    friend_clubs = []

    if person in person_to_clubs:
        person_clubs = person_to_clubs[person]
    else:
        person_clubs = []

    if person in person_to_friends:
        friend_list = person_to_friends[person]
    else:
        friend_list = []

    for item in friend_list:
        if item in person_to_clubs:
            for club in person_to_clubs[item]:
                if club not in person_clubs:
                    friend_clubs.append(club)

    friend_clubs.sort()
    return friend_clubs


def recommend_clubs(
        person_to_friends: Dict[str, List[str]],
        person_to_clubs: Dict[str, List[str]],
        person: str,) -> List[Tuple[str, int]]:
    """Return a list of club recommendations for person based on the
    "person to friends" dictionary person_to_friends and the "person
    to clubs" dictionary person_to_clubs using the specified
    recommendation system.

    >>> recommend_clubs(P2F, P2C, 'Stephanie J Tanner',)
    [('Comet Club', 1), ('Rock N Rollers', 1), ('Smash Club', 1)]

    >>> recommend_clubs(P2F, P2C, 'DJ Tanner-Fuller')
    []

    """
    friend_clubs = get_clubs_of_friends(person_to_friends,
                                        person_to_clubs, person)
    in_club_clubs = get_clubs_of_club_persons(person_to_clubs, person)
    recommended_clubs = friend_clubs + in_club_clubs

    final_lst = []
    for club in recommended_clubs:
        club_count = 0
        for each_club in recommended_clubs:
            if club == each_club:
                club_count += 1
        final_lst.append((club, club_count))

    new_lst = []
    for i in final_lst:
        if i not in new_lst:
            new_lst.append(i)
    return sort_club_list(new_lst)


if __name__ == '__main__':
    pass
    #profiles_file = open('profiles.txt')
    # print(load_profiles(profiles_file))

    # If you add any function calls for testing, put them here.
    # Make sure they are indented, so they are within the if statement body.
    # That includes all calls on print, open, and doctest.

#import doctest
# doctest.testmod()
