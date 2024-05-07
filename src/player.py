#!/usr/bin/env python3
from colors import *
from random import sample, choice

# Cores disponíveis para o palpite
colors = [RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE]
apostas = []


def checagem(retorno, guess_hist):
    if retorno not in guess_hist:
        return True
    return False


# fazer com que ordem não importe nesse processo


def zero_acerto(guess_hist, res_hist):
    lista = sample(colors, 4)
    print("Guess generated by player function:", lista)
    # se checagem == verdadeiro
    if checagem(lista, guess_hist):
        return lista
    # se checagem == falso
    return zero_acerto(guess_hist, res_hist)


def um_acerto(guess_hist, res_hist):
    # while True:
    aposta = choice(guess_hist[-1])
    # if aposta not in apostas:
    apostas.append(aposta)
    # break
    lista = [x for x in colors if x not in guess_hist[-1]]
    lista.append(aposta)
    print("Guess generated by player function:", lista)
    # se checagem == verdadeiro
    if checagem(lista, guess_hist):
        return lista
    # se checagem == falso
    del apostas[-1]
    return um_acerto(guess_hist, res_hist)


def dois_acerto(guess_hist, res_hist):
    while True:
        aposta = sample(
            guess_hist[-1], 2
        )  # aposta que dois elementos da última tentativa estão corretos
        if aposta[0] != apostas[-1]:
            apostas.append(aposta[0])
            if aposta[1] != apostas[-2]:
                apostas.append(aposta[1])
                break
            del apostas[-1]
    lista = [x for x in colors if x not in guess_hist[-1]]
    lista[-1] = aposta[-1]
    lista.append(aposta[-2])
    print("Guess generated by player function:", lista)
    # se checagem == verdadeiro
    if checagem(lista, guess_hist):
        return lista
    # se checagem == falso
    del apostas[-1]
    del apostas[-1]  # apaga as duas apostas feitas
    return dois_acerto(guess_hist, res_hist)


def tres_acerto(guess_hist, res_hist):
    match res_hist[-2][0]:
        case (
            1
        ):  # tem que analisar os casos que é 1, 3; 1, 3, 3; 1, 3, 3, 3... posso fazer uma lista de elementos que eu sei que estão errados e inseri-los la
            lista = guess_hist[-1].copy()
            aposta = choice([x for x in colors if x not in lista])
            apostas.append(aposta)
            lista.remove(apostas[-1])
            lista.append(aposta)
            # se checagem == verdadeiro
            if checagem(lista, guess_hist):
                return lista
            # se checagem == falso
    # adicionar os cases restantes
    # analisar se vale a pena fazer com set
    lista = guess_hist[-1].copy()
    apostas.append(choice(lista))
    while True:
        aposta = choice(colors)
        if aposta != apostas[-1]:
            apostas.append(aposta)
            break
    lista.remove(apostas[-2])
    lista.append(apostas[-1])
    print("Guess generated by player function:", lista)
    if checagem(lista, guess_hist):
        return lista
    # refazer se checagem == False
    # analisar se o jogo anterior também foi 3. se sim, continuar trocando o mesmo item pelos outros possíveis


def player(guess_hist, res_hist):
    try:
        match res_hist[-1][0]:
            case 0:
                return zero_acerto(guess_hist, res_hist)
            case 1:
                return um_acerto(guess_hist, res_hist)
            case 2:
                return dois_acerto(guess_hist, res_hist)
            case 3:
                return tres_acerto(guess_hist, res_hist)
            # case 4: bruno salles
    except:  # IndexError
        return zero_acerto(guess_hist, res_hist)
