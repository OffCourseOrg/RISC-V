from gdb_remote_client import GdbRemoteClient

# Connect to stub running on localhost, TCP port 3333
cli = GdbRemoteClient("localhost", 1234) 
cli.connect()

# Example how to interact with the stub:

# cli.cmd("...") sends a command and returns the response
resp = cli.cmd("qSupported")
print("The remote stub supports these features: " + resp)  

resp = cli.cmd("g")
print("Values of general-purpose registers: " + resp)

resp = cli.cmd("vMustReplyEmpty")
if resp != "":
    raise RuntimeError("Unexpected reply to command vMustReplyEmpty")

# No-ack mode can be configured by cli.set_no_ack_mode(True)
resp = cli.cmd("QStartNoAckMode")
if resp != "OK":
    raise RuntimeError("The stub refused to enter the no-ack mode")
cli.set_no_ack_mode(True)  # no ACKs from now on

# Some commands don't produce the response immediately but only after
# the target halts (e.g. the vCont command). For such commands, 
# the cli.cmd_no_reply() method must be used.
cli.cmd_no_reply("vCont;c")  
time.sleep(2.0)
cli.ctrl_c()  # Interrupt the running process

# When the target halts, the stop reply from the stub can be fetched 
# by cli.get_stop_reply(). This method returns both the stop reply
# and the text, printed to the console during the program run.
stop_reply, console_text = cli.get_stop_reply()
print("Process halted with this stop reply: " + stop_reply)
if len(console_text) > 0:
    print("This console output was produced while the program ran: " + console_text)
else:
    print("No console output was produced while the program ran.")

# ...
# ...

# Finally, disconnect
cli.disconnect()
