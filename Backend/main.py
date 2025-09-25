from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from .Classes import Estudiante, Programa


app = FastAPI()
@app.get("/crear_estudiante_form", response_class=HTMLResponse)
def crear_estudiante_form():
    return """\
<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Crear Estudiante</title>
</head>
<body>
    <h1>Crear Estudiante</h1>
    <form action=\"/crear_estudiante\" method=\"post\">
        <label for=\"nombre\">Nombre:</label>
        <input type=\"text\" id=\"nombre\" name=\"nombre\" required><br><br>

        <label for=\"apellido\">Apellido:</label>
        <input type=\"text\" id=\"apellido\" name=\"apellido\" required><br><br>

        <label for =\"Direccion\">Direccion:</label>
        <input type = \"text\" id = \"Direccion\" name = \"Direccion\" required><br><br>

        <label for=\"Celular\">Celular:</label>
        <input type=\"number\" id=\"Celular\" name=\"Celular\" required><br><br>

        <input type=\"submit\" value=\"Crear Estudiante\">
    </form>
</body>
</html>
    """

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

programa = Programa(Codigo=1, Nombre="Ingeniería", Creditos=120)

@app.post("/crear_estudiante")
async def crear_estudiante(nombre: str = Form(...), apellido: str = Form(...), Direccion: str = Form(...), Celular: int = Form(...)):
    estudiante = Estudiante(Nombre =  nombre, Apellido = apellido, Direccion = Direccion, Celular = Celular)
    programa.CrearEstudiante(estudiante)
    return JSONResponse({"message": "Estudiante creado", "id": estudiante.Id, "nombre": estudiante.Nombre, "apellido": estudiante.Apellido, "direccion": estudiante.Direccion, "celular": estudiante.Celular})

@app.get("/")
def root():
    return {"message": "API running"}
