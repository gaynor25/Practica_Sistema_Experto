from experta import Fact, KnowledgeEngine, Rule, NOT

# Representa los síntomas que presenta el paciente.
class Sintoma(Fact):
    pass


# Representa el diagnóstico encontrado por el sistema.
class Diagnostico(Fact):
    pass

class SistemaExperto(KnowledgeEngine):
    #GRIPE
    @Rule(
        Sintoma(fiebre=True, tos=True, dolor_de_garganta=True)
    )
    def diagnosticar_gripe(self):
        print("Diagnostico: Gripe")
        print("Se recomienda descansar, tomar liquido y consultar con un medico")
        self.declare(Diagnostico(enfermedad="Gripe"))

   #MIGRAÑA
    @Rule(
        Sintoma(fiebre=True, dolor_de_cabeza=True, nauseas=True)
    )
    def diagnosticar_migraña(self):
        print("Diagnostico: Migraña")
        print("Se recomienda acudir con el medico y descansar en un area sin luz")
        self.declare(Diagnostico(enfermedad="Migraña"))

   #ALERGIA
    @Rule(
            Sintoma(estornudos=True, congestion_nasal=True, picazon_ojos=True)
        )
    def diagnosticar_alergia(self):
        print("Diagnostico: Alergia")            
        print("Se recomienda acudir con el medico y evitar lugares con poco aire circulando")
        self.declare(Diagnostico(enfermedad="Alergia"))

    #GASTROENTERITIS
    @Rule(
            Sintoma(dolor_estomago=True, diarrea=True, vomitos=True)
        )
    def diagnosticar_gastroenteritis(self):
        print("Diagnostico: Gastroenteritis")            
        print("Se recomienda acudir con el medic☻")
        self.declare(Diagnostico(enfermedad="Gastroenteritis"))

    #REGLA DE RESPALDO
    @Rule(
        NOT(Diagnostico())
    )
    def diagnostico_no_encontrado(self):
        print("Diagnostico: NO ENCONTRADO")
        print("Se recomienda acudir con un doctor para recibir un diagnostico certero")

# CASO 1
print("\n--- CASO 1 ---")
engine = SistemaExperto()
engine.reset()

engine.declare(Sintoma(
    fiebre=True,
    tos=True,
    dolor_de_garganta=True
))

engine.run()


# CASO 2
print("\n--- CASO 2 ---")
engine = SistemaExperto()
engine.reset()

engine.declare(Sintoma(
    estornudos=True,
    congestion_nasal=True,
    picazon_ojos=True
))

engine.run()


# CASO 3
print("\n--- CASO 3 ---")
engine = SistemaExperto()
engine.reset()

engine.declare(Sintoma(
    dolor_estomago=True,
    diarrea=True,
    vomitos=True
))

engine.run()


# CASO 4
print("\n--- CASO 4 ---")
engine = SistemaExperto()
engine.reset()

engine.declare(Sintoma(
    cansancio=True,
    mareo=True
))

engine.run()


# CASO 5
print("\n--- CASO 5 ---")
engine = SistemaExperto()
engine.reset()

engine.declare(Sintoma(
    fiebre=True,
    tos=True,
    dolor_de_garganta=True,
    estornudos=True,
    congestion_nasal=True
))

engine.run()
