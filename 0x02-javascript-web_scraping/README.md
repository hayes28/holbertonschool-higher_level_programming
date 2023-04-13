# 0x02. JavaScript - Web Scraping
This project covers the basics of web scraping using JavaScript. The project contains 6 mandatory tasks that cover topics such as reading and writing files, making HTTP requests, accessing and manipulating JSON data, and using modules such as request and fs.

## Learning Objectives
By the end of this project, students should be able to:

- Explain why JavaScript programming is useful in web scraping
- Manipulate JSON data
- Use the request and fetch APIs
- Read and write files using the fs module

## Requirements
- Allowed editors: vi, vim, emacs
- All files will be interpreted on Ubuntu 14.04 LTS using node (version 10.14.x)
- All files should end with a new line
- The first line of all files should be exactly #!/usr/bin/node
- A README.md file, at the root of the folder of the project, is mandatory
- Code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
- All files must be executable
- The length of the files will be tested using wc
- var is not allowed

## Tasks
### Task 0: Readme
Write a script that reads and prints the content of a file. The first argument is the file path. The content of the file must be read in utf-8. If an error occurs during the reading, print the error object.

### Task 1: Write Me
Write a script that writes a string to a file. The first argument is the file path. The second argument is the string to write. The content of the file must be written in utf-8. If an error occurs while writing, print the error object.

### Task 2: Status Code
Write a script that displays the status code of a GET request. The first argument is the URL to request (GET). The status code must be printed like this: code: <status code>. You must use the module request.

### Task 3: Star Wars Movie Title
Write a script that prints the title of a Star Wars movie where the episode number matches a given integer. The first argument is the movie ID. You must use the Star Wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id. You must use the module request.

### Task 4: Star Wars Wedge Antilles
Write a script that prints the number of movies where the character “Wedge Antilles” is present. The first argument is the API URL of the Star Wars API: https://swapi-api.hbtn.io/api/films/. Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API. You must use the module request.

### Task 5: Loripsum
Write a script that gets the contents of a webpage and stores it in a file. The first argument is the URL to request. The second argument is the file path to store the body response. The file must be UTF-8 encoded. You must use the module request.

### Task 6: How Many Completed?
Write a script that computes the number of tasks completed by user ID. The first argument is the API URL: https://jsonplaceholder.typicode.com/todos. Only print users with completed tasks. You must use the module request.
