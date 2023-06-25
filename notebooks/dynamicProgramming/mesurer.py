import time
def mesure ( fonction ) :
    #This is a decorator
    def mesure_execution (n,p) :
        start_time = time.time ()
        result = fonction(n,p)
        stop_time = time.time ()
        total=stop_time-start_time
        print("Temps d'execution :{} secondes ".format (total ) )
        return result
    return mesure_execution