tarefa_terca = True
tarefa_quinta = True

# if tarefa_terca and tarefa_quinta:
#   print('TV de 50" e um sorvete')
# elif tarefa_terca != tarefa_quinta:
#   print('TV de 32" e um sorvete')
# else:
#   print('fique em casa')

tv_50 = tarefa_terca and tarefa_quinta
tv_32 = tarefa_terca != tarefa_quinta
sorvete = tarefa_terca or tarefa_quinta
saude = not sorvete

print('TV 50": {}, TV 32": {}, Sorvete: {}, Saúde: {}'.format(tv_50, tv_32, sorvete, saude))