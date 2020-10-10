from functions import *

gods = {'Greek': ['Zeus', 'Poseidon', 'Athena', 'Apollo', 'Artemis', 'Ares', 'Hades'],
		'Roman': ['Bellona', 'Cupid', 'Hercules', 'Janus', 'Mercury', 'Discordia', 'Nox'],
		'Norse': ['Fenrir', 'Heimdallr', 'Hel', 'Loki', 'Odin', 'Thor', 'Tyr'],
		'Egyptian': ['Anubis', 'Khepri', 'Osiris', 'Bastet', 'Thoth', 'Sobek', 'Neith']}

dump_pkl('../Level 1/Challenge 2/data.pkl', gods)

data = open_pkl('../Level 1/Challenge 2/data.pkl')

#for keys, values in data.items():
#	print(keys)
#	print(values)

data['Greek'].append('Hera')

dump_pkl('../Level 1/Challenge 2/data.pkl', data)
data = open_pkl('../Level 1/Challenge 2/data.pkl')

for keys, values in data.items():
	print(keys)
	print(values)