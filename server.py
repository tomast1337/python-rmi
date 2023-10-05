"""
Pyro4 RMI Server Example
"""
import Pyro4
import rich
print = rich.print

@Pyro4.expose
class Calculator(object):
    def eval(self,data:str):
        result = 0
        # eval the data math expression
        try:
            result = eval(data)
        except Exception as e:
            print(e)
        return result

# Create a Pyro daemon
daemon = Pyro4.Daemon()

# Register the object with the daemon
uri = daemon.register(Calculator)

# Print the uri so we can use it in the client later
print("Ready. Object uri =", uri)

# Start the event loop of the server to wait for calls
daemon.requestLoop()
