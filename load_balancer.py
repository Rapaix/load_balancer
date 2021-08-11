

def read_file(archive):
    """
        faz a leitura do arquivo de entrada e retorna um array de inteiros formatado
        WIP - verificar os limites
              verificar se tem arquivo
              e retorna erro
    """
    with open(archive, 'r') as read:
        arr = []
        lines = read.readlines()
        ttask, umax = lines[:2]
        msg = ''
        if int(ttask) < 1 or int(ttask) > 10:
            msg = f'O valor {int(ttask)} de ttask está fora dos limites'
            return msg
        elif int(umax) < 1 or int(umax) > 10:
            msg = f'O valor {int(umax)} de umax está fora dos limites'
            return msg
        else:
            for i in lines:
                arr.append(int(i))
            msg = arr
    return msg


def load_balancer(arr, ttask, umax):
    """
        Algoritmo 
    """

    tick = 0
    arr = arr
    list_servers = {}
    total_users_serv = 0
    num_servidor = 1
    counter = 0
    qtd_servers_inactives = 0
    total_cost = 0
    finished = False
    ttask = ttask
    umax = umax
    output_file = open('output.txt', 'r+')
    result = []

    while finished == False:
        try:
            line = arr[counter]
        except:
            line = 0
        tick += 1

        if tick > ttask:
            try:
                pos = arr[tick-ttask-1]
            except:
                pos = 0
            for n in range(pos):
                for servidor in list_servers:
                    if list_servers[servidor]['NumUser'] > 0:
                        list_servers[servidor]['NumUser'] = int(
                            list_servers[servidor]['NumUser']) - 1
                        if list_servers[servidor]['NumUser'] == 0:
                            list_servers[servidor]['Status'] = 'Inativo'
                        break
                    else:
                        list_servers[servidor]['Status'] = 'Inativo'
            # counter += 1

        for i in range(line):
            total_users_serv += 1
            if total_users_serv <= umax:
                try:
                    list_servers['Servidor' +
                                 str(num_servidor)]['NumUser'] = total_users_serv
                except:
                    list_servers['Servidor'+str(num_servidor)] = {
                        'NumUser': total_users_serv, 'Status': 'Ativo'}
            else:
                total_users_serv = 1
                num_servidor += 1
                list_servers['Servidor'+str(num_servidor)
                             ] = {'NumUser': total_users_serv, 'Status': 'Ativo'}

        output = ''
        for j, servidor in enumerate(list_servers):
            if list_servers[servidor]['Status'] == 'Inativo':
                qtd_servers_inactives += 1
            else:
                try:
                    list_servers[servidor]['Tick'] += 1
                except:
                    list_servers[servidor]['Tick'] = 1
                output = output + \
                    str(list_servers[servidor]['NumUser']) + ','

                qtd_servers_inactives = 0
        if output == '':
            # print('0')
            output_file.write('0\n')
            result.append('0')
        else:
            # print(output[:-1])
            output_file.write(output[:-1]+'\n')

        if arr[0] != 0:
            if qtd_servers_inactives == len(list_servers):
                finished = True

        counter += 1
        result.append(output)

    for server in list_servers:
        total_cost = total_cost + (list_servers[server]['Tick'] * 1)
        result[-1] = str(total_cost)

    # print(total_cost)
    print(result)
    output_file.write(str(total_cost)+'\n')

    output_file.close()
    print('Processamento finished com Sucesso!')

    return result


file_array = read_file('input_teste.txt')


print(load_balancer(file_array[2:], file_array[0], file_array[1]))
