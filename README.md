<div>
  <img src="https://user-images.githubusercontent.com/69850751/175876062-f252cc1b-bd44-46b3-9ddb-a7692b2eede4.png" alt="hbnb logo">
</div>

## Description

Airbnb clone is a complete web application with front-end interfacing, a back-end API, and database storage.

## Storage

The above classes are handled by the abstracted storage engine defined in the
[FileStorage](./models/engine/file_storage.py) class.

Every time the backend is initialized, AirBnB instantiates an instance of
`FileStorage` called `storage`. The `storage` object is loaded/re-loaded from
any class instances stored in the JSON file `file.json`. As class instances are
created, updated, or deleted, the `storage` object is used to register
corresponding changes in the `file.json`.

## Console

The console is a command line interpreter that permits management of the backend
of AirBnB. It can be used to handle and manipulate all classes utilized by
the application (achieved by calls on the `storage` object defined above).

### Using the Console

The AirBnB console can be run both interactively and non-interactively.
To run the console in non-interactive mode, pipe any command(s) into an execution
of the file `console.py` at the command line.
