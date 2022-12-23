# main.py
from typing import List
from uuid import uuid4
from uuid import UUID
from fastapi import FastAPI
from fastapi import HTTPException 
from models import Gender, Roles, User

#Descripcion de swagger (/doc)
description = """

## Trabajo para Basisty.

## Usuarios

Van a ser capaz de:

* **Crear usuarios** (_implementado y funcionando_).
* **Borrar usuarios** (_implementado y funcionando_).
"""

app = FastAPI(
     title="API de Esteban y Flor 🚀",
    description=description,
    version="1.0.0",
    terms_of_service="https://www.basisty.com/es/",
    contact={
        "name": "Estebanquito",
        "url": "https://www.basisty.com/es/",
        "email": "estebandiaczun@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


db: List[User] = [
 User(
 id=uuid4(),
 first_name="Esteban",
 last_name="Diaczun",
 gender=Gender.male,
 roles=[Roles.user],
 ),
 User(
 id=uuid4(),
 first_name="Flor",
 last_name="Tala",
 gender=Gender.female,
 roles=[Roles.user],
 ),
 User(
 id=uuid4(),
 first_name="Lucas",
 last_name="Faso",
 gender=Gender.male,
 roles=[Roles.user],
 ),
 User(
 id=uuid4(),
 first_name="Sofia",
 last_name="Papi",
 gender=Gender.male,
 roles=[Roles.admin, Roles.user],
 ),
]

#METODOS

#Metodo hola mundito
@app.get("/", tags=["Hola mundito"])
async def root():
 return {"HOLA MUNDITO"}

#metodo para crear usuarios
@app.post("/create", tags=["Crear usuario"])
async def create_user(user: User):
    return {"id": user.id}

#metodo ver los usuarios
@app.get("/users", tags=["Ver los usuarios"])
async def get_users():
    return db

#Metodo para borrar usuarios
@app.delete("/delete/{id}", tags=["Borrar un usuario"])
async def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
        raise HTTPException(
            status_code=404, detail=f"Fallo la eliminacion del usuario, id {id} no encontrada."
        )
        

