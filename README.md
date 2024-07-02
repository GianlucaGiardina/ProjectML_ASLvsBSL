# Progetto di Classificazione delle Immagini

Questo repository contiene il codice e i dati per il progetto di classificazione delle immagini. Il progetto utilizza vari modelli di deep learning per classificare immagini estratte da video. 

## Struttura delle Cartelle

- **Dataset**: Contiene il dataset presente all’interno di Roboflow, diviso a sua volta in
train, test e validation;
- **Strumenti utilizzati**: all’interno di questa cartella sono contenuti gli script sviluppati per poter estrapolare i frame dai video;
- **Notebook**: il contenuto della cartella include tutti i notebook creati, ognuno dedicato a una rete neurale specifica.

## Contenuto dei Notebook

- **MobileNetV2.ipynb**: il notebook contiene l’addestramento con MobileNetV2 e, successivamente, la classificazione utilizzata per l’elaborato, che coinvolge sia MobileNetV2 che DenseNet121;
- **MobileNetV2Dataset2.ipynb**: questo notebook è stato utilizzato per addestrare MobileNetV2 con il dataset variato contenente più soggetti;
- **densenet.ipynb**: presenta l’addestramento di DenseNet121;
- **VGG6.ipynb**: notebook contenente gli sviluppi della rete VGG16;
- **AlexNet.ipynb**: notebook contenente gli sviluppi della rete AlexNet;
- **demo.ipynb**: Questo permette di testare i modelli attraverso due modalità:
  1. Upload di un’immagine: carica un’immagine inerente a uno dei due alfabeti per verificarne l’identificazione.
  2. Selezione di un alfabeto e una parola: vengono prese le immagini che rappresentano quella parola e identificate con i tre modelli MobileNetV2, VGG16 e DenseNet121.

Per eseguire `demo.ipynb`, è sufficiente aprirlo e avviarlo su Google Colab, poiché i tre modelli sono salvati su Google Storage e vengono scaricati automaticamente.

All'interno di tutti i notebook è presente il link colab così da poter rieseguire il codice se necessario.