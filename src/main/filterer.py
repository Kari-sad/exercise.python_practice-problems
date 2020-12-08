# Created by Leon Hunter at 12:10 PM 12/08/2020
class Filterer(object):
    def remove_characters(string_to_remove_from, characters_to_remove):
        result = str(string_to_remove_from)
        for char in string_to_remove_from:
            if char in characters_to_remove:
                result = result.replace(char, '')
        return result

    def remove_vowels(self, string_to_remove_from):
        vowels = list("aeiouAEIOU")
        return self.remove_characters(string_to_remove_from, vowels)

    def remove_consonants(self, string_to_remove_from):
        consonant = "bcdfghjklmnpqrstvwxyz"
        consonant_List= consonant.lower() + consonant.upper()
        return self.remove_characters(string_to_remove_from,consonant_List)
