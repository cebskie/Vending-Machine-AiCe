import re

class VendingMachineDFA:
    def __init__(self, transition_file, refund_enabled=False):
        self.states = set()
        self.alphabet = set()
        self.start_state = "S0"
        self.accept_states = set()
        self.reject_states = "REJECT"
        self.transitions = {}
        self.current_state = self.start_state
        self.balance = 0
        self.refund_enabled = refund_enabled
        self.trace = [self.current_state]
        self.load_transitions(transition_file)

    def load_transitions(self, filename):
        with open(filename, "r") as file:
            lines = file.readlines()

        transition_pattern = re.compile(r"(S\d+)\s+(\d+)\s+(S\d+\*?)")

        for line in lines:
            line = line.strip()
            if line.startswith("States:"):
                self.states = set(line.split(": ")[1].split(", "))
            elif line.startswith("Alphabet:"):
                self.alphabet = set(map(int, line.split(": ")[1].split(", ")))
            elif line.startswith("Start:"):
                self.start_state = line.split(": ")[1]
                self.current_state = self.start_state
            elif line.startswith("Accept:"):
                self.accept_states = set(line.split(": ")[1].split(", "))
            elif line and not line.startswith("Transitions:"):
                match = transition_pattern.match(line)
                if match:
                    state_from, amount, state_to = match.groups()
                    amount = int(amount)
                    if state_to.endswith("*"):
                        state_to = state_to.rstrip("*")
                        self.accept_states.add(state_to)
                    if state_from not in self.transitions:
                        self.transitions[state_from] = {}
                    self.transitions[state_from][amount] = state_to

    def insert_money(self, amount):
        if amount not in self.alphabet:
            print("Nominal tidak diterima! Harap masukkan pecahan 1000, 2000, 5000 atau 10000")
            return
        if self.balance + amount > 10000:
            print("Batas maksimal uang yang diterima adalah Rp10.000!")
            return

        self.balance += amount
        next_state = self.transitions.get(self.current_state, {}).get(amount, self.current_state)

        if next_state != self.current_state:
            self.current_state = next_state
            self.trace.append(self.current_state)

        available_drinks = self.get_available_drinks()
        if available_drinks:
            print(f"ON: {', '.join(available_drinks)}")
        print(f"Saldo saat ini: Rp{self.balance}")

    def get_available_drinks(self):
        available = []
        if self.balance >= 3000: available.append("Minuman A")
        if self.balance >= 4000: available.append("Minuman B")
        if self.balance >= 6000: available.append("Minuman C")
        return available

    def buy_drink(self, choice):
        price_map = {"A": 3000, "B": 4000, "C": 6000}
        if choice in price_map and self.balance == price_map[choice]:
            print(f"Lintasan DFA: {' → '.join(self.trace)}")
            print(f"Minuman {choice} dapat dibeli. Status: ACCEPTED.")
            print("Terima kasih telah menggunakan vending machine!")
            exit()
        else:
            self.current_state = self.reject_states
            self.trace.append(self.current_state)
            print(f"Lintasan DFA: {' → '.join(self.trace)}")
            print("Saldo tidak pas. Status: REJECTED")
            exit()

# Contoh penggunaan
vending_machine = VendingMachineDFA("vending_dfa.txt", refund_enabled=False)
while True:
    user_input = input("Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): ")
    if user_input in {"A", "B", "C"}:
        vending_machine.buy_drink(user_input)
    else:
        try:
            vending_machine.insert_money(int(user_input))
        except ValueError:
            print("Input tidak valid, masukkan nominal angka atau pilihan minuman!")
