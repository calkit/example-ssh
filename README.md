# SSH example

This example executes a command on a remote server.
It copies project files back and forth.

Note this will probably fail if run from Windows because Git will probably
send a file with the wrong line endings.

## Add your SSH key to the server

Assuming you've created one and added it to the agent,

```sh
ssh-copy-id $USER@$HOST
```
