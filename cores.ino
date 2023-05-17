void setup() {
  Serial.begin(9600);  // Inicia a comunicação serial com uma taxa de 9600 bps
  pinMode(6, OUTPUT);  //  Define o pino 6 como saída
  pinMode(7, OUTPUT);  // Define o pino 7 como saída
  pinMode(8, OUTPUT);  // Define o pino 8 como saída
}

void loop() {
if (Serial.available() > 0) { // Verifica se há dados disponíveis para leitura
    String message = Serial.readString(); // Lê a mensagem enviada pelo Python
  
    if (message == "1"){

      digitalWrite(7, HIGH);  //Acende o LED amarelo
      delay(2000);
      digitalWrite(7, LOW);  // Apaga o LED am

    } else if (message == "2"){

      digitalWrite(8, HIGH);  // Acende o LED vermelho
      delay(2000);
      digitalWrite(8, LOW);  // Apaga o LED vermelho
    } else if (message == "3"){

      digitalWrite(6, HIGH);  // Acende o LED verde
      delay(2000);
      digitalWrite(6, LOW);  // Apaga o LED verde
    } 
  }
}