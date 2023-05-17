import cv2
import numpy as np
import serial

porta = 'COM3'
baud_rate = 9600

ser = serial.Serial(porta, baud_rate)

ledVerde = 6
ledAmarelo = 7
ledVermelho = 8

# Capturar e processar imagens
cap = cv2.VideoCapture(0)
corMudou = ''
corFinal = ''

while True:
    _, img = cap.read()
    altura, largura, _ = img.shape
    margem = 100
    campo = img[margem:altura-margem, margem:largura-margem]
    cv2.rectangle(img, (margem, margem), (largura-margem, altura-margem), (255, 0, 0), 3)

    corMediaLinha = np.average(campo, axis=0)
    corMedia = np.average(corMediaLinha, axis=0)
    r, g, b = int(corMedia[2]), int(corMedia[1]), int(corMedia[0])
    cor = [r, g, b]
    print(cor)
    
    if r >= 140 and g >= 140 and b <= 60:
        corFinal = 'Amarelo'
        ser.write(b'1')  # Envie o comando para acender o LED amarelo
    elif np.argmax(cor) == 0:
        corFinal = 'Vermelho'
        ser.write(b'2')  # Envie o comando para acender o LED vermelho
    elif np.argmax(cor) == 1:
        corFinal = 'Verde'
        ser.write(b'3')  # Envie o comando para acender o LED verde
    else:
        corFinal = 'Desligado'
        ser.write(b'0')  # Envie o comando para apagar todos os LEDs

    if corFinal != corMudou:
        ser.write(b'0')  # Envie o comando para apagar todos os LEDs

    corMudou = corFinal
    print(corFinal)

    cv2.imshow('Img', img)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
ser.close()