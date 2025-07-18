# Ghidra Python REST API client
This library provides the synchronous client for the [unofficial Ghidra extension](https://github.com/kotcrab/ghidra-rest-api) that adds read-only REST API to your Ghidra project.

## Installation

Right now there's no distribution available at pypi.org, so you'll have to install it from here.
Either `pip install git+https://github.com/Nemoumbra/ghidra-rest-client-python.git@main`
(pip is smart enough to install from Github) or clone the repository and do a local installation.
This package is using `setuptools` so make sure it's present and not too old.
---
If your PyCharm is struggling with the package installed as editable, try reinstalling with this command instead: `pip install -e /path/to/cloned/repo --config-settings editable_mode=compat`.


## Usage

Create an instance of the class `GhidraClient`, possibly submitting a URI for the extension's endpoint
(by default it uses `http://127.0.0.1:18489`). Please refer to the `ghidra-rest-api` repository for the [details](https://github.com/kotcrab/ghidra-rest-api/#usage) on how to
start the server and how to pick a custom port.
```py
client = GhidraClient()

# Issue your requests to the API through this client:
result = client.get_memory("0x08804000", 0x10)
raw_bytes_1 = b64decode(result.memory)
raw_bytes_2 = client.get_memory_raw(0x08804000, 16)
# (Demonstrating how you can specify some arguments both as string or as int)

assert raw_bytes_1 == raw_bytes_2
```

This library supports every method from the Ghidra REST API with minor differences. That is, the additional argument
`format=raw` is not supported by `client.get_memory`. Instead, it is implemented as a separate method `client.get_memory_raw`.
The full list of methods is present in the extension's repository.