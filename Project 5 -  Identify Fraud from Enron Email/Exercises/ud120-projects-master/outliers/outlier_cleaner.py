def outlierCleaner(predictions, ages, net_worths):
 import numpy as np
 cleaned_data = np.concatenate((predictions, ages, net_worths, abs(net_worths-predictions)), axis = 1)
 cleaned_data = cleaned_data[np.argsort(cleaned_data[:,3])]
 return cleaned_data[:int(len(cleaned_data)*.9),1:]
