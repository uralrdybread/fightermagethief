
# coding: utf-8

# In[6]:


from random import randint

player = input("Player, please choose the Fighter, Mage or Thief: ").lower()
rand_num = randint(0,2)
if rand_num == 0:
    opponent = "fighter"
elif rand_num == 1:
    opponent = "mage"
else:
    opponent = "thief"
    
print(f"Opponent plays {opponent}" )

if player == opponent:
    print("The fight is a draw!")
elif player == "fighter":
    if opponent == "thief":
        print("The Fighter stands triumphant over the Thief")
    else:
        print("The Fighter is no match for the Mage's arcane prowess")
elif player == "mage":
    if opponent == "fighter":
        print("The Fighter is no match for the Mage's arcane prowess")
    else:
        print("The Mage is overwhelmed by the Thief's skill and cunning")
elif player == "thief":
    if opponent == "fighter":
        print("The fighter stands triumphant over the thief")
    else:
        print("The Mage is overwhelmed by the thief's skill and cunning")
else:
    print("Please choose either the Fighter, Mage or Thief!")
    

