from qiskit import QuantumCircuit, QuantumRegister
from qiskit_aer import AerSimulator
import numpy as np
import random
"""
the first large part of commented code is the code I had initially written for the Automatic production of function, 
but then realised was broken, and didnt have the heart to delete. Ignore it if it bothers you, read it if you find it interesting, 
even though there is nothing interesting about it.



def Function(indice):

	#Choose one of the two and uncomment them to have that function



	# First, we have a choice. We can input the function ourselves or let it auto generate
	



	# manual setup
	if (indice == 0):
		return ;
	elif (indice == 1):
		return ;
	elif (indice == 2):
		return ;
	elif (indice == 3):
		return ;
	elif (indice == 4):
		return ;
	elif (indice == 5):
		return ;
	elif (indice == 6):
		return ;
	elif (indice == 7):
		return ;
	else:
		return 0;
	"""
	#Place whatever value you need within the index, and you can customize the function




	# Automated setup
	"""
	
	# choosing if function is balanced or constant

	#Choice

	n = random.choice([1,2])
	
	

	#Case 1 : Balanced
	
	if n == 1:
		print("Balanced")
		#Creating base function list
		FunctionList = [0, 0, 0, 0, 0, 0, 0, 0]
		i = 0
		while (i < 4):
			l = random.choice([0, 1, 2, 3, 4, 5, 6, 7])
			if FunctionList.index(l) == 0:
				FunctionList.index(l) = 1;
			else:
				i = i - 1


	

	#Case 2 : Constant
	
	elif n == 2:
		print("Constant")
		#Further cases for producing either 1 filled or 0 filled
		m = random.choice([1,2])
	
		#Case A : 1 Filled
		if m == 2:
			FunctionList = [1, 1, 1, 1, 1, 1, 1, 1]

		#Case B : 0 Filled
		elif m == 1:
			FunctionList = [0, 0, 0, 0, 0, 0, 0, 0]
	"""

	
	
	#Returning an index
	return FunctionList.index(indice)



def Query():
	qc = QuantumCircuit(4)
 
    	if np.random.randint(0, 2):
        	#Flip output qubit with 50% chance
        	qc.x(3)
    	if np.random.randint(0, 2):
        	# return constant circuit with 50% chance
        	return qc
 
    	#Choose half the possible input strings
    	on_states = np.random.choice(
        	range(2**3),  # numbers to sample from
        	2**3 // 2,  # number of samples
        	replace=False,  # makes sure states are only sampled once
    	)
 
    	def add_cx(qc, bit_string):
        	for qubit, bit in enumerate(reversed(bit_string)):
            	if bit == "1":
                	qc.x(qubit)
        	return qc
 
    	for state in on_states:
        	qc.barrier()  # Barriers are added to help visualize how the functions are created.
        	qc = add_cx(qc, f"{state:0b}")
        	qc.mcx(list(range(3)), 3)
        	qc = add_cx(qc, f"{state:0b}")
 
    	qc.barrier()
 
    	return qc



def CircuitMaker():
   	
	qc = QuantumCircuit(4,3)
    
    	#Making the Negative state for the extra last qubit
    	qc.x(3)
    	qc.h(3)
    
    	#Hadamard to all qubits
    	qc.h(range(3))
    
    	qc.barrier()
    
    	#Apply the function as the next step
    	qc.append(oracle.to_gate(), range(4))
    
    	qc.barrier()
    
    	#Again apply hadamard to the 3 qubits
    	qc.h(range(3))
    
    	#Measure the input qubits
    	qc.measure(range(3), range(3))
    
    	return qc


def ResultGiver():
	qc = compile_circuit(function)
	
 	#The next few lines were blatantly copied from IBM
   	result = AerSimulator().run(qc, shots=1, memory=True).result()
    	measurements = result.get_memory()
    	if "1" in measurements[0]:
        	return "balanced"
		else:
    		return "constant"
	

	





