# SSH example

This example executes a command on a remote server.
It copies project files back and forth.

## Add your SSH key to the server

Assuming you've created one and added it to the agent,

```sh
ssh-copy-id $USER@$HOST
```
