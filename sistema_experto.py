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
        
    #COVID-19
    @Rule(
             Sintoma(fiebre=True, tos_seca=True, perdida_olfato=True)
        )
    def diagnosticar_covid19(self):
        print("Diagnostico: covid19")            
        print("Se recomienda acudir con el medico y tomar unas semanas de cuarentena")
        self.declare(Diagnostico(enfermedad="covid19"))

    #Resfriado comun
        @Rule(
                Sintoma(congestion_nasal=True, estornudos=True, tos_leve=True)
            )
        def diagnosticar_resfriado(self):
            print("Diagnostico: Resfriado comun")            
            print("Se recomienda ir a consulta y seguir indicaciones")
            self.declare(Diagnostico(enfermedad="resfriado comun"))

    #Bronquitis
    @Rule(
            Sintoma(tos_persistente=True, produccion_flema=True, dificultad_respiratoria=True)
    )
    def diagnosticar_bronquitis(self):
        print("Diagnostico: Bronquitis")
        print("Se recomienda quedarse en casa y tomar reposo")
        self.declare(Diagnostico(enfermedad="Bronquitis"))

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

# CASO 6
print("\n--- CASO 6 ---")
engine = SistemaExperto()
engine.reset()

engine.declare(Sintoma(
    fiebre=True,
    tos_seca=True,
    perdida_olfato=True
))

engine.run()

# CASO 7
print("\n--- CASO 7 ---")
engine = SistemaExperto()
engine.reset()

engine.declare(Sintoma(
    congestion_nasal=True,
    estornudos=True,
    tos_leve=True
))

engine.run()

# CASO 8
print("\n--- CASO 8 ---")
engine = SistemaExperto()
engine.reset()

engine.declare(Sintoma(
    tos_persistente=True,
    produccion_flema=True,
    dificultad_respiratoria=True
))

engine.run()

print("\nANALISIS DE CONFLICTOS")
engine = SistemaExperto()
engine.reset()

engine.declare(Sintoma(fiebre = True, 
                       tos=True,
                       dolor_de_garganta=True,
                       estornudos=True,
                       congestion_nasal=True,
                       picazon_ojos=True))

engine.run()
