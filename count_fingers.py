import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
#detectar a palma da mão
mp_maos = mp.solutions.hands
#pega cordenadas para desenhar
mp_desenhar = mp.solutions.drawing_utils

maos = mp_maos.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)

while True:
    success, image = cap.read()
    # Detecte os pontos de referência das mãos 
    resultado = maos.process(image)
    #cordenadas x e y das mãos na web cam
    hand_landmarks = resultado.multi_hand_landmarks
    print(hand_landmarks)

    cv2.imshow("Controlador de Midia", image)

    key = cv2.waitKey(1)
    if key == 32:
        break

cv2.destroyAllWindows()
