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

def print_response_options(responses):
    print("Response Options:")
    i = 1
    for x in responses:
        print("{num}: {val}".format(num=i, val=x))
        i += 1

def handle_votes(response_counter, votes):
    for vote in votes:
        if (vote.isnumeric() == False):
            raise TypeError("non-numeric vote")
    for vote in votes:
        response_counter[int(vote)-1] += 1
    return response_counter

def get_votes(response_counter):
    print("Put in your votes! You can put \"-n name\" at the beginning to include your name in the list of voters.")
    print("An empty vote submission will end the voting phase.")
    voters = []
    while True:
        try:
            votestring = input("> ")
            match votestring.split():
                case []:
                    break
                case ["-n", name, *votes]:
                    response_counter = handle_votes(response_counter, votes)
                    voters.append(name)
                case [*votes]:
                    response_counter = handle_votes(response_counter, votes)
        except TypeError:
           print("Votes must only contain numbers and your name, and your name must come first.")
        except IndexError:
            print("You tried to vote for a number that doesn't exist, please try again.")
    return response_counter, voters

def display_results():
    pass

def main():
    question = get_question()
    responses = get_responses()
    print_response_options(responses)
    votecounter = [0]*len(responses)
    vote_counter, voters = get_votes(votecounter)

main()
