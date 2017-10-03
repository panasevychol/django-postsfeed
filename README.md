# django-postsfeed

That's a simple API to view and edit the post feed.
There're two types of users can be registered: reporters and editors

Reporters can:
- view all approved and not approved posts
- create posts

Editors can:
- everything that reporters can
- approve posts

Unregistered users can:
- view only approved posts

Also everybody can filter search results by substring in title or body

All API is built on GET requests. I know that's not secure but that's easier to check how it works then API with POST requests.

## How to run
Written in Python3
```
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```
The application will be available at `localhost:8000`

#### Admin panel
You can add some entries through Django admin panel

## URL scheme

#### /posts/show
Shows posts

GET parameters:
- token
- title_contains
- body_contains
- limit
- offset
Example: `/posts/show?token=some-token&title_contains=substring&limit=2`

#### /posts/create
Create posts. Only reporters and editors allowed to do that

GET parameters:
- title
- body
- token
Example: `/posts/create?token=some-token&title=cool title&body=cool body`

#### /posts/approve
Approve posts. Only editors allowed to do that

GET parameters:
- id
- token
Example: `/posts/approve?token=some-token&id=1`

#### /users/register
Register a new user.

GET parameters:
- email
- password
- role (editor or reporter)
Example: `/users/register?email=email@example.com&password=password&role=reporter`

#### /users/get-token
Request for user token with email and password

GET parameters:
- email
- password
Example: `/users/get-token?email=email@example.com&password=password`

#### /users/get-profile
Get user's profile by token

GET parameters:
- token
Example: `/users/get-profile?token=some-token`
