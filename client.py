import sys
import requests

VERSION = "0.0.1-alpha"

def breaker(num: int=50, char: str="*") -> None:
    print("\n" + num*char + "\n")


def handler_2(kb_key: str, response) -> None:
    breaker()
    print(f" --- {' '.join([k.upper() for k in kb_key.split('_')])} ---\n")

    i: int = 0
    keys: list = []
    for key, _ in response.json()["questions"].items():
        print(f"{i+1}. {' '.join([k.upper() for k in key.split('_')]).title()}")
        keys.append(key)
        i += 1

    choice_2 = input("\n\nEnter Choice : ")

    if int(choice_2) > i:
        print("\n --- INVALID INPUT ---")
    else:
        breaker()
        print(f" --- {' '.join([k for k in keys[int(choice_2)-1].split('_')]).upper()} ---\n")
        i: int = 0
        for question in response.json()["questions"][keys[int(choice_2)-1]]:
            print(f"{i+1}. {question}")
            i += 1
    
        choice_3 = input("\n\nEnter Choice : ")

        if int(choice_3) > len(response.json()["answers"][keys[int(choice_2)-1]]):
            print("\n --- INVALID INPUT ---")
        else:
            breaker()
            print(f" --- {response.json()['questions'][keys[int(choice_2)-1]][int(choice_3)-1].upper()} ---\n")
            print(f"{response.json()['answers'][keys[int(choice_2)-1]][int(choice_3)-1]}")
        


def main():

    args: str ="--root-url"    
    root_url:str = "http://127.0.0.1:10000"

    if args in sys.argv: root_url = sys.argv[sys.argv.index(args) + 1]

    breaker()
    print(f" --- CBQ CHATBOT {requests.request(method='GET', url=f'{root_url}/chatbot-version').json()['version']} Python Client ---")

    while True:
        breaker()
        choice_1 = input("1. Telephone Banking\n2. Mobile Banking\n3. Internet Banking\n4. Exit\n\n\nEnter Choice : ")
        assert len(choice_1) == 1, "Invalid Input"

        if choice_1 == "1": 
            response = requests.request(method="GET", url=f"{root_url}/telephone-banking")

            if response.status_code == 200:
                breaker()
                print(" --- TELEPHONE BANKING ---\n")

                for i in range(len(response.json()["questions"])):
                    print(f"{i+1}. {response.json()['questions'][i]}")
                    i += 1
                
                choice_2 = input("\n\nEnter Choice : ")

                if int(choice_2) >= len(response.json()["questions"]):
                    print("\n --- INVALID INPUT ---")
                else:
                    print(f"\n{response.json()['answers'][int(choice_2)-1]}")
        
        elif choice_1 == "2": 
            response = requests.request(method="GET", url=f"{root_url}/mobile-banking")
            if response.status_code == 200: 
                handler_2("mobile_banking", response)

        elif choice_1 == "3": 
            response = requests.request(method="GET", url=f"{root_url}/internet-banking")
            if response.status_code == 200: 
                handler_2("internet_banking", response)

        elif choice_1 == "4": break

        else:
            breaker() 
            print("--- INVALID INPUT ---")

    breaker()


if __name__ == "__main__":
    sys.exit(main() or 0)
