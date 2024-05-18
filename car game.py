# car engine simulation game

command=""
started=False
while True:
    command=input(">").lower()
    if command =="start":
        if started:
            print("car already started.")
        else:
            started=True
            print("car started.")
    elif command=="stop":
        if not started:
            print("car already stopped")
        else:
            started=False
            print("car stopped.")
    elif command=="help":
        print("start-to start the car"
              "stop-to stop the car"
              "quit-to quit")
    elif command=="quit":
        break
    else:
        print("Sorry, I don't understand this")


