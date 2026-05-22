from storage import *
from security import hash_password
from logger import log_event

class VotingApp:
    def __init__(self):
        self.voters = load_json(VOTER_FILE, {})
        self.candidates = load_json(CANDIDATE_FILE, {})
        self.voted = set(load_json(VOTED_FILE, []))
        self.admin = load_json(ADMIN_FILE, {"password": hash_password("admin123"), "closed": False})

    def register_voter(self, vid, name):
        if vid in self.voters:
            print("Voter exists")
            return
        self.voters[vid] = name
        save_json(VOTER_FILE, self.voters)
        log_event(f"Registered voter {vid}")

    def add_candidate(self, cid, name):
        if cid in self.candidates:
            print("Candidate exists")
            return
        self.candidates[cid] = {"name": name, "votes": 0}
        save_json(CANDIDATE_FILE, self.candidates)
        log_event(f"Added candidate {cid}")

    def vote(self, vid, cid):
        if self.admin["closed"]:
            print("Election closed")
            return
        if vid not in self.voters:
            print("Not registered")
            return
        if vid in self.voted:
            print("Duplicate vote")
            return
        if cid not in self.candidates:
            print("Invalid candidate")
            return

        self.candidates[cid]["votes"] += 1
        self.voted.add(vid)

        save_json(CANDIDATE_FILE, self.candidates)
        save_json(VOTED_FILE, list(self.voted))
        log_event(f"{vid} voted for {cid}")
        print("Vote recorded")

    def close(self, password):
        if hash_password(password) != self.admin["password"]:
            print("Wrong password")
            return
        self.admin["closed"] = True
        save_json(ADMIN_FILE, self.admin)
        print("Election closed")

    def results(self):
        if not self.admin["closed"]:
            print("Election open")
            return
        total = sum(c["votes"] for c in self.candidates.values())
        for c in self.candidates.values():
            percent = (c["votes"]/total*100) if total else 0
            print(c["name"], c["votes"], f"{percent:.2f}%")