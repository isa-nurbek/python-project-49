import prompt 


def welcome():
    print("Welcome to the Brain Games!")
    ask_name = prompt.string("May I have your name?")
    
    print(f"Hello, {ask_name}")
    return ask_name