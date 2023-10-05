"""
Pyro4 RMI Client Example
"""
import Pyro4
import rich
from rich.prompt import Prompt
print = rich.print
input = Prompt.ask

# Get the uri of the server object
uri = input("[bold green]Enter the uri of the server object:[/bold green]")

if uri == "":
    print("[bold red]No uri provided[/bold red]")
    print("[bold red]Exiting...[/bold red]")
    exit()

# Create a Pyro proxy to the server object
calculatorRO = Pyro4.Proxy(uri)

# Loop to get user input and call the server object
data_in = ""
while(data_in != "exit"):
    rich.print("[bold green]Enter a math expression to evaluate or 'exit':[/bold green]")
    data_in = input(">>> ",default="1+1")
    if(data_in != "exit"):
        print(f"{data_in} = {calculatorRO.eval(data_in)}")

print("[bold red]Exiting...[/bold red]")

