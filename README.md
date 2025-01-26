# SSH example

[Project page](https://calkit.io/calkit/example-ssh) |
[GitHub repo](https://github.com/calkit/example-ssh)

A [Calkit](https://github.com/calkit/calkit) example project that
executes a command on a remote server using SSH.
It copies project files back and forth.

Note this will probably fail if run from Windows because Git will probably
send a file with the wrong line endings.

## Setup

### Create an SSH key and add it to the agent

See [these docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

This is only necessary if you haven't done this before.
Optionally, you can create a new key just for this host.
Don't use a passphrase if you want your commands to run without entering
it each time.
This should be okay if your machine is secure.

### Add your SSH key to the server

Assuming you've created one and added it to the agent, call:

```sh
ssh-copy-id $USER@$HOST
```

If created a unique key for this remote host,
use the `-i` flag to specify that key file.

### Fill in the correct environment details

In `calkit.yaml`, there is an environment called `cluster`.
Replace any relevant values there to match your remote machine.
