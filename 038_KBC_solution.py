questions = [
    ["What is the capital of India?", "Bhopal", "Delhi", "Mumbai", "Kolkata", 2],
    ["Which is the most famous place to visit in India?", "Taj Mahal", "Golconda Fort", "Red Fort", 1],
    ["What is another name for India?", "Bharat", "Hindustani", "Hinduism", "Ironworld", 1],
    ["Who is known as the Father of the Nation in India?", "Mahatma Gandhi", "Jawaharlal Nehru", "Subhas Chandra Bose", "Bhagat Singh", 1],
    ["Which Indian city is known as the 'Pink City'?", "Jaipur", "Udaipur", "Jodhpur", "Bikaner", 1],
    ["Which is the largest state in India by area?", "Maharashtra", "Madhya Pradesh", "Rajasthan", "Uttar Pradesh", 3],
    ["What is the national animal of India?", "Lion", "Elephant", "Tiger", "Leopard", 3],
    ["Which river is considered the holiest river in India?", "Yamuna", "Ganga", "Godavari", "Narmada", 2],
    ["Who was the first Prime Minister of India?", "Sardar Patel", "Lal Bahadur Shastri", "Indira Gandhi", "Jawaharlal Nehru", 4],
    ["Which is the highest mountain peak in India?", "Nanda Devi", "Kangchenjunga", "Mount Everest", "K2", 2]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000]
money = 0

for i in range(len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"a. {question[1]}      b. {question[2]}")
    print(f"c. {question[3]}      d. {question[4]}")
    
    reply = int(input("Enter your answer (1-4) or 0 to quit: "))
    
    if reply == 0:
        if i > 0:
            money = levels[i-1]
        break
    if reply == question[5]:
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 10000000
        money = levels[i]
    else:
        print("Wrong answer!")
        break

print(f"You have won Rs. {money}")
