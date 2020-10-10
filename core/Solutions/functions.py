import pickle

def open_pkl(file_loc):
	file = open(file_loc, 'rb')
	data = pickle.load(file)
	file.close()
	return data

def dump_pkl(file_loc, data):
	file = open(file_loc, 'wb')
	pickle.dump(data, file)
	file.close()