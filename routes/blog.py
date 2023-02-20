from bson import ObjectId
from fastapi import APIRouter

from model.blog import Blog
from config.db import conn
from schemas.blog import blogEntity, blogsEntity

blog = APIRouter()

@blog.get('/')
async def find_all_blogs():
    return blogsEntity(conn.local.blog.find())

@blog.get('/{id}')
async def find_one_blog(id):
    return blogEntity(conn.local.blog.find_one({"_id":ObjectId(id)}))

@blog.post ('/post')
async def create_blog(blog: Blog):
    conn.local.blog.insert_one(dict(blog))
    return blogsEntity(conn.local.blog.find())

@blog.put('/{id}')
async def update_blog(id,blog: Blog):
    conn.local.blog.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(blog)
    })
    return blogEntity(conn.local.blog.find_one({"_id":ObjectId(id)}))


