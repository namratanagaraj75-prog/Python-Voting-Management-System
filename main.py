from voting_app import VotingApp
import os

app = VotingApp()

while True:
    print("\n1.Register 2.Add Candidate 3.Vote 4.Close 5.Results 6.Exit 7.Reset")

    ch = input("Choice: ")

    if ch == "1":
        app.register_voter(input("ID:"), input("Name:"))

    elif ch == "2":
        app.add_candidate(input("ID:"), input("Name:"))

    elif ch == "3":
        app.vote(input("Voter ID:"), input("Candidate ID:"))

    elif ch == "4":
        app.close(input("Admin password:"))

    elif ch == "5":
        app.results()

    elif ch == "6":
        print("Exiting...")
        break

    elif ch == "7":
        files = [
            "data/candidates.json",
            "data/voters.json",
            "data/votes.json",
            "data/votes.log"
        ]

        for file in files:
            try:
                with open(file, "w") as f:
                    if file.endswith(".json"):
                        f.write("{}")
                    else:
                        f.write("")
            except:
                pass

        print("Election reset successful.")

    else:
        print("Invalid option")