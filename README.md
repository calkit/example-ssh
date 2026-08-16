# SSH example

[Project page](https://calkit.io/calkit/example-ssh) |
[GitHub repo](https://github.com/calkit/example-ssh)

A [Calkit](https://github.com/calkit/calkit) example project that runs one
pipeline stage on another machine over SSH, and the rest locally.

The `raw-data` stage collects data in the `py` environment on a remote
host; `plot` then reads that data and makes a figure here.
Calkit moves the project to a workspace on that host, runs the stage there,
and brings the outputs back.

## Setup

There isn't a separate setup step.
Run the pipeline and Calkit asks for whatever is missing:

```sh
calkit run
```

In a terminal, that prompts for the host and user (saving them to `.env`),
offers to create an SSH key if you don't have one, offers to authorize this
machine on the host with `ssh-copy-id`, and offers to install Calkit there
if it's missing.
Nothing happens without you agreeing to it.

To check the setup without running anything, use:

```sh
calkit check env -n remote
```

Outside a terminal---in CI, say---nothing is prompted for, because there's
nobody to answer.
It fails with the exact commands to run instead.
