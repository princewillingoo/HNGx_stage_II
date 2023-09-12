
# FastAPI CRUD API Documentation

This documentation overviews the FastAPI CRUD API, including: 
- Endpoints request/response formats
- Sample usage
- Limitations

## Endpoints

### Create a New Person
- **URL**: `/api/`
- **Method**: POST
- **Request Format** -> JSON:
  - `name` (string, required): The person's name.
- **Response Format** -> JSON:
  - `id` (integer): The unique identifier of the created person.
  - `name` (string): The name of the person.                    

### Retrieve a Person by ID
- **URL:** `/api/{id}`
- **Method:** GET
- **Response Format**  -> JSON:
  - `id` (integer): The person's unique identifier.
  - `name` (string): The name of the person.

### Update a Person by ID
- **URL:** `/api/{id}`
- **Method:** PUT
- **Request Format** -> JSON:
  - `name` (string, required): The updated name of the person.
- **Response Format** -> JSON:
  - `id` (integer): The unique identifier of the updated person.
  - `name` (string): The updated name of the person.

### Delete a Person by ID
- **URL:** `/api/{id}`
- **Method:** DELETE
- **Response Format:**
  - `Status Code`: 204

## Sample Usage

### Create Person
#### Request
```
curl -X 'POST' \
  '<base url>/api/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{ "name": "Ihuoma Princewill" }'
```
#### Response
```
{ "name": "Ihuoma Princewill", "id": 2 }
```

### Get Person
#### Request
```
curl -X 'GET' \
  'http://127.0.0.1:8000/api/2/' \
  -H 'accept: application/json'
```
#### Response
```
{ "name": "Ihuoma Princewill", "id": 2 }
```

### Update Person
#### Request
```
curl -X 'PUT' \
  'http://127.0.0.1:8000/api/2/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{ "name": "Lawrence Gideon" }'
```
#### Response
```
{ "name": "Lawrence Gideon", "id": 2 }
```
### Delete Person
#### Request
```
curl -X 'DELETE' \
  'http://127.0.0.1:8000/api/2/' \
  -H 'accept: */*'
```
#### Response
```
Status Code -> 204 
```
## Limitations

- No specification on authentication and authorization. This can be a security risk, as anyone can access and modify the data without proper authentication and authorization mechanisms.
- The API is specific to CRUD operations for a "Person" resource. It may not cover more complex use cases or multiple resource types.
- There is no mention of API versioning. Without versioning, future changes to the API may break existing client applications.
