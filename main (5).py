import random

action = ["jump on", "sit on", "stomp on", "throw salt on", "dance on", "lick", "kick", "sniff"]

target = ["your cat", "your dog", "your neighbor", "your dad's car", "your mom's car", "a telphone pole", "a fridge"]

witness = ["your mom", "your dad", "your best friend", "your teacher", "the president of the United States", "your crush", "your worse enemy"]



truths= ["Who's your favorite teacher?", "What is your credit card security code?", "What is the last crime you have commited?", "How do you feel about Obama?", "What is your favorite song?", "Favorite person in this room", "How tall are you?", "Open your wallet"]

responses= ["No way!", "Figures", "Typical you", "I can't belive it", "I hate you", "Be normal", "Not funny"]




def main():
  td= input("Truth or Dare: ")

  if td.lower().startswith('t'):
    print(random.choice(truths))
    t= input()
    print("Hm... "+ t+ "? ")
    print(random.choice(responses))

  elif td.lower().startswith('d'):
    dare= "I dare you to "+ random.choice(action)+ " "+ random.choice(target)+ " in front of "+ random.choice(witness)
    print(dare)
    
  else:
    print("not valid")

main()