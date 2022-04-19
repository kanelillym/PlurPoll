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

def display_single_result(options, votes, index):
    print("{what}: {num}".format(what=options[index], num=votes[index]))

def print_voter_list(voters):
    if len(voters) == 0:
        return
    elif len(voters) == 1:
        print("{name} voted.".format(name=voters[0]))
        return
    for i in range(0, len(voters)-1):
        print(voters[i], end=", ")
    print("and {name} voted.".format(name=voters[-1]))

def display_results(question, options, votes, voters):
    if max(votes) == 0:
        print("No one voted.")
        return
    index_max = votes.index(max(votes))
    print("{q}\n{o} won with {v} vote(s).".format(q=question, o=options[index_max], v=votes[index_max]))
    for i in range(0, len(options)):
        display_single_result(options, votes, i)
    print_voter_list(voters)

def main():
    question = get_question()
    responses = get_responses()
    print_response_options(responses)
    votecounter = [0]*len(responses)
    vote_counter, voters = get_votes(votecounter)
    display_results(question, responses, vote_counter, voters)

main()
