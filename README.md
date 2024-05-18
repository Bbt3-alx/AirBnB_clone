# AirBnB Clone Console

This project is a basic command-line interpreter for managing the objects of an AirBnB clone application.
The interpreter allows users to create, view, update and delete instances of various classes, such as `BaseModel`.

## Table of Contents
1. [Descriotion](#description)
2. [Features](#Features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Commands](#commands)
6. [Authors](#authors)


## Description

The AirBnB clone console is a custom command-line interface (CLI) That provides various commands to interact with the backend of an AirBnB service.
The console is built with Python's `cmd` module and includes a storage system that saves and loads objects to and from a JSON file.


## Features

- **Create objects**: Instantiate new objects and save them to storage.
- **Show objects**: Display the string representation of an object based on its class name and ID.
- **Destroy objects**: Delete an object from storage.
- **All objects**: Update attributes of an objects.


## Installation

1. Clone The reposiory to your local machine:
	```bash
	git clone https://github.com/Bbt3-alx/AirBnB_clone.git
	cd AirBnB_clone
```
3. Ensure you have Python 3.8+ installed on your machine.

3. No additional dependencies are required.


## Usage

To start the console, run the following command from the project root directory
	```bash
	python3 console.py
```

You will be presented with the `(hbnb) ` prompt wjere you can enter commands.


## Commands

Here are the primary commands available in the console:
- create <class>
	- Create a new instance of a class, saves it, and prints the ID.
	- Exemple: `create BaseModel`

- show <class><id>
	- Shows the string representation of an instance based on class name and ID.
	- Example: `show BaseModel 123-5678-9012`

- desstroy <class><id>
	- Delete an instance based on class name and ID.
	- Example: `dstroy BaseModel 123-5678-9012`

- all[class]
	- Prints all string representation of all instances or all instances of a specific class.
	- Example: `all` or `all BaseModel`

- update<class><id><attribute_name><attribute_valu>
	- Updates an instance based on class name and ID by adding or updating an attribute.
	- Example: `update baseModel 123-5678-9012 name "New Name"`

- quit
	- Exit the console.

- EOF
	- Exit the console(end-of-file).


## Authors
- [Brehyma Traore](https://github.com/Bbt3-alx)
- [Taofeek AKINBAMI](https://github.com/Techspacenation1995)

