# Bayesian Network

miscellaneous -> Bayesian_Network:	

	- classe BayesianNetwork: racchiude le funzioni necessarie a gestire il DAG che rappresenta la rete Bayesiana
		init:	crea la matrice di incidenza del grafo come matrice numpy NxN di zeri, imposta il limite di figli e padri per ogni nodo. Inizializza il seed per il generatore casuale di numeri.
		generate_DAG:	crea un DAG casuale di N archi.
		set/get_matrix:	permette di accedere in scrittura/lettura alla matrice di incidenza del BN
		get_n: restituisce il numero di nodi del BN
		get_parents: restituisce la lista dei padri del nodo 'node_number'
		get_children: restituisce la lista dei figli del nodo 'node_number'
		add_link: permette di aggiungere un arco da link[0] in link[1] verificando preventivamente che il grafo rimanga un DAG
		remove_link: rimuove l'arco da link[0] in link[1]
		change_link: inverte il verso dell'arco fra link[0] e link[1] verificando preventivamente che il grafo rimanga un DAG
	
	- funzione search_path_bfs: prende in ingresso due nodi 'u', 'v' e un BN. Restituisce True se è presente un cammino (orientato) da v in u, False altrimenti.

dataset_generator -> csv_to_numpy:

	- funzione csv_to_numpy: prende in ingresso tre percorsi di file csv. 'states_path' contiene il nome degli stati seguiti dalla dimensione del loro dominio (in questo caso booleano). Es. [X1,2,X2,2,...,2]. 'prob_table_path' contiene N righe ed indica all'i-esima riga quale sia la probabilità che l'i-esimo stato assuma valore 1 data la configurazione di tutti i suoi padri (in ordine di comparsa nello 'states-path'). 'structure_path' contiene la matrice di incidenza del grafo di partenza. La funzione restituisce dunque un array con i domini, la matrice di incidenza come matrice numpy ed un array con le probabilità di ogni evento.
