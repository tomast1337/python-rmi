"""
Pyro4 RMI Client Example
"""
import Pyro4
import rich
from rich.prompt import Prompt
print = rich.print
input = Prompt.ask

# Get the uri of the server object
uri = input("Enter the uri of the server object: ")

if uri == "":
    print("No uri entered, exiting...")
    exit()

# Create a Pyro proxy to the server object
eval = Pyro4.Proxy(uri)

# Loop to get user input and call the server object
entrada = ""
while(entrada != "exit"):
    rich.print("[bold green]Enter a math expression to evaluate or 'exit':[/bold green]")
    entrada = input(">>> ",default="1+1")
    if(entrada != "exit"):
        print(f"{entrada} = {eval.eval(entrada)}")

print("Exiting...")

