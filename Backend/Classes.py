from dataclasses import dataclass
from random import randint
from dataclasses import field



@dataclass
class Estudiante:
    Id: int = None
    Nombre: str = ""
    Apellido: str = ""
    Direccion: str = ""
    Celular: int = 0

    def MatricularPrograma(self, Programa: 'Programa'):
        Programa.CrearEstudiante(self)


@dataclass
class Curso:
    Id:int 
    Nombre: str
    Creditos: int

@dataclass
class Programa:
    Codigo: int
    Nombre: str
    Creditos: int
    Estudiantes: list[Estudiante] = field(default_factory=list)
    Cursos: list[Curso] = field(default_factory=list)

    def CrearEstudiante(self, Estudiante: Estudiante):
        if not  Estudiante.Id:
            PossibleId = randint(1000, 9999)
            while PossibleId in self.Estudiantes:
                PossibleId = randint(1000, 9999)
            Estudiante.Id = PossibleId    
        self.Estudiantes.append(Estudiante)
        

    def CrearCurso(self, Curso: Curso):
        self.Cursos.append(Curso)



