# shell-chat (aka. schat)

```schat``` is a rather simple chat tool. There is no server, just a shared temporary file. There is no user registration, nor moderation.

```schat``` is made for multi-user systems, where sometimes communication is needed but no irc or internet uplink is available.

```
schat -- system local chat
    usage: schat [CHATUSER]
```

## Commands
There is a bunch of commands available from the chat interface:

```
/bye 			Gracefully leave this chat.
/clear			Wipe the chatlog.
/help 			Print this help message.
/logdate 		Print current log time stamp.
/names			List active users.
/nick 			Rename yourself.
/reset			Reset chat listen process.
```

Every command introduced with '/' is interpreted as a regular shell command, so ```/bash``` will open a shell! This should not be a security thread, as the user already has shell access to this system.