#include <MFRC522.h>
#include <SPI.h>

int RST_PIN=9;
int SS_PIN=10;

MFRC522 rfid(SS_PIN, RST_PIN);
byte ID[4] = {0,0,0,0};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  SPI.begin();
  rfid.PCD_Init();

}

void loop() {
  // put your main code here, to run repeatedly:
  if(! rfid.PICC_IsNewCardPresent()){
    return;
    }
  if(! rfid.PICC_ReadCardSerial()){
    return;
    }
  if( rfid.uid.uidByte[0] == ID[0] && 
  rfid.uid.uidByte[1] == ID[1] && 
  rfid.uid.uidByte[2] == ID[2] && 
  rfid.uid.uidByte[3] == ID[3]){
    Serial.println("engelli karti");
  }
}
