# from dataclasses import dataclass
from sqlmodel import SQLModel, Field
from sqlmodel import select
from typing import Optional
from pydantic import validator
from statistics import mean


#@dataclass
class Beer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    estilo: str
    sabor: int
    rotulo: int
    valor: int
    pontos: int = 0


    @validator("sabor", "rotulo", "valor")
    def validacao(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} deve ser entre 1 e 10.")
        return v

    @validator("pontos", always=True)
    def calculo_pntos(cls, v, values):
        pontos = mean(
            [
                values["sabor"],
                values["rotulo"],
                values["valor"]
            ]
        )
        return int(pontos)


bavaria = Beer(name='Bavária', estilo='Baratinha', sabor=6, rotulo=4, valor=10)

