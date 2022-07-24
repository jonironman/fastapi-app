from pydantic import BaseModel, Field, EmailStr


class PostSchema(BaseModel):
    id : int = Field(default=None)
    title : str = Field(default=None)
    content : str = Field(default=None)
    
    class Config:
        schema_extra = {
            "post_demo": {
                "title" : "some title animals",
                "content" : "some content about animals"
            }
        }


class UserSchema(BaseModel):
    fullname : str = Field(default=None)
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class COnfig:
        the_schema = {
            "user_demo": {
                "name" : "Kos",
                "email" : "kos@ex.com",
                "password" : "123"
            }
        }

class UserLoginSchema(BaseModel):
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class COnfig:
        the_schema = {
            "user_demo": {
                "email" : "kos@ex.com",
                "password" : "123"
            }
        }