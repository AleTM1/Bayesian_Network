# Structure learning for Bayesian Networks

miscellaneous -> Bayesian_Network.py:	

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

dataset_generator -> csv_to_numpy.py:

	- funzione csv_to_numpy: prende in ingresso tre percorsi di file csv. 'states_path' contiene il nome degli stati seguiti dalla dimensione del loro dominio (in questo caso booleano). Es. [X1,2,X2,2,...,2]. 'prob_table_path' contiene N righe ed indica all'i-esima riga quale sia la probabilità che l'i-esimo stato assuma valore 1 data la configurazione di tutti i suoi padri (in ordine di comparsa nello 'states-path'). 'structure_path' contiene la matrice di incidenza del grafo di partenza. La funzione restituisce dunque un array con i domini, la matrice di incidenza come matrice numpy ed un array con le probabilità di ogni evento.

dataset_generator -> topological_order.py:

	- funzione topological_ord: prende in ingresso la matrice di incidenza di un DAG e restituisce un ordinamento topologico degli N nodi. L'ordinamento è ottenuto con l'algoritmo di Kahn. L'algoritmo si inizializza a partire dal set di nodi privi di archi entranti restituito dalla funzione 'starter_set'.
	- funzione starter_set: prende in ingresso una matrice di incidenza ed il numero di nodi da cui è ricavata. Restituisce la lista dei nodi privi di archi entranti.
	- funzione get_children: prende in ingresso matrice di incidenza, numero di nodi ed un nodo 'node_number' per cui si svolge la richiesta. Restituisce la lista dei figli di 'node_number'.
	- funzione has_parents: prende in ingresso matrice di incidenza, numero di nodi ed un nodo 'node_number' per cui si svolge la richiesta. Restituisce True se 'node_number' ha almeno un arco entrante, False altrimenti.
	
dataset_generator -> dataset_generator.py:

	- funzione get_parents: prende in ingresso matrice di incidenza, numero di nodi ed un nodo 'node_number' per cui si svolge la richiesta. Restituisce la lista dei padri di 'node_number'.
	- funzione dataset_gen: prende in ingresso l'array dei domini, la matrice di incidenza, la matrice con le probabilità note degli eventi ed il numero 'n' di elemnti del dataset. Le probabilità sono immesse nello stesso formato fornito da 'csv_to_numpy'. La funzione restituisce un dataset di dimensione n. Il dataset viene creato inserendo i valori nella riga (campione) segunedo l'ordine indicato dall'ordinamento topologico ed utilizzando la libreria random per generare, di volta in volta, un numero pseudocasuale fra 0 ed 1.
	
structure_learn -> score_function.py:

	- funzione score_function: prende in ingresso un oggetto 'bayesian_network' della classe BayesianNetwork ed il dataset correlato. Restituisce lo score del 'bayesian_network' rispetto al dataset fornito. ij_array[] contiene le liste di tutte le configurazioni dei padri per ognuno degli n stati. Nij_array[] contiene le liste del numero di volte che ciascuna delle ij-esime configurazioni sono presenti nel dataset. Nijk_array[] analogamente conta per ogni configurazione ij quante volte lo stato i-esimo assume il k-esimo valore del proprio dominio. Lo score function è calcolato usando la formula del BIC-score
	
structure_learn -> hill_climbing.py:

	- funzione BIC_hill_climbing: prende in ingresso la lista dei domini, il dataset ed il numero 't' di restart da eseguire. Restituisce il miglior score trovato ed il BN a cui è associato. Implementa un algoritmo greedy volto a massimizzare lo score restituito dalla score_function ed esegue t restart. Ogni tentativo viene inzializzato a partire da un DAG casuale e, ad ogni iterazione finché possibile, viene scelta la 'mossa' migliore per massimizzare lo score. Viene poi mantenuto in memoria solo lo score migliore mai raggiunto ed il BN da cui è stato ricavato.
	
main_.py:

	- funzione main: Questa funzione contiene in chiaro le stringhe che indicano i tre path necessari alla funzione csv_to_numpy, il numero 'n' che indica la dimensione del dataset da generare ed il numero 't' di restart da eseguire. Dopo aver caricato i dati e generato il dataset, queste informazioni vengono passate alla funzione hill_climbing che restituirà i valori ottenuti nella variabile 'result'. Infine il main() si occupa di stampare il BN ottenuto dal dataset generato ed il relativo score.
	
conditional_independence -> conditional_dependence_search.py:
	
	- funzioni get_children/parents: identiche a quelle sopra.
	- funzione path_finder_undirect_graph: prende in ingresso un nodo sorgente 'src', un nodo destinazione 'dst' ed una matrice di incidenza (come matrice numpy) a cui appartengono i nodi precedenti. Restituisce la lista di tutti i possibili cammini da 'src' a 'dst' utilizzando il metodo 'all_simple_paths()' della libreria networkx.
	- funzione search_conditional_dependence: prende in ingresso la matrice di incidenza del BN. Per ogni coppia di nodi non adiacenti stampa la condizione affinché i due nodi siano condizionalmente (o marginalmente) indipendenti. Il criterio impiegato è quello della D-separation. 
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
