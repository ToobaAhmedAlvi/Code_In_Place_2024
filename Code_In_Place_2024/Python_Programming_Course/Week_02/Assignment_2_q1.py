user_input = float(input("Enter your weight on Earth: "))
print("Weight on Earth:", user_input)
choice_planet=input("""Input the planet name from the list below\n 1.Mercury \n 2. Venus \n 3.  Jupiter \n 4. Saturn \n 5. Uranus \n 6. Neptune\n""")

def mercury_weight():
    global user_input
    MERCURY_EQUIVALENT_WEIGHT = 37.6
    result = user_input * MERCURY_EQUIVALENT_WEIGHT
    print("Weight on Mercury:", round(result, 2))

def venus_weight():
    global user_input
    VENUS_EQUIVALENT_WEIGHT = 88.9
    result = user_input * VENUS_EQUIVALENT_WEIGHT
    print("Weight on Venus:", round(result, 2))

def jupiter_weight():
    global user_input
    JUPITER_EQUIVALENT_WEIGHT = 236.0
    result = user_input * JUPITER_EQUIVALENT_WEIGHT
    print("Weight on Jupiter:", round(result, 2))

def saturn_weight():
    global user_input
    SATURN_EQUIVALENT_WEIGHT = 108.1
    result = user_input * SATURN_EQUIVALENT_WEIGHT
    print("Weight on Saturn:", round(result, 2))

def uranus_weight():
    global user_input
    URANUS_EQUIVALENT_WEIGHT = 81.5
    result = user_input * URANUS_EQUIVALENT_WEIGHT
    print("Weight on Uranus:", round(result, 2))

def neptune_weight():
    global user_input
    NEPTUNE_EQUIVALENT_WEIGHT = 114.0
    result = user_input * NEPTUNE_EQUIVALENT_WEIGHT
    print("Weight on Neptune:", round(result, 2))

def main():
    global user_input;global choice_planet
    print(user_input)
    if choice_planet=='Mercury':
        print(user_input)
        mercury_weight()
    elif choice_planet=='Venus':
        venus_weight()       
    elif choice_planet=='Jupiter':
        jupiter_weight()
    elif choice_planet=='Saturn':
        uranus_weight()
    elif choice_planet=='Uranus':
        uranus_weight()
    else:
        neptune_weight()





