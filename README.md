# Technology Team Rover

## Utili

- [Git repo](https://github.com/Sapienza-Technology-2021/Socket-GUI)
- [Homepage European Rover Challenge](https://roverchallenge.eu/en/main-page/)
- [Regolamento Challenge](https://drive.google.com/file/d/1fdFG12WW0QmHjRp6cL2ikP8UFmEpzSka/view)

## Requisiti di sviluppo GUI

- [QT Creator](https://www.qt.io/download-open-source)
- [PyCharm](https://www.jetbrains.com/pycharm/download/) (consigliato)

## Requisiti di esecuzione

- `python3.9`, [Download](https://www.python.org/)
  - Deve essere impostato nella variabile d'ambiente PATH
- `PyQt5`, [pip3 install PyQt5](https://pypi.org/project/PyQt5/)
- `pyserial`, [pip3 install pyserial](https://pyserial.readthedocs.io/en/latest/pyserial_api.html)
- `pyqtgraph`, [pip3 install pyqtgraph](https://pyqtgraph.readthedocs.io/en/latest/)

## Esecuzione

- Server
  - Lanciare `.\server.bat` oppure la configurazione "Server" in PyCharm
- Interfaccia
  - `.\gui.bat` oppure la configurazione "Interfaccia" in PyCharm

## Protocollo di comunicazione socket

Vedi `JSON.md`

## Protocollo di comunicazione con Teensy

Vedi [repository firmware](https://github.com/Sapienza-Technology-2021/Rover-firmware/blob/master/README.md)