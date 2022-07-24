from email.policy import default
import imp
from shutil import register_unpack_format
import uvicorn
from fastapi import FastAPI, Body, Depends
from app.model import PostSchema, UserLoginSchema, UserSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer


users = []

posts = [    
    {
                "id": 1,
                "title": "tigers",         
                "content" : "tiger has 1"
             },
             {
                "id": 2,
                "title": "wolf",         
                "content" : "wolf has 2"
             }
]

app = FastAPI()



# Get - for testing
@app.get("/", tags=["posts"])
def greet():
    return {
        "hello": "world!"}



# Get post 
@app.get("/posts/", tags=["posts"])
def all_posts():
    return { "data":  posts}

# Get single post
@app.get("/posts/{id}", tags=["posts"])
def get_one_post(id: int):
    if id > len(posts):
        return {
            "error": "post with ID does not exist!"
        }
    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }

#4 Create post
@app.post("/posts/", dependencies=[Depends(jwtBearer())], tags=["posts"])
def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "info": "post Added!"
    }



#5 user singup
@app.post("/user/signup", tags=["user"])
def user_signup( user: UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False

@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "error" : "invalid login details!"
        }
