class Curso:
    
    def _init_(self, nome, codigo):
        self.nome = nome 
        self.codigo = codigo 
        self.professor = None 

   
    def designar_professor(self, professor):
        self.professor = professor 


class Professor:
    
    def _init_(self, nome, matricula):
        self.nome = nome 
        self.matricula = matricula
        self.cursos = [] 
    
    def lecionar_curso(self, curso):
        self.cursos.append(curso) 

    
    def listar_cursos(self):
        print(f"O professor {self.nome} leciona os seguintes cursos:")
        for curso in self.cursos: 
            print(f"- {curso.nome} ({curso.codigo})")

curso1 = Curso("Matemática", "MAT101")
curso2 = Curso("Física", "FIS102")
curso3 = Curso("Química", "QUI103")


prof1 = Professor("Alice", "1234")
prof2 = Professor("Bruno", "5678")


curso1.designar_professor(prof1)
curso2.designar_professor(prof2)
curso3.designar_professor(prof1)


prof1.lecionar_curso(curso1)
prof1.lecionar_curso(curso3)
prof2.lecionar_curso(curso2)


prof1.listar_cursos()
prof2.listar_cursos()