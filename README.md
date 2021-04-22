# Library (MyTona Test Task)

Python API-only web-service for managing books.

## Usage

To lauch the local server that will serve the API build the container first:

```bash
docker build . -t mytona_library
```

Then run it:

```bash
docker run -p 8000:8000 mytona_library
```

## API

Seeing available endpoints:

```bash
curl -X GET "http://localhost:8000"
```
```json
{"authors":"http://localhost:8000/authors/","books":"http://localhost:8000/books/"}
```

Listing all authors:

```bash
curl -X GET "http://localhost:8000/authors/"
```
```json
{"detail":"Authentication credentials were not provided."}
```

`author` endpoint (as well as `books` endpoint) requries an authentication. Authenticate with following credentials:

| Login | Password |
|-------|----------|
| john_doe | john_doe_library |

Listing all books:

```bash
curl -X GET --user john_doe:john_doe_library "http://localhost:8000/books/"
```

```json
[
  {
    "id": 2,
    "title": "Harry Potter and the Order of the Phoenix",
    "description": "There is a door at the end of a silent corridor. And it’s haunting Harry Pottter’s dreams. Why else would he be waking in the middle of the night, screaming in terror?",
    "authors": [
      {
        "id": 2,
        "name": "J.K. Rowling"
      },
      {
        "id": 6,
        "name": "Mary GrandPré"
      }
    ]
  },
  {
    "id": 4,
    "title": "The Book Thief",
    "description": "It is 1939. Nazi Germany. The country is holding its breath. Death has never been busier, and will be busier still.",
    "authors": [
      {
        "id": 5,
        "name": "Markus Zusak"
      }
    ]
  },
  {
    "id": 1,
    "title": "The Hunger Games",
    "description": "In the ruins of a place once known as North America lies the nation of Panem, a shining Capitol surrounded by twelve outlying districts. The Capitol is harsh and cruel and keeps the districts in line by forcing them all to send one boy and one girl between the ages of twelve and eighteen to participate in the annual Hunger Games, a fight to the death on live TV.",
    "authors": [
      {
        "id": 1,
        "name": "Suzanne Collins"
      }
    ]
  },
  {
    "id": 3,
    "title": "To Kill a Mockingbird",
    "description": "The unforgettable novel of a childhood in a sleepy Southern town and the crisis of conscience that rocked it. \"To Kill A Mockingbird\" became both an instant bestseller and a critical success when it was first published in 1960. It went on to win the Pulitzer Prize in 1961 and was later made into an Academy Award-winning film, also a classic.",
    "authors": [
      {
        "id": 3,
        "name": "Harper Lee"
      }
    ]
  }
]
```

Listing all authors:

```bash
curl -X GET --user john_doe:john_doe_library "http://localhost:8000/authors/"
```

```json
[
  {
    "id": 3,
    "name": "Harper Lee"
  },
  {
    "id": 2,
    "name": "J.K. Rowling"
  },
  {
    "id": 4,
    "name": "Jane Austen"
  },
  {
    "id": 5,
    "name": "Markus Zusak"
  },
  {
    "id": 6,
    "name": "Mary GrandPré"
  },
  {
    "id": 1,
    "name": "Suzanne Collins"
  }
]
```

Listing books filtered by authors:

```bash
curl -X GET --user john_doe:john_doe_library "http://localhost:8000/books/?authors=J.K.+Rowling,Harper+Lee"
```

```json
[
  {
    "id": 2,
    "title": "Harry Potter and the Order of the Phoenix",
    "description": "There is a door at the end of a silent corridor. And it’s haunting Harry Pottter’s dreams. Why else would he be waking in the middle of the night, screaming in terror?",
    "authors": [
      {
        "id": 2,
        "name": "J.K. Rowling"
      },
      {
        "id": 6,
        "name": "Mary GrandPré"
      }
    ]
  },
  {
    "id": 3,
    "title": "To Kill a Mockingbird",
    "description": "The unforgettable novel of a childhood in a sleepy Southern town and the crisis of conscience that rocked it. \"To Kill A Mockingbird\" became both an instant bestseller and a critical success when it was first published in 1960. It went on to win the Pulitzer Prize in 1961 and was later made into an Academy Award-winning film, also a classic.",
    "authors": [
      {
        "id": 3,
        "name": "Harper Lee"
      }
    ]
  }
]
```

Accessing the specific book:

```bash
curl -X GET --user john_doe:john_doe_library "http://localhost:8000/books/1/"
```

```json
{
  "id": 1,
  "title": "The Hunger Games",
  "description": "In the ruins of a place once known as North America lies the nation of Panem, a shining Capitol surrounded by twelve outlying districts. The Capitol is harsh and cruel and keeps the districts in line by forcing them all to send one boy and one girl between the ages of twelve and eighteen to participate in the annual Hunger Games, a fight to the death on live TV.",
  "authors": [
    {
      "id": 1,
      "name": "Suzanne Collins"
    }
  ]
}
```

Adding a new book:

```bash
curl -X POST --user john_doe:john_doe_library --header "Content-Type: application/json" --data '{"title": "Catching Fire", "authors": [{"id": 1, "name": "Suzanne Collins"}]}' "http://localhost:8000/books/"
```

```json
{
  "id": 6,
  "title": "Catching Fire",
  "description": "",
  "authors": [
    {
      "id": 1,
      "name": "Suzanne Collins"
    }
  ]
}
```

Updating the existing book:

```bash
curl -X PUT --user john_doe:john_doe_library --header "Content-Type: application/json" --data '{"title": "The Hunger Games: Catching Fire", "authors": [{"id": 1, "name": "Suzanne Collins"}]}' "http://localhost:8000/books/6/"
```

```json
{
  "id": 6,
  "title": "The Hunger Games: Catching Fire",
  "description": "",
  "authors": [
    {
      "id": 1,
      "name": "Suzanne Collins"
    }
  ]
}
```

Deleting the existing book:

```bash
curl -X DELETE --user john_doe:john_doe_library "http://localhost:8000/books/6/"
```

Adding a new author:

```bash
curl -X POST --user john_doe:john_doe_library --header "Content-Type: application/json" --data '{"name": "John Green"}' "http://localhost:8000/authors/"
```

```json
{"id": 7, "name": "John Green"}
```

Updating the existing author:

```bash
curl -X PUT --user john_doe:john_doe_library --header "Content-Type: application/json" --data '{"name": "John Michael Green"}' "http://localhost:8000/authors/7/"
```

```json
{"id": 7, "name": "John Michael Green"}
```

Deleting the existing author:

```bash
curl -X DELETE --user john_doe:john_doe_library "http://localhost:8000/authors/7/"
```
