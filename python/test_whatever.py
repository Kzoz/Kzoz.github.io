import random

lib_of_list = ["what","no","need","apple","banana","cinnamon","diamond","sun","view","light","element","pen","vague","house","mix","kite","dog","cat","zoom","round","yes",]
user_input = input("Enter a word")
user_ending = user_input.endswith()
print(user_ending)
first_word = random.choice(lib_of_list)
pc_ending = first_word.endswith()
print(pc_ending)
