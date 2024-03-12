class Computador:

    def _init_(self, marca, modelo, processador, memoria, hd):
        
        self.marca = marca
        self.modelo = modelo
        self.processador = processador
        self.memoria = memoria
        self.hd = hd
        
        self.monitor = None
    
 
    def conectar_monitor(self, monitor):
        
        if isinstance(monitor, Monitor):
            
            self.monitor = monitor
           
            return f"Monitor {monitor.marca} {monitor.modelo} conectado ao computador {self.marca} {self.modelo}."
        else:
           
            return "O monitor não é válido."


class Monitor:
  
    def _init_(self, marca, modelo, tamanho, resolucao):
       
        self.marca = marca
        self.modelo = modelo
        self.tamanho = tamanho
        self.resolucao = resolucao


computador1 = Computador("Dell", "Inspiron 15", "Intel Core i5", "8 GB", "256 GB")


monitor1 = Monitor("LG", "UltraWide", "29\"", "2560x1080")


print(computador1.conectar_monitor(monitor1))