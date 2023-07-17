import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message

def run_block_a():
    response = input("Which program in 'Block A: basics' do you wish to run?")
    if response == "simple message":
        simple_message.run()
    elif response == "multiline_message":
         multiline_message.run2()


def run():
    isrunning = True

    while(isrunning):
        print("What you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[q] Quit")
        response = input()

        if response == "a":
            run_block_a()
        elif response == "q":
            break
        else:
            print("Invalid option! Please try again.")

run()