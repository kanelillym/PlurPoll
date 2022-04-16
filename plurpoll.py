def get_question():
    return input("What are we trying to decide? ")

def get_responses():
    response_list = []
    response = "garbage starting data"
    while response != "":
        response = input("Response option: ")
        if response == "":
            break
        response_list.append(response)
    return response_list

def get_votes():
    pass

def display_results():
    pass

def main():
    question = get_question()
    responses = get_responses()
    votecounter = [0]*len(responses)
    get_votes()
    display_results()

main()
